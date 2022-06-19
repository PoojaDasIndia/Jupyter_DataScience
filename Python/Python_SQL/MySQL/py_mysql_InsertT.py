
import mysql.connector as con


try:
#database k sath  connection
    mydb=con.connect(
        host='localhost',
        user='root',
        password='poojadas1993',
        database='EmployeeDetail'
        )
    print(mydb.is_connected()) 
    # n times insert happen
    n=int(input("Enter the number of record want to insert : "))
    for i in range(n):
        
        Emplyee_Id=int(input("Enter Employee ID:"))
        firstname=input("Enter First name:")
        lastname=input("Enter Last Name:")
        Age=int(input("Enter Age:"))
        Department=input("Enter Department:")
        Salary=float(input("Enter Salary:"))


        #insert function (EmpID,FirstName,LastName,Age,Department,Salary) 

        query=f"INSERT INTO employeedemo VALUES ({Emplyee_Id},'{firstname}','{lastname}',{Age},'{Department}',{Salary})"
        
        # Insert table    
        cur=mydb.cursor()
        cur.execute(query)
        # query""INSERT INTO employeedemo (EmpID,FirstName) VALUES (%s,%s)
        # excute many if  we pass list of tuple l=[(),(),()]
        # cur.executemany(query,l)  
        print(f"{i+1} Values inserted into the table!!")
        mydb.commit()

     
    mydb.close()

except Exception as e:
    mydb.close()
    print(str(e))    