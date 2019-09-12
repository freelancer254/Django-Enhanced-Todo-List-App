
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView
urlpatterns = [
     path('',views.home,name="home"),
     path('delete/<list_id>',views.delete, name="delete"),
     path('cross_off/<list_id>',views.cross_off, name="cross_off"),
     path('uncross/<list_id>',views.uncross, name="uncross"),
     path('edit/<list_id>',views.edit, name="edit"),
     path('accounts/login/',LoginView.as_view(),name="login"),
     path('accounts/logout/',LogoutView.as_view(next_page='home'),name="logout"),
     path('email/',views.email,name="email"),
  
]
  