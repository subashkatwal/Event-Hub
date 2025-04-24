from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),  # Admin panel URL
    path('user/', include('user.urls')),  # User-related URLs
    path('event/', include('event.urls')),  # Event-related URLs
    path('', include('event.urls')),
    
    
    # Login URL configuration
    path('accounts/login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
