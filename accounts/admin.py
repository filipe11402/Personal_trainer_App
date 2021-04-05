from django.contrib import admin
from .models import CustomUser, PersonalTrainer, Client
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
	list_display = ('username', 'email', 'is_active', 'is_superuser', 'is_pt', 'is_client')

	fieldsets = UserAdmin.fieldsets + (
			('Roles', {'fields': ('is_pt', 'is_client',)}),
		)

	add_fieldsets = UserAdmin.add_fieldsets + (
			('Roles', {'fields': ('is_pt', 'is_client',)}),
		)


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(PersonalTrainer)
admin.site.register(Client)
