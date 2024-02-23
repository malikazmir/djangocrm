import mysql.connector

dataBase = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	passwd = 'amaR2627#'

	)




cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE malikazmir")

print('All Done!')