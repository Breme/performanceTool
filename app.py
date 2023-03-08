from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    num_inputs = 1
    if request.method == 'POST':
        num_inputs = int(request.form['num_inputs'])
    return render_template('index.html', num_inputs=num_inputs)

@app.route('/results', methods=['POST'])
def results():
    inputs = []
    form_data=request.form
    for i in range(int(list(form_data.items()))):
        input_name = 'input{}'.format(i)
        inputs.append(request.form[input_name])
    return render_template('results.html', inputs=inputs)

if __name__ == '__main__':
    app.run(debug=True)


