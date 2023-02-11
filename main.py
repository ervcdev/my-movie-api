from fastapi import FastAPI

app = FastAPI()  #creación de una instancia
app.title = "My aplicación con FastAPI"  #Colocar nombre a la app
app.version = "0.0.1" #Colocar version en especifico

#creacion del endpoin
@app.get('/', tags=['home']) #Se agrega el home para agrupar determinadas rutas
def message():
    return "Hello world! desde mi celular"







































