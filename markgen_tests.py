import os
import unittest

from markgen import (paragraph, link, image, ulist, emphasis, header, quote,
                     olist, pre)


class MarkgenTests(unittest.TestCase):

    def test_pagagraph(self):
        p = paragraph('hello world')
        assert p == "hello world\n\n"

    def test_link(self):
        l = link('click here', 'http://www.example.com/')
        assert l == '[click here](http://www.example.com/)'

        l = link('click there!', 'https://localhost', 'please')
        assert l == '[click there!](https://localhost "please")'

    def test_image(self):
        i = image('kitty!', 'http://example.com/kitty.jpg')
        assert i == '![kitty!](http://example.com/kitty.jpg)'

        i = image('nuther kitty', 'https://localhost/nutherkitty.gif',
                'herp derp')
        assert i == ('![nuther kitty](https://localhost/nutherkitty.gif'
                ' "herp derp")')

    def test_ulist(self):
        l = ulist(['foo bar',
                   'bar baz!',
                   1337])
        assert l == '* foo bar\n* bar baz!\n* 1337'

    def test_olist(self):
        l = olist(['foo bar',
                   'bar baz!',
                   1337])
        assert l == '1. foo bar\n2. bar baz!\n3. 1337'

    def test_emphasis(self):
        b = emphasis('hello dolly')
        assert b == '*hello dolly*'

        b = emphasis('hello molly', 2)
        assert b == '**hello molly**'

        b = emphasis('hello my baby', 3, '_')
        assert b == '___hello my baby___'

    def test_header(self):
        h = header('the title')
        assert h == '# the title'

        h = header('the subtitle', 3)
        assert h == '### the subtitle'

        h = header('title 1', 1, True)
        assert h == 'title 1\n======='

        h = header('title 2', 2, True)
        assert h == 'title 2\n-------'

        h = header('title 3', 3, True)
        assert h == 'title 3\n*******'

    def test_quote(self):
        q = quote('this is the winter\nof our disco\ntest.')
        assert q == '> this is the winter\n> of our disco\n> test.'

        # Not valid markdown, but something the function can produce, as used
        # by pre()
        q = quote('this is the winter\nof our disco\ntest.', '||')
        assert q == '||this is the winter\n||of our disco\n||test.'

    def test_pre(self):
        p = pre('this quick brown fox\njumped over the\nlazy codeblock.')
        assert p == '    this quick brown fox\n    jumped over the\n    lazy codeblock.'

        p = pre('echo "hello world!"', True)
        assert p == '`echo "hello world!"`'
    
    def test_generate_document(self):
        content = ''
        content += paragraph('Hello world!')
        content += paragraph(
                link('go here', 'http://example.com/')
                + ' or have a '
                + image('kitten',
                    'http://www.catster.com/files/post_images/'
                    '35653cc7aab32e647da2cd81e37ed1c9.gif'))
        content += ulist(['foobar',
                          'well hello there',
                          emphasis('yo momma')])

        base_path = os.path.abspath(os.path.dirname(__file__))
        file_content = open(os.path.join(base_path,
            'markgen_test_doc.md'), 'r').read()[:-1]

        assert content == file_content


if __name__ == '__main__':
    unittest.main()
