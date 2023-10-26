import flet as ft
from flet_route import Params, Basket
from Control import Controle as Controle2


class Visao:
    def __init__(self):
        print('oi')

    def Mostrar(self):
        self.teste = 1
        Controle2.Controle2(self.teste)

    def dropdown_changed(self):
        self.teste = "QuickSort"
        Controle2.Controle2(self.teste)
    def teste2(self, page: ft.Page, params: Params, basket: Basket):
        return ft.View(
            "/page1/:my_id",
            controls=[

                ft.Text(" THis is the page 1 view"),
                ft.ElevatedButton('go to back home page', on_click=lambda _: page.go('/')),
                ft.Stack(
                    [
                        ft.Row(
                            [
                                ft.Container(
                                    ft.Dropdown(
                                        # lable="Gerar Dados"
                                        hint_text="Gerar Dados",
                                        border_radius=10,
                                        width=150,
                                        options=[
                                            ft.dropdown.Option("Automático"),
                                            ft.dropdown.Option("Inserir"),
                                        ],
                                        alignment=ft.alignment.center,
                                    ),
                                    bgcolor=ft.colors.SURFACE_VARIANT,
                                    border_radius=10
                                ),
                            ],
                            left=10,
                        ),
                        ft.Row(
                            [
                                ft.Container(
                                    ft.Dropdown(
                                        hint_text="Ordenação",
                                        border_radius=10,
                                        on_change=self.dropdown_changed(),
                                        width=150,
                                        # color=ft.colors.WHITE,
                                        options=[
                                            ft.dropdown.Option("MergeSort"),
                                            ft.dropdown.Option("QuickSort"),
                                            ft.dropdown.Option("HeapSort"),
                                        ],
                                        alignment=ft.alignment.center,
                                    ),
                                    bgcolor=ft.colors.SURFACE_VARIANT,
                                    border_radius=10,
                                ),
                            ],
                            left=180
                        ),
                    ]
                ),
                page.add(ft.ElevatedButton("teste", on_click=self.Mostrar()))

            ]
        )
