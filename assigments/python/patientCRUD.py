import mysql.connector

try:
    conn = mysql.connector.connect(host='localhost',port=3308,
                                         database='healthcare',
                                         user='root',
                                         password='sameer',
                                         auth_plugin='mysql_native_password')
except Exception as e:
    print(e)

while True:
    usrOption = int(input("Select Any Option: \n 1. Search a Patient\n 2. Create a Patient\n 3. Update a Patient \n 4. Delete a Patient\n"))

    if (usrOption == 1):
        patientId=(input("Enter Patient ID: "))

        try:
            mycursor=conn.cursor()  
            mycursor.execute("SELECT * FROM patient pa INNER JOIN person pe ON pa.patientId=pe.personId WHERE patientId = '{}'".format(patientId))  
            result=mycursor.fetchall()
            for i in result: 
                print("\n Patient ID: {} \n SSN: {} \n DOB: {} \n Person Name: {} \n Gender: {}".format(i[0],i[1],i[2], i[4],i[6]))  

        except Exception as e:
            print(e)
            conn.close()

        break
    elif (usrOption == 2):
        patientId = int(input("Enter patient ID: "))
        # patientName = input("Enter patient name: ")
        patientdob = input("Enter patient DOB: ")
        # patientGender = input("Enter patient gender: ")
        # patientAddress = input("Enter patient address: ")
        patientSSN = int(input("Enter SSN: "))
        try:
            mycursor=conn.cursor()  
            mycursor.execute("INSERT INTO patient VALUES ( {0},{1},'{3}')".format(patientId,patientdob,patientSSN))  
        
        except Exception as e:
            print(e)
            conn.close()

        break
    elif (usrOption == 3):

        patientId=(input("Enter Patient ID: "))
        dob = int(input("Enter Patient DOB: "))
        try:
            mycursor=conn.cursor()  
            mycursor.execute("UPDATE patient SET dob = {0} WHERE patientId = {1}".format(dob,patientId))  
        
        except Exception as e:
            print(e)
            conn.close()
        break

    elif (usrOption == 4):
        patientId=(input("Enter Patient ID: "))
        try:
            mycursor=conn.cursor()  
            mycursor.execute("DELETE FROM patient WHERE patientId={}".format(patientId))  
        
        except Exception as e:
            print(e)
            conn.close()
        break
    else:
        print("Please Enter correct option!!")

