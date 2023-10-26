import flet as ft
from flet_route import Routing, path
import Vision.Visao as Visao
import Vision.InserirValores as Inserir
Teste = Inserir.Inserir.secundaria
#Page1 = teste.Page1
Home = Visao.Visao.Home
class Main:
    def __init__(self):
        def main(page: ft.Page):
            app_routes = [
                path(url = "/",clear = True ,view=Home),
                path(url = "/inserir/:my_id",clear = True, view=Teste),
                #path(url = "/page1/:my_id",clear = True, view=Page1)
            ]

            Routing(page=page, 
                    app_routes=app_routes )
            page.go(page.route)
        ft.app(target = main)