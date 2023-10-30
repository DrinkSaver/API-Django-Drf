from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from ApiDrinkSaver.models.user import User, UserProfile, BarOwnerProfile
from ApiDrinkSaver.models.apiKey import APIKey


class APIKeyAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'key']
    list_display_links = ['user', 'name', 'key']
    search_fields = ['user__username', 'user__email', 'name']
    list_filter = ['user']
    ordering = ['-user']

    def get_fields(self, request, obj=None):
        fields = super(APIKeyAdmin, self).get_fields(request, obj)
        if not request.user.is_superuser:
            fields.remove('user')
        return fields


class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'is_bar_owner', 'is_lambda_user')
    list_filter = ('is_staff', 'is_bar_owner', 'is_lambda_user')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'date_of_birth', 'profile_image', 'bio', 'location')}),
        ('User Type', {'fields': ('is_staff', 'is_bar_owner', 'is_lambda_user')}),
        ('Bar Owner Info', {'fields': ('bar_name', 'address')}),
        ('Permissions', {'fields': ('groups', 'user_permissions')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )


admin.site.register(APIKey, APIKeyAdmin)
admin.site.register(User, CustomUserAdmin)
admin.site.register(UserProfile)
admin.site.register(BarOwnerProfile)
