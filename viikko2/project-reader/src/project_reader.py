from urllib import request
from project import Project
import toml

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        #print(content)
        # konvertoi merkkijonon sanakirjaksi tomlin avulla
        content_dict = toml.loads(content)
        #print(content_dict)

        # tämän jälkeen tulostetaan nimi, description, dependencies ja dev-dependencies
        #print(content_dict["tool"]["poetry"]["name"])
        #print(content_dict["tool"]["poetry"]["description"])
        #print(content_dict["tool"]["poetry"]["dependencies"])
        #print(content_dict["tool"]["poetry"]["group"]['dev']['dependencies'])
        # tallennetaan muuttujiiin 
        name = content_dict["tool"]["poetry"]["name"]
        description = content_dict["tool"]["poetry"]["description"]
        dependencies = content_dict["tool"]["poetry"]["dependencies"]
        dev_dependencies = content_dict["tool"]["poetry"]["group"]['dev']['dependencies']

        # laajennetaan ratkaisua sisältämään myös auhors, lincece ja muut 
        license = content_dict["tool"]["poetry"]["license"]
        authors = list(content_dict["tool"]["poetry"]["authors"])
        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        #self, name, licence, authors:list ,description, dependencies, dev_dependencies
        return Project(name, license, authors, description, dependencies, dev_dependencies)
