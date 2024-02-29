import sqlite3
import pandas as pd

conn = sqlite3.connect('STAFF.db')

table_name = 'INSTRUCTOR'
attribute_list = ['ID', 'FNAME', 'LNAME', 'CITY', 'CCODE']

table_name1 = 'DEPARTMENT'
attribute_list1 = ['DEPT_ID', 'DEP_NAME', 'MANAGER_ID', 'LOC_ID']

# Read the data from the CSV file
file_path = "C:\MOUKHLISSI\DATA\Coursera_dataEngineering\Py Project For Data Engineering\Week1\INSTRUCTOR.csv"
df = pd.read_csv(file_path, names = attribute_list)

# Read the data from the CSV department file
file_path1 = "C:\MOUKHLISSI\DATA\Coursera_dataEngineering\Py Project For Data Engineering\Week1\DEPARTMENT.csv"
df1 = pd.read_csv(file_path1, names = attribute_list1)

df.to_sql(table_name, conn, if_exists = 'replace', index =False)
print('Table INSTRUCTOR is ready')

df1.to_sql(table_name1, conn, if_exists = 'replace', index =False)
print('Table DEPARTMENTS is ready')


# Viewing all the data in the table INSTRUCTOR
query_statement = f"SELECT * FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

# Viewing all the data in the table DEPARTMENT
query_statement = f"SELECT * FROM {table_name1}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

# Viewing the first name of all the instructors
query_statement = f"SELECT FNAME FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)


# Append the data to the table INSTRUCTOR
data_dict = {'ID' : [100],
            'FNAME' : ['John'],
            'LNAME' : ['Doe'],
            'CITY' : ['Paris'],
            'CCODE' : ['FR']}
data_append = pd.DataFrame(data_dict)

# Append the data to the table DEPARTMENTS
data_dict1 = {'DEPT_ID' : [9],
            'DEP_NAME' : ['Quality Assurance'],
            'MANAGER_ID' : [30010],
            'LOC_ID' : ['L0010']}
data_append1 = pd.DataFrame(data_dict1)

data_append.to_sql(table_name, conn, if_exists = 'append', index = False)
data_append1.to_sql(table_name1, conn, if_exists = 'append', index = False)

query_statement = f"SELECT FNAME FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

query_statement = f"SELECT * FROM {table_name1}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)


conn.close()
