from django.contrib import admin
from .models import Volunteer,End_user,Family_grp,Scheme,Linked_Scheme,Gender
# Register your models here.
admin.site.register(Volunteer)
admin.site.register(End_user)
admin.site.register(Family_grp)
admin.site.register(Scheme)
admin.site.register(Linked_Scheme)
# admin.site.register(Gender)