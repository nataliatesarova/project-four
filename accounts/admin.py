from django.contrib import admin
from .models import Profile, CustomUser
# Register your models here.

# Info to display on admin page


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name')

# Profile info
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'profile_picture', 'created_on', 'updated_on')
    list_filter = ('created_on', 'updated_on')
    search_fields = ('user__username', 'user__email')


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Profile, ProfileAdmin)
