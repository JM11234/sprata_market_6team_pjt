from . import views
from django.urls import path, include

app_name = "products"
urlpatterns = [
    path('create/',views.create, name='product_create'),
    path('<int:pk>/detail/',views.detail,name='product_detail'),
    path('<int:pk>/delete/', views.delete,name='product_delete'),
]
