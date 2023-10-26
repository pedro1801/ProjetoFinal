import flet as ft
from flet_route import Params, Basket
class teste:
    def Page1(page: ft.Page, params: Params, basket: Basket):

        return ft.View(
            "/page1/:my_id",

            controls = [

                ft.Text(" THis is the page 1 view"),
                ft.ElevatedButton('go to back home page', on_click = lambda _: page.go('/'))
            ]
        )