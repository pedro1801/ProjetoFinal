import flet as ft
from flet_route import Params, Basket


class Inserir:
    def __init__(self):
        print('oi')

    def page2(self, page: ft.Page, params: Params, basket: Basket):
        return ft.View(
            "/page2/FletApp",

            controls=[

                # ft.Text(" THis is the page 2 view"),
                ft.ElevatedButton('go to back home page', on_click=lambda _: page.go('/')),
                ft.Stack(
                    [
                        ft.Row(
                            [
                                ft.Container(

                                    ft.Dropdown(
                                        hint_text="Gera",
                                        options=[
                                            ft.dropdown.Option("Teste2"),
                                            ft.dropdown.Option("teste3")
                                        ],
                                    ),

                                ),
                            ],
                        ),
                    ],
                ),
            ]
        )
