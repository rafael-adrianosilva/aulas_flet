import flet as ft
# IMPORTA A BIBLIOTECA FLET E CRIA UM APELIDO(ALIAS) PARA ELA, CHAMADO "FT".

def main(page: ft.Page):
    page.title = "Meu Primeiro App Flet" # DEFINE O TÍTULO DA JANELA (PÁGINA DO APLICATIVO.)
    page.bgcolor = "#b0c4de" # DEFINE A COR DE FUNDO DA PÁGINA DO APLICATIVO.
    page.vertical_alignment = ft.MainAxisAlignment.CENTER # ALINHA O CONTEÚDO DA PÁGINA VERTICALMENTE AO CENTRO.
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER # ALINHA O CONTEÚDO DA PÁGINA HORIZONTALEMENTE AO CENTRO.
    page.add(
        ft.Text("Bem-Vindo ao meu primeiro aplicativo Flet!", color="blue", weight=ft.FontWeight.BOLD),
        ft.Text("Aqui você pode executar o que quiser", color="black", size=20)
    )

ft.run(main)