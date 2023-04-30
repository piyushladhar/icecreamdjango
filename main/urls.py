from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path("",views.index,name="index"),
    path("register/",views.register,name="register"),
    path("login/",views.login,name="login"),
    path("logout/",views.user_logout,name="logout"),
    path("order/<int:id>",views.order,name="order")
]
