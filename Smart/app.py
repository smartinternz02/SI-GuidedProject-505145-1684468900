import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

output1 = ''


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/predict')
def predicted():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    # output = round(prediction[0], 2)
    output = prediction[0]
    if (output == 0):
        output = 'bad'
    else:
        output = 'good'

    return render_template('show.html', prediction_text='the predicted grade for the milk is {}'.format(output))


if __name__ == "__main__":
    app.run(debug=True)
