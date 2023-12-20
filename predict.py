import pickle

from flask import Flask
from flask import request
from flask import jsonify
from  pandas import DataFrame

file = 'model.bin'

with open(file, 'rb') as f_in:
   dv, model = pickle.load(f_in)

app = Flask('poisonous')

@app.route('/predict', methods=['POST'])
def predict():
    parameters = request.get_json() # return a dict

    X = DataFrame.from_dict([parameters])
    X = dv.transform(X)
    y_pred = model.predict(X)

    result = {
        "payload": parameters,
        "poisonous": bool(y_pred)
    }

    return jsonify(result)
    

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)