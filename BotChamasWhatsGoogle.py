# CRIADO POR MATEUS SANTOS DE JESUS.
# Instagram: teeusantos20
# Linkedin: https://www.linkedin.com/in/mateus-santos-095a53210

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv

# CRIADO POR MATEUS SANTOS DE JESUS.
# Instagram: teeusantos20
# Linkedin: https://www.linkedin.com/in/mateus-santos-095a53210

class WhatsappBot:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(
            executable_path=r'./chromedriver.exe', chrome_options=options)

    def EfetuarLogin(self):
        self.driver.get('https://web.whatsapp.com')
        #CONFIRMAÇÃO DO LOGIN NO QR CODE.
        verificar_qr = self.driver.find_elements_by_class_name('_3jid7')
        while(verificar_qr):
            verificar_qr = self.driver.find_elements_by_class_name('_3jid7')
        
    def EnviarMensagens(self, contatos, number_p, mensagem):
        relatorio = []
        numero_atual = 0
        #PROCESSO DE ENVIAR MENSAGEM.
        for pessoa in contatos:
            #VERIFICANDO VARIAVEIS
            mensagem = bot.VerificarVariaveis(mensagem, pessoa[0])
            self.driver.get(f"https://web.whatsapp.com/send?phone={number_p}+{pessoa[1]}&text&app_absent=0")
            #NUMERO ATUAL DO ENVIO DE MENSAGENS.
            numero_atual = number_p+pessoa[1]
            #ESPERANDO CARREGAR.
            bot.EsperandoLoading()
            #CSS da mensagem de erro.
            time.sleep(2)
            numero_invalido = self.driver.find_elements_by_class_name('_3SRfO')
            #CONDIÇÃO CASO O NÚMERO NÃO SEJA WHATSAPP.
            time.sleep(2)
            #INJETANDO A MENSAGEM.
            chat_box = self.driver.find_element_by_class_name('_2A8P4')
            chat_box.send_keys(mensagem)
            #CAPTURANDO O BOTÃO ENVIAR.
            time.sleep(2)
            botao_enviar = self.driver.find_element_by_xpath("//span[@data-icon='send']")
            time.sleep(2)
            #CLICANDO EM ENVIAR
            botao_enviar.click()
            print(pessoa)
            time.sleep(3)
            relatorio.append(pessoa[1])
        print('RELATORIO NÚMEROS.', relatorio)
        return relatorio

    #FUNÇÃO PARA VERIFICAR E SUBSTITUIR AS VARIAVEIS NA MENSAGEM.
    #[[fullname]] CORRESPONDE AO NOME COMPLETO.
    #[[fistname]] corresponde ao primeiro nome.
    #Somente esses duas variaveis até então.
    def VerificarVariaveis(self, mensagem, pessoa):
        #NOME COMPLETO.
        if '[[fullname]]' in mensagem:
            mensagem = mensagem.replace('[[fullname]]', pessoa)
            print(pessoa, "Nome completo adicionado.")
        #PRIMEIRO NOME.
        if '[[fistname]]' in mensagem:
            primeiro_nome = str(pessoa).split()[0]
            mensagem = mensagem.replace('[[fistname]]', primeiro_nome)
            print(pessoa, "Primeiro nome adicionado.")
        return mensagem

    #ESSA FUNÇÃO PARA AGUARDAR O LOADING.
    def EsperandoLoading(self):
        tela_loading = self.driver.find_elements_by_class_name('_37lq_')
        time.sleep(1)
        while(tela_loading):
            time.sleep(2)
            tela_loading = self.driver.find_elements_by_class_name('_37lq_')
        time.sleep(2)
        
    #FUNÇÃO PARA GERAR O RELATORIO.
    def Relatorio_Numero(self, relatorio, local_arquivo):
        print(relatorio)
        arquivo = open(local_arquivo, 'w+')
        for pessoa in relatorio:
            if(pessoa[2]):
                arquivo.writelines(pessoa[1])
                arquivo.writelines(' | Enviado.\n')
            else:
                arquivo.writelines(pessoa[1])
                arquivo.writelines(' | Nao Enviado.\n')
        arquivo.close()

    #FAZ UM TRATAMENTO O NÚMERO DE TELEFONE RETIRANDO OS CARACTERES ESPECIAIS.
    def Coletar_dados(self, arquivo):
        contatos = []
        with open(arquivo, encoding='utf-8') as csvfile:
            tabela = csv.reader(csvfile, delimiter=',')
            for list_dado in tabela:
                #TRANSFORMANDO LISTA EM VARIAVEL.
                var_dado = list_dado[0]
                #RETIRANDO OS CARACTERES ESPECIAIS.
                var_dado = var_dado.replace('(', '')
                var_dado = var_dado.replace(')', '')
                var_dado = var_dado.replace('-', '')
                #TRATAR AS VARIAVEIS PARA SEPARAR O NOME DO NÚMERO.
                contatos.append((var_dado.split(";")))
            print(contatos)
            return contatos


#LIGANDO O BOT.
bot = WhatsappBot()
#COLETANDO OS DADOS DA PLANILHA.
dados = bot.Coletar_dados('tester.csv')
#CÓDIGO VAI AGUARDAR ATÉ QUE SEJA FEITO O LOGIN NO WHATSAPP.
bot.EfetuarLogin()
#ENTRADAS PARA O BOT ENVIAR MENSAGEM.
#OS DADOS DA PLANILHA(APENAS AS DUAS PRIMEIRAS COLUNAS ATÉ O MOMENTO), NÚMERO DO PAIS E MENSAGEM.
relatorio = bot.EnviarMensagens(dados, '55', '[[fistname]] Olá [[fullname]] me chamo: ChamasBot(até o momento) [[fistname]], estou aprendendo a enviar o seu nome completo [[fullname]] em qualquer parte da mensagem. [[fullname]], [[fistname]]')
#GERANDO RELATORIO DE ERRO.
bot.Relatorio_Numero(relatorio, 'relatorio.txt')



# CRIADO POR MATEUS SANTOS DE JESUS.
# Instagram: teeusantos20
# Linkedin: https://www.linkedin.com/in/mateus-santos-095a53210