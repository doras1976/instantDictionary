import justpy as jp

from webapp.dictionary import Dictionary
from webapp.home import Home
from webapp.about import About

imports = list(globals().values())

for obj in imports:
    if hasattr('path'):
        jp.Route(obj.path, obj.serve)
#
# jp.Route(Home.path, Home.serve)
# jp.Route(About.path, About.serve)
# jp.Route(Dictionary.path, Dictionary.serve)


jp.justpy(port=8001)
