from flask import Flask

app = Flask(__name__)

import json
import xml.etree.ElementTree as ET

class user():
    def __init__(self,name=None,age=None):
        self._name = name   #abstraction 
        self._age = age

    def get_name(self):
        return self._name
    def get_age(self):
        return self._age
    
    def get_data_from_json(self,filename):
        with open(filename) as f:
            data = json.load(f)
        return user(data.get('name'),data.get('age'))
    
    def get_data_from_xml(self,filename):
        tree = ET.parse(filename)
        root = tree.getroot()
        name=root.find('name').text
        age=int(root.find('age').text)
        return user(name,age)
    

