# Example Python Code to Insert a Document 
from pymongo import MongoClient


class AnimalShelter:
    """Provides create and read operations for the AAC animals collection."""

    def __init__(self,username,password):
        """Initialize the MongoDB connection."""

       
        host = "localhost"
        port = 27017
        database = "aac"
        collection = "animals"

        self.client = MongoClient(
            f"mongodb://{username}:{password}@{host}:{port}/"
            "?authSource=admin"
        )

        self.database = self.client[database]
        self.collection = self.database[collection]

    def create(self, data):
        """Insert one document and return True if successful."""

        if not isinstance(data, dict) or not data:
            return False

        try:
            result = self.collection.insert_one(data)
            return result.inserted_id is not None
        except Exception as error:
            print("Create error:", error)
            return False

    def read(self, query):
        """Return matching documents as a list."""

        if not isinstance(query, dict):
            return []

        try:
            return list(self.collection.find(query))
        except Exception as error:
            print("Read error:", error)
            return []
        
    def update(self, query, new_values):
        """Update matching documents and return the number modified."""

        if not isinstance(query, dict) or not isinstance(new_values, dict):
            return 0

        try:
            result = self.collection.update_many(
                query,
                {"$set": new_values}
            )
            return result.modified_count
        except Exception as error:
            print("Update error:", error)
            return 0
        

            
    def delete(self, query):
        """Delete matching documents and return the number removed."""

        if not isinstance(query, dict):
            return 0

        try:
            result = self.collection.delete_many(query)
            return result.deleted_count
        except Exception as error:
            print("Delete error:", error)
            return 0