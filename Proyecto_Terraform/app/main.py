from fastapi import FastAPI
from starlette.responses import RedirectResponse

app = FastAPI()

@app.get("/")
def raiz():
    return RedirectResponse(url="/docs/")

@app.get("/validar/{numero}")
def validar_capicua(numero:str):
    respuesta = "No es capicua"

    if numero == numero[::-1]:
      respuesta = "Es capicua"
      return{
         "numero": numero,
         "validacion":respuesta
      }