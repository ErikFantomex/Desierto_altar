from django.shortcuts import render

# Create your views here.
def placeListMap(request):
    return render(request,'cddfrontend/places_base.html')
