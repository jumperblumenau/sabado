import tkinter as Tk
import pandas as pd
import os

from tkinter import *
import tkinter.filedialog
from tkinter import messagebox

janela = Tk()
arquivo = tkinter.filedialog.askopenfilename(title="Selecione o arquivo")
janela.destroy()

buscas_df = pd.read_excel(arquivo)
print(buscas_df.head())