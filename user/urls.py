from django.urls import path

from user import views


app_name = 'user'

urlpatterns = [
    path('users', views.ListUserView.as_view(), name='list'),
    path('users/create/', views.CreateUserView.as_view(), name='create'),
    path('users/token/', views.CreateTokenView.as_view(), name='token'),
    path('users/me/', views.ManageUserView.as_view(), name='me'),
]
