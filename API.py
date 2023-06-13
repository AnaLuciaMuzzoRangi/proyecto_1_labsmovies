from fastapi import FastAPI
import uvicorn 

import pandas as pd
import numpy as np

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel


app = FastAPI() # creo la app para inciar fastapi


from Funciones import Movies #importo desde el archivo funciones la clase Movies()
movies_obj = Movies() #instancio mi clase Movies() como obj, para luego poder llamarlas en las funciones 

url = "https://drive.google.com/file/d/1_5VBROkcp-IhadlTPA5HzgvLH3IvvKWB/view?usp=sharing"
url = "https://drive.google.com/uc?id=" + url.split('/')[-2]

df_movies_new = pd.read_csv(url)

@app.get('/cantidad_filmaciones_mes/{month}')
async def get_count_movies_month(month: str):
    return movies_obj.get_count_movies_month(month=month)


@app.get('/cantidad_filmaciones_dia/{day}')
async def get_count_movies_day(day: str):
    return movies_obj.get_count_movies_day(day=day)


@app.get('/score_titulo/{title}')
async def get_score_title(title: str):
    return movies_obj.get_score_title(title=title)


@app.get('/votos_titulo/{title}')
async def get_votes_title(title: str):
    return movies_obj.get_votes_title(title=title)


@app.get('/get_actor/{actor}')
async def get_actor(actor: str):
    return movies_obj.get_actor(actor=actor)


@app.get('/get_director/{director}')
async def get_director(director: str):
    return movies_obj.get_director(director=director)

@app.get("/get_recomendacion/{titulo}")
async def recomendacion_peliculas(titulo: str):
    return movies_obj.get_recomendacion(titulo=titulo)





