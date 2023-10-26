import flet as ft
from flet_route import Params, Basket

class Teste:
    def __init__(self):
        print('oi')
    def home(self,page: ft.Page, params: Params, basket: Basket):
        return ft.View(
            "/",

            controls= [
                ft.TextField(label="First name", autofocus=True),
                ft.TextField(label="Last name"),
                ft.ElevatedButton("Go to page 1", on_click=lambda _: page.go("/page1/10")),
                ft.ElevatedButton("Go to page 2", on_click=lambda _: page.go("/page2/FletApp")),
            ]
        )
