from django.contrib import admin
from company_users.models import CompanyUser

class AdminCompanyUser(admin.ModelAdmin):
    list_display = ('id', 'email', 'name', 'type', 'date_joined')
    search_fields = ('id', 'email', 'name', 'type')
    list_filter = ('type', 'date_joined')

admin.site.register(CompanyUser, AdminCompanyUser)