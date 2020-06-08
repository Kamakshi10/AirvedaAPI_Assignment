
from django.contrib import admin
from django.urls import path
from iotapp.models import devices 
from iotapp.views import homeView,list, retrieve,create,delete,retrieve_readings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homeView),
    path('list/',list),
    path('retrieve/<int:pk>/',retrieve),
    path('create/',create),
    path('delete/<int:pk>/',delete),
    path('retrieve_readings/<str:pk>/readings/<str:parameter>/<str:starton>/<str:endon>/',retrieve_readings),
    

]
