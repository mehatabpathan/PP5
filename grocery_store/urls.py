"""grocery_store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.defaults import page_not_found
from django.shortcuts import render

from django.http import HttpResponseRedirect

class NotFoundRedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if response.status_code == 404:
            # Redirect to your custom 404 page
            return HttpResponseRedirect('/custom_404/')
        return response

def custom_page_not_found(request, exception):
    return render(request, '404.html', status=404)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    path('products/', include('products.urls')),
    path('bag/', include('bag.urls')),
    path('checkout/', include('checkout.urls')),
    path('profile/', include('profiles.urls')),
    path('contact/', include('contact.urls')),
    path('blog/', include('blog.urls')),
    path('custom_404/', custom_page_not_found, name='custom_404'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'grocery_store.views.custom_page_not_found'

# Serve custom error pages when DEBUG is True
if settings.DEBUG:
    from django.views import defaults as default_views

    urlpatterns += [
        path('404/', default_views.page_not_found, kwargs={'exception': Exception('Not Found')}),
        path('400/', default_views.bad_request, kwargs={'exception': Exception('Bad Request')}),
        path('403/', default_views.permission_denied, kwargs={'exception': Exception('Permission Denied')}),
        path('500/', default_views.server_error),
    ]
