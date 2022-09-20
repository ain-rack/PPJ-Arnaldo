from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.metrics import dp, sp
from kivy.utils import rgba, QueryDict
from kivy.clock import Clock
from kivy.properties import StringProperty

Builder.load_file('views/home/produtos.kv')
class Produtos(BoxLayout):

    def __init__(self, **kw) -> None:
        super().__init__(**kw)
