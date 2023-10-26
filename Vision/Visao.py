import flet as ft
from flet_route import Params, Basket
import Control.Controle as Controle2
import Vision.InserirValores as Inserir

class Visao:
    def Home(page: ft.Page, params: Params, basket: Basket):
                dlg = ft.AlertDialog(
                    title=ft.Text(), on_dismiss=lambda e: print("Dialog dismissed!")
                )
                def Mostrar(e):
                    teste = 1
                    Controle2.Controle2(teste)
                def dropdown_changed(e):
                    teste = e.control.value
                    if teste == "Inserir":
                        print("Vai para o inserir")
                        page.go("/inserir/10")
                    Controle2.Controle2(teste)
                page.title="ProjetoFinal"
                return ft.View(
                    "/",
                    controls=
                    [
                        ft.AppBar(
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
                                            ft.ElevatedButton(text="Buscar",width=150,height=50,on_click=Mostrar),

                                        ),
                                    ],
                                    bottom=2,
                                    left=520,
                                ),

                            ],
                        ),
                    ],
                )
                    ]
                )
    def __init__(self):
        self.teste = 1
        self.Home