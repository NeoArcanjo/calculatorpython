# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 19:03:09 2019

@author: Rafael Arcanjo
"""
#  Copyright (c) 2019. Rafael Arcanjo

from kivy.core.window import Window

'''
Criar uma funçao que faça o fatiamento da entrada e por recursividade, 
calcule expressões matematicas,sem usar eval
'''

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
# from kivy.core.window import Window
from kivy.uix.popup import Popup


class Calculadora(GridLayout):
    def __init(self, *args, **kwargs):
        """

        :param args:
        :param kwargs:
        """
        super().__init__()
        pass

    @staticmethod
    def confirmacao(*args, **kwargs):
        box = BoxLayout(orientation='vertical', spacing=10, padding=10)
        botoes = BoxLayout(spacing=10)

        Pop = Popup(title='Sair do Aplicativo?', content=box, size_hint=[None, None], size=[400, 350],
                    color=[0, 1, 0, 0.8])

        sim = Button(text='Sim', background_color=[0.2, 1, 0.1, 1], size_hint=[None, None], size=[160, 100],
                     on_release=App.get_running_app().stop)
        nao = Button(text='Não', background_color=[1, 0.2, 0.1, 1], size_hint=[None, None], size=[160, 100],
                     on_release=Pop.dismiss)

        botoes.add_widget(sim)
        botoes.add_widget(nao)

        atencao = Image(source="images/atencao.png")
        box.add_widget(atencao)
        box.add_widget(botoes)

        Pop.open()

    @staticmethod
    def ler_historico(*args):
        arquivo = open('historico.txt', 'r')
        leitura = arquivo.read()
        return leitura

    def memoria(self):
        arquivo = open('historico.txt', 'r')
        entrada = arquivo.readlines()
        saida = entrada[-1::]
        saida = saida[::-2]
        arquivo.close()
        self.display.text = ''.join(saida)

    def gravar_historico(self, entrada):
        arquivo = open('historico.txt', 'w')
        arquivo.write(entrada)
        arquivo.close()
        self.display.text = ''

    def limpar_entrada(self, entrada):
        if entrada:
            saida = entrada
            cont = 0
            for let in entrada:
                cont += 1
                if let == '=':
                    saida = entrada[cont:]
            self.display.text = saida

    @staticmethod
    def varredura(palavra):
        saida = []
        for letra in palavra:
            if letra not in ['0', '1', '2', '3', '4',
                             '5', '6', '7', '8', '9', '.']:
                saida.append(letra)
        return "".join(saida)

    def atualiza(self, entrada):
        if entrada:
            if entrada[-1::] in ['+', '-', '/', 'x', 'i', '^']:
                self.apaga_digito(entrada)

    @staticmethod
    def valida_split(lista):
        """

        :type lista: list
        """
        for i in lista:
            if i != '':
                saida = i
        return saida

    def apaga_digito(self, palavra):
        if palavra:
            newArr = []
            saida = ''
            for i in range(0, len(palavra) - 1):
                newArr.append(palavra[i])
            saida = "".join(newArr)
            self.display.text = saida

    def percentagem(self, calculation):
        if calculation:
            try:
                base, percentual = calculation.split("x")
                valor = float(base) * float(percentual) / 100
                self.display.text += '%=' + str(valor)
            except Exception:
                self.display.text = "Error"

    @staticmethod
    def decimal_bin(num):
        if num:
            try:
                num = int(num)
                soma = 0
                pot = 0
                while num >= 1:
                    soma = num % 2 * 10 ** pot + soma
                    num = int(num / 2)
                    pot = pot + 1
                return str(soma)
            except ValueError:
                return "Error"

    @staticmethod
    def bin_decimal(num):
        if num:
            try:
                num = int(num)
                soma = 0
                pot = 0
                while num != 0:
                    soma = num % 10 * 2 ** pot + soma
                    num = int(num / 10)
                    pot = pot + 1
                return str(soma)
            except ValueError:
                return "Error"

    def soma_bin(self, entrada):
        if entrada:
            oper = self.varredura(entrada)
            if oper == '+':
                try:
                    num1, num2 = entrada.split('+')
                    soma = int(self.bin_decimal(num1)) + int(self.bin_decimal(num2))
                    self.display.text += '=' + self.decimal_bin(soma)
                except ValueError:
                    self.display.text = "Error"
            elif oper == '-':
                try:
                    num1, num2 = entrada.split('-')
                    soma = int(self.bin_decimal(num1)) - int(self.bin_decimal(num2))
                    self.display.text += '=' + self.decimal_bin(soma)
                except Exception:
                    self.display.text = "Error"

    def fake_function(self, entrada):
        return str(self.inteirizar(float(eval(entrada))))

    def aritmetica(self, entrada):
        oper = self.varredura(entrada)
        verifica = oper
        if verifica == "":
            output = entrada
        elif verifica == '!':
            convoca = self.valida_split(entrada.split(oper))
            output = self.fatorial(convoca)
        elif len(oper) > 1:
            output = self.fake_function(entrada)
        else:
            num1, num2 = entrada.split(oper)
            output = self.calcula(num1, oper, num2)
        return output

    def fibonacci(self, num):
        if num:
            try:
                num = int(num)
                resultado = [0]
                aux1, base = 0, 1
                while base < num:
                    resultado.append(base)
                    aux1, base = base, aux1 + base
                self.display.text += '=' + str(resultado)
            except Exception:
                self.display.text = "Error"

    def fatorial(self, num):
        if num:
            num = int(num)
            try:
                if num < 0:
                    return 'Digite número maior ou igual a zero'
                elif num in [0, 1]:
                    return 1
                else:
                    return num * self.fatorial(num - 1)
            except Exception:
                self.display.text = "Error"

    def sqrt_2(self, numero):
        if numero:
            try:
                self.display.text += '=' + str(self.inteirizar(float(numero) ** (1 / 2)))
            except Exception:
                self.display.text = "Error"

    def sqrt_3(self, numero):
        if numero:
            try:
                self.display.text += '=' + str(self.inteirizar(float(numero) ** (1 / 3)))
            except Exception:
                self.display.text = "Error"

    def peso_ideal(self, altura):
        if altura:
            try:
                altura = float(altura)
                self.display.text += '=' + str(round((72.7 * altura) - 58, 2))
            except Exception:
                self.display.text = "Error"

    def calculate(self, calculation):
        if calculation:
            try:
                self.display.text += '=' + str(self.aritmetica(calculation))
            except Exception:
                self.display.text = "Error"

    def calcula(self, numero1, operacao, numero2):
        if numero1 in [None, '', ' ']:
            numero1 = 0
        if numero2 in [None, '', ' ']:
            numero2 = numero1
        if operacao == '+':
            saida = float(numero1) + float(numero2)
        elif operacao == '-':
            saida = float(numero1) - float(numero2)
        elif operacao in ['*', 'x']:
            saida = float(numero1) * float(numero2)
        elif operacao == '/':
            saida = float(numero1) / float(numero2)
        elif operacao in ['**', '^']:
            saida = float(numero1) ** float(numero2)
        elif operacao.lower() == 'i':
            numero1 = float(numero1)
            numero2 = float(numero2)
            if numero1 < numero2:
                numero1, numero2 = numero2, numero1
            saida = round(float(numero1) / (float(numero2) ** 2), 2)
        else:
            saida = "ERROR"
        return self.inteirizar(saida)

    def inteirizar(self, saida):
        """

        :type saida: float
        """
        if saida == int(saida):
            saida = int(saida)
        return saida


class ToolBoxPC(App):
    def build(self):
        self.icon = 'logo.png'
        Window.release_all_keyboards()
        return Calculadora()


ToolBoxPC().run()
