from django.urls import path
from webapp.views import *
from . import views
urlpatterns = [
        path('dht11',Dht11Get.as_view()),
        path('pumb',Pumb.as_view()),
        path('pumb2',Pumb2.as_view()),
        path('spray',Spray.as_view()),
        path('moudle',Moudlebat.as_view()),
        path('soilmid',SoilGet.as_view()),
        path('deep',DeepGet.as_view()),
        path('light',LightGet.as_view())
        ]
