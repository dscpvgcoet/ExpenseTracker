"""
    Main parth.
"""
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from . import views

admin.autodiscover()

urlpatterns = [

    # Examples:
    # url(r'^$', 'django_723e.views.home', name='home'),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^$', views.home, name='home'),
    url(r'^api/', include("django_723e.api.urls")),
    url(r'^admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
