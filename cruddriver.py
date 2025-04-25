#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pymongo import MongoClient
from bson.objectid import ObjectId

class CrudDriver (object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, user_, pass_, host_, port_, db_, col_):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        USER = user_
        PASS = pass_ 
        HOST = host_
        PORT = port_
        DB = db_
        COL = col_
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]
        

# Creates a new document if there is valid input
    def create(self, data):
        if data is not None and data != {}:
            self.collection.insert_one(data)  # data should be dictionary
            return True
        else:
            return False

# Returns documents in a list that match the data argument
    def read(self, data):
        if data is not None:
            return list(self.collection.find(data))
        else:
            return list()

# Updates all fields in documents matching the query. Creates the fields specified in data if they're nonexistent
    def update(self, query, data):
        if data is not None:
            result = self.collection.update_many(query, {'$set': data})
            return result.modified_count
        else:
            return 0

# Deletes all documents matching the data argument
    def delete(self, data):
        if data is not None and data != {}:
            result = self.collection.delete_many(data)
            return result.deleted_count
        else:
            return 0