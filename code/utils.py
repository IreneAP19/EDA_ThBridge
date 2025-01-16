import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.colors as mcolors
import matplotlib.patches as patches
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns

class display(object):
    """Representador HTML de múltiples objetos"""
    template = """<div style="float: left; padding: 10px;">
    <p style='font-family:"Courier New", Courier, monospace'>{0}</p>{1}
    </div>"""
    def __init__(self, *args):
        self.args = args
        
    def _repr_html_(self):
        return '\n'.join(self.template.format(a, eval(a)._repr_html_())
                         for a in self.args)
    
    def __repr__(self):
        return '\n\n'.join(a + '\n' + repr(eval(a))
                           for a in self.args)
    


def multi_index(arrays,data):
    name=["Ages", "Measure"]
    tuples = list(zip(*arrays))
    multi_index = pd.MultiIndex.from_tuples(tuples, names=name)

# Asignamos los multi_index jerarquicos a los nimbre de las columnsa
    data.columns = multi_index

    #establecemos como nombre de las filas a los paises
    data = data.set_index("Country/area")

    #eliminamos la primera fila con los nombre que hemos puesto como indices
    data= data.loc["Afghanistan":, :]
    return data

def calcular_medias_num(data,clasificacion,continentes,cont_paises):#ponemos clasificacion ya que lo usaremos en genero y edades
    medias=[]
    for continente in continentes: #tengo las listas de continentes y poblacion con el mismo orden
        try:
            #hacemos una lista de los paises por continente y comprobamos si estan en el DF
            paises=cont_paises.get(continente,[])
            #devuelveme el pais de la lista de paises (de cada continente) si ese pais esta en el DF
            paises_noeliminados=[pais for pais in paises if pais in data.index]
            if paises_noeliminados: #para los paises que estan en en el DF
                media=data.loc[paises_noeliminados,clasificacion].mean()
                medias.append(media)
            else:
                medias.append(None)
        except KeyError:
            medias.append(None)
    return medias


def test_corr(r,n):#correlacion y muestra(continentes)
    # Grados de libertad
    df = n - 2

    # Cálculo de t
    t = r * ((n - 2) ** 0.5) / ((1 - r**2) ** 0.5)

    # Valor p (dos colas)
    p_value = stats.t.sf(abs(t), df) * 2

    return p_value

def calcular_medias(data,clasificacion,continentes,num_pob,cont_paises):#ponemos clasificacion ya que lo usaremos en genero y edades
    medias=[]
    for posicion,continente in enumerate(continentes): #tengo las listas de continentes y poblacion con el mismo orden
        try:
            #hacemos una lista de los paises por continente y comprobamos si estan en el DF
            paises=cont_paises.get(continente,[])
            #devuelveme el pais de la lista de paises (de cada continente) si ese pais esta en el DF
            paises_noeliminados=[pais for pais in paises if pais in data.columns]
            if paises_noeliminados: #para los paises que estan en en el DF
                media=data.loc[clasificacion,paises_noeliminados].mean()
                poblacion_afectada=(media*num_pob[posicion])/100
                medias.append(poblacion_afectada)
            else:
                medias.append(None)
        except KeyError:
            medias.append(None)
    return medias
#se ha modificado ligeramente la función para adaptarla a los datos de la edad

def melt_datos(dato_inicial):
    dato_reset=dato_inicial.reset_index()
    melted = pd.melt(dato_reset, id_vars=['Country/area'], var_name='Rango de Edad', value_name='Num de Personas')
    return melted