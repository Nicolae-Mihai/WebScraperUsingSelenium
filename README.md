# InsideOutAnalizer

The program needs to automatically extract and store desired data from computer
legible documents.
In this exercise the student needs create a program that searches for reviews
and their scores and stores at least 10.000 reviews (prefferably similar items).

The following is an example using washing machines on amazon:

After searching on amazon for a product, the web page shows all the products 
related to the search. The page loads images,descriptions, prices and more 
information that is not relevant for this exercise. The reviews section is 
located at the bottom of the page.
Acording to the Exercise requirements the student has to create a scrypt using 
Python to extract 10.000 reviews and their scores.
    1. The script needs to recieve an input from the user which will become the
searched term. For example "washing machine".
    2. The program needs to automatically search on amazon for the user input
and store 10.000 reviews texts and their scores.
    3. The program needs to clean the review text, removing any irelevant 
characters that could interfe with the training. The scores have to be reduced
to two options 0 for negative scores and 1 for positive comments.
    4. Once the comments are processed all the information needs to be stored in
a CVS with 2 columns. The first column will contain the scores (0 or 1) and the second 
will contain the cleaned review text.


 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Después de realizar una búsqueda en Amazon, el sistema muestra todos los productos que coinciden con
las palabras clave seleccionadas por el usuario. Si se selecciona uno de estos productos, Amazon carga
de manera completa toda la información relacionada con el mismo, incluyendo imágenes, precio y otros
detalles relevantes. Además, al final de la página del producto, se presentan los comentarios de los
usuarios que han comprado y utilizado el producto.
De acuerdo a los requisitos especificados, el estudiante debe crear un script en Python que extraiga
información de 10,000 comentarios de productos en Amazon. A continuación, se proporciona un resumen
del procedimiento:
1. Entrada de Palabra Clave: El script debe solicitar al usuario una palabra clave de búsqueda, por
ejemplo, "lavadora".
2. Búsqueda y Extracción de Datos: El programa debe automatizar la búsqueda en Amazon y
recopilar la información de productos necesaria para alcanzar al menos 10,000 comentarios. Esto
incluirá la valoración (1 a 5 estrellas) y el texto asociado a cada comentario.
3. Procesamiento de Datos: El script debe limpiar los comentarios, eliminando caracteres
irrelevantes que puedan interferir con el entrenamiento. Además, debe reducir las valoraciones de
estrellas a dos opciones (0 para comentarios negativos y 1 para comentarios positivos).
4. Almacenamiento en un archivo CSV: Una vez que se han procesado los comentarios, el script
debe guardar la información en un archivo CSV con dos columnas. La primera columna contendrá
las valoraciones (0 o 1) y la segunda columna contendrá el texto procesado de la reseña.
Para llevar a cabo este proyecto, se pueden utilizar bibliotecas como BeautifulSoup para el web scraping
de Amazon, y herramientas de procesamiento de texto en Python, como nltk o re, para la limpieza de
texto. Para la reducción de valoraciones de estrellas, puedes utilizar una función que asigne un valor de 0
o 1 según un umbral predefinido.
