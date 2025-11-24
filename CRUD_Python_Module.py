# CRUD_Python_Module.py

from pymongo import MongoClient
from pymongo.errors import PyMongoError


class AnimalShelter:
    """
    CRUD operations for the 'animals' collection in the 'aac' database.
    """

    def __init__(
        self,
        username: str,
        password: str,
        host: str = "127.0.0.1",
        port: int = 27017,
        auth_db: str = "admin",
        data_db: str = "aac",
        collection: str = "animals",
    ):
        """
        Initialize MongoDB client and authenticate using provided credentials.
        """

        # Build connection URI with username/password
        uri = f"mongodb://{username}:{password}@{host}:{port}/?authSource={auth_db}"

        try:
            # Connect to MongoDB
            self.client = MongoClient(uri)

            # Select the working database and collection
            self.database = self.client[data_db]
            self.collection = self.database[collection]

            # Test connection
            self.client.admin.command("ping")

        except PyMongoError as e:
            print(f"[ERROR] Could not connect to MongoDB: {e}")
            self.client = None
            self.database = None
            self.collection = None

    # ----------------------------------------------------------------------
    # C — CREATE
    # ----------------------------------------------------------------------
    def create(self, data):
        """
        Insert a document (dict) or list of documents into the collection.
        Returns True on success, False on failure.
        """
        if self.collection is None:
            print("[ERROR] No collection available. Check your connection.")
            return False

        if data is None:
            print("[ERROR] No data provided to insert.")
            return False

        try:
            # If a dict is provided
            if isinstance(data, dict):
                # Avoid duplicate key issues if _id is present
                data.pop("_id", None)
                result = self.collection.insert_one(data)
                return result.acknowledged

            # If a list of dicts is provided
            elif isinstance(data, list):
                for doc in data:
                    if isinstance(doc, dict):
                        doc.pop("_id", None)
                result = self.collection.insert_many(data)
                return result.acknowledged

            else:
                print("[ERROR] Data must be dict or list of dicts.")
                return False

        except PyMongoError as e:
            print(f"[ERROR] Insert failed: {e}")
            return False

    # ----------------------------------------------------------------------
    # R — READ
    # ----------------------------------------------------------------------
    def read(self, query: dict = None, projection: dict = None):
        """
        Query for documents in the collection using find().

        :param query: MongoDB filter dictionary. If None, defaults to {} (all docs).
        :param projection: Optional projection dictionary to limit returned fields.
        :return: List of matching documents (each a dict). Empty list on failure.
        """
        if self.collection is None:
            print("[ERROR] No collection available.")
            return []

        if query is None:
            query = {}

        if not isinstance(query, dict):
            print("[ERROR] Query must be a dictionary.")
            return []

        if projection is not None and not isinstance(projection, dict):
            print("[ERROR] Projection must be a dictionary if provided.")
            return []

        try:
            if projection is not None:
                cursor = self.collection.find(query, projection)
            else:
                cursor = self.collection.find(query)

            results = list(cursor)
            return results

        except PyMongoError as e:
            print(f"[ERROR] Read failed: {e}")
            return []

    # ----------------------------------------------------------------------
    # U — UPDATE
    # ----------------------------------------------------------------------
    def update(self, query: dict, new_values: dict) -> int:
        """
        Update all documents matching 'query'.
        Returns the number of documents modified.
        """
        if self.collection is None:
            print("[ERROR] No collection available.")
            return 0

        if not isinstance(query, dict) or not isinstance(new_values, dict):
            print("[ERROR] Query and update values must be dictionaries.")
            return 0

        try:
            result = self.collection.update_many(query, {"$set": new_values})
            return result.modified_count
        except PyMongoError as e:
            print(f"[ERROR] Update failed: {e}")
            return 0

    # ----------------------------------------------------------------------
    # D — DELETE
    # ----------------------------------------------------------------------
    def delete(self, query: dict) -> int:
        """
        Delete all documents matching 'query'.
        Returns the number of documents deleted.
        """
        if self.collection is None:
            print("[ERROR] No collection available.")
            return 0

        if not isinstance(query, dict):
            print("[ERROR] Query must be a dictionary.")
            return 0

        try:
            result = self.collection.delete_many(query)
            return result.deleted_count
        except PyMongoError as e:
            print(f"[ERROR] Delete failed: {e}")
            return 0
