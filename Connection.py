import mysql.connector
import csv

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Xuluoyujie9",
  database="newsTRAINING"
)

mycursor = mydb.cursor()

with open('news_dataset.csv', encoding="utf8") as csvfile:
    data = csv.reader(csvfile)
    next(data) # skip the first row
    for row in data:
        if row[4] == '':
            row[4] = "/"
            mycursor.execute("INSERT INTO newsarticles( ArticleID, Title, CategoryID, CategoryName, Date, URL, Content) VALUES (%s, %s, %s, %s, %s, %s, %s)", row)

mydb.commit()
mydb.close()