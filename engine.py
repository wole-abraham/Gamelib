""" database engine technically is just json files """

import json
from auth import User

class FileStorage():

    path = 'database.json'
    __objects = {}

    def reload(self):
        try:
            with open(self.path,  encoding='utf-8') as file:
                for data, value in json.load(file).items():
                    FileStorage.__objects[data] = User.to_obj(value)

        except (FileNotFoundError, FileExistsError):
            pass

    def new(self, obj):
        key = f'User.{obj.id}'
        FileStorage.__objects[key] = obj
        
    
    def save(self):
        """ serializes the data """
        json_data = {}
        for objs, values in FileStorage.__objects.items():
            json_data[objs] = values.to_dict()
        with open(self.path, mode='w', encoding='utf-8') as file:
            json.dump(json_data, file)
                
    def all(self):
        for values in FileStorage.__objects.values():
            print(values.to_dict())
           

        