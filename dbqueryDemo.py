#Demonstrate successful connection to SQL Server and AdventureWorks test database.
#Demonstrate that dataset (data) can be retrieved from various tables in database - Full recordset. Using a FOR loop. Use record sorting.

import re
import pyodbc

conn = pyodbc.connect('Driver={SQL Server Native Client 11.0};'         # defining the driver name
                          'Server=XXXX\SQLEXPRESS02;'              # defining the server name
                          'Database=AdventureworksLT2019;'                  # defining the database name
                          'Trusted_Connection=yes;')                    # making the connection as trusted and its value is yes

cursor = conn.cursor()             # defining the cursor variable to store the output of the query
cursor.execute('SELECT CustomerID,CompanyName FROM [AdventureWorksLT2019].[SalesLT].[Customer] where CustomerID BETWEEN 1 ANd 50 Order BY CompanyName')   ## sql query to fetch the customer ID and respective company name
result_lst = []         #  defining the empty array to store the query output
for i in cursor:#for loop to iterate the values stored in cursor
    #print(i)                  # printing the values of sql query values on terminal
    s1 = re.sub("[(,')]", "", str(i))      ## trimming the output string,  with re class, which is in the query result and storing in the variable to put in the list box
    result_lst.append(s1)              # Appending the value after trimming in the array
    print(s1)            # printing the values of query output. Here customer ID and respective customer's company name is printing.
