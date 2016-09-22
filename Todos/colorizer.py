# -*- coding: utf-8 -*-


class _Colorizer(object):
    """Amazing!!"""

    def __init__(self):
        esc = "\x1b["

        self.codes = {}
        self.codes[""] = ""
        self.codes["reset"] = esc + "39;49;00m"

        self.codes["bold"] = esc + "01m"
        self.codes["faint"] = esc + "02m"
        self.codes["standout"] = esc + "03m"
        self.codes["underline"] = esc + "04m"
        self.codes["blink"] = esc + "05m"
        self.codes["overline"] = esc + "06m"

        dark_colors = ["black", "darkred", "darkgreen", "brown", "darkblue",
                       "purple", "teal", "lightgray"]
        light_colors = ["darkgray", "red", "green", "yellow", "blue",
                        "fuchsia", "turquoise", "white"]

        x = 30
        for d, l in zip(dark_colors, light_colors):
            self.codes[d] = esc + "%im" % x
            self.codes[l] = esc + "%i;01m" % x
            x += 1

        del d, l, x

        self.codes["darkteal"] = self.codes["turquoise"]
        self.codes["darkyellow"] = self.codes["brown"]
        self.codes["fuscia"] = self.codes["fuchsia"]
        self.codes["white"] = self.codes["bold"]

    def reset_color(self):
        return self.codes["reset"]

    def colorize(self, color_key, text):
        return self.codes[color_key] + text + self.codes["reset"]

    def ansiformat(self, attr, text):
        """
        Format ``text`` with a color and/or some attributes::

            color       normal color
            *color*     bold color
            _color_     underlined color
            +color+     blinking color
        """
        result = []
        if attr[:1] == attr[-1:] == '+':
            result.append(self.codes['blink'])
            attr = attr[1:-1]
        if attr[:1] == attr[-1:] == '*':
            result.append(self.codes['bold'])
            attr = attr[1:-1]
        if attr[:1] == attr[-1:] == '_':
            result.append(self.codes['underline'])
            attr = attr[1:-1]
        result.append(self.codes[attr])
        result.append(text)
        result.append(self.codes['reset'])
        return ''.join(result)


colorizer = _Colorizer()


def make_colorizer(color):
    """Creates a function that colorizes text with the given color.

    For example:

        green = make_colorizer('darkgreen')
        red = make_colorizer('red')

    Then, you can use:

        print "It's either " + green('OK') + ' or ' + red('Oops')
    """
    def inner(text):
        return colorizer.colorize(color, text)
    return inner
