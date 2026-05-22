from django.contrib import admin
from .models import Victim

@admin.register(Victim)
class VictimAdmin(admin.ModelAdmin):
    list_display = ['name', 'status', 'county', 'age', 'approval', 'submitted_at']
    list_filter = ['approval', 'status', 'county']
    search_fields = ['name', 'how_it_happened']
    list_editable = ['approval']
    readonly_fields = ['submitted_at', 'photo']
    ordering = ['-submitted_at']

    actions = ['approve_submissions', 'reject_submissions']

    def approve_submissions(self, request, queryset):
        queryset.update(approval='approved')
        self.message_user(request, f"{queryset.count()} submission(s) approved.")
    approve_submissions.short_description = "✅ Approve selected submissions"

    def reject_submissions(self, request, queryset):
        queryset.update(approval='rejected')
        self.message_user(request, f"{queryset.count()} submission(s) rejected.")
    reject_submissions.short_description = "❌ Reject selected submissions"