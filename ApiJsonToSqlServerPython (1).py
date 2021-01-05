import requests
import json
import pyodbc


def save_to_database(reponse_json):
    with open('reponse_json_covid19.json', 'w') as jsonFile:
        json.dump(reponse_json, jsonFile)

    conn = pyodbc.connect('DRIVER={SQL Server};'
                          'SERVER=LAPTOP-VCDSLPEP\SQLEXPRESS;'
                          'DATABASE=covid19;'
                          'Trusted_Connection=yes;')
    cursor = conn.cursor()

    cursor.execute("""DECLARE @json NVARCHAR(MAX); SET @json = (SELECT  * FROM OPENROWSET 
    (BULK 'C:\\Users\\adelh\\Desktop\\reponse_json_covid19.json',SINGLE_CLOB) AS json);

    IF OBJECT_ID('dbo.MyTableName') IS NOT NULL
      DROP TABLE dbo.MyTableName;

    SELECT * INTO MyTableName
    FROM OPENJSON(@json, '$.Countries')
      WITH (        
        Country NVARCHAR(500) '$.Country',
        CountryCode NVARCHAR(500) '$.CountryCode',
        Slug NVARCHAR(500) '$.Slug',
        NewConfirmed NVARCHAR(500) '$.NewConfirmed',
        TotalConfirmed NVARCHAR(500) '$.TotalConfirmed',
        NewDeaths NVARCHAR(500) '$.NewDeaths',
        TotalDeaths NVARCHAR(500) '$.TotalDeaths',
        NewRecovered NVARCHAR(500) '$.NewRecovered',
        TotalRecovered NVARCHAR(500) '$.TotalRecovered',
        Date NVARCHAR(500) '$.Date',
        Premium NVARCHAR(500) '$.Premium'
      );""")

    conn.commit()


if __name__ == '__main__':
    response = requests.get('https://api.covid19api.com/summary').json()
    print(json.dumps(response, indent=4, sort_keys=True))
    save_to_database(response)
