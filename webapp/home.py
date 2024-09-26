import justpy as jp


class Home:
    path = '/'

    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)

        layout = jp.QLayout(a=wp, view="hHh lpR fFf")
        header = jp.QHeader(a=layout)
        toolbar = jp.QToolbar(a=header)
        drawer = jp.QDrawer(a=layout, show_if_above=True, v_model="left", bordered=True)
        jp.QBtn(a=toolbar, dense=True, flat=True, round=True, icon="menu",
                click=cls.remove_drawer, drawer=drawer)
        jp.QToolbarTitle(a=toolbar, text="Instant dictionary")

        container = jp.QPageContainer(a=layout)

        div = jp.Div(a=container, classes="bg-gray-200 h-screen p-2")
        jp.Div(a=div, text="This is the home page", classes="text-4xl m-2")
        jp.Div(a=div, text="""
            kfljsflijdslif;jdsdlifjdsfl;idjfl;djfli;djfl;i
            """, classes="text-lg")
        return wp

    @staticmethod
    def remove_drawer(widget, msg):
        if widget.drawer.value:
            widget.drawer.value = False
        else:
            widget.drawer.value = True


