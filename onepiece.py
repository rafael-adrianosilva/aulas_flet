import flet as ft


def main(page: ft.Page):
    def mostrar_mensagem(e):
        page.add(
            ft.Text("Eu vou ser o Rei dos Piratas.")
        )
    page.add(
        ft.Text("Olá meu nome é Luffy."),
        ft.Image(
            src="images/luffy-meat.gif",
            height=450
        ),
        ft.Button(
            content="Clique aqui",
            on_click=mostrar_mensagem,
            width=500,
            color="white",
            bgcolor="#9FC4E8",
        )
    )


ft.run(main)
