import datetime
from typing import Dict
import flet as ft 
import locale
locale.setlocale(locale.LC_ALL,'pt_BR')
saved_notes = [
    {
        'id': 1,
        'title': 'Lista de Compras',
        'date': datetime.date(2023, 12, 24),
        'content': 'Comprar itens essenciais para a semana: leite, pão, ovos, frutas.',
        'color': 'blue',
        'expand': True,
    },
    {
        'id': 2,
        'title': 'Ideias para o Projeto',
        'date': datetime.date(2023, 12, 25),
        'content': '1. Pesquisar tendências de design.\n2. Esboçar layouts iniciais.\n3. Definir tecnologias a serem utilizadas.',
        'color': 'green',
        'expand': False,
    },
    {
        'id': 3,
        'title': 'Reunião com a Equipe',
        'date': datetime.date(2023, 12, 26),
        'content': 'Agendar reunião com a equipe para discutir os progressos do projeto.',
        'color': 'indigo',
        'expand': False,
    },
    {
        'id': 4,
        'title': 'Aniversário da Maria',
        'date': datetime.date(2024, 1, 10),
        'content': 'Comprar presente e preparar surpresa para a festa de aniversário da Maria.',
        'color': 'purple',
        'expand': False,
    },
    {
        'id': 5,
        'title': 'Leitura Recomendada',
        'date': datetime.date(2024, 1, 15),
        'content': 'Livro recomendado: "A Arte da Guerra" de Sun Tzu.',
        'color': 'orange',
        'expand': False,
    },
    {
        'id': 6,
        'title': 'Metas para o Ano Novo',
        'date': datetime.date(2024, 1, 1),
        'content': '1. Fazer exercícios regularmente.\n2. Aprender uma nova habilidade.\n3. Viajar para um lugar diferente.',
        'color': 'pink',
        'expand': True,
    },
    {
        'id': 7,
        'title': 'Ligar para o Dentista',
        'date': datetime.date(2024, 1, 5),
        'content': 'Marcar consulta para check-up odontológico.',
        'color': 'cyan',
        'expand': True,
    },
    {
        'id': 8,
        'title': 'Pensamentos do Dia',
        'date': datetime.date(2024, 1, 2),
        'content': 'Refletir sobre as conquistas do ano passado e definir novos objetivos para o futuro.',
        'color': 'brown',
        'expand': True,
    },
    {
        'id': 9,
        'title': 'Receita de Jantar',
        'date': datetime.date(2024, 1, 8),
        'content': 'Experimentar a nova receita de risoto de cogumelos para o jantar.',
        'color': 'grey',
        'expand': False,
    },
    {
        'id': 10,
        'title': 'Agradecimentos',
        'date': datetime.date(2023, 12, 31),
        'content': 'Agradecer pelas experiências do ano que passou e expressar gratidão aos amigos e familiares.',
        'color': 'indigo',
        'expand': False,
    },
]
def main(page:ft.Page):
    page.bgcolor=ft.colors.BLACK38
    def sombra(e):
        if e.control.shadow:
            e.control.shadow=None
        else:
            e.control.shadow = ft.BoxShadow(
                blur_radius=40,
                color=ft.colors.WHITE,
                blur_style=ft.ShadowBlurStyle.OUTER,
                
            )
    
    def open_note(e):
        page.controls.pop()
        
        for sn in saved_notes:
            if sn['id']== e.control.data:
                page.add(note_details(note=sn))
                return
        
        page.add(note_details())    
    def notes():
        return ft.ResponsiveRow(
            columns=2,
            controls=[
                ft.Container(
                    col=2 if sn['expand'] else 1,
                    bgcolor=sn['color'],
                    padding=ft.padding.all(10),
                    border_radius=ft.border_radius.all(10),
                    shadow=None,
                    content=ft.Column(
                        controls=[
                            ft.Text(value=sn['title'],
                                    style=ft.TextThemeStyle.HEADLINE_MEDIUM,
                                    max_lines=3,
                                    overflow=ft.TextOverflow.ELLIPSIS,
                                    color=ft.colors.WHITE,
                                    ),
                            ft.Text(value=sn['date'].strftime('%b. %d,%Y'),
                                    style=ft.TextThemeStyle.BODY_MEDIUM,
                                    color=ft.colors.WHITE,
                                    )
                        ]
                    ),
                    on_hover=sombra,
                    data=sn['id'],
                    on_click=open_note,
                    
                )for sn in saved_notes
            ]
        )
    layout=ft.Container(
        expand=True,
        padding=ft.padding.all(20),
        content=ft.Column(
            controls=[
                ft.Text(value='NOTEX',style=ft.TextThemeStyle.DISPLAY_LARGE,color=ft.colors.WHITE,size=40),
                ft.Column(
                    expand=True,
                    scroll=ft.ScrollMode.AUTO,
                    controls=[notes()]
                )
            ],spacing=2,
        )
        
    )
    page.floating_action_button=ft.FloatingActionButton(
        icon=ft.icons.ADD,
        shape=ft.CircleBorder(),
        tooltip='adicionar nova nota',
        bgcolor=ft.colors.INDIGO,
        on_click=open_note,
    )
    def tela_inicial(e):
        page.controls.pop()
        layout.content.controls[-1]=notes()
        page.add(layout)
        
    def note_details(note:dict[str,str]=dict()):
        if note.get('date'):
            date=note['date'].strftime('%b, %d, %Y')
            
        else:
            date= datetime.datetime.today().strftime('%b, %d, %Y')
        def change_note(e):
            if e.control.data!=None:
                for sn in saved_notes:
                    if sn['id']== e.control.data:
                        sn['title']=title.value
                        sn['content']=content.value
                        sn['date']=datetime.datetime.today()
            else:
                saved_notes.append({
                    'id':saved_notes[-1]['id']+1,
                    'title':title.value,
                    'date':datetime.datetime.today(),
                    'content':content.value,
                    'color':"blue",
                    'expand':False,
                })
        def enable_saved_button(e):
            btn.disabled=False
            btn.update()
        return ft.Container(
            expand=True,
            padding=ft.padding.all(10),
            content=ft.Column(
                controls=[
                    ft.IconButton(icon=ft.icons.ARROW_BACK,on_click=tela_inicial),
                    title:=ft.TextField(
                        color=ft.colors.WHITE,
                        value=note.get('title'),
                        max_length=50,
                        text_style=ft.TextStyle(size=20,weight=ft.FontWeight.BOLD),
                        border=ft.InputBorder.UNDERLINE,
                        hint_text='qual será o titulo da sua nota?',
                        hint_style=ft.TextStyle(italic=True),
                        content_padding=ft.padding.only(bottom=20),
                        bgcolor=ft.colors.BLACK12,
                        on_change=enable_saved_button,
                        
                    ),
                    ft.Text(value=date,color=ft.colors.WHITE),
                    content:=ft.TextField(
                        value=note.get('content'),
                        text_style=ft.TextStyle(size=20),
                        border=ft.InputBorder.NONE,
                        multiline=True,
                        min_lines=5,
                        hint_text='digite sua anotação',
                        hint_style=ft.TextStyle(italic=True),
                        color=ft.colors.WHITE,
                        on_change=enable_saved_button,
                    ),
                    btn := ft.ElevatedButton(
                        text='salvar alterações',
                        disabled=True,
                        bgcolor=ft.colors.INDIGO,
                        color=ft.colors.WHITE,
                        on_click=change_note,
                        data=note.get('id'),
                        
                    )
                ],spacing=-2,
            )
        )
    page.add(layout)
    #page.add(note_details())
if __name__=="__main__":
    ft.app(target=main)