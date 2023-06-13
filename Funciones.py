import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

class Movies():

    def __init__(self):
       
        url = "https://drive.google.com/file/d/1_5VBROkcp-IhadlTPA5HzgvLH3IvvKWB/view?usp=sharing"
        url = "https://drive.google.com/uc?id=" + url.split('/')[-2]
        self._df_movies_new = pd.read_csv(url)
        self._df_movies_new['release_date'] = pd.to_datetime(self._df_movies_new['release_date'],
                                                         format='%Y-%m-%d')


    def get_count_movies_month(self, month=''):

        valid_months = {'enero': '1', 'febrero': '2', 'marzo': '3', 'abril': '4',
                        'mayo': '5', 'junio': '6', 'julio': '7', 'agosto': '8',
                        'septiembre': '9', 'setiembre': '9', 'octubre': '10',
                        'noviembre': '11', 'diciembre': '12'}

        if month.lower() in valid_months:
            variable = valid_months.get(month.lower())
            condition = self._df_movies_new['release_date'].dt.strftime('%m') == variable
            return {'month': month,
                    'amount': f'{self._df_movies_new[condition]["title"].count()}'}

        return {'Mensaje': f'El mes ingresado no existe: {month}'}


    def get_count_movies_day(self, day=''):

        valid_days = {'lunes': 0, 'martes': 1, 'miercoles': 2, 'jueves': 3,
                      'viernes': 4, 'sabado': 5, 'domingo': 6}

        if day.lower() in valid_days:
            condition = self._df_movies_new['release_date'].dt.dayofweek == valid_days.get(day.lower())
            return {'day': day, 'amount': f'{self._df_movies_new[condition]["title"].count()}'}

        return {'Mensaje': f'El dia ingresado no existe: {day}'}


    def get_score_title(self, title=''):

        df_aux = self._df_movies_new['title'].str.lower()
        index = df_aux[df_aux == title.lower()].index
        if len(index.values) > 0:
            df_aux = self._df_movies_new.iloc[index][['title', 'release_year', 'popularity']]
            return {'title': f'{df_aux["title"].values[0]}',
                    'year': f'{df_aux["release_year"].values[0]}',
                    'popularity': f'{df_aux["popularity"].values[0].round(1)}'}

        return {'Mensaje': f' La Pelicula `{title}` ingresada no se encuentra'}


    def get_votes_title(self, title=''):

        df_aux = self._df_movies_new['title'].str.lower()
        index = df_aux[df_aux == title.lower()].index
        if len(index.values) > 0:
            df_aux = self._df_movies_new.iloc[index][['title', 'release_year', 'vote_count',
                                                  'vote_average']]
            if df_aux["vote_count"].values[0] >= 2000:
                return {'title': f'{df_aux["title"].values[0]}',
                        'year': f'{df_aux["release_year"].values[0]}',
                        'total_votes': f'{int(df_aux["vote_count"].values[0])}',
                        'average_votes': f'{df_aux["vote_average"].values[0].round(1)}'}

            return {'Mensaje': f'La Pelicula `{title}` no cuenta con votos'}

        return {'Mensaje': f'La Pelicula `{title}` ingresada no se encuentra'}


    def get_actor(self, actor=''):

        df_aux = self._df_movies_new['cast'].str.lower()
        index_list = list(df_aux[df_aux.str.contains(actor.lower())].index.values)
        movies_count = len(index_list)
        if movies_count > 0:
            ret_mean = 0
            for index in index_list:
                ret_mean += self._df_movies_new.iloc[index]['return']
            if movies_count > 0:
                ret_mean = (ret_mean/movies_count).round(1)
            else:
                ret_mean = 0
            return_list = [self._df_movies_new['return'].iloc[ret] for ret in index_list]
            max_value = max(return_list)
            index_max_return = index_list[return_list.index(max_value)]
            return {'actor': actor,
                    'movie_count': f'{movies_count}',
                    'max_return': f'{self._df_movies_new.iloc[index_max_return]["return"].round(1)}',
                    'average_return': f'{ret_mean}'}

        return {'Mensaje': f'El actor `{actor}` ingresado no se encuentra'}


    def get_director(self, director=''):

        df_aux = self._df_movies_new['director'].str.lower()
        index_list = list(df_aux[df_aux.str.contains(director.lower())].index.values)
        if len(index_list)> 0:
            m_list = [self._df_movies_new['title'].iloc[ret] for ret in index_list]
            d_list = [self._df_movies_new['release_year'].iloc[ret] for ret in index_list]
            rev_list = [self._df_movies_new['revenue'].iloc[ret] for ret in index_list]
            c_list = [self._df_movies_new['budget'].iloc[ret] for ret in index_list]
            ret_list = [self._df_movies_new['return'].iloc[ret] for ret in index_list]
            max_value = max(ret_list)

            index_var = index_list[ret_list.index(max_value)]
            return {'director': director,
                    'max_return_title': f'{self._df_movies_new.iloc[index_var]["title"]}',
                    'max_return': f'{self._df_movies_new.iloc[index_var]["return"].round(1)}',
                    'movies': f'{m_list}',
                    'year': f'{d_list}',
                    'return_movie': f'{ret_list}',
                    'budget_movie': f'{c_list}',
                    'revenue_movie': f'{rev_list}'}

        return {'Mensaje': f' El Director `{director}` ingresado no se encuentra'}

    def recomendacion_peliculas(titulo, df_movies_new):
        titulo = titulo.lower()

        # Calcular la matriz TF-IDF
        tfidf = TfidfVectorizer()
        tfidf_matrix = tfidf.fit_transform(df_movies_new['title'])

        # Calcular la similitud de coseno entre las películas
        cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

        # Obtener el índice de la película seleccionada
        indices = pd.Series(df_movies_new.index, index=df_movies_new['title'].str.lower()).drop_duplicates()
        if titulo not in indices:
            return "Película no encontrada"

        index = indices[titulo]

        # Calcular las puntuaciones de similitud de la película seleccionada con todas las demás
        scores = list(enumerate(cosine_sim[index]))

        # Ordenar las películas por su puntuación de similitud en orden descendente
        scores = sorted(scores, key=lambda x: x[1], reverse=True)

        # Obtener los índices de las películas similares (excluyendo la película seleccionada)
        similar_movie_indices = [i for i, _ in scores if i != index]

        # Obtener las primeras 5 películas similares
        peliculas_similares = df_movies_new.iloc[similar_movie_indices][:5][['title', 'vote_average']].values.tolist()

        if len(peliculas_similares) == 0:
            return {"No se encontraron películas similares"}
        else:
            return {peliculas_similares}