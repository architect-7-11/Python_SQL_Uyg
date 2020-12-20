import mysql.connector



connection = mysql.connector.connect(
    host = "*********",
    user = "*********",
    password = "*********",
    database = "*********"
)


def Tablo_Olustur():                  
    """
    veritabaninda tablo mevcut degilse tablo olusturmak icin
    """
    connection = mysql.connector.connect(
    host = "*********",
    user = "*********",
    password = "*********",)


    mycursor = connection.cursor()
    mycursor.execute("create database urun_kayıt")












