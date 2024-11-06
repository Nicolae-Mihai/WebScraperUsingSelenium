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
Acording to the Exercise requirements the student has to create a script
    1. The script needs to recieve an input from the user which will become the
searched term. For example "washing machine".
    2. The program needs to automatically search on amazon for the user input
and store 10.000 reviews texts and their scores.
    3. The program needs to clean the review text, removing any irelevant 
characters that could interfe with the training. The scores have to be reduced
to two options 0 for negative scores and 1 for positive comments.
    4. Once the comments are processed all the information needs to be stored in
a CVS with 2 columns. The first column will contain the scores (0 or 1) and the 
second will contain the cleaned review text.

In order to complete the exercise librarys such as BeautifulSoup for web 
scraping and nltk or re for text cleanup could be used.
For the score reducction the student can use a function that assigns a value of
0 or 1 acording to a predefined range.
