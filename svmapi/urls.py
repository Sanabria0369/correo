from django.urls import path
from .views import clasificar
urlpatterns = [ path('clasificar/', clasificar) ]
