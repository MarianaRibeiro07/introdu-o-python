import flet as ft

def main(page: ft.Page):
    page.title = "Tela de Login"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.bgcolor = "#0707078E"

    nome = ft.TextField(label="Seu Nome", width=300, autofocus=True, text_size=20, border_color="white", color="pink")
    termo = ft.Checkbox(label="Aceito os termos e condições", label_style=ft.TextStyle(color="white"))
    mensagem = ft.Text("", size=15, color="white", text_align=ft.TextAlign.CENTER)

    def enviar(e):
        if termo.value: 
            mensagem.value = f"Oi, {nome.value}!"
            page.update()

    page.add(
        ft.Text("Formulario de Login", size=30, color="pink"),
        nome,    
        termo,
        ft.ElevatedButton("Entrar", width=300, bgcolor="#FF00AA", color="white", on_click=enviar),
        mensagem,
    )

ft.app(main)