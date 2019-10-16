import MySQLdb,os

path='/home/irvin/Desktop/django/realestate/scripts'
absPath = os.path.abspath(path)
print(absPath)

conn = MySQLdb.connect(host='localhost',
                          user='root',
                          passwd='root..',
                          db='testdatabase')

db_cursor = conn.cursor()

query = "LOAD DATA LOCAL INFILE '"+ absPath + "/data.csv" + "' INTO TABLE testdatabase.properties_properties FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 LINES "

db_cursor.execute(query)
conn.commit()
