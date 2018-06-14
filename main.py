import cherrypy
import os
from jinja2 import Environment, FileSystemLoader
import connection

CUR_DIR = os.path.dirname(os.path.abspath(__file__))
env=Environment(loader=FileSystemLoader(CUR_DIR),
trim_blocks=True)

class tempo:

    @cherrypy.expose()
    def index(self):
        template = env.get_template('index3.html')
        # RENDER TEMPLATE PASSING IN DATA
        return template.render(title='TOP 10 RECORDS',list_header=self.getHeader(), records=self.getRecords(),site_title="Kapil's Solution",searchRes = '')

    def getHeader(self):
        #header = {"Name", "Age", "Adress"}
        header = connection.VisibleFields()
        return header

    def getRecords(self):
        #records = {"Kapil": "231","sachin":"192"}
        records = connection.VisibleData()
        return records
    
    @cherrypy.expose()
    def resultset(self,name = None):
        if name:
            #output = "Hello "+ name
            output = connection.getResultbyName(name)
            print(output)
        else:
            output = "Please enter valid name"
        template = env.get_template('index3.html')
        return template.render(title='TOP 10 RECORDS',list_header=self.getHeader(), records=self.getRecords(),site_title="Kapil's Solution",searchRes = output)

if __name__ == '__main__':
    conf = {
        '/': {
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './public'
        }
    }
    cherrypy.quickstart(tempo(), '/', conf)