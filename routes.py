from tree_of_thoughts import TreeOfThoughts
from flask import Flask, render_template, jsonify

app = Flask(__name__)

tree_of_thoughts = TreeOfThoughts()
@app.route('/ideas', methods=['GET'])
def getidea():
    user_input = input(f"Enter your idea for brainstorming :")
    ideas = tree_of_thoughts.getidea(user_input)
    ideas_list = [idea.name for idea in ideas.solutions]
    # return jsonify(ideas_list)
    return render_template("index.html", ideas=ideas_list)

if __name__ == '__main__':
    app.run(debug=True)