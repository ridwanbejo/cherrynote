from database import *

class NoteModel:
    def __init__(self):
        self.db = db
        self.cursor = cursor
        
    def all_post(self):
        sql = "select * from note where id_user = 1 order by tanggal_diperbaharui desc" 
        try :
            self.cursor.execute(sql)
            temp_results = self.cursor.fetchall()
            results = []
            i = 1
            for row in temp_results:
                num = i
                results.append({'num':num, 'id_note':row[0], 'judul':row[2], 'tag':row[3], 'isi':row[4], 'tanggal_dibuat':row[5], 'tanggal_diubah':row[6]})
            return results
        except:
            print "Error : tidak bisa mengambil data"
    
    def get_post_by_id(self, id_note):
        sql = "select * from note where id_user = 1 and id_note = %d order by tanggal_diperbaharui desc" % (id_note) 
        try :
            self.cursor.execute(sql)
            row = self.cursor.fetchone()
            results = {}
            results.update({'id_note':row[0], 'judul':row[2], 'tag':row[3], 'isi':row[4], 'tanggal_dibuat':row[5], 'tanggal_diubah':row[6]})
            return results
        except:
            print "Error : tidak bisa mengambil data"

    def insert_post(self, judul, tag, isi):
        sql = "insert into note (id_user, judul, tag, isi, tanggal_dibuat, tanggal_diperbaharui) values (%d, '%s', '%s', '%s', '%s', '%s')" % (1, judul, tag, isi, '2013-10-15', '2013-10-15') 
        try:
            self.cursor.execute(sql)
            db.commit()
            print "Info : data berhasil diisikan.."
        except:
            db.rollback()
            print "Error : pengisian data gagal.."
            
    def update_post(self, judul, tag, isi, id_note):
        sql = "update note set judul='%s', tag='%s', isi='%s' where id_note=%d" % (judul, tag, isi, int(id_note)) 
        try:
            self.cursor.execute(sql)
            db.commit()
            print "Info : data berhasil diubah.."
        except:
            db.rollback()
            print "Error : pengubahan data gagal.."
    
    def delete_post(self, id_note):
        sql = "delete from note where id_note=%d" % (int(id_note)) 
        try:
            self.cursor.execute(sql)
            db.commit()
            print "Info : data berhasil dihapus.."
        except:
            db.rollback()
            print "Error : penghapusan data gagal.."
    
    def get_post_by_tag(self, tag):
        sql = "select * from note where tag like '%%%s%%'" % (tag)
        try :
            self.cursor.execute(sql)
            temp_results = self.cursor.fetchall()
            results = []
            i = 1
            for row in temp_results:
                num = i
                results.append({'num':num, 'id_note':row[0], 'judul':row[2], 'tag':row[3], 'isi':row[4], 'tanggal_dibuat':row[5], 'tanggal_diubah':row[6]})
            return results
        except:
            print "Error : tidak bisa mengambil data"
