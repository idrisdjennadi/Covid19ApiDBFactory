# Covid19ApiDB

Rapport: Coronavirus COVID19 API

Rapport réalisé par:
idris DJENNADI;
adel HAMACHE

INTRODUCTION:

La maladie à coronavirus 2019, ou la ou la Covid-19 (acronyme anglais de coronavirus disease 2019), est une maladie infectieuse émergente de type zoonose virale causée par la souche de coronavirus SARS-CoV-2
Cette API fournit des informations sur la maladie coronavirus, provenant de plusieurs sources, Chaque pays envoie des rapports officiels différemment. D’une fois par jour à toutes les heures. 
Contient des Données épidémiologiques mondiales (Pays,code de pays, nombre de cas actuelle, nombre de cas confirmé au total, décès etc.) dans chaque pays

![covid-19-monde](https://user-images.githubusercontent.com/75087474/103657336-12795000-4f6a-11eb-9da3-023bccd44d42.jpg)


Conception du schéma de données:

1- Accéder à l’API Covid-19 :

un API gratuit, pas de clé necessaire pour avoir l'accès à ses données.
Donc la premiière étape est de connecter à Postman et choisir Coronavirus COVID19 API sur https://documenter.getpostman.com/view/10808728/SzS8rjbc?fbclid=IwAR2YDfjJaPmF5dj02UUa1MBYGWAxqQr4ELPL6LZb5vVexwD5geOB5yFiDFo 

![get api](https://user-images.githubusercontent.com/75087474/103666088-74d74e00-4f74-11eb-97ae-685b7d6c381d.PNG)

De la on récupère le lien d'accès à l'API https://api.covid19api.com/ et l'exploiter après sur pycharm 


2- Connecxion et  Récupération de données:

En premier lieu on crée une base de donnée (Covid19) vide c'est-à-dire on met pas de table dessus (juste notre base vide)

![bddr](https://user-images.githubusercontent.com/75087474/103661048-92a1b480-4f6e-11eb-992a-c28be879db66.PNG)

Ensuite par ces lignes de code sous pycharm, on se connecte à notre API et on récupère ses données structurées dans un fichier json :

![1](https://user-images.githubusercontent.com/75087474/103662054-c5987800-4f6f-11eb-9440-c2c5b2b998b6.PNG)

![az](https://user-images.githubusercontent.com/75087474/103664091-2cb72c00-4f72-11eb-98b8-6b71a8f0f8ee.PNG)

![3](https://user-images.githubusercontent.com/75087474/103660210-a13b9c00-4f6d-11eb-81e9-e059753594f2.PNG)

on obtient ces résultats aprés exécution du code:

![resltata execusion code](https://user-images.githubusercontent.com/75087474/103662169-e8c32780-4f6f-11eb-8b19-ec2f36684fba.PNG)


Egalement on aura notre fichier json téléchargé. 

Ensuite après avoir eu la connection vers SQL Server et mit le chemin d'accès de notre fichier json, on actualise notre base de données et introduire la requète suivante:

![req](https://user-images.githubusercontent.com/75087474/103663049-f5944b00-4f70-11eb-94d1-b3315ed8f33d.PNG)

on obtient notre table MyTableName bien rempli avec les données de notre Coronavirus COVID19 API comme suit: 

![table](https://user-images.githubusercontent.com/75087474/103663322-41df8b00-4f71-11eb-9c7f-02aa004beafd.PNG)

