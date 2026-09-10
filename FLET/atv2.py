import flet as ft

def main(page: ft.Page):
    page.title = "Perfil"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = "#385740"
    page.padding = ft.Padding(top=70, left=0, right=0, bottom=60)

    page.add(
        ft.Container(
            content=ft.Column(
                [
                    ft.Text("Rafaela Oliveira", size=30, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER, color="#33723C"),
                    ft.Text("Desenvolvedora Mobile", size=20, text_align=ft.TextAlign.CENTER, color="#396F44"),
                    ft.Row(
                        [
                            ft.Icon(ft.Icons.EMAIL, size=30, color="#396F44"),
                            ft.Text("rafaela.oliveira@example.com", color="#396F44")
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    ft.Row(
                        [
                            ft.Icon(ft.Icons.PHONE, size=30, color="#396F44"),
                            ft.Text("+55 11 98765-4321", color="#396F44")
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            width=300,
            height=200,
            bgcolor="#a3ebb5",
            padding=20,
            border_radius=10,
        )
    )

ft.run(main)