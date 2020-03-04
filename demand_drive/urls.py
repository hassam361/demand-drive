
from django.contrib import admin
from django.urls import path
from website import views as web_views
from users import views as user_views
from django.contrib.auth import views as auth_views 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', web_views.home, name='home'),
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'),name='logout'),
    path('register/',user_views.register,name='register'),
]
