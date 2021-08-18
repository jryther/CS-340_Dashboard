from pymongo import MongoClient
from pymongo import ReturnDocument


class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to
        # access the MongoDB databases and collections.
         self.client = MongoClient('mongodb://%s:%s@localhost:37723/?authSource=AAC' % (username, password))
         self.database = self.client['AAC'];
        

    # Complete this create method to implement the C in CRUD.
    def create(self, data):

        # Verify that dictionary containing record data was provided, else raise an exception
        if data is not None:

            # Store the results of the insert to variable
            insert_result = self.database.animals.insert_one(data)  # data should be dictionary

            # If insert was successful, return True, else, return False
            if insert_result.inserted_id:
                status = True
            else:
                status = False
            return status
        else:
            raise Exception("Nothing to save, because data parameter is empty")

    # Method to implement the R in CRUD.
    def read(self, data):
        # Verify that search criteria was provided, else raise an exception
        if data is not None:
            animalsCollection = self.database.animals.find(data,{"_id":False})  # data should be dictionary   
            return animalsCollection

        else:
            raise Exception("No search criteria provided")

    # Method to implement the U in CRUD.
    def update(self, animal, change):

        # store the user values to local variables
        animalToFind = animal
        informationToUpdate = change

        # Verify that update criteria was provided
        if change is not None:
            result = self.database.animals.find_one_and_update(animalToFind, informationToUpdate,
                                                               return_document=ReturnDocument.AFTER)
            if result is not None:
                return result
            else:
                return ("Update failed. Please try again.")
        else:
            raise Exception("No change provided")

    # Method to implement the D in CRUD
    def delete(self, animal):

        # Verify that deletion record was provided
        if animal is not None:
            delete_result = self.database.animals.delete_one(animal)
            return delete_result
        else:
            raise Exception("No animal ID provided")

    def test(self, data):
        return data


