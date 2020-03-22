
from django.contrib import admin
from django.urls import path
from website import views as web_views
from users import views as user_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views 

from website import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('demand/<int:pk>/', web_views.DemandDetailView, name='demand-detail'),
    path('', web_views.DemandListView.as_view(), name='home'),
    path('demand/new/', web_views.DemandCreateView.as_view(), name='demand-create'),
    path('demand/<int:pk>/update/', web_views.DemandUpdateView.as_view(), name='demand-update'),
    path('demand/<int:pk>/delete/', web_views.DemandDeleteView.as_view(), name='demand-delete'),
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'),name='logout'),
    path('register/',user_views.register,name='register'),
    path('demand/<int:pk>/vote',web_views.VoteToggle.as_view(),name='demand-vote'),
    path('api/demand/<int:pk>/vote',web_views.VoteApiToggle.as_view(),name='api-demand-vote'),
    path('demand/<int:pk>/review/', web_views.ReviewDemand.as_view(),name='review-demand')
   
   
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)