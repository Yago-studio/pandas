import pandas as pd
import pymysql

mydb = pymysql.connect(
  host="localhost",
  user="root",
  passwd="2450512223",
  database="testdb"
)

query = "SELECT * FROM insurance_order"
filename = "test.csv"
df = pd.read_sql(query, mydb)
df.to_csv(filename, index=False, encoding="utf-8-sig")
