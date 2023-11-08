import flet as ft
from flet_route import Params, Basket
import Control.Controle as Controle2
class Informar:
    def Valores(page: ft.Page, params: Params, basket: Basket):
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
            page.clean()
        def Buscar(e):
            cl.clean()
            Controle2.Controle2(0,"HashTable",0,0)
            hash = Controle2.hashTable
            Codigo = Controle2.Codigo
            print(Codigo)
            print(hash.get(Codigo))
            cl.controls.append(ft.Text("Codigo | Nome"))
            cl.controls.append(ft.Text(f"{Codigo} | {hash.get(Codigo)}"))
            page.update()
        def Salvar_Codigo(e):
            Codigo = e.control.value
            Controle2.Controle2(0,0,0,Codigo)
        Nomes = Controle2.Lista_Nome
        Codigos = Controle2.Lista_Codigo
        cl = ft.Column(
            spacing=10,
            height=200,
            width=200,
            scroll=ft.ScrollMode.ALWAYS,
            on_scroll_interval=0,
        )
        cl.controls.append(ft.Text("Codigo | Nome"))
        for i in range(0,len(Codigos)):
            cl.controls.append(ft.Text(f"{Codigos[i]} | {Nomes[i]}", key=str(i)))
            i += 1
        
        return ft.View(
            "/Valores/:my_id",

            controls=[
                ft.Container(cl, border=ft.border.all(1),width=700,height=600),
                ft.Stack
                (
                    [
                        ft.Row
                        (
                            [
                                ft.Container
                                (
                                    ft.ElevatedButton("Voltar",on_click=Voltar,color=ft.colors.BLACK,bgcolor=ft.colors.BLUE_700,on_hover=on_hover),
                                ),
                            ],
                        ),
                        ft.Row
                        (
                            [
                                ft.Container
                                (
                                    ft.ElevatedButton("Buscar",on_click=Buscar,color=ft.colors.BLACK,bgcolor=ft.colors.BLUE_700,on_hover=on_hover),
                                ),
                            ],
                            left=100,
                        ),
                        ft.Row
                        (
                            [
                                ft.Container
                                (
                                    ft.TextField(label="Codigo",on_change=Salvar_Codigo),
                                ),
                            ],
                            left=200,
                            height=30
                        ),

                    ]
                )
            ]
        )
    def __init__(self):
        self.Valores