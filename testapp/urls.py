from django.urls import path

from .views import show_categories, show_node


urlpatterns = [
    path('', show_categories, name='index'),
    path('node/<int:pk>/', show_node, name='node'),
]
