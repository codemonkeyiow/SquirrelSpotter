from django.shortcuts import render
from django.views.generic import TemplateView


class Index(TemplateView):
    template_name = 'Spotter/index.html'

    def get(self, request):
        return render(
            request,
            self.template_name,
            {},
        )