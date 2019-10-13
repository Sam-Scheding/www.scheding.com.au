from django.contrib import admin
from api.account_details.models import UserDetails, Link
# Register your models here.
admin.site.register(UserDetails)
admin.site.register(Link)
