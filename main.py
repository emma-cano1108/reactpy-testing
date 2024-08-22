from reactpy import component, html, use_state
from fastapi import FastAPI
from reactpy.backend.fastapi import configure
app = FastAPI()

questions = [
    {"id":1, "text":"☆"},
    {"id":2, "text":"☆"},
    {"id":3, "text":"☆"},
    {"id":4, "text":"☆"},
    {"id":5, "text":"☆"}
]
def function1(e):
    print("Hello World")

@component
def star(el):
    
    return html.li({"key":el["id"]}, el["text"])

@component
def stars():
    list = [star(el) for el in questions]
    return html.section({"style": {"font-size": "30px"}}, html.ul({"style":{"display": "flex","list-style": "none"}},list))


@component
def App():
    return html.header(
        html.h1({"style":{"background":"black", "color":"white"}}, "Header"),
        html.button("Hola"),
        Question(1),
        Rating(2),
        Question(3),
        Rating(4)
    )

@component
def Question(number):
    return html.div({"style":{"margin-left": "100px"}},
        html.h1({"style":{"font-family": "Jetbrains Mono"}},f"Question {number}"),
        html.p("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus pharetra."),
        html.input({"type":"text", "placeholder": "Escribe aquí", "on_change": function1}),
        html.button({"on_click": function1}, "Continuar")
    )

@component
def Rating(number):
    rating, set_rating = use_state(0)

    return html.div({"style":{"margin-left": "100px"}},
        html.h1({"style":{"font-family": "Jetbrains Mono"}},f"Rating {number}"),
        stars(),
        html.button({"on_click": function1}, "Continuar")
    )

configure(app, App)

   