

## SISTEMA DE RECOMENDACION DE PELICULAS 

Objetivo del proyecto :  proporcionar servicios de agregación de plataformas de streaming. 

# Propuesta de Trabajo 

1- En el archivo ETL podrás encontrar todas las Transformaciones pertinentes que se realizaron a los datos.

2- Seguido en el archivo EDA encontraras todo el analisis exploratorio de los datos, donde investigue sobre algunas variables interesantes. 

3- En el archivo Funciones he resumido la clase Movies donde trabaje las principales funciones, que luego  serviran para realizar la app en FASTAPI.

Las 6 funciones creadas para los endpoints que se consumirán en la API fueron:

* def cantidad_filmaciones_mes( Mes) :

 Se ingresa un mes en idioma Español. Debe devolver la cantidad de películas que fueron estrenadas en el mes consultado en la totalidad del conjunto de datos.
                    Ejemplo de retorno: Xcantidad de peliculas fueron estrenadas en el mes deX

* def cantidad_filmaciones_dia( Dia) : 

Se ingresa un día en idioma Español. Debe devolver la cantidad de películas que fueron estrenadas en el día consultado en la totalidad del conjunto de datos.
                    Ejemplo de retorno: Xcantidad de películas fueron estrenadas en los díasX

* def score_titulo( titulo_de_la_filmación) : 

Se ingresa el título de una filmación esperando como respuesta el título, el año de estreno y el score.
                    Ejemplo de retorno: La película Xfue estrenada en el año Xcon una puntuación/popularidad deX

* def votos_titulo( titulo_de_la_filmación) : 

Se ingresa el título de una filmación esperando como respuesta el título, la cantidad de votos y el valor promedio de las votaciones. La misma variable deberá contar con al menos 2000 valoraciones, caso contrario, debemos contar con un mensaje avisando que no cumple esta condición y que por ende, no se devuelve ningun valor.
                    Ejemplo de retorno: La película Xfue estrenada en el año X. La misma cuenta con un total de Xvaloraciones, con un promedio deX

* def get_actor( nombre_actor) :

 Se ingresa el nombre de un actor que se encuentra dentro de un dataset debiendo devolver el éxito del mismo medido a través del retorno. Además, la cantidad de películas que en las que ha realizado y el promedio de retorno. La definición no deberá considerar directores.
                    Ejemplo de retorno: El actor Xha recibido de Xcantidad de filmaciones, el mismo ha obtenido un retorno de Xcon un promedio de Xpor filmación

* def get_director( nombre_director) :

 Se ingresa el nombre de un director que se encuentra dentro de un dataset debiendo devolver el éxito del mismo medido a través del retorno. Además, deberá devolver el nombre de cada película con la fecha de lanzamiento, retorno individual, costo y ganancia de la misma.

4- Sistema de recomendación :

Ha sido creado dentro del archivo funciones, esta funcion consiste en recomendar películas a los usuarios similares al titulo ingresado, por lo que se debe encontrar la similitud de puntuación entre esa película y el resto de películas, se ordenarán según la partitura de similitud y devolverá una lista de Python con 5 valores, cada uno siendo el string del nombre de las películas con mayor puntaje, en orden descendente.





