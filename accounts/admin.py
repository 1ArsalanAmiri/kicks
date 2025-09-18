from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from .models import User, Address


@admin.register(User)
class CustomUserAdmin(BaseUserAdmin):
    list_display_links = ('id', 'email')
    ordering = ("-signup_date",)
    list_display = ("id", "email", "username", "phone_number", "is_active", "is_staff", "is_superuser", "signup_date")
    list_filter = ("is_staff", "is_superuser", "is_active")
    search_fields = ("email", "username", "phone_number")
    readonly_fields = ("signup_date", "last_login")

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Personal info"), {"fields": ("username", "phone_number")}),
        (_("Permissions"), {"fields": ("is_active", "is_staff", "is_superuser")}),
        (_("Important dates"), {"fields": ("last_login", "signup_date")}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "password1", "password2", "is_active", "is_staff", "is_superuser"),
        }),
    )

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "full_name", "city", "state", "postal_code")
    search_fields = ("first_name", "last_name", "city", "state", "postal_code", "user__email")
    list_filter = ("state", "city")