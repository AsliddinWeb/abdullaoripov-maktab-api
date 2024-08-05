from django.contrib import admin
from django.urls import path, include

# Static settings
from django.conf import settings
from django.conf.urls.static import static

# Swagger UI
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Ijod Maktabi API",
      default_version='v1',
      description="Ijod Maktabi API"
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

# Admin custom
admin.site.site_title = "AbdullaOripov-Maktab.Uz"
admin.site.site_header = "Admin panel"
admin.site.index_title = "Dashboard"

urlpatterns = [
    path('admin/', admin.site.urls),

    # Swagger
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    # Api
    path('api/v1/settings/', include('settings_app.urls')),
    path('api/v1/navs/', include('navbar_app.urls')),
    path('api/v1/home/', include('home_app.urls')),
    path('api/v1/page/', include('page_app.urls')),
    path('api/v1/news/', include('news_app.urls')),
    path('api/v1/message/', include('message_app.urls')),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
