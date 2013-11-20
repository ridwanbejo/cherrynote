#!/usr/bin/env python
from note import Note
from db import UserModel
from jinja2 import Environment, FileSystemLoader
import cherrypy

env = Environment(loader=FileSystemLoader('templates'))

class User:
    
    _cp_config = {'tools.sessions.on': True}
    
    def __init__(self):
        self.usermdl = UserModel()
    
    @cherrypy.expose
    def login(self, username=None, password=None):
        data_user = self.usermdl.get_user(username, password)
        if len(data_user) != 0:
            cherrypy.session['data_user'] = data_user
        else:
            cherrypy.session['error_login_msg'] = 'Akun tidak ditemukan'
        raise cherrypy.HTTPRedirect('/')

    @cherrypy.expose
    def logout(self):
        if cherrypy.session.get('data_user'):
            del cherrypy.session['data_user']
            raise cherrypy.HTTPRedirect('/')
        else:
            raise cherrypy.HTTPRedirect('/')
        
            
    
