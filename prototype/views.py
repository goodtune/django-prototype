from django.shortcuts import render

from prototype.helpers import get_page
from prototype.helpers import get_template


def prototype(request, path):
    page = get_page(path)
    context = page['context']
    return render(request, get_template(path), context)
