import flask
from keras.models import load_model
import sys

sys.path.insert(0, "/util")
from util import data_process

app = flask.Flask(__name__)

model = load_model("./model/kanji.h5")

@app.route('/')
def hello_world():
  return "hello!"

@app.route('/predict', methods=["GET", "POST"])
def kanji_recognizer():
  data = {"success": False}

  params = flask.request.json
  if (params == None):
      params = flask.request.args

  try:
    if(params != None):
      img_string = params["image-base64"]
      x = data_process.process(img_string)
      pred = model.predict(x)
      result = data_process.get_top(pred, 8)
      data["prediction"] = data_process.get_characters(result)
      data["success"] = True
  except Exception as e:
    data["error"] = str(e)
  
  return flask.jsonify(data)