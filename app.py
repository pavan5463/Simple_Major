from sys import stderr

from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))
col=['stories_four','stories_one','stories_three','stories_two','lotsize','bedrooms','bathrms','driveway','recroom','fullbase','gashw','airco','garagepl','prefarea']

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/recheck',methods=['POST','GET'])
def recheck():
    return render_template('index.html')


@app.route('/loginacc',methods=['POST','GET'])
def loginacc():
    return render_template('login.html')

@app.route('/filedata',methods=['POST','GET'])
def filedata():
    return render_template('files.html')
@app.route('/cvr.ac.in',methods=['POST','GET'])
def cvrweb():
    return redirect(url_for('http://cvr.ac.in/home4/'))

@app.route('/code_login')
def codelogin():
    return render_template('code_login.html')







@app.route('/predict', methods=['POST', 'GET'])
def predict():
    int_features = [int(x) for x in request.form.values()]
    final=[np.array(int_features, dtype=float)]
    prediction=model.predict(final)
    output=round(prediction[0],2)

    return render_template('conform.html', pred='Rs:₹{} Only.'.format(output))

if __name__ == '__main__':
    app.run(debug=True)
