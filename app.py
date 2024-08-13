from flask import Flask, render_template, redirect, request, flash, session
from surveys import satisfaction_survey as survey
from flask_debugtoolbar import DebugToolbarExtension
app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"
debug = DebugToolbarExtension(app)
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False


response_key = "responses"
# They've done: RESPONSES_KEY = "responses" instead 

@app.route("/")
def home_page():
    """Show instructions, survey name, and button to start survey"""
    return render_template("survey_start.html", survey = survey)

@app.route("/begin", methods=["POST"])
def start_survey():
    """Clear the session of responses."""
    session[response_key] = []
    return redirect("/questions/0")

@app.route("/answer", method = ["POST"])
def answered_questions():
    """Save the answer and move on to next question"""
    choice = request.form["answer"]

    responses = session[response_key]
    responses.append(choice)
    session[response_key] = responses

    if (len(responses) == len(survey.questions)):
        return render_template("completion.html")
    else:
        return redirect(f"/questions/{len(responses)}")
    
@app.route("/quesitons/<int:question_idx>")
def display_question(question_idx):
    responses = session.get(response_key)

    if (responses is None):
        # trying to get to questions too soon -- return them to home page 
        return redirect ("/")
    if (len(responses) == len(survey.questions)):
        # answered all questions, send them to completion page 
        return render_template ("/completion.html")
    if (len(responses) != question_idx):
        # trying to access questions out of order
        flash("Invalid question ID - Must access questions in order")
        return redirect (f"/questions/{len(responses)}")
    question = survey.questions[question_idx]
    return render_template("quesiton.html", question_num = question_idx, question = question)


if __name__ == "__main__":
    app.run(debug=True)
