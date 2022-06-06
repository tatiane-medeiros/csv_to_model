from django.urls import path

from . import views

app_name = 'tabela'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.update_option, name='update_source'),
    path('ajax/load-sources', views.load_sources, name='ajax_load_sources'),
]