from django.urls import path
from .views import *
from django.views.generic.base import TemplateView
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from django.conf import settings
# TemplateView is built-indjango class based view class which is used to render the request to templates

urlpatterns = [
    # FBV
    # path('',index),
    # path('addfood',addfood),
    path('',TemplateView.as_view(template_name= 'foodapp/index.html'),name='Home'),
    # CBV 
    path('addfood',login_required(FoodCreateView.as_view()),name='AddFood'),
    # FBV
    # path('addfood',AddFood,name='addfood'),
    path('foodlist',login_required(FoodListView.as_view()),name='FoodMenu'),
    path('foodupdate/<pk>',FoodUpdateView.as_view(),name='FoodUpdate'),
    path('fooddelete/<pk>',FoodDeleteView.as_view(),name='FoodDelete'),
    path('fooddetail/<pk>',FoodDetailView.as_view(),name='FoodDetail')

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)