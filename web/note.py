#!/usr/bin/env python
from db import NoteModel
from jinja2 import Environment, FileSystemLoader
import cherrypy

env = Environment(loader=FileSystemLoader('templates'))

class Note:
    
    _cp_config = {'tools.sessions.on': True}
    
    def __init__(self):
        self.notemdl = NoteModel()
    
    @cherrypy.expose
    def index(self, tag=None):
        if cherrypy.session.get('data_user'):
            tmpl = env.get_template('index.html')
            if tag:
                posts = self.notemdl.get_post_by_tag(tag)
            else:
                if tag is None:
                    posts = self.notemdl.all_post()
                elif tag=='':
                    posts = []
            print posts
            return tmpl.render(posts=posts, data_user=cherrypy.session.get('data_user'))
        else:
            tmpl = env.get_template('login.html')
            if cherrypy.session.get('error_login_msg'):
                error_login_msg = cherrypy.session.get('error_login_msg')
                del cherrypy.session['error_login_msg']
                return tmpl.render(error_login_msg=error_login_msg)
            else:
                return tmpl.render()
        
    @cherrypy.expose
    def lihat_tulisan(self, id_note):
        if cherrypy.session.get('data_user'):
            tmpl = env.get_template('lihat_tulisan.html')
            post = self.notemdl.get_post_by_id(int(id_note))
            print post
            return tmpl.render(post=post, data_user=cherrypy.session.get('data_user'))
        else:
            raise cherrypy.HTTPRedirect('/')
            
    @cherrypy.expose
    def tulisan_baru(self):
        if cherrypy.session.get('data_user'):
            tmpl = env.get_template('tulisan_baru.html')
            return tmpl.render(data_user=cherrypy.session.get('data_user'))
        else:
            raise cherrypy.HTTPRedirect('/')
            
    @cherrypy.expose
    def proses_tulisan_baru(self, judul=None, tag=None, elm1=None):
        if cherrypy.session.get('data_user'):
            self.notemdl.insert_post(judul, tag, elm1)
            raise cherrypy.HTTPRedirect("/")
        else:
            raise cherrypy.HTTPRedirect('/')
            
    @cherrypy.expose
    def ubah_tulisan(self, id_note):
        if cherrypy.session.get('data_user'):
            tmpl = env.get_template('ubah_tulisan.html')
            post = self.notemdl.get_post_by_id(int(id_note))
            return tmpl.render(post=post, data_user=cherrypy.session.get('data_user'))
        else:
            raise cherrypy.HTTPRedirect('/')
        
    @cherrypy.expose
    def proses_ubah_tulisan(self, judul=None, tag=None, elm1=None, id_note=None):
        if cherrypy.session.get('data_user'):
            self.notemdl.update_post(judul, tag, elm1, id_note)
            raise cherrypy.HTTPRedirect("/")
        else:
            raise cherrypy.HTTPRedirect('/')
        
    @cherrypy.expose
    def hapus_tulisan(self, id_note):
        if cherrypy.session.get('data_user'):
            self.notemdl.delete_post(id_note)
            raise cherrypy.HTTPRedirect("/")
        else:
            raise cherrypy.HTTPRedirect('/')
        
    @cherrypy.expose
    def ekspor(self):
        if cherrypy.session.get('data_user'):
            yield "mengekspor tulisan ..."
        else:
            raise cherrypy.HTTPRedirect('/')
        
    
    @cherrypy.expose
    def cari(self):
        if cherrypy.session.get('data_user'):
            tmpl = env.get_template('cari_tulisan.html')
            return tmpl.render(data_user=cherrypy.session.get('data_user'))
        else:
            raise cherrypy.HTTPRedirect('/')
