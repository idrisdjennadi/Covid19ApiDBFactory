# Covid19ApiDBFactory

Rapport: Coronavirus COVID19 API

Rapport réalisé par:
idris DJENNADI
adel HAMACHE

INTRODUCTION:

La maladie à coronavirus 2019, ou la ou la Covid-19 (acronyme anglais de coronavirus disease 2019), est une maladie infectieuse émergente de type zoonose virale causée par la souche de coronavirus SARS-CoV-2
Cette API fournit des informations sur la maladie coronavirus, provenant de plusieurs sources, Chaque pays envoie des rapports officiels différemment. D’une fois par jour à toutes les heures. 
Contient des Données épidémiologiques mondiales (Pays,code de pays, nombre de cas actuelle, nombre de cas confirmé au total, décès etc.) dans chaquee pays

![covid-19-monde](https://user-images.githubusercontent.com/75087474/103657336-12795000-4f6a-11eb-9da3-023bccd44d42.jpg)


Conception du schéma de données:

1- Accéder à l’API Covid-19 :

un API gratuit, pas de clé necessaire pour avoir l'accès a ses données.
Donc la premiière étape est de connecter à Postman et choisir Coronavirus COVID19 API sur https://documenter.getpostman.com/view/10808728/SzS8rjbc?fbclid=IwAR2YDfjJaPmF5dj02UUa1MBYGWAxqQr4ELPL6LZb5vVexwD5geOB5yFiDFo 

De la on récupère le lien d'accès a l'API https://api.covid19api.com/ et l'exploiter sur python comme suit: 

![3](https://user-images.githubusercontent.com/75087474/103660210-a13b9c00-4f6d-11eb-81e9-e059753594f2.PNG)

