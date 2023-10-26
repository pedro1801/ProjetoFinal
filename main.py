import flet as ft
from flet_route import Routing, path
from Vision.Visao import Visao
from Vision.InserirValores import Inserir
from Vision.teste import Teste

def main(page: ft.Page):
    x = Visao()
    y = Inserir()
    z = Teste()
    app_routes = [
        path(url="/", clear=True, view=z.home),
        path(url="/page1/:my_id", clear=True, view=x.teste2),
        path(url="/page2/:name", clear=True, view=y.page2)
    ]

    Routing(page=page,
            app_routes=app_routes)

    page.go(page.route)


ft.app(target=main)
