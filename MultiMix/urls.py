
from django.contrib import admin
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.Home_view,name="home"),
    path("service/",views.Service_view,name="service"),
    path("about/",views.Aboutus_view,name="about"),
    path("gallery/",views.Gallery_view,name="gallery"),
    path("contact/",views.Contact_view,name="contact"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
