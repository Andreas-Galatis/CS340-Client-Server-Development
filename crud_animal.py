""" Andreas Galatis
    CS-340 Client/Server Development
    4-1 Milestone: Create and Read in Python
    July 31, 2022
    crud_animal.py
"""


from pymongo import MongoClient
from bson.objectid import ObjectId
from bson.json_util import dumps


class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB  """

    # Initializing the MongoClient. This helps to
    # access the MongoDB databases and collections.
    def __init__(self, username=None, password=None):
        if username and password:
            self.client = MongoClient('mongodb://%s:%s@localhost:38938/aac' % (username, password))
        else:
            self.client = MongoClient('mongodb://%s:%s@localhost:38938')
        self.database = self.client['aac']
        

    # Method to implement the Create function in CRUD
    def create(self, data):
        if data is not None:
            insert = self.database.animals.insert_one(data)  # data should be in dictionary
            if insert != 0:
                return True
            else:
                return False
        else:
            raise Exception("Nothing to save, because data parameter is empty")
            

    # Method to implement the Read function in CRUD
    def read(self, data):
        if data is not None:
            result = self.database.animals.find(data,{"_id":False})
        else:
            raise Exception("Nothing to read, because data parameter is empty")
            
        return (result)
    
    # Method to implement the Update function in CRUD
    def update(self, look_up, data):
        if look_up and data is not None:
            update_result = self.database.animals.update_many(look_up, data)
            return dumps(self.read(look_up))
        else:
            raise Exception("Nothing to update, because look-up or data parameter is empty")
            return False
        
    
    # Method to implement the delete function in CRUD
    def delete(self, data):
        if data is not None:           
            remove = self.database.animals.delete_many(data)
            return dumps(self.read(data))
        else:
            raise Exception("Nothing to delete, because the data parameter is empty")
        
        return (result)
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        
