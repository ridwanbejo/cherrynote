import MySQLdb

db = MySQLdb.connect('localhost', 'root', 'root', 'cherry_note')
cursor = db.cursor()
