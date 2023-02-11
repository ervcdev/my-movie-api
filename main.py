from fastapi import FastAPI
from fastapi.responses import HTMLResponse #importaciòn de la clase para utilizar html

app = FastAPI() 
app.title = "My aplicación con FastAPI" 
app.version = "0.0.1" 

movies = [
    {
        'id': 1,
        'title': 'Avatar',
        'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        'year': '2009',
        'rating': 7.8,
        'category': 'Acción'    
    } 
]
#creacion del endpoin
@app.get('/', tags=['home']) 
def message():
    return HTMLResponse('<h1>Hello world</h1>') #utilizando html

#creaciòn de la ruta peliculas, y la etiqueta peliculas
@app.get('/movies', tags=['movies'])
def get_movies(): #devuelve el listado de las peliculas
    return movies








































