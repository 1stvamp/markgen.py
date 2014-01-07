# -*- coding: utf-8 -*-
import os
import unittest

from markgen import (paragraph, link, image, ulist, emphasis, header, quote,
                     olist, pre, inline_pre)


class MarkgenTests(unittest.TestCase):

    def test_pagagraph(self):
        p = paragraph(u'hello world')
        assert p == u"hello world\n\n"

    def test_link(self):
        l = link(u'click here', u'http://www.example.com/')
        assert l == u'[click here](http://www.example.com/)'

        l = link(u'click there!', u'https://localhost', u'please')
        assert l == u'[click there!](https://localhost "please")'

    def test_image(self):
        i = image(u'kitty!', u'http://example.com/kitty.jpg')
        assert i == u'![kitty!](http://example.com/kitty.jpg)'

        i = image(u'nuther kitty', u'https://localhost/nutherkitty.gif',
                u'herp derp')
        assert i == (u'![nuther kitty](https://localhost/nutherkitty.gif'
                u' "herp derp")')

    def test_ulist(self):
        l = ulist([u'foo bar',
                   u'bar baz!',
                   1337])
        assert l == u'* foo bar\n* bar baz!\n* 1337'

    def test_olist(self):
        l = olist([u'foo bar',
                   u'bar baz!',
                   1337])
        assert l == u'1. foo bar\n2. bar baz!\n3. 1337'

    def test_emphasis(self):
        b = emphasis(u'hello dolly')
        assert b == u'*hello dolly*'

        b = emphasis(u'hello molly', 2)
        assert b == u'**hello molly**'

        b = emphasis(u'hello my baby', 3, '_')
        assert b == u'___hello my baby___'

    def test_header(self):
        h = header(u'the title')
        assert h == u'# the title'

        h = header(u'the subtitle', 3)
        assert h == u'### the subtitle'

        h = header(u'title 1', 1, True)
        assert h == u'title 1\n======='

        h = header(u'title 2', 2, True)
        assert h == u'title 2\n-------'

        h = header(u'title 3', 3, True)
        assert h == u'title 3\n*******'

    def test_quote(self):
        q = quote(u'this is the winter\nof our disco\ntest.')
        assert q == u'> this is the winter\n> of our disco\n> test.'

        # Not valid markdown, but something the function can produce, as used
        # by pre()
        q = quote(u'this is the winter\nof our disco\ntest.', u'||')
        assert q == u'||this is the winter\n||of our disco\n||test.'

    def test_pre(self):
        p = pre(u'this quick brown fox\njumped over the\nlazy codeblock.')
        assert p == u'    this quick brown fox\n    jumped over the\n    lazy codeblock.'

        p = pre(u'echo "hello world!"', True)
        assert p == u'`echo "hello world!"`'

        p = inline_pre(u'echo "hello world!"')
        assert p == u'`echo "hello world!"`'
    
    def test_generate_document(self):
        content = ''
        content += paragraph(u'Hello world! ☺')
        content += paragraph(
                link(u'go here', u'http://example.com/')
                + u' or have a '
                + image(u'kitten',
                    u'http://www.catster.com/files/post_images/'
                    u'35653cc7aab32e647da2cd81e37ed1c9.gif'))
        content += ulist([u'foobar',
                          u'well hello there',
                          emphasis(u'yo momma')])

        base_path = os.path.abspath(os.path.dirname(__file__))

        file_content = open(os.path.join(base_path,
            'markgen_test_doc.md'), 'r').read()
        if hasattr(file_content, 'decode'):
            file_content = file_content.decode('utf8')

        file_content = file_content[:-1]

        assert content == file_content


if __name__ == '__main__':
    unittest.main()
