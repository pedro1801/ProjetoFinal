import os
import shutil
import flet as ft
from flet_route import Params, Basket
class GrafoProfundidade:
    def secundaria(page: ft.Page, params: Params, basket: Basket):
        def limpar():
            page.clean()
        def on_hover(e):
            e.control.bgcolor = ft.colors.CYAN_ACCENT_700 if e.data == "true" else ft.colors.BLUE_700
            e.control.update()
        def Voltar(e):
            page.go("/")
        page.title="ProjetoFinal"
        page.window_height = 900
        page.window_width = 700
        page.window_maximizable = False
        page.window_center()
        page.update()

        images = ft.GridView(
            expand=5,
            runs_count=5,
            max_extent=680,
            child_aspect_ratio=1.3,
            spacing=5,
            run_spacing=3,
        )
        for i in range(1, 5):
            images.controls.append(
            ft.Image(
                src=f"Imagens/image{i}.png",
                fit=ft.ImageFit.NONE,
                repeat=ft.ImageRepeat.NO_REPEAT,
                border_radius=ft.border_radius.all(75),
            )
        )
        page.update()

        return ft.View(
            "/GrafoP/:my_id",
            controls=[
                images,
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
                    ],
                ),
                
            ],
        )
    
    def __init__(self):
        self.secundaria