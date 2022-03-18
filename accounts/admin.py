from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import User

# Register your models here.
class AccountAdmin(UserAdmin):
	list_display = ('email', 'username', 'date_joined', 'last_login', 'is_active', 'is_admin', 'is_superuser')
	search_fields = ('email', 'username')
	readonly_fields = ('id', 'date_joined', 'last_login')

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()


admin.site.site_header = 'Whisky.com Admin Panel'
admin.site.register(User, AccountAdmin)