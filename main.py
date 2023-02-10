from fastapi import FastAPI

#creación de una instancia
app = FastAPI() 

#creacion del empoin
@app.get('/')
def message():
    return "Hello world! desde mi celular"







































