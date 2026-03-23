import flet as ft


def main(page: ft.Page):
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
            bgcolor="#D1D1D1",
        ),
    )


ft.run(main)
