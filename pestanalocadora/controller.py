from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp import RequestHandler
from google.appengine.ext.webapp.util import run_wsgi_app
from model import Contato
import datetime


class HomeHandler(RequestHandler):
    '''
    Classe que representa as requisicoes para a pagina de home do sistema.
    '''

    def get(self):
        self.response.out.write(template.render('pages/home.html', {}))
        
        
        
        
 
class ServicoHandler(RequestHandler):
    '''
    Classe que representa as requisicoes para a pagina de servico do sistema.
    '''
    
    def get(self):
        self.response.out.write(template.render('pages/servico.html', {}))
        
        
        


class VeiculoHandler(RequestHandler):
    '''
    Classe que representa as requisicoes para a pagina de veiculos do sistema.
    '''
    
    def get(self):
        self.response.out.write(template.render('pages/veiculo.html', {}))
        
        
        
        

class ContatoHandler(RequestHandler):
    '''
    Classe que representa o formulario de contato do sitema.
    '''
    
    def get(self):
        self.response.out.write(template.render('pages/contato.html', {}))

    def post(self):
        if self.request.get('email'):
           self.email = self.request.get('email');
                
        contato = Contato(nome=self.request.get('name'),
                              email=self.email,
                              mensagem=self.request.get('comment'),
                              dataContato=datetime.datetime.now().date())
        if contato.isValid():
           contato.put() 
        return  self.redirect('/')





class AdministradorHandler(RequestHandler):
    '''
    Classe que representa o administrador do sistema.
    '''
          
    def get(self):
        self.response.out.write(template.render('pages/entrada-admin.html', {}))


    def post(self):
        return  self.response.out.write(template.render('pages/painel-aplicacao.html', {}))






application = webapp.WSGIApplication(
                                     [('/', HomeHandler), ('/contato', ContatoHandler),
                                        ('/servico', ServicoHandler), ('/veiculo', VeiculoHandler),
                                        ('/pestanaadmin', AdministradorHandler),
                                      ('/login', AdministradorHandler),

                                    ],
                                     debug=True)
def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
