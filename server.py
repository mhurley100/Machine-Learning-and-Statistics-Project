# flask for web app.
import flask as fl
# numpy for numerical work.
import numpy as np
import json
from randF import RandomF as rf

# Create a new web app.
app = fl.Flask(__name__)

# Add root route.
@app.route("/")
def home():
  return app.send_static_file('index.html')

# Add linear route.
@app.route('/api/randF/<string:speed>')
def RF(speed):
  speed = str(speed)
  return {"value":rf.randF(speed)}


# Add normal route.
@app.route('/api/normal')
def normal():
  return {"value": np.random.normal()}