from flask import Flask, request
from quiz import Quiz
from question import Question
from settings import Connection

app = Flask(__name__)
db = Connection().client()
quiz = Quiz(db)
question = Question(db)


@app.route("/quiz/<int:quiz_id>", methods=["GET"])
def quiz_get(quiz_id):
    response = quiz.get_quiz(quiz_id)
    return response


@app.route("/question/<int:question_id>", methods=["GET"])
def question_get(question_id):
    response = question.get_question(question_id)
    return response


@app.route("/quiz", methods=["POST"])
def quiz_post():
    payload = request.json
    response = quiz.post_quiz(payload)
    return response, 201


@app.route("/question", methods=["POST"])
def question_post():
    payload = request.json
    response = question.post_question(payload)
    return response, 201


@app.errorhandler(404)
def response_for_404(_):
    return {}, _.code


@app.errorhandler(400)
def response_for_400(_):
    return {
               "status": "failure",
               "reason": _.description
           }, _.code


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
