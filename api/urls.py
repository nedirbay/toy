from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('banners/',views.Banners.as_view()),
    path('categories/',views.CatagoriesList.as_view()),
    path('items/<slug:slug>',views.ItemList.as_view()),
    path('itemdetail/<slug:slug>',views.ItemWithFiles.as_view()),
    path('orders/', views.OrderCreateView.as_view(), name='order-create'),

]
