import flet as ft


def main(page: ft.Page):
    page.bgcolor = "#202020"
    def segredo_ellie(e):
        page.add(
            ft.Text("comi seu bife :)")
        )
    page.add(
        ft.Text("Eu tenho um segredo..."),
        ft.Image(
            src="images/ellie.jpeg",
            height=450
        ),
        ft.Button(
            content="Saiba o segredo da Ellie",
            on_click=segredo_ellie,
            width=500,
            color="white",
            bgcolor="#7A7A7A",
        ),
    )


ft.run(main)
