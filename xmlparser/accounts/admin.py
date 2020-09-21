from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext, gettext_lazy as _
from .models import User, Student

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'full_name', 'login_count', 'is_active', 'is_staff')
    list_display_links = ('username', 'email',)

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal Info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )

    def full_name(self, obj):
        return obj.get_full_name()


class StudentAdmin(admin.ModelAdmin):
    list_display = ('email', 'full_name', 'registration_numner', 'is_passed', 'is_active')

    def full_name(self, obj):
        return obj.user.get_full_name()

    def email(self, obj):
        return obj.user.email

    def is_active(self, obj):
        return obj.user.is_active

admin.site.register(User, CustomUserAdmin)
admin.site.register(Student, StudentAdmin)
