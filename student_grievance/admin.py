from django.contrib import admin
from django.http import HttpResponse

# Register your models here.
from student_grievance.models import first,report_data,login_data,register_data

class firstAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'Website','description')
    search_fields = ('name', 'email')

    
admin.site.register(first, firstAdmin)

#action to mark selected reports as Reviewed
def mark_as_reviewed(modeladmin, request, queryset):
    queryset.update(status='Reviewed')
    return 

def mark_as_cleared(modeladmin, request, queryset):
    queryset.update(status='Cleared')
    return 


class reportAdmin(admin.ModelAdmin):
    list_display = ('status_id', 'first_name','last_name', 'email', 'phone', 'Course', 'description', 'images','status')
    search_fields = ('first_name', 'email', 'Course')
    actions = [mark_as_reviewed,mark_as_cleared]  # Adding the action to the admin interface

admin.site.register(report_data, reportAdmin)


class LoginAdmin(admin.ModelAdmin):
    list_display = ('username', 'password')
    search_fields = ('username',)

admin.site.register(login_data, LoginAdmin)

class RegisterAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'username', 'password', 'cpassword')
    search_fields = ('first_name', 'email', 'username')

admin.site.register(register_data, RegisterAdmin)



