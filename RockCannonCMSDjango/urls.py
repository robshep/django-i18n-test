
"""
URL configuration for RockCannonCMSDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import include,path

# Note 06 import i18n_patterns
from django.conf.urls.i18n import i18n_patterns

import cms_main.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    # Note 13 this is needed for the language switcher
    path('i18n/', include('django.conf.urls.i18n')),
]

# NOTE 07 include the app module using i18n_patterns (my main module is called cms_main)
urlpatterns += i18n_patterns(
    path('', include("cms_main.urls")),
)

