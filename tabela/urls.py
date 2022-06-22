from django.urls import path

from . import views

app_name = 'tabela'
urlpatterns = [
    path('', views.index, name='index'),
    path('filter', views.filter_tabela, name='filtered'),
    path('<int:pk>/', views.update_option, name='update_source'),
    path('ajax/load-sources', views.load_sources, name='ajax_load_sources'),
    path('add-source/', views.add_source, name='add_source'),
]