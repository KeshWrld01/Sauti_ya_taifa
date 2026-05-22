from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django_daraja.mpesa.core import MpesaClient
from .models import Donation
import json

def donate(request):
    if request.method == 'POST':
        phone = request.POST.get('phone')
        amount = int(request.POST.get('amount'))
        name = request.POST.get('name', 'Anonymous')

        cl = MpesaClient()
        callback_url = 'https://your-url.ngrok.io/donations/callback/'

        response = cl.stk_push(phone, amount, 'SautiDonation', 'Donation to Sauti Ya Taifa', callback_url)
        data = response.json()

        Donation.objects.create(
            name=name,
            phone_number=phone,
            amount=amount,
            checkout_request_id=data.get('CheckoutRequestID', ''),
        )

        return JsonResponse(data)

    return render(request, 'donations/donate.html')


@csrf_exempt
def mpesa_callback(request):
    if request.method == 'POST':
        payload = json.loads(request.body)
        stk = payload['Body']['stkCallback']

        checkout_id = stk['CheckoutRequestID']
        result_code = stk['ResultCode']

        try:
            donation = Donation.objects.get(checkout_request_id=checkout_id)
            if str(result_code) == '0':
                items = stk['CallbackMetadata']['Item']
                for item in items:
                    if item['Name'] == 'MpesaReceiptNumber':
                        donation.mpesa_receipt_number = item['Value']
                donation.status = 'completed'
            else:
                donation.status = 'failed'
            donation.save()
        except Donation.DoesNotExist:
            pass

    return HttpResponse('OK')