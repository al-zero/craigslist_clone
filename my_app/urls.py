from django.urls import path
from .views import home_view
from .views import new_search


urlpatterns = [

    path('', home_view, name='home'),

    path('new_search/', new_search, name='new_search')

]
