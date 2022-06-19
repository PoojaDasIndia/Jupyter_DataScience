
import mysql.connector as con


#database k sath  connection
mydb=con.connect(
    host='localhost',
    user='root',
    password='poojadas1993',
    database='EmployeeDetail'
    )

#alter table    
# query="ALTER TABLE employeedemo MODIFY  Salary Float(10,3); "
query="ALTER TABLE employeedemo ADD Department varchar(60) AFTER Age"   
cur=mydb.cursor()
cur.execute(query)  




 