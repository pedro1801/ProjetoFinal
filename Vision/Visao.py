import flet as ft
from flet_route import Params, Basket
import Control.Controle as Controle2

class Visao:
    def Home(page: ft.Page, params: Params, basket: Basket):
                page.title="ProjetoFinal"
                page.window_height = 900
                page.window_width = 700
                page.window_maximizable = False
                page.window_center()
                def on_hover(e):
                    e.control.bgcolor = ft.colors.CYAN_ACCENT_700 if e.data == "true" else ft.colors.BLUE_700
                    e.control.update()
                def Mostrar(e):
                    page.go("/Valores/2")
                def dropdown_changed(e):
                    Valores = e.control.value
                    if Valores == "Profundidade":
                         Controle2.Controle2(0,Valores,0,0)
                         page.go("/GrafoP/3")
                         Valores = 0
                    if Valores == "Largura":
                         Controle2.Controle2(0,Valores,0,0)
                         page.go("/GrafoP/3")
                         Valores=0 
                    if Valores == "Inserir":
                        Valores = 0
                        page.go("/inserir/1")
                    Controle2.Controle2(0,Valores,0,0)
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
                                            on_hover=on_hover,
                                            bgcolor=ft.colors.BLUE_700,
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
                                                    ft.dropdown.Option("HashTable"),
                                                ],
                                                alignment=ft.alignment.center,
                                            ),
                                            on_hover=on_hover,
                                            bgcolor=ft.colors.BLUE_700,
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
                                                on_change=dropdown_changed,
                                                #color=ft.colors.WHITE,
                                                options=[
                                                    ft.dropdown.Option("Largura"),
                                                    ft.dropdown.Option("Profundidade"),
                                                ],
                                                alignment=ft.alignment.center,
                                            ),
                                            on_hover=on_hover,
                                            bgcolor=ft.colors.BLUE_700,
                                            border_radius=10
                                        ),
                                    ],
                                    left=350,
                                ),
                                ft.Row(
                                    [
                                        ft.Container(
                                            ft.ElevatedButton(text="Buscar",width=150,height=50,on_click=Mostrar,bgcolor=ft.colors.BLUE_700,color=ft.colors.BLACK,on_hover=on_hover),
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
        self.Valores = 1
        self.Home