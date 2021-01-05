# flask for web app.
import flask as fl

# numpy for numerical work.
import numpy as np

#from randF import RandomF as rf
#from nn import neuNet as nn
# Create a new web app.
app = fl.Flask(__name__)

# Add root route.
@app.route("/")
def home():
  return app.send_static_file('index.html')

# Add linear route.
@app.route('/api/randF/<float:speed>')
@app.route('/api/randF/<int:speed>')
def RF(speed):
  prediction = rf.randF([[speed]])
  return {"value": str(prediction[0])}


# Add normal route.
@app.route('/api/normal')
def normal():
  return {"value": np.random.normal()}


#NN
@app.route('/api/nn1/<string:speed>')
def kr(speed):
    
    speed = float(speed)
    return nn.Kneu(speed)
