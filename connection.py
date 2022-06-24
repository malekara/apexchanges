def connectToDataBase(ip,port,serviceName,username,password):
    import cx_Oracle
    dsn_tns = cx_Oracle.makedsn(ip, port, service_name=serviceName) # if needed, place an 'r' before any parameter in order to address special characters such as '\'.
    conn = cx_Oracle.connect(user=username, password=password, dsn=dsn_tns) # if needed, place an 'r' before any parameter in order to address special characters such as '\'. For example, if your user name contains '\', you'll need to place 'r' before the user name: user=r'User Name'
    c = conn.cursor()
    return c;
   # c.execute('select * from DUAL') # use triple quotes if you want to spread your query across multiple lines
   # for row in c:
   #     print (row[0]) # this only shows the first two columns. To add an additional column you'll need to add , '-', row[2], etc.
    #conn.close()
    #this is another change