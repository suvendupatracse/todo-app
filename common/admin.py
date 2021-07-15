from django.contrib import admin
from django.contrib.auth.models import Group


from common.models import User

admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass
