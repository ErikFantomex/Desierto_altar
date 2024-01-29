from django.contrib.gis import admin
from .models import Category,Place,City


# Register your models here.
admin.site.register(Category)
class CustomGeoAdmin(admin.GISModelAdmin):
  gis_widget_kwargs = {
    'attrs': {
      'default_zoom': 12,
      'default_lon': -110.966667,
      'default_lat': 29.066667
    }
  }
  
@admin.register(Place)
class PlaceAdmin(CustomGeoAdmin):
  pass

@admin.register(City)
class CityAdmin(CustomGeoAdmin):
  pass

