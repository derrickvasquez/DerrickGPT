from flask import Flask, render_template, request, jsonify
import openai
from openai.error import OpenAIError

app = Flask(__name__)

# Initialize OpenAI client with your API key
openai.api_key = "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"

@app.route("/")
def index():
    return render_template("index.html")  # Renders the frontend

@app.route("/chat", methods=["POST"])
def chat():
    # Get user input from the POST request
    user_input = request.json.get("message")
    try:
        # Correct OpenAI API call
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Replace with the appropriate model (e.g., "gpt-4" or "gpt-3.5-turbo")
            messages=[{"role": "user", "content": user_input}]
        )
        # Extract the bot's response
        bot_message = response['choices'][0]['message']['content'].strip()
        return jsonify({"response": bot_message})
    except OpenAIError as e:
        # Handle OpenAI-related errors
        return jsonify({"response": f"An error occurred: {str(e)}"}), 500

if __name__ == "__main__":
    # Run the Flask app
    app.run(debug=True)
