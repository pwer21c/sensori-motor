from result.models import Action,Result,Mode

from django.contrib import admin

class ActionAdmin(admin.ModelAdmin):
    fieldsets =[
                (None, {'fields':['verbe']}),
                ('Date information',{'fields':['pub_date'],'classes':['collapse']})
                ]
    list_display=('verbe','pub_date')
    search_fields=['verbe']
    
admin.site.register(Action,ActionAdmin)
admin.site.register(Result)
admin.site.register(Mode)
# Create your models here.


    