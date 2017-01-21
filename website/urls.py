from django.conf.urls import url
from django.utils.translation import ugettext as _
from django.views.generic.base import RedirectView

from .views import IndexView, RecipeView

favicon_view = RedirectView.as_view(url='/static/favicon.ico', permanent=True)

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    # Translators: recipe is the parent tag of a recipe
    url(r'^' + _("recipe") + '/(?P<slug>\w+)$', RecipeView.as_view(), name='recipe'),
    url(r'^favicon\.ico$', favicon_view),
]
