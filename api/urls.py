
from django.urls import re_path as url
from.views import *
from rest_framework.urlpatterns import format_suffix_patterns
    


urlpatterns = [
  url(r'^api/Usuario/$',usuarioViewSet.as_view())
]
urlpatterns=format_suffix_patterns(urlpatterns)
