import flet as ft

def main(page: ft.Page):
    page.title = "Cartão de apresentação"
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    page.bgcolor = "#d9b7f5"
    page.window.width = 320
    page.window.height = 600
    page.padding=(ft.Padding(top=70, left=0, right=0, bottom=60))
   
    page.add(
      ft.Text("Radael Leclerc", size=30, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER, color="#7124AB"),
      ft.Text("Desenvolvedora de Software", size=20, text_align=ft.TextAlign.CENTER, color="#663F75"),
)

ft.run(main)