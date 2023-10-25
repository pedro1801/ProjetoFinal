import flet as ft
teste = 0
def main(page: ft.Page):
    def Mostrar(e):
        teste = 1
    def dropdown_changed(e):
        teste = e.control.value
        secundaria()
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
                                    border_radius=10,
                                    width=150,
                                    #color=ft.colors.WHITE,
                                    options=[
                                        ft.dropdown.Option("Teste"),
                                    ],
                                    alignment=ft.alignment.center,
                                ),
                                bgcolor=ft.colors.SURFACE_VARIANT,
                                border_radius=10
                            ),
                        ],
                        left=350,
                    ),
                ],
            ),
        ],
    )
    def secundaria(page: ft.Page):
            first_name = ft.TextField(label="First name", autofocus=True)
            last_name = ft.TextField(label="Last name")
            greetings = ft.Column()
            page.window_height=600
            page.window_width = 400
            page.window_min_height = 600
            page.window_max_height = 600
            page.window_max_width = 400
            page.window_min_width = 400
            page.window_maximizable = False
            page.window_full_screen = True
            page.window_always_on_top = True
            page.window_center()
            def btn_click(e):
                greetings.controls.append(ft.Text(f"Hello, {first_name.value} {last_name.value}!"))
                first_name.value = ""
                last_name.value = ""
                page.update()
                first_name.focus()
                page.window_destroy()
            page.add(
                first_name,
                last_name,
                ft.ElevatedButton("Say hello!", on_click=btn_click),
                greetings,
            )
    page.add(ft.ElevatedButton("teste",on_click=Mostrar))
ft.app(target=main)
