from flask import Flask, request, render_template

app = Flask(__name__)

def generate_response(user_input):
    # Basic example of response generation
    if "how are you" in user_input:
        return "I'm doing well, thank you!"
    elif "your name" in user_input:
        return "I'm just a chatbot. I don't have a name."
    else:
        return "Sorry, I didn't understand that. Can you please ask again?"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['user_input']
    response = generate_response(user_input)
    return {'response': response}

if __name__ == '__main__':
    app.run(debug=True)
