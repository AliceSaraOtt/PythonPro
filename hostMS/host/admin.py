from django.contrib import admin
import models
import auth_admin
# Register your models here.

class HostAdmin(admin.ModelAdmin):
    list_display = ('hostname','ip_addr','idc','system_type')
    list_filter = ('idc',)
    search_fields = ('hostname','ip_addr')
    list_editable = ('idc','system_type')

class BindHostToUserInline(admin.TabularInline):
    model = models.BindHostToUser.host_groups.through

class HostGroupAdmin(admin.ModelAdmin):
    inlines = [BindHostToUserInline,]

class BindHostToUserAdmin(admin.ModelAdmin):
    list_display = ('host','host_user','get_groups')


admin.site.register(models.Host,HostAdmin)
admin.site.register(models.HostGroup,HostGroupAdmin)
admin.site.register(models.HostUser)
admin.site.register(models.BindHostToUser,BindHostToUserAdmin)
admin.site.register(models.IDC)

# admin.site.register(models.Host,HostAdmin)
# admin.site.register(models.HostGroup,HostGroupAdmin)
# admin.site.register(models.HostUser)
# admin.site.register(models.BindHostToUser,BindHostToUserAdmin)
# admin.site.register(models.IDC)
# admin.site.register(models.TaskLog,TaskLogAdmin)
# admin.site.register(models.TaskLogDetail,TaskLogDetailAdmin)
