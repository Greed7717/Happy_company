from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello_view),
    path('now_date/', views.now_dateView),
    path('goodbye/', views.goodbye),
    path('', views.post_list_view),
    path('post_detail/<int:id>', views.post_detali_view)
]