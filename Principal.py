import Vision.main as main
import Control.Controle as Controle2
import os
import shutil
class Teste:
    def __init__(self):
        pasta = "Imagens"
        # Verifique se a pasta existe
        if os.path.exists(pasta):
            # Use shutil.rmtree para excluir a pasta e seu conteúdo recursivamente
            shutil.rmtree(pasta)
        Controle2.Controle2(1,0,0,0)
        main.Main()
    __init__(self=0)