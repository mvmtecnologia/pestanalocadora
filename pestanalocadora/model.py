
from google.appengine.api import mail
from google.appengine.ext import db
import logging


"""
@author: matheus cardoso
@author: soliva
 
Copyright (C) 2013 MVM Tecnologia, Inc.

""" 
class Contato(db.Model):
    '''
    classe responsavel em representar o
    contato feito pelo cliente
    '''
    nome = db.StringProperty()
    email = db.EmailProperty()
    mensagem = db.TextProperty()
    dataContato = db.DateProperty()

    
    def isValid(self):
        if self.nome and self.email and self.mensagem and self.dataContato:
            return True
        else: False
     
    
    def enviarEmail(self):
            logging.info('enviando email..')
            mail.send_mail(sender="contato@mvmtecnologia.com.br",
            to=self.email,
            subject="Contato MVMTecnologia",
            body='''Muito obrigado por entrar em contato conosco, em breve estaremos retornando.''')    
            
            
            
            
