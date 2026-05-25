from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django_daraja.mpesa.core import MpesaClient
from .models import Member
from datetime import date, timedelta
import json

def join(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        id_number = request.POST.get('id_number')
        phone = request.POST.get('phone_number')
        county = request.POST.get('county')

        # Check if already registered
        if Member.objects.filter(email=email).exists():
            return render(request, 'members/join.html', {
                'error': 'This email is already registered. Contact us if you need help.'
            })

        if Member.objects.filter(id_number=id_number).exists():
            return render(request, 'members/join.html', {
                'error': 'This ID number is already registered.'
            })

        # Create pending member
        member = Member.objects.create(
            full_name=full_name,
            email=email,
            id_number=id_number,
            phone_number=phone,
            county=county,
            status='pending'
        )

        # Initiate STK push
        cl = MpesaClient()
        callback_url = 'https://sautiyataifa-production.up.railway.app/join/callback/'

        response = cl.stk_push(
            phone, 1000,
            'SautiMembership',
            'Sauti Ya Taifa Registration + Subscription',
            callback_url
        )
        data = response.json()

        member.checkout_request_id = data.get('CheckoutRequestID', '')
        member.save()

        # Return member id for polling
        return JsonResponse({
            **data,
            'member_id': str(member.member_id)
        })

    return render(request, 'members/join.html')


@csrf_exempt
def join_callback(request):
    if request.method == 'POST':
        payload = json.loads(request.body)
        stk = payload['Body']['stkCallback']

        checkout_id = stk['CheckoutRequestID']
        result_code = stk['ResultCode']

        try:
            member = Member.objects.get(checkout_request_id=checkout_id)
            if str(result_code) == '0':
                items = stk['CallbackMetadata']['Item']
                for item in items:
                    if item['Name'] == 'MpesaReceiptNumber':
                        member.mpesa_receipt_number = item['Value']
                member.status = 'active'
                member.subscription_expires = date.today() + timedelta(days=365)
            else:
                member.status = 'pending'
            member.save()
        except Member.DoesNotExist:
            pass

    return HttpResponse('OK')


def check_payment(request, member_id):
    """Poll this endpoint to check if payment is complete"""
    try:
        member = Member.objects.get(member_id=member_id)
        return JsonResponse({
            'status': member.status,
            'receipt': member.mpesa_receipt_number,
            'name': member.full_name,
        })
    except Member.DoesNotExist:
        return JsonResponse({'status': 'not_found'})


def success(request, member_id):
    try:
        member = Member.objects.get(member_id=member_id, status='active')
        return render(request, 'members/join.html', {
            'breadcrumbs': [
                {'name': 'Join Us', 'url': None}
            ]
        })
    except Member.DoesNotExist:
        return redirect('join')