# flask for web app.
import flask as fl

# numpy for numerical work.
import numpy as np

# Import the joblib API to serialise NumPy array
import joblib
# Load RandomForest
randomF = joblib.load("model.pkl")

# Create a new web app.
app = fl.Flask(__name__)

# Add route
@app.route('/')
def index():
    return app.send_static_file('index.html')

# Add randomF route
@app.route('/api/model/<float:s>')
@app.route('/api/model/<int:s>')
def model(s):
    p = randomF.predict(([[s]]))
    return {"value": str(p[0])} 
  

#Runs programe when called
if __name__ == "__main__":
    app.run(debug=True)
