import mysql.connector
from settings import Aq_Settings

user = Aq_Settings.read_settings

mydb = mysql.connector.connect(
  host=Aq_Settings.read_settings('MySql', 'server'),
  user=Aq_Settings.read_settings('MySql', 'username'),
  password=Aq_Settings.read_settings('MySql', 'password'),
)

print(mydb)