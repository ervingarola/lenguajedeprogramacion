import mysql.connector
import os

class MYSQLDB:

       def ___init___(self,host,user,password,database):

          self.host = host 
          self.user = user
          self.pw = password
          self.db = database
          self.connection = None

def connect(self):
    try:
       if(self.connection==None):
         self.connection = mysql.connector.connect(
            host = self.host,
             user = self.user,
             password =self.pw,
             database = self. db
         )

         os.system("color a2")
         print("conecte sastifactoriamente ")

   
    except mysql.connector.Error as error: 
          print("ERROR")
         

db =MYSQLDB("localhost","root","","testlp")
print("connectado")