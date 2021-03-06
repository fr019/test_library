from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model

from test_library.users.forms import UserChangeForm, UserCreationForm

User = get_user_model()


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):

    form = UserChangeForm
    add_form = UserCreationForm
    fieldsets = (
                    ("User", {"fields": ("name",)}),
                    (None, {'fields': ('username', 'password')}),
                    ('Personal info', {'fields': ('first_name', 'middle_name', 'last_name', 'email')}),
                    ('Permissions', {
                        'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
                    }),
                    ('Important dates', {'fields': ('last_login', 'date_joined')}),
                 )
    list_display = ["username", "get_full_name", "is_superuser"]
    search_fields = ["name"]
