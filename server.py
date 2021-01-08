# Flask for web app.
import flask as fl

# Import NumPy for numerical computation.
import numpy as np

# Import the joblib API to serialise NumPy array.
import joblib

# Load RandomForest data output by Jupyter Notebook.
randomF = joblib.load("model.pkl")

# Create a new web app.
app = fl.Flask(__name__)

# Add route
@app.route('/')
def index():
    return app.send_static_file('index.html')

# Add randomF route
@app.route('/api/model/<float:rf>')
@app.route('/api/model/<int:rf>')
# Adapted from https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsRegressor.html
def model(rf):
    pr = randomF.predict([[rf]])
    return {"value": str(pr[0])} 
  

#Runs programe when called
if __name__ == "__main__":
    app.run(debug=True)
