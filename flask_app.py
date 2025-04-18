from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def landing_page():
    return render_template('landing_page.html')

@app.route('/get_cluster')
def get_cluster():
    return render_template('input_form.html')

@app.route('/process',methods=['POST'])
def process():
    name = request.form.get('name')
    email = request.form.get('email')
    candidate_id = request.form.get('candidate_id')

    if(email == 'prashu@gmail.com'):
        return render_template('below_average.html')
    elif(email == 'pragyan@gmail.com'):
        return render_template('average.html')
    elif(email == 'achint@gmail.com'):
        return render_template('good.html')
    else:
        return render_template('ready.html')

if __name__ == '__main__':
    app.run(debug=True)