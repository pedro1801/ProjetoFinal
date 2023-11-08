import flet as ft
from flet_route import Routing, path
import Vision.Visao as Visao
import Vision.InserirValores as Inserir
import Vision.InformarValores as Informa
import Vision.Grafo as GrafosProfundidade
Insert = Inserir.Inserir.secundaria
Valore = Informa.Informar.Valores
Grafo1 = GrafosProfundidade.GrafoProfundidade.secundaria
#Page1 = teste.Page1
Home = Visao.Visao.Home
class Main:
    def __init__(self):
        def main(page: ft.Page):
            page.title="ProjetoFinal"
            page.window_height = 900
            page.window_width = 700
            page.window_maximizable = False
            page.window_center()
            app_routes = [
                path(url = "/",clear = True ,view=Home),
                path(url = "/inserir/:my_id",clear = True, view=Insert),
                path(url = "/Valores/:my_id",clear = True, view=Valore),
                path(url = "/GrafoP/:my_id",clear= True, view=Grafo1)
            ]

            Routing(page=page, 
                    app_routes=app_routes )
            page.go(page.route)
        ft.app(target = main)