import flet as ft

def main(page: ft.Page):
    page.title = "Meu appzinho fletinho"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.bgcolor = "#95b1f1"

    # Criando funções para os botões
    def diminuir(e):
        caixa_texto.value = str(int(caixa_texto.value) - 1)
        page.update()

    def aumentar(e):
        caixa_texto.value = str(int(caixa_texto.value) + 1)
        page.update()

# Criando os itens da página
    botao_menos = ft.IconButton(ft.Icons.REMOVE, on_click=diminuir)
    caixa_texto = ft.TextField(value="0", width=100, text_align=ft.TextAlign.CENTER)
    botao_mais = ft.IconButton(ft.Icons.ADD, on_click=aumentar)

    page.add(
    ft.Row(
        [botao_menos,caixa_texto,botao_mais],
        alignment=ft.MainAxisAlignment.CENTER,

        )
)

ft.run(main)