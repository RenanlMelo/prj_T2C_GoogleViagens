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

    def inserindo_dados_planilha (self, arg_dictPaisesInfo:list):
        """
        """

        var_dtTodosDestinos = pd.DataFrame(arg_dictPaisesInfo)
        var_dtTodosDestinos.to_excel("Passagens.xlsx", index=False, header=True)

        sorted_dtInfo = dict(sorted(arg_dictPaisesInfo.items(), key=lambda item: item[1])[:10])
            