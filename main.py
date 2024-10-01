import inspect

import justpy as jp

from webapp.page import Page
from webapp.dictionary import Dictionary
from webapp.home import Home
from webapp.about import About

imports = list(globals().values())

for obj in imports:
    if inspect.isclass(obj):
        if issubclass(obj, Page) and hasattr(obj, 'path'):
            jp.Route(obj.path, obj.serve)

jp.justpy(port=8001)
