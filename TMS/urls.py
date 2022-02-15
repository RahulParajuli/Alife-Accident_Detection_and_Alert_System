from django.urls import  path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.index, name='index'),
    path('profile/', views.profile, name='profile'),
    path('register', views.register_view, name="register"),
    path('features', views.features, name="features"),
    path('login', views.login_view, name = "login"),
    path('about', views.about, name = "about"),
    path('authenticate', views.register),
    path('validate', views.login_check),
    path('news', views.news),
    path('road_condition', views.road_cond),
    path('dashboard', views.dashboard),
    path('contact', views.contact),
    path('traffic_update', views.traffic_update),
    # path('logout', views.logout_view),
]