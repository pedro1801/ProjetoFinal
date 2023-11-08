import flet as ft

def main(page: ft.Page):
    page.title = "GridView Example"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 50
    page.title="ProjetoFinal"
    page.window_height = 900
    page.window_width = 700
    page.window_maximizable = False
    page.window_center()
    page.update()

    images = ft.GridView(
        expand=5,
        runs_count=5,
        max_extent=600,
        child_aspect_ratio=1.3,
        spacing=10,
        run_spacing=3,
    )

    page.add(images)

    for i in range(1, 5):
        images.controls.append(
            ft.Image(
                src=f"Imagens/image{i}.png",
                fit=ft.ImageFit.NONE,
                repeat=ft.ImageRepeat.NO_REPEAT,
                border_radius=ft.border_radius.all(10),
            )
        )
    page.update()

ft.app(target=main, view=ft.AppView.FLET_APP)