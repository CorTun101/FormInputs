from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/', methods=['GET'])
def main():
    # found in ../templates/
    return render_template("main_page.html")

@app.route('/process_inputs', methods=['POST'])
def process_inputs():
    name = request.form.get('input_name', '')
    dropdown = request.form.get('input_dropdown', '')
    select = request.form.get('input_select', '')
    freeform = request.form.get('input_freeform', '')
    return render_template("main_page.html", input_data=dropdown,
                           output="You're a wizard %s." % name)

#XMEN XMEN  MARVEL'S XMEN.
#A person types in thier name, and the ability(s) they want in to be in the xmen
#Some powers describtions will have a key word which will also include a response of its own
#for example: if a person includes transform and/or clone