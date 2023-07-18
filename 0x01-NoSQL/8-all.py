#!/usr/bin/env python3
""" This is a function that returns all the documents in a collection.
"""
import pymongo
import mongodb

def list_all(mongo_collection):
    """args: takes a mongo collection as argument
       return: returns a list.
    """
   document = []
   for documents in mongo_collection:
       document.append(documents)
    return document
