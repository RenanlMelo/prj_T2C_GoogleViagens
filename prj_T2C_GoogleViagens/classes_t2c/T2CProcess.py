from botcity.web import WebBot, Browser, By
from botcity.core import DesktopBot
from prj_T2C_GoogleViagens.classes_t2c.utils.T2CMaestro import T2CMaestro, LogLevel, ErrorType
from prj_T2C_GoogleViagens.classes_t2c.utils.T2CExceptions import BusinessRuleException
from prj_T2C_GoogleViagens.classes.chrome import Chrome
from prj_T2C_GoogleViagens.classes.excel import Excel
import datetime
import re

#Classe responsável pelo processamento principal, necessário preencher com o seu código no método execute
class T2CProcess:
    """
    Classe responsável pelo processamento principal.

    Parâmetros:
    
    Retorna:
    """
    #Iniciando a classe, pedindo um dicionário config e o bot que vai ser usado e enviando uma exceção caso nenhum for informado
    def __init__(self, arg_clssExcel:Excel, arg_clssChrome:Chrome, arg_dictConfig:dict, arg_clssMaestro:T2CMaestro, arg_botWebbot:WebBot=None, arg_botDesktopbot:DesktopBot=None):
        """
        Inicializa a classe T2CProcess.

        Parâmetros:
        - arg_dictConfig (dict): dicionário de configuração.
        - arg_clssMaestro (T2CMaestro): instância de T2CMaestro.
        - arg_botWebbot (WebBot): instância de WebBot (opcional, default=None)
        - arg_botDesktopbot (DesktopBot): instância de DesktopBot (opcional, default=None)

        Retorna:

        Raises:
        - Exception: caso nenhum bot seja fornecido.
        """
        if(arg_botWebbot is None and arg_botDesktopbot is None): raise Exception("Não foi possível inicializar a classe, forneça pelo menos um bot")
        else:
            self.var_botWebbot = arg_botWebbot
            self.var_botDesktopbot = arg_botDesktopbot
            self.var_dictConfig = arg_dictConfig
            self.var_clssMaestro = arg_clssMaestro
            self.var_clssChrome = arg_clssChrome
            self.var_clssExcel = arg_clssExcel
            
    #Parte principal do código, deve ser preenchida pelo desenvolvedor
    #Acesse o item a ser processado pelo arg_tplQueueItem
    def execute(self, arg_tplQueueItem:tuple):
        """
        Método principal para execução do código.

        Parâmetros:
        - arg_tplQueueItem (tuple): item da fila a ser processado.

        Retorna:
        """


        """
        Implemente aqui o seu código de execução.
        Acesse o item a ser processado usando arg_tplQueueItem.

        Exemplo:
        ```
        def execute(self, arg_tplQueueItem: tuple):
            item = arg_tplQueueItem[1]
            # Seu código de processamento aqui
        ```

        Este é apenas um exemplo e o print() é apenas um espaço reservado.
        """

        var_dictPassagens = self.var_clssChrome.extract_prices(arg_strQueueItem=str(arg_tplQueueItem[7]))

        self.var_clssExcel.inserindo_dados_planilha(arg_dictPaisesInfo=var_dictPassagens)
