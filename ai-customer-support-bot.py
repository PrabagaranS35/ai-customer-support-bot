from flask import Flask, request, jsonify
from flask_ngrok import run_with_ngrok

# Initialize the Flask app
app = Flask(__name__)
run_with_ngrok(app)  # Use ngrok for exposing the app to the internet

# Define possible chatbot responses
responses = {
    "hello": "Hi! How can I help you?",
    "help": "Sure, I can help. Please tell me your issue.",
    "bye": "Goodbye! Have a nice day!"
}

# Define the chat route
@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "").lower()  # Get user message
    response = responses.get(user_input, "I'm sorry, I don't understand that.")
    return jsonify({"response": response})

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
