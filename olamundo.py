import flet as ft

def main (page: ft.Page):
    page.title = "meu appzinho "
    page.add(ft.Text("ola mundooooo🍓"))
    
# ft.run(main,view=ft.AppView.WEB_BROWSER) -- COMO ABRIR EM TELA WEB 
ft.run(main)