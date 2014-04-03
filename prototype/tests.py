from django.template import TemplateDoesNotExist
from django.test import TestCase
from django.test.utils import override_settings


class PrototypeTest(TestCase):

    urls = 'prototype.urls'

    def test_template_does_not_exist(self):
        with self.assertRaises(TemplateDoesNotExist):
            res = self.client.get('/path/does/not/exist/')
