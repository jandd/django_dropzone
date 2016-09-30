from django.conf.urls import url
from .views import UploadImageView

urlpatterns = [
    url(r'^image/upload/$', UploadImageView.as_view(), name="image_upload")
]
