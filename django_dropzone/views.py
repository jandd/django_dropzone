from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.views.generic import FormView
from django.conf import settings

from django_dropzone.forms import UploadForm
import json


class UploadImageView(FormView):
    form_class = UploadForm
    success_url = reverse_lazy(getattr(settings, 'DJANGO_DROPZONE_SUCCESS_URL_NAME', 'home'))
    template_name = "django_dropzone/image_upload.html"

    def form_valid(self, form):
        image_file = form.save(commit=True)
        if self.request.is_ajax():
            return HttpResponse(content_type="application/json", content=json.dumps({
                'id': image_file.id,
                'url': image_file.image.url,
            }))
        return super(UploadImageView, self).form_valid(form)
