from django.contrib import admin
from .models import SolidarityMessage, FamilyDonation

@admin.register(SolidarityMessage)
class SolidarityMessageAdmin(admin.ModelAdmin):
    list_display = ['message', 'county', 'is_approved', 'created_at']
    list_filter = ['is_approved', 'county']
    list_editable = ['is_approved']
    ordering = ['-created_at']
    actions = ['approve_messages', 'delete_selected']

    def approve_messages(self, request, queryset):
        queryset.update(is_approved=True)
        self.message_user(request, f"{queryset.count()} message(s) approved.")
    approve_messages.short_description = "✅ Approve selected messages"

@admin.register(FamilyDonation)
class FamilyDonationAdmin(admin.ModelAdmin):
    list_display = ['phone_number', 'amount', 'status', 'mpesa_receipt_number', 'created_at']
    list_filter = ['status']
    ordering = ['-created_at']
    readonly_fields = ['phone_number', 'amount', 'checkout_request_id', 'mpesa_receipt_number', 'created_at']