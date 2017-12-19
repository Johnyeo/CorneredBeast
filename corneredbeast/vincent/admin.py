from django.contrib import admin
from corneredbeast.vincent.models import weidongurls, weidongusers


# Register your models here.
class weidongurls_admin(admin.ModelAdmin):
    list_display = ['name', 'url', 'environment', 'create_time']
    search_fields = ['name']
    list_filter = ['environment','comment','category']

class weidongusers_admin(admin.ModelAdmin):
    list_display = ['username', 'nickname', 'password', 'phone', 'email', 'portrait', 'belongtourl', 'environment',
                    'flag', 'create_time']


admin.site.register(weidongurls, weidongurls_admin)
admin.site.register(weidongusers, weidongusers_admin)
