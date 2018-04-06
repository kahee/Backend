from django.contrib import admin

# Register your models here.

from .models import CityHotplace, TravelInformation, TravelSchedule, CompanyInformation, CityInformation,TravelInformationImage

admin.site.register(CityInformation)
admin.site.register(CityHotplace)
admin.site.register(CompanyInformation)
admin.site.register(TravelInformation)
admin.site.register(TravelSchedule)
admin.site.register(TravelInformationImage)