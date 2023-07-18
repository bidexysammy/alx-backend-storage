#!/usr/bin/env python3
""" This function adds a document to a collection
"""

def insert_school(mongo_collection, **kwargs):
    """args:
       mongo_collection is the collection object
       **kwargs is the document to be added
       Return:
       it returns the id of the newly added document 
    """
    rreturn mongo_collection.insert(kwargs)
       
