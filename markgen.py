def header(content, depth=1, underline=False):
    if underline:
        char = ('=', '-', '*')[((depth-1) if depth < 4 else 3)]
        return "{0}\n{1}".format(content, (char * len(content)))
    return "{0} {1}".format(('#' * depth), content)


def quote(content, prefix='> '):
    return "\n".join("{0}{1}".format(prefix, c) for c in content.split("\n"))


def paragraph(content):
    return "{0}\n\n".format(content)


def emphasis(content, strength=1, char='*'):
    return "{0}{1}{0}".format((char * strength), content)


def ulist(content, marker='*'):
    return "\n".join("* {0}".format(c) for c in content)


def olist(content):
    return "\n".join("{0}. {1}".format((i + 1), c) for i, c in enumerate(content))


def link(content, address, title=None):
    title = ' "{0}"'.format(title) if title is not None else ''
    return "[{0}]({1}{2})".format(content, address, title)


def image(content, address, title=None):
    return "!{0}".format(link(content, address, title))


def pre(content, inline=False):
    if inline:
        return "`{0}`".format(content)

    return quote(content, '    ')
