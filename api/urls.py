from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('categories/',views.CatagoriesList.as_view()),
    path('items/<slug:slug>',views.ItemList.as_view()),
]
