import flet as ft
from Control import Controle as Controle2


class Visao:
    def __init__(self):
        self.teste = 0
        def main(page: ft.Page):
            dlg = ft.AlertDialog(
                title=ft.Text(), on_dismiss=lambda e: print("Dialog dismissed!")
            )
            def Mostrar(e):
                self.teste = 1
                Controle2.Controle2(self.teste)
            def dropdown_changed(e):
                self.teste = e.control.value
                Controle2.Controle2(self.teste)
            page.title="ProjetoFinal"
            page.appbar = ft.AppBar(
                bgcolor=ft.colors.GREY,
                actions=[
                    ft.Stack(
                        [
                            ft.Row(
                                [
                                    ft.Container(
                                      ft.Dropdown(
                                            #lable="Gerar Dados"
                                            hint_text="Gerar Dados",
                                            border_radius=10,
                                            width=150,
                                            #color=ft.colors.WHITE,
                                            options=[
                                                ft.dropdown.Option("Automático"),
                                                ft.dropdown.Option("Inserir"),
                                            ],
                                            on_change=dropdown_changed,
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
                                            on_change=dropdown_changed,
                                            width=150,
                                            #color=ft.colors.WHITE,
                                            options=[
                                                ft.dropdown.Option("MergeSort"),
                                                ft.dropdown.Option("QuickSort"),
                                                ft.dropdown.Option("HeapSort"),
                                            ],
                                            alignment=ft.alignment.center,
                                        ),
                                        bgcolor=ft.colors.SURFACE_VARIANT,
                                        border_radius=10
                                    ),
                                ],
                                left=180,
                            ),
                            ft.Row(
                                [
                                    ft.Container(
                                        ft.Dropdown(
                                            hint_text="Grafos",
                                            border_radius=10,
                                            width=150,
                                            #color=ft.colors.WHITE,
                                            options=[
                                                ft.dropdown.Option("Largura"),
                                                ft.dropdown.Option("Profundidade"),
                                            ],
                                            alignment=ft.alignment.center,
                                        ),
                                        bgcolor=ft.colors.SURFACE_VARIANT,
                                        border_radius=10
                                    ),
                                ],
                                left=350,
                            ),
                            ft.Row(
                                [
                                    ft.Container(
                                        ft.ElevatedButton(text="Buscar",width=150,height=50),

                                    ),
                                ],
                                bottom=2,
                                left=520,
                            ),

                        ],
                    ),
                ],
            )
            page.add(ft.ElevatedButton("teste",on_click=Mostrar))
        ft.app(target=main,assets_dir="InserirValores")