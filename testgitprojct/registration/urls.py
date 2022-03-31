from django.urls import path
from . import views

urlpatterns = [
    path('reg', views.RegUser.as_view(), name='register'),
    path('auth', views.AuthUser.as_view(), name='auth'),
    path('prof', views.prof, name='prof'),
]
