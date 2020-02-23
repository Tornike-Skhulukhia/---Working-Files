from functions import calculate_gpa

from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
def gpa():
    return render_template('index.html')


@app.route('/gpa_result', methods=['POST'])
def gpa_result():
    textarea_input = request.form.get('raw_scores')
    raw_scores = [int(score) for score in 
                    textarea_input.split('\r\n') if score.strip() != ""]

    GPA = calculate_gpa(raw_scores)

    return f'შენი GPA არის {GPA}'





app.run(debug=True)
