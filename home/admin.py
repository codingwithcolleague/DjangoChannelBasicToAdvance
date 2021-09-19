from django.contrib import admin
from home.models import Notification

# Register your models here.
# admin.site.register(Notification)

@admin.register(Notification)
class NotificationModel(admin.ModelAdmin):
    fields = ['user' , 'notification' , 'is_seen'  ]