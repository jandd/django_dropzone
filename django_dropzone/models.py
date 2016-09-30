from django.db import models
from django.utils.translation import ugettext_lazy as _


class UploadFile(models.Model):
    image = models.ImageField(upload_to="temp_image/%Y/%m/%d", verbose_name=_('Upload file'), width_field='image_width',
                              height_field='image_height')
    image_width = models.IntegerField(default=0)
    image_height = models.IntegerField(default=0)
