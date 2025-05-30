from django.contrib import admin
from .models import UserProfile 

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'full_name', 'age', 'blood_group', 'area', 'phone')  
