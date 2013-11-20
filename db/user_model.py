from database import *

class UserModel:
    def __init__(self):
        self.db = db
        self.cursor = cursor
    
    def get_user(self, username, password):
        sql = "select * from users where username='%s' and password = '%s'" % (username, password) 
        results = {}
        try :
            self.cursor.execute(sql)
            row = self.cursor.fetchone()
            results.update({'id_users':row[0], 'username':row[1], 'email':row[3], 'facebook':row[4], 'twitter':row[5], 'deskripsi':row[6]})
            return results
        except:
            print "Error : tidak bisa mengambil data"
            return results
