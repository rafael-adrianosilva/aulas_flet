import flet as ft


def main(page: ft.Page):
    page.title = "Colunas"
    page.bgcolor = "#5E575739"
    page.add(
        ft.Container(
            expand=True,
            content=ft.Column(
                controls=[
                    ft.Text("Topo da Tela"),
                    ft.Button(content="Botão Centralizado"),
                    ft.Text("Base da Tela")
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
        )
    )


ft.run(main)
