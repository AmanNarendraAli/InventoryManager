from django.urls import path
from . import views
app_name = 'invApp'
urlpatterns = [
    path('',views.home_view,name='home'),
    path('list/',views.read_view,name='productlist'),
    path('create/',views.create_view,name='createproduct'),
    path('update/<int:product_id>/',views.update_view,name='updateproduct'),
    path('delete/<int:product_id>/',views.delete_view,name='deleteproduct')
]
