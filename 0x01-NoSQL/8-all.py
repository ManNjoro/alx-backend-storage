#!/usr/bin/env python3
'''
script that lists all documents in a collection.
'''


def list_all(mongo_collection):
    '''
    lists all documents in a collection.
    '''
    if mongo_collection is not None:
        return mongo_collection.find()
    return []
