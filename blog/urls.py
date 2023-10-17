from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.helloView),
    path('now_date/', views.now_dateView),
    path('goodbye/', views.goodbye),
]