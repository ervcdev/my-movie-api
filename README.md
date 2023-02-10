# my-movie-api
curso de FastApi introductorio de platzi

## Creación del entorno virtula en ubuntu

* Creación del entorno virtual
    ```sh
    python3 -m venv venv
    ```

* Activación del entorno virtual

    ```sh
    source venv/bin/activate
    ```
---

## Creación del entorno virtual en windows
* creación del entorno virtual
    ```sh
    python -m venv env
    ```
* activación del entorno vitual
    ```sh
    venv/Scripts/activate
    ```
---
## Desactivar el entorno virtual
```sh
deactivate
```

---
## Instalaciòn de los modulos que vamos a necesitar para crear la app

* instalacion de fastapi en ubuntu
    ```sh
    pip3 install fastapi
    ```
* instalación de fastApi en windows
    ```sh
    pip install fastapi
    ```
## Actualizar pip

```sh
python -m pip install --upgrade pip
```

## instalación del modulo donde va a correr, uvicorn
```sh
pip install uvicorn
```
## Correr la app
```sh
uvicorn main:app 
```
## Correr la app, pero que se recarge automaticamente

```sh
uvicorn main:app --reload
```

## Correr la app pero cambiando el puerto
```sh
uvicorn main:app --reload --port 1234
```
## Correr la app la app tanto en el pc como en el celular
```sh
uvicorn main:app --reload --port 1234 -- host 0.0.0.0
```




