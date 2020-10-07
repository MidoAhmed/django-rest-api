from django.urls import path, include
from . import views

app_name = 'adoptions'
urlpatterns = [
    path('', views.home, name='home'),
    path('<int:pet_id>/', views.pet_detail, name='pet_detail')
]
