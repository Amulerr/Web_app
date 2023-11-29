from django.contrib import admin
from .models import Dismissal, Business_trip, Employees, Employment_history

class Dismissal_admin(admin.ModelAdmin):
    
    def s_employee(self,obj):
        return obj.employee.surname
    def n_employee(self,obj):
        return obj.employee.name
    def m_employee(self,obj):
        return obj.employee.middle_name
    
    s_employee.short_description='Фамилия'
    n_employee.short_description='Имя'
    m_employee.short_description='Отчество'

    list_display=('s_employee','n_employee', 'm_employee','id','order','date')
    search_fields=('Employee__surname', 'Employee__name', 'Employee__middle_name')

    raw_id_fields=('employee', )

class Business_trip_admin(admin.ModelAdmin):
    def s_employee(self,obj):
        return obj.employee.surname
    def n_employee(self,obj):
        return obj.employee.name
    def m_employee(self,obj):
        return obj.employee.middle_name
    
    s_employee.short_description='Фамилия'
    n_employee.short_description='Имя'
    m_employee.short_description='Отчество'

    list_display=('s_employee','n_employee', 'm_employee','id','days','city')
    search_fields=('Employee__surname', 'Employee__name', 'Employee__middle_name')

    raw_id_fields=('employee', )

class Employees_admin(admin.ModelAdmin):
    list_display=('id','surname','name','middle_name','email')
    search_fields=('surname','name')

class Employment_history_admin(admin.ModelAdmin):

    def s_employee(self,obj):
        return obj.employee.surname
    def n_employee(self,obj):
        return obj.employee.name
    def m_employee(self,obj):
        return obj.employee.middle_name
    
    s_employee.short_description='Фамилия'
    n_employee.short_description='Имя'
    m_employee.short_description='Отчество'

    list_display=('s_employee','n_employee', 'm_employee','organisation','reason','position')
    
    search_fields=('Employee__surname', 'Employee__name', 'Employee__middle_name')

    raw_id_fields=('employee', )


admin.site.register(Employees,Employees_admin)
admin.site.register(Employment_history, Employment_history_admin)
admin.site.register(Dismissal, Dismissal_admin)
admin.site.register(Business_trip,Business_trip_admin)