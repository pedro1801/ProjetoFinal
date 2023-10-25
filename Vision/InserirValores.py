import flet as ft

class Inserir:
    def __init__(self,teste):
        self.teste = teste
        def secundaria(page: ft.View):
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