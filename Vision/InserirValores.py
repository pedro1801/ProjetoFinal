import flet as ft
from flet_route import Params, Basket
import Control.Controle as Controle2
class Inserir:
    def secundaria(page: ft.Page, params: Params, basket: Basket):
        page.title="ProjetoFinal"
        page.window_height = 900
        page.window_width = 700
        page.window_maximizable = False
        page.window_center()
        def on_hover(e):
            e.control.bgcolor = ft.colors.CYAN_ACCENT_700 if e.data == "true" else ft.colors.BLUE_700
            e.control.update()
        def Voltar(e):
            page.go("/")
        def Salvar_Nome(e):
            Nome = e.control.value
            Controle2.Controle2(0,0,Nome,0)
        def Salvar_Codigo(e):
            Codigo = e.control.value
            #Codigo = int(Codigo)                   
            Controle2.Controle2(0,0,0,Codigo)
        def Inserir(e):
            Controle2.Controle2(0,"Inserir",0,0)
            page.go('/')
        return ft.View(
            "/inserir/:my_id",

            controls=[
                ft.TextField(label="Nome",on_change=Salvar_Nome),
                ft.TextField(label="Codigo",on_change=Salvar_Codigo),
                ft.Stack
                (
                    [
                        ft.Row
                        (
                            [
                                ft.Container
                                (
                                    ft.ElevatedButton('Inserir', on_click =Inserir,bgcolor=ft.colors.BLUE_700,color=ft.colors.BLACK,on_hover=on_hover),
                                    ft.ElevatedButton("Voltar",on_click=Voltar,left=80,bgcolor=ft.colors.BLUE_700,color=ft.colors.BLACK,on_hover=on_hover),
                                ),
                            ],
                        ),
                        ft.Row
                        (
                            [
                                ft.Container
                                (
                                    ft.ElevatedButton("Voltar",on_click=Voltar,bgcolor=ft.colors.BLUE_700,color=ft.colors.BLACK,on_hover=on_hover),
                                ),
                            ],
                            left=100
                        ),

                    ],
                ),
            ]
        )
    def __init__(self):
        self.secundaria