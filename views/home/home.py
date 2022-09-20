from smtpd import MailmanProxy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.metrics import dp, sp
from kivy.utils import rgba, QueryDict
from kivy.clock import Clock
from kivy.properties import StringProperty

import pandas as pd
import numpy as np
from scipy.interpolate import make_interp_spline
import matplotlib as mpl
import matplotlib.pyplot as plt

from widgets.kivyplt import MatplotFigure

Builder.load_file('views/home/home.kv')
class Home(BoxLayout):


    def moeda(n=0, t="R$ "):
        return f"{t}{n:.2f}".replace('.', ',')




    def __init__(self, **kw) -> None:
        super().__init__(**kw)
        Clock.schedule_once(self.render, .1)
    



    def render(self, _):                        #quando o APP abrir 
        x = np.array([x for x in range(12)])
        xlabels = ['', 'Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
        y = np.array([30, 50, 43, 44, 20, 53, 70, 64, 60, 55, 58, 50])                   #PONTOS NO GRAFICO

        xy_spline = make_interp_spline(x, y)
        x1 = np.linspace(x.min(), x.max(), 500)
        y1 = xy_spline(x1)

        chart = mpl.figure.Figure(figsize=(2,2))
        chart.gca().spines['top'].set_visible(False)
        chart.gca().spines['left'].set_visible(False)
        chart.gca().spines['right'].set_visible(False)
        chart.gca().set_xticklabels(xlabels)
        chart.gca().plot(x1, y1)
        
        plot = MatplotFigure(chart)
        self.ids.graph.clear_widgets()
        self.ids.graph.add_widget(plot)
        

    andressa_df = pd.read_excel(r"Planilhas\Andressa.xlsx")
    bruna_df = pd.read_excel(r"Planilhas\Bruna.xlsx")
    fernanda_df = pd.read_excel(r"Planilhas\Fernanda.xlsx")
    jessica_df = pd.read_excel(r"Planilhas\Jessica.xlsx")
    maria_df = pd.read_excel(r"Planilhas\Maria.xlsx")
    rafaela_df = pd.read_excel(r"Planilhas\Rafaela.xlsx")

    total_df = pd.read_excel(r"Planilhas\TOTAL.xlsx")

    maior_df = andressa_df[["Produto","Quantidade Vend."]].sort_values(by=['Quantidade Vend.'], ascending=False).reset_index()
    maior_df.drop(['index'], axis=1)

    produtos = []
    produtos_vend = dict()
    produtos_vend['produtos'] = maior_df["Produto"] 
    produtos_vend['quantidade'] = maior_df["Quantidade Vend."]
    for prod in produtos_vend['quantidade']:
        produtos.append(prod)

    produtos_vend['quantidade'] = str(produtos)
    
    valor = andressa_df["Total"].sum()
    valor_porcentagem = valor - (valor * 35 / 100)
    vendas = StringProperty(moeda(valor))
    vendas2 = StringProperty(moeda(valor_porcentagem))


