from django.contrib import admin
from .models import User, EmailOTP
from django.utils.html import format_html

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email_link', 'first_name', 'last_name', 'gender', 'is_active', 'is_staff', 'signup_date')
    list_filter = ('is_active', 'is_staff', 'gender', 'signup_date')
    search_fields = ('email', 'first_name', 'last_name')
    readonly_fields = ('signup_date',)
    ordering = ('-signup_date',)

    def email_link(self, obj):
        return format_html('<a href="/admin/accounts/user/{}/change/">{}</a>', obj.id, obj.email)
    email_link.short_description = 'Email'

@admin.register(EmailOTP)
class EmailOTPAdmin(admin.ModelAdmin):
    list_display = ('email', 'code', 'is_used', 'attempts', 'blocked_until', 'created_at')
    list_filter = ('is_used',)
    search_fields = ('email', 'code')
    readonly_fields = ('created_at',)


    def user_link(self, obj):
        return format_html('<a href="/admin/accounts/user/{}/change/">{}</a>', obj.user.id, obj.user.email)
    user_link.short_description = 'User'
