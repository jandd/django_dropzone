from django.conf.urls import url

from .views import UploadImageView

urlpatterns = [
    url(r'^upload/$', UploadImageView.as_view())
]
