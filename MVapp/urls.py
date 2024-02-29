from django.urls import path
from MVapp import views
app_name = 'MVapp'

urlpatterns = [
path('', views.index, name='index'),
]
