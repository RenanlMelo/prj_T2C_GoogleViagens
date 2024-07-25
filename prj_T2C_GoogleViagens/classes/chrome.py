from prj_T2C_GoogleViagens.classes_t2c.T2CInitAllSettings import T2CInitAllSettings as InitAllSettings
from prj_T2C_GoogleViagens.classes_t2c.utils.T2CExceptions import BusinessRuleException
from prj_T2C_GoogleViagens.classes_t2c.utils.T2CMaestro import T2CMaestro as Maestro, LogLevel, ErrorType

from botcity.web import WebBot, Browser, By
from botcity.core import DesktopBot
import pandas as pd
import re

class Chrome:
    """
    """

    def __init__ (self, arg_botWebbot: WebBot, arg_botDesktopbot: DesktopBot, arg_clssMaestro: Maestro):
        """
        """
        if(arg_botWebbot is None and arg_botDesktopbot is None):
            raise Exception("Não foi possível inicializar a classe, forneça pelo menos um bot")
        else:
            self.var_botWebbot = arg_botWebbot
            self.var_botDesktopbot = arg_botDesktopbot
            self.var_clssMaestro = arg_clssMaestro

    def open_browser(self, arg_strUrl:str):
        """
        """
        # Abrir página
        self.var_botWebbot.browse(arg_strUrl)
        self.var_botWebbot.maximize_window()

    def extract_table(self):
        """
        """
        self.var_clssMaestro.write_log("Extraindo tabela dos países.")

        table = self.var_botWebbot.find_element('//table[@class="std100 hover tabsort sticky"]', By.XPATH)

        var_listMatches = re.findall(r'[0-9] *([A-ú ]+) *[0-9,]+', table.text)
        var_listPaises = []

        for index, row in enumerate(var_listMatches):
            var_listPaises.append(row.strip())
            print(row, ' adicionado a lista de países.')
        
            if index == 29:
                self.var_clssMaestro.write_log("Tabela extraída com sucesso.")

                return var_listPaises

    def extract_prices(self, arg_strQueueItem:str):
        """
        """
        # Input "De onde?"
        pesquisa_de = self.var_botWebbot.find_element(ensure_clickable=True, ensure_visible=True, selector="/html/body/c-wiz[2]/div/div[2]/div/c-wiz/div[2]/div/div/div[1]/div[1]/section/div/div[1]/div[1]/div[1]/div[2]/div[1]/div/div[1]/div/div[1]/div/div/input",by=By.XPATH)
        pesquisa_de.clear()
        pesquisa_de.send_keys("São Paulo")
        self.var_botWebbot.wait(1000)
        self.var_botWebbot.key_enter(wait=1000)

        # Acessando próximo input
        pesquisa_para_onde = self.var_botWebbot.find_element(ensure_clickable=True, ensure_visible=True, selector="/html/body/c-wiz[2]/div/div[2]/div/c-wiz/div[2]/div/div/div[1]/div[1]/section/div/div[1]/div[1]/div[1]/div[2]/div[1]/div/div[2]/div/div[1]/div/div/input",by=By.XPATH)
        self.var_botWebbot.tab(wait=2000)
        pesquisa_para_onde.send_keys(str(arg_strQueueItem))

        # Clicando no país
        button_pais = self.var_botWebbot.find_element(ensure_clickable=True, ensure_visible=True, selector=f'//li//div//div[contains(text(), "País")]', by=By.XPATH)
        button_pais.click()

        # Acessando datas de saída e retorno        
        self.var_botWebbot.tab(wait=1000)
        button_data_especifica = self.var_botWebbot.find_element(ensure_clickable=True, ensure_visible=True, selector='//button[span[span[contains(text(), "Datas específicas")]]]', by=By.XPATH)
        button_data_especifica.click()

        # Preenchendo input data de saída        
        input_data_partida = self.var_botWebbot.find_element(ensure_clickable=True, ensure_visible=True, selector="/html/body/c-wiz[2]/div/div[2]/div/c-wiz/div[2]/div/div/div[1]/div[1]/section/div/div[1]/div[1]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[2]/div/div[2]/span/div/div[1]/div/div[1]/div/input", by=By.XPATH)
        input_data_partida.send_keys("27/07/2024")
        
        # Acessando e inserindo input data de retorno
        self.var_botWebbot.tab(wait=1000)
        input_data_volta = self.var_botWebbot.find_element(ensure_clickable=True, ensure_visible=True, selector="/html/body/c-wiz[2]/div/div[2]/div/c-wiz/div[2]/div/div/div[1]/div[1]/section/div/div[1]/div[1]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[2]/div/div[2]/span/div/div[1]/div/div[2]/div/input", by=By.XPATH)
        input_data_volta.send_keys("30/07/2024")
        self.var_botWebbot.key_enter(wait=1000)
        self.var_botWebbot.key_enter(wait=1000)

        # Salvando todas as passagens
        self.var_botWebbot.wait(5000)
        var_dictInfo = self.var_botWebbot.find_element(r"//*[@id='yDmH0d']/c-wiz[2]/div/div[2]/div/c-wiz/div[2]/div/div/div[1]/main/div/div[2]/div/ol", By.XPATH)

        # Armazenando valores das passagens
        var_dictMatches = re.findall(r"(?:([A-ú \-]+)[\nR\$]+ ([0-9.]{5,6})[\n[0-9 A-ú]+)", var_dictInfo.text)

        return var_dictMatches