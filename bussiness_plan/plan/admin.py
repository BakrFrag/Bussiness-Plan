from django.contrib import admin
from .models import BussinessPlan , Question , Section
# Register your models here.
admin.site.register([Section,Question,BussinessPlan])
