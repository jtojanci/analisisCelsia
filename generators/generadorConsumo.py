import random
def generarDatos():
    datos = []
    for i in range(5000):
        dato={}
        id= random.randint(0,10000)
        referencia=random.choice(["ACH01","ACH22","ACH43"])
        marca=random.choice(["SONY","RICO","KALLEY"])
        capacidad=random.randint(100,2000)
        ciudad=random.choice(["Medellín","Envigado","Bello","Caldas","Sabaneta"])
        responsable=random.choice(["Luis Perez","Daniel Quitero","Federico Gutierrez","Anibal Gaviria","Sergio Fajardo"])

        dato=[id,referencia,marca,capacidad,ciudad,responsable]
        datos.append(dato)
    return datos

print(generarDatos())
