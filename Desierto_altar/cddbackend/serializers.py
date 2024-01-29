from .models import Category,Place,City
from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields ='__all__'

class PlaceSerializer(GeoFeatureModelSerializer):
    #Llave foranea
  categories = serializers.SlugRelatedField(queryset=Category.objects.all(), slug_field='category_name')
  
  class Meta:
    model = Place
    geo_field ='point_geom'
    
    fields =(
        'pk',
        'categories',
        'place_name',
        'description',
        'created_at',
        'modified_at',
        'image',
    )
#Clase para obtener las ciudades mas cercanas 

#De la misma manera poder Georeferenciar los ejemplares en un radio de proximidad 

class CitySerializer(GeoFeatureModelSerializer):
    proximity = serializers.SerializerMethodField('get_proximity')


    def get_proximity(self,obj):
        if obj.distance:
            return f'{obj.distance.km:.1f} km' if obj.distance.km >= 1 else f'{obj.distance.m:.1f} m'
        return False 
    
    class Meta:
        model = City
        geo_field ='point_geom'

        fields =(
            'pk',
            'name',
            'proximity'
        )
