import flet as ft
from flet_route import Params, Basket
import Control.Controle as Controle2
class Inserir:
    def secundaria(page: ft.Page, params: Params, basket: Basket):
        global Nome
        global Codigo
        def Salvar_Nome(e):
            Nome = e.control.value
            Controle2.Controle2(0,0,Nome,0)
        def Salvar_Codigo(e):
            Codigo = e.control.value
            Controle2.Controle2(0,0,0,Codigo)
        def Inserir(e):
            Controle2.Controle2(0,"Inserir",0,0)
            page.go('/')
        #page.window_center()
        return ft.View(
            "/inserir/:my_id",
            #page.window_height=600,
            #page.window_width = 400,
            #page.window_min_height = 600
            #page.window_max_height = 600
            #page.window_max_width = 400
            #page.window_min_width = 400
            #page.window_maximizable = False
            #page.window_full_screen = True
            #page.window_always_on_top = True
            #page.window_center()
            controls=[
                #ft.Text(),
                ft.TextField(label="Nome",on_change=Salvar_Nome),
                ft.TextField(label="Codigo",on_change=Salvar_Codigo),
                ft.ElevatedButton('Inserir', on_click =Inserir),
                #ft.ElevatedButton("teste",on_click=print_teste()),
            ]
            #def btn_click(e):
            #    greetings.controls.append(ft.Text(f"Hello, {first_name.value} {last_name.value}!"))
            #    first_name.value = ""
            #    last_name.value = ""
            #    page.update()
            #    first_name.focus()
            #    page.window_destroy()
        )
    def __init__(self):
        self.secundaria