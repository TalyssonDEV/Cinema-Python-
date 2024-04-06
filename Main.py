from kivy.app import App # type: ignore
from kivy.uix.boxlayout import BoxLayout # type: ignore
from kivy.uix.button import Button # type: ignore
from kivy.uix.label import Label # type: ignore
from kivy.uix.textinput import TextInput # type: ignore
from kivy.uix.carousel import Carousel # type: ignore
from kivy.uix.image import AsyncImage # type: ignore

class Filme:
    def __init__(self, titulo, diretor, genero, ano_lancamento):
        self.titulo = titulo
        self.diretor = diretor
        self.genero = genero
        self.ano_lancamento = ano_lancamento

class No:
    def __init__(self, filme):
        self.filme = filme
        self.proxNo = None

class ListaFilmes:
    def __init__(self):
        self.fim = None
        self.quant = 0

    def esta_vazia(self):
        return self.fim is None

    def insere_lista_vazia(self, novo_filme):
        novo_no = No(novo_filme)
        novo_no.proxNo = novo_no
        self.fim = novo_no
        self.quant += 1

    def insere_no_frente(self, novo_filme):
        novo_no = No(novo_filme)
        if self.fim is None:
            self.insere_lista_vazia(novo_filme)
            return
        novo_no.proxNo = self.fim.proxNo
        self.fim.proxNo = novo_no
        self.quant += 1

    def insere_no_fim(self, novo_filme):
        novo_no = No(novo_filme)
        if self.fim is None:
            self.insere_lista_vazia(novo_filme)
            return
        novo_no.proxNo = self.fim.proxNo
        self.fim.proxNo = novo_no
        self.fim = novo_no
        self.quant += 1

    def remove_do_inicio(self):
        if self.fim is None:
            return
        if self.fim.proxNo == self.fim:
            self.fim = None
        else:
            self.fim.proxNo = self.fim.proxNo.proxNo
        self.quant -= 1

    def exibe_lista(self):
        if self.fim is None:
            return "Lista de filmes vazia!"
        atual = self.fim.proxNo
        lista_filmes = []
        for _ in range(self.quant):
            lista_filmes.append(atual.filme)
            atual = atual.proxNo
        return lista_filmes
    
class MyTextInput(TextInput):
    def __init__(self, **kwargs):
        super(MyTextInput, self).__init__(**kwargs)
        self.bind(focus=self.on_focus_change)

    def on_focus_change(self, instance, value):
        if value:
            self.font_size = '40sp'
        else:
            self.font_size = '20sp'

class FilmeApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.lista_filmes = ListaFilmes()

    def build(self):
        layout = BoxLayout(orientation='vertical')

        # Carousel de imagens
        carousel_layout = self.create_carousel()
        layout.add_widget(carousel_layout)

        # Caixa de mensagem
        self.message_box = Label(text='', size_hint=(1, 0.1))
        layout.add_widget(self.message_box)

        # Widgets para entrada de dados
        input_layout = BoxLayout(orientation='horizontal', size_hint=(1, 0.2))
        self.titulo_input = TextInput(hint_text='Título do filme')
        self.diretor_input = TextInput(hint_text='Diretor do filme')
        self.genero_input = TextInput(hint_text='Gênero do filme')
        self.ano_input = TextInput(hint_text='Ano de lançamento do filme')
        input_layout.add_widget(self.titulo_input)
        input_layout.add_widget(self.diretor_input)
        input_layout.add_widget(self.genero_input)
        input_layout.add_widget(self.ano_input)
        layout.add_widget(input_layout)

        # Botões
        button_layout = BoxLayout(orientation='horizontal', size_hint=(1, 0.1))
        button_layout.add_widget(Button(text='Adicionar filme', on_press=self.adicionar_filme, size_hint=(0.25, 1)))
        button_layout.add_widget(Button(text='Inserir na frente', on_press=self.inserir_na_frente, size_hint=(0.25, 1)))
        button_layout.add_widget(Button(text='Inserir na fim', on_press=self.insere_no_fim, size_hint=(0.25, 1)))
        button_layout.add_widget(Button(text='Exibir lista de filmes', on_press=self.exibir_lista, size_hint=(0.25, 1)))
        layout.add_widget(button_layout)

        # Rótulo para exibir mensagem
        self.message_label = Label(text='', size_hint=(1, None), height=30)
        layout.add_widget(self.message_label)

        return layout

    def adicionar_filme(self, instance):
        titulo = self.titulo_input.text
        diretor = self.diretor_input.text
        genero = self.genero_input.text
        ano_lancamento = int(self.ano_input.text)

        novo_filme = Filme(titulo, diretor, genero, ano_lancamento)
        self.lista_filmes.insere_no_frente(novo_filme)

        # Atualiza o rótulo com a mensagem
        self.message_label.text = 'Filme adicionado: {} ({})'.format(titulo, ano_lancamento)

        self.titulo_input.text = ''
        self.diretor_input.text = ''
        self.genero_input.text = ''
        self.ano_input.text = ''

    def inserir_na_frente(self, instance):
        titulo = self.titulo_input.text
        diretor = self.diretor_input.text
        genero = self.genero_input.text
        ano_lancamento = int(self.ano_input.text)

        novo_filme = Filme(titulo, diretor, genero, ano_lancamento)
        self.lista_filmes.insere_no_frente(novo_filme)

        # Atualiza o rótulo com a mensagem
        self.message_label.text = 'Filme inserido na frente: {} ({})'.format(titulo, ano_lancamento)

        self.titulo_input.text = ''
        self.diretor_input.text = ''
        self.genero_input.text = ''
        self.ano_input.text = ''
        
    def insere_no_fim(self, instance):
        titulo = self.titulo_input.text
        diretor = self.diretor_input.text
        genero = self.genero_input.text
        ano_lancamento = int(self.ano_input.text)

        novo_filme = Filme(titulo, diretor, genero, ano_lancamento)
        self.lista_filmes.insere_no_frente(novo_filme)

        # Atualiza o rótulo com a mensagem
        self.message_label.text = 'Filme inserido na fim: {} ({})'.format(titulo, ano_lancamento)

        self.titulo_input.text = ''
        self.diretor_input.text = ''
        self.genero_input.text = ''
        self.ano_input.text = ''

    def exibir_lista(self, instance):
        filmes = self.lista_filmes.exibe_lista()
        if isinstance(filmes, str):  # Verifica se a lista está vazia
            self.message_label.text = filmes
        else:
            self.message_label.text = 'Lista de filmes:'
            for filme in filmes:
                self.message_label.text += '\n{} ({}) - {}'.format(filme.titulo, filme.ano_lancamento, filme.diretor)

    def create_carousel(self):
        carousel_layout = BoxLayout(orientation='vertical')
        carousel = Carousel(direction='right')
        
        
        src = ["src/imagem1.png","src/imagem2.png","src/imagem3.png","src/imagem4.png","src/imagem5.png","src/imagem7.jpg"]
        for img_source in src:
            image = AsyncImage(source=img_source, allow_stretch=True, size_hint=(1, 1))  # O tamanho da imagem é definido automaticamente
            carousel.add_widget(image)

        carousel_layout.add_widget(carousel)
        return carousel_layout

if __name__ == '__main__':
    FilmeApp().run()
