import justpy as jp
from definition import Definition
from webapp.layout import DefaultLayout
from webapp.page import Page
import requests


class Dictionary(Page):
    path = "/dictionary"

    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)

        lay = DefaultLayout(a=wp)
        container = jp.QPageContainer(a=lay)

        div = jp.Div(a=container, classes="bg-gray-200 h-screen")
        jp.Div(a=div, text="Instant English Dictionary", classes="text-4xl m-2")
        jp.Div(a=div, text="Get the definition of any English word instantly as you type", classes="text-lg")

        input_div = jp.Div(a=div, classes="grid grid-cols-2")
        output_div = jp.Div(a=div, classes="m-2 p-2 text-lg border-2 h-40")

        input_box = jp.Input(a=input_div, placeholder="Enter an English word",
                 classes="m-2 bg-gray-100 border-2 border-gray-200 rounded w-64 focus:bg-white focus:outline-none focus:border-purple-500 "
                         "py-2 px-4 ", outputdiv=output_div)
        input_box.on("input", cls.get_definition)
        # jp.Button(a=input_div, text="Get Definition", classes="border-2 border-gray-300 text-gray-500", click=cls.get_definition,
        #           outputdiv=output_div, inputbox=input_box)

        return wp

    # get_definition with button with input box
    @staticmethod
    def get_definition(widget, msg):
        # get difinition w/o api
        # defined = Definition(widget.value).get()

        # get definition via api
        req = requests.get(f"http://127.0.0.1:8000/api?w={widget.value}")
        data = req.json()
        widget.outputdiv.text = " ".join(data['definition'])

    # get_definition with button
    # @staticmethod
    # def get_definition(widget, msg):
    #     defined = Definition(widget.inputbox.value).get()
    #     widget.outputdiv.text = " ".join(defined)






