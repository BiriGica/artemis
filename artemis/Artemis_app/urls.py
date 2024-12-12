from django.urls import path
from Artemis_app import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('registrar/', views.regitrarRelatos, name='regitrarRelatos')
]