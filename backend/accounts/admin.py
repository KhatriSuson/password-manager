from django.contrib import admin
from accounts.models import UserProfile
from credentials.models import Credential
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Credential)