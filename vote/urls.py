from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView
from home import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('home',views.homy,name='home'),
    path('',views.ind,name='ind'),
    path('logoutuser/',views.logoutuser,name='logoutuser'),
]
urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
