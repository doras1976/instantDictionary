import justpy as jp
from webapp.layout import DefaultLayout
from webapp.page import Page


class Home(Page):
    path = '/'

    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)

        lay = DefaultLayout(a=wp)

        container = jp.QPageContainer(a=lay)

        div = jp.Div(a=container, classes="bg-gray-200 h-screen p-2")
        jp.Div(a=div, text="This is the home page", classes="text-4xl m-2")
        jp.Div(a=div, text="""
            kfljsflijdslif;jdsdlifjdsfl;idjfl;djfli;djfl;i
            """, classes="text-lg")
        return wp




