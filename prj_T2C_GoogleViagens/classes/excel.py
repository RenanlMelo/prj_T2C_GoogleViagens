from prj_T2C_GoogleViagens.classes_t2c.utils.T2CMaestro import T2CMaestro, LogLevel, ErrorType
from prj_T2C_GoogleViagens.classes_t2c.utils.T2CExceptions import BusinessRuleException
import pandas as pd
import numpy as np

class Excel:
    """
    """

    def __init__ (self):
        """
        """

    def inserindo_dados_planilha (self, arg_listPaisesInfo:list):
        """
        """

        var_dtTodosDestinos = pd.DataFrame(arg_listPaisesInfo)
        var_dtTodosDestinos.to_excel("Passagens.xlsx", index=False, header=True, sheet_name="Todos")

        sorted_dtInfo = list(sorted(arg_listPaisesInfo, key=lambda item: item[1])[:10])

        var_dtDestinosBaratos = pd.DataFrame(sorted_dtInfo)
        var_dtDestinosBaratos.to_excel("Passagens.xlsx", index=False, header=True, sheet_name="Baratos")
            