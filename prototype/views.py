import os

from django.views.generic import TemplateView


class PrototypeView(TemplateView):
    """
    Simple ``TemplateView`` subclass that will determine the template path
    dynamically based upon it's urlconf.
    """

    def get_template_names(self):
        return os.path.join('prototype', self.kwargs['path'], 'index.html')


prototype = PrototypeView.as_view()
