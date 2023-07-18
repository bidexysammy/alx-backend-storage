#!/usr/bin/env python3
""" This is a function that returns all the documents in a collection.
"""

def list_all(mongo_collection):
    """args: takes a mongo collection as argument
       return: returns a list.
    """
   return mongo_collection.find()
