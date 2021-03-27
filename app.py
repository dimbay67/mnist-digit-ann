import pandas as pd

from flask import Flask, request, jsonify, render_template
from training.utils.model import *

# load model checkpoint
model = NN()
model.load_state_dict(torch.load("training/model.pt"))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    # preprocess json input from web
    x = pd.Series(request.json).to_numpy()
    x = preprocess(x)

    # get prediction
    prediction = predict_model(x, model)

    return f"{prediction}"

if __name__ == "__main__":
    app.run(debug=True)