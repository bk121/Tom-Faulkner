from flask import Flask, request
from generate_response import process 
  
  
app = Flask(__name__, static_folder='../frontend/build', static_url_path='/')


@app.route('/')
def index():
    return app.send_static_file('index.html')
  
  
@app.route('/data', methods=['GET'])
def get_time():
    email=request.args['email']
    response=process(email)
    return {'text': response}

  
      
if __name__ == '__main__':
    app.run(debug=True)