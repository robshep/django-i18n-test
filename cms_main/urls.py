from django.urls import path
from django.contrib import admin
# Note 08 include this function but with an alias '_' to make the code neater
from django.utils.translation import gettext_lazy as _

from . import views

# Note 09 the URLS are then translated using _("msg")
urlpatterns = [
    path("", views.show_map, name="map"),
    path(_("about"), views.show_about, name="about"),
    path(_("list"), views.show_rc_list, name="rc_list"),
    path( _("rock/<int:rc_id>"), views.show_rc_detail, name="rc_detail")
]