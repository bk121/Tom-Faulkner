from flask import Flask, request
import datetime
from generate_response import process 
  
x = datetime.datetime.now()
  
# Initializing flask app
app = Flask(__name__)
  
  
# Route for seeing data
@app.route('/data', methods=['GET'])
def get_time():
    email=request.args['email']
    response=process(email)
    return {'text': response}

  
      
# Running app
if __name__ == '__main__':
    app.run(debug=True)