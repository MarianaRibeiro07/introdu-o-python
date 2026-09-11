import flet as ft

def main(page: ft.Page):
    page.title = "Controle de itens"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.bgcolor = "#A17B9E"  

    nome = ft.TextField(label="Novo item",width=220,text_size=16,border_color="pink",color="white",)
    lista_itens = ft.Column(alignment=ft.MainAxisAlignment.CENTER)

    # Funções
    def criar_linha_item(texto):
        qtd_texto = ft.Text("1", size=16, color="white")

        def diminuir(e):
             qtd_texto.value = str(int(qtd_texto.value) - 1)
             page.update()

        def aumentar(e):
            qtd_texto.value = str(int(qtd_texto.value) + 1)
            page.update()

        def remover(e):
            lista_itens.controls.remove(linha)
            page.update()

        linha = ft.Row(
            [ft.Text(texto, size=16, color="black", width=100),
                ft.IconButton(ft.Icons.REMOVE, icon_color="#FF0000", on_click=diminuir
                ),
                qtd_texto,
                ft.IconButton( ft.Icons.ADD, icon_color="#00FF26", on_click=aumentar
                ),
                ft.IconButton(
                    ft.Icons.DELETE_OUTLINE,icon_color="#CD0089",on_click=remover, ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
        return linha

    # Função botão 'Adicionar'
    def enviar(e):
        if nome.value.strip():
            lista_itens.controls.append(criar_linha_item(nome.value))
            nome.value = ""
            page.update()

    botao_adicionar = ft.ElevatedButton("Adicionar",bgcolor="#CD0089",color="white",height=45,on_click=enviar, )

    page.add(
        ft.Text("Lista de itens", size=30, color="white"),
        ft.Row([nome, botao_adicionar], alignment=ft.MainAxisAlignment.CENTER),
        # Lista onde os novos itens aparecem abaixo
        lista_itens,
    )
ft.app(main)