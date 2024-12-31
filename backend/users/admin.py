from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Company, Director, HistoricalChange

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'phone_number')  # Customize as needed
    search_fields = ('username', 'email', 'first_name', 'last_name')
class DirectorInline(admin.TabularInline):
    model = Director
    extra = 1  # Number of empty forms to display in the inline

class HistoricalChangeInline(admin.TabularInline):
    model = HistoricalChange
    extra = 1  # Number of empty forms to display in the inline

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'legal_form', 'registration_date', 'legal_status', 'headquarters', 'sector')
    search_fields = ('name', 'uid')
    list_filter = ('legal_status', 'sector')
    inlines = [DirectorInline, HistoricalChangeInline]

class DirectorAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'company')
    search_fields = ('name', 'role')
    list_filter = ('company',)

class HistoricalChangeAdmin(admin.ModelAdmin):
    list_display = ('company', 'change_type', 'date')
    search_fields = ('company__name', 'change_type')
    list_filter = ('change_type', 'company')

# Register the models with the custom admin classes
admin.site.register(Company, CompanyAdmin)
admin.site.register(Director, DirectorAdmin)
admin.site.register(HistoricalChange, HistoricalChangeAdmin)