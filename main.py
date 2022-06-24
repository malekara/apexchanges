import connection

cursor = connection.connectToDataBase('localhost','1521','orcl','TEST','TEST');
cursor.execute('select * from SAMPLE_TABLE')
for row in cursor:
    print(row[0],row[1],row[2])