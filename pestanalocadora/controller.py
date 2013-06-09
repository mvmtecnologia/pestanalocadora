from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp import RequestHandler
from google.appengine.ext.webapp.util import run_wsgi_app
from model import Contato
import datetime


class HomeHandler(RequestHandler):
    def get(self):
        self.response.set_status(500)
        self.response.out.write(template.render('pages/home.html', {}))
 
class ServicoHandler(RequestHandler):
    def get(self):
        self.response.out.write(template.render('pages/servico.html', {}))

class VeiculoHandler(RequestHandler):
    def get(self):
        self.response.out.write(template.render('pages/veiculo.html', {}))

class ContatoHandler(RequestHandler):
    emailHelper=None
          
    def get(self):
        self.response.out.write(template.render('pages/contato.html', {}))


    def post(self):
            if self.request.get('email'):
                self.emailHelper = self.request.get('email');
                
            contato = Contato(nome=self.request.get('name'),
                              email=self.emailHelper,
                              mensagem=self.request.get('input-message'), 
                              dataContato=datetime.datetime.now().date())
            print contato
            
#            if contato.isValid():
#                contato.put() 
#                contato.enviarEmail()
        
#                return  self.redirect('/')
#            else:
                #TODO:melhorar isso.
            return  self.redirect('/')
            


application = webapp.WSGIApplication(
                                     [('/', HomeHandler),('/contato', ContatoHandler),
                                        ('/servico', ServicoHandler), ('/veiculo', VeiculoHandler),
                                       
                                    ],
                                     debug=True)
def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
