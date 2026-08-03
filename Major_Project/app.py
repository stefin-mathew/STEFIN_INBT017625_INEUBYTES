from flask import Flask, render_template, request, jsonify
import json
import random

app = Flask(__name__)

# Load chatbot intents
with open("intents.json", "r", encoding="utf-8") as file:
    intents = json.load(file)


def get_response(user_message):
    """
    Return a chatbot response based on the user's message.
    """

    message = user_message.lower()

    # Check every intent
    for intent in intents["intents"]:

        for pattern in intent["patterns"]:

            if pattern.lower() in message:
                return random.choice(intent["responses"])

    # Default response
    for intent in intents["intents"]:

        if intent["tag"] == "default":
            return random.choice(intent["responses"])

    return "Sorry! I couldn't understand your question."


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/respond", methods=["POST"])
def respond():

    data = request.get_json()

    if not data or "message" not in data:
        return jsonify({
            "response": "Please enter a valid message."
        })

    user_message = data["message"]

    bot_reply = get_response(user_message)

    return jsonify({
        "response": bot_reply
    })


@app.route("/health")
def health():

    return jsonify({
        "status": "running",
        "message": "Chatbot API is working successfully."
    })


@app.errorhandler(404)
def not_found(error):

    return jsonify({
        "error": "404 - Page Not Found"
    }), 404


@app.errorhandler(500)
def internal_error(error):

    return jsonify({
        "error": "500 - Internal Server Error"
    }), 500


if __name__ == "__main__":
    app.run(debug=True)
