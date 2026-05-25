from django.contrib import admin
from .models import Member

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'county', 'status', 'mpesa_receipt_number', 'joined_at', 'subscription_expires']
    list_filter = ['status', 'county']
    search_fields = ['full_name', 'email', 'id_number']
    readonly_fields = ['member_id', 'joined_at', 'checkout_request_id', 'mpesa_receipt_number']
    ordering = ['-joined_at']