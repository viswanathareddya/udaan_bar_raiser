import copy

from utils import validate_payload
from pymongo import ReturnDocument
from schemas import quiz_schema
from flask import abort


class Quiz:
    def __init__(self, db):
        self.db = db

    def get_quiz(self, quiz_id):
        doc = self.db['Quizs'].find_one({'id': quiz_id}, {'_id': 0})
        if not doc:
            abort(400, "requested quiz id is not found")
        if 'questions' not in doc or not doc['questions']:
            return "This quiz doesn't have any questions tagged"
        return doc

    def post_quiz(self, payload):
        validate_payload(payload, quiz_schema)
        doc = self.db['counters'].find_one_and_update({'_id': 'Quiz'}, {'$inc': {'sequence': 1}},
                                                      return_document=ReturnDocument.AFTER)
        payload['id'] = doc['sequence']
        response = copy.deepcopy(payload)
        self.db['Quizs'].insert(payload)
        return response
