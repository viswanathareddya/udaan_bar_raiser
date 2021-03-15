import copy

from utils import validate_payload
from pymongo import ReturnDocument
from schemas import question_schema
from flask import abort


class Question:
    def __init__(self, db):
        self.db = db

    def get_question(self, question_id):
        doc = self.db['Questions'].find_one({'id': question_id}, {'_id': 0})
        if not doc:
            abort(400, "No question id requested is found")
        return doc

    def post_question(self, payload):
        validate_payload(payload, question_schema)
        doc = self.db['counters'].find_one_and_update({'_id': 'Question'}, {'$inc': {'sequence': 1}},
                                                      return_document=ReturnDocument.AFTER)
        payload['id'] = doc['sequence']
        response = copy.deepcopy(payload)
        self.db['Questions'].insert(payload)
        return response
