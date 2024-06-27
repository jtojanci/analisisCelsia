from generators.generadorConsumo import generarDatos
import pandas as pd

def analizarDatos():
    datos=generarDatos()
    tabla=pd.DataFrame(datos,columns=["id","referencia","marca","capacidad","ciudad","responsable"])

    tabla.to_csv("consumo.csv",index=False)

analizarDatos()