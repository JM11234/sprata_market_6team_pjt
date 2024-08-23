from . import views
from django.urls import path, include

app_name = "products"
urlpatterns = [
    path('create/',views.create, name='product_create'),
    path('<int:pk>/detail/',views.detail,name='product_detail'),
    path('<int:pk>/delete/', views.delete,name='product_delete'),
    path('<int:pk>/update/',views.update,name='product_update'),
    path('<int:pk>/comment_create/',views.comment_create,name='comment_create'),
    path('<int:pk>/comment_delete/',views.comment_delete,name='comment_delete'),
    # path('<int:pk>/like/', views.like, name="product_like"),
]
