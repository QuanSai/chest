"""PROJECT_NAME URL Configuration
"""
from django.views.generic.base import TemplateView
from django.contrib import admin
from django.conf.urls import include, url
# Ex: from applications.api.v1.routes import (api_router, my_app_router)

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # Web App Entry
    url(r'^$', TemplateView.as_view(
        template_name="app/index.html"),
        name='index'),

    # API:V1
    # Ex: url(r'^api/v1/', include(api_router.urls)),
    #     url(r'^api/v1/', include(my_app _router.urls)),
]
