import numpy as np
from flask import Flask, render_template, request
import pickle
import math

model = pickle.load(open('model.pkl', 'rb'))

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    # For rendering results on HTML GUI
    int_features = [str(x) for x in request.form.values()]
    temp_features = [np.array(int_features)]

    if temp_features[0][1] == "female" or temp_features[0][1] == "Female":
        temp_features[0][1] = 1
    else:
        temp_features[0][1] = 0

    if temp_features[0][4] == "Nonsmoker" or temp_features[0][4] == "nonsmoker" or temp_features[0][4] == "non-smoker" or temp_features[0][4] == "Non-smoker":
        temp_features[0][4] = 0
    else:
        temp_features[0][4] = 1

    final_features = np.array(temp_features, dtype=np.float32)
    prediction = model.predict(final_features)
    output = math.ceil(prediction[0])
    return render_template('index.html', prediction_text='Premium: Rs. {}'.format(output))


if __name__ == "__main__":
    app.run(debug=True)
