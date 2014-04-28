from django.contrib import admin

from apps.domain.models import DomainDetail


class DomainDetailAdmin(admin.ModelAdmin):
    
    list_display = ('name', 'get_url', 'email', 'username', 'password',
                    'has_additional_info')
    ordering = ('name',)
    list_filter = ('name',)
    
    def has_additional_info(self, obj):
        return bool(obj.additional_info)
    has_additional_info.boolean = True

    def get_url(self, obj):
        return '<a href="%s" target="_blank">%s</a>' % (obj.url, obj.url)
    get_url.short_description = 'URL'
    get_url.allow_tags = True

admin.site.register(DomainDetail, DomainDetailAdmin)
