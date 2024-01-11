from .import views
from django.urls import path, include

app_name = 'shop'
urlpatterns = [
    path('', views.allprodcat, name='allprodcat'),
    path('<slug:c_slug>/', views.allprodcat, name='product_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/', views.proDetail, name='proCatdetail')
]