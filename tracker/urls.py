from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('applications/', views.application_list, name='application_list'),
    path('applications/create/', views.create_application, name='create_application'),
    path('applications/<int:pk>/edit/', views.update_application, name='update_application'),
    path('applications/<int:pk>/delete/', views.delete_application, name='delete_application'),
    path('applications/<int:pk>/interview/', views.add_interview, name='add_interview'),
    path('applications/<int:pk>/ai-analysis/', views.ai_analysis, name='ai_analysis'),
    path('register/', views.register, name='register'),
]