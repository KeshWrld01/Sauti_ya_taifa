from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django_daraja.mpesa.core import MpesaClient
from .models import SolidarityMessage, FamilyDonation
import json

def home(request):
    return render(request, 'core/home.html')

def healing(request):
    if request.method == 'POST':
        action = request.POST.get('action')

        # Handle solidarity message
        if action == 'message':
            message = request.POST.get('message')
            county = request.POST.get('county', '')
            sender_name = request.POST.get('sender_name', '').strip() or 'Anonymous'
            if message:
                SolidarityMessage.objects.create(
                    message=message,
                    county=county,
                    sender_name=sender_name
                )
            return redirect('healing')
        
        # Handle donation
        if action == 'donate':
            phone = request.POST.get('phone')
            amount = int(request.POST.get('amount'))

            cl = MpesaClient()
            callback_url = 'https://your-url.ngrok.io/healing/callback/'

            response = cl.stk_push(
                phone, amount,
                'HealingHouse',
                'Donation to affected families — Sauti Ya Taifa',
                callback_url
            )
            data = response.json()

            FamilyDonation.objects.create(
                phone_number=phone,
                amount=amount,
                checkout_request_id=data.get('CheckoutRequestID', ''),
            )
            return JsonResponse(data)

    messages = SolidarityMessage.objects.filter(is_approved=True).order_by('-created_at')[:20]
    return render(request, 'core/healing.html', {
        'messages': messages,
        'breadcrumbs': [
            {'name': 'Healing House', 'url': None}
        ]
    })

@csrf_exempt
def healing_callback(request):
    if request.method == 'POST':
        payload = json.loads(request.body)
        stk = payload['Body']['stkCallback']
        checkout_id = stk['CheckoutRequestID']
        result_code = stk['ResultCode']

        try:
            donation = FamilyDonation.objects.get(checkout_request_id=checkout_id)
            if str(result_code) == '0':
                items = stk['CallbackMetadata']['Item']
                for item in items:
                    if item['Name'] == 'MpesaReceiptNumber':
                        donation.mpesa_receipt_number = item['Value']
                donation.status = 'completed'
            else:
                donation.status = 'failed'
            donation.save()
        except FamilyDonation.DoesNotExist:
            pass

    return HttpResponse('OK')