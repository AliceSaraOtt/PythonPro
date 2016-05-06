from django.contrib import admin
import models
# Register your models here.

admin.site.register(models.Host)
admin.site.register(models.HostGroup)
admin.site.register(models.HostUser)
admin.site.register(models.UserProfile)
admin.site.register(models.IDC)
admin.site.register(models.Department)
admin.site.register(models.BindHostToUser)
