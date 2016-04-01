import yaml
import os.path

from django.http import Http404


def get_page(path):
    url = ('/%s/' % path) if path else '/'
    with open('prototype.yml') as f:
        data = yaml.load(f)
    try:
        return data['urls'][url] or {}
    except KeyError:
        raise Http404("Requested %s page not found." % url)


def get_template(path):
    candidates = [
        os.path.join(path, 'index.html'),
        '%s.html' % path,
    ]
    for template in candidates:
        if os.path.exists(os.path.join('templates', template)):
            return template
