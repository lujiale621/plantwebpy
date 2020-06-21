from django.urls import path
from webapp.views import *
from . import views
urlpatterns = [
        path('dht11',Dht11Get.as_view()),
        path('pumb',Pumb.as_view())
        ]
