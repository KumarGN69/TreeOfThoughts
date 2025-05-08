from tree_of_thoughts import TreeOfThoughts
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

tree_of_thoughts = TreeOfThoughts()
@app.route('/ideas', methods=['GET'])
def getidea():
    user_input = request.args.get('query')
    ideas = tree_of_thoughts.getidea(user_input)
    thoughts = [{"name":idea.name, "description":idea.description} for idea in ideas.solutions]
    # print(thoughts)
    return render_template("index.html", ideas = thoughts, thought=user_input)

@app.route('/submit', methods=['POST'])
def submit_text():
    text = request.form['text']
    ideas = tree_of_thoughts.getidea(text)
    thoughts = [{"name":idea.name, "description":idea.description} for idea in ideas.solutions]
    return render_template("index.html", ideas = thoughts, thought=text)
    # Process the text as needed
    # return f'Text received: {text}'

if __name__ == '__main__':
    app.run(debug=True)

