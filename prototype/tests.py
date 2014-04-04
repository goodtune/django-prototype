from django.template import TemplateDoesNotExist
from django.test import TestCase
from django.test.utils import override_settings


class PrototypeTest(TestCase):

    urls = 'prototype.urls'

    @override_settings(TEMPLATE_DIRS=())
    def test_template_does_not_exist(self):
        """
        View will not exist because we've overloaded the TEMPLATE_DIRS
        setting so that it will not find the file located at
        ``prototype/path/does/not/exist/index.html`` as a result.
        """
        with self.assertRaises(TemplateDoesNotExist):
            res = self.client.get('/path/does/not/exist/')

    def test_template_now_exists(self):
        """
        Now that we've fallen back to the standard TEMPLATE_DIRS settings the
        template file will be located.
        """
        res = self.client.get('/path/does/not/exist/')
        self.assertContains(res, '<h1>Example</h1>', html=True)

    def test_simple_inheritance(self):
        """
        The template at ``prototype/index.html`` has no implementation of it's
        own and should be returning the primitive base template.
        """
        res = self.client.get('/')
        texts = (
            "<head><title>Untitled</title></head>",
            "<body><h1>Untitled</h1></body>",
        )
        for text in texts:
            self.assertContains(res, text, html=True)

    def test_inheritance_with_blocks(self):
        """
        The template at ``prototype/example/index.html`` overloads each of the
        blocks in the primitive base template.
        """
        res = self.client.get('/example/')
        texts = (
            "<head><title>Example</title></head>",
            "<body><h1>Inheritance</h1><p>See, it works!</p></body>",
        )
        for text in texts:
            self.assertContains(res, text, html=True)
