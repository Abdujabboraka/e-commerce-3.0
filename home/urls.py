from django.urls import path
from .views import homepage, detail, select_by_category, search

urlpatterns = [
    path('', homepage , name='homepage'),
    path('detail/<int:pk>', detail, name='detail'),
    path('wear/<int:category_id>/', select_by_category, name='category'),
    path('search/', search, name='search'),

]