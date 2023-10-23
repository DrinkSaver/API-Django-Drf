from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from ApiDrinkSaver.models.user import CustomUser, UserProfile, BarOwnerProfile


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


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(UserProfile)
admin.site.register(BarOwnerProfile)