from django.contrib import admin

from myapp.models import signup
from myapp.models import Booking
# Register your models here.
admin.site.register(signup)
admin.site.register(Booking)