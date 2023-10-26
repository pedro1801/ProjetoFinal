import flet as ft
from flet_route import Params, Basket
class Inserir:
    def secundaria(page: ft.Page, params: Params, basket: Basket):
        #page.window_center()
        return ft.View(
            "/inserir/:my_id",
            #page.window_height=600,
            #page.window_width = 400,
            #page.window_min_height = 600
            #page.window_max_height = 600
            #page.window_max_width = 400
            #page.window_min_width = 400
            #page.window_maximizable = False
            #page.window_full_screen = True
            #page.window_always_on_top = True
            #page.window_center()
            controls=[
                #ft.TextField(label="First name", autofocus=True),
                #ft.TextField(label="Last name"),
                ft.ElevatedButton('go to back home page', on_click = lambda _: page.go('/')),
            ]
            #def btn_click(e):
            #    greetings.controls.append(ft.Text(f"Hello, {first_name.value} {last_name.value}!"))
            #    first_name.value = ""
            #    last_name.value = ""
            #    page.update()
            #    first_name.focus()
            #    page.window_destroy()
        )
    def __init__(self):
        self.secundaria