#run app.py file in vscode
# dependencies
from flask import Flask,request,jsonify

# Flask App configuration  
app = Flask(__name__)
  
@app.route('/find_symbols_in_names', methods = ['POST'])
def postJsonHandler():
    print (request.is_json)
    content = request.get_json()
    print (content)
    return 'JSON posted'

@app.route('/symbols_in_names', methods = ['GET'])
def getJsonHandler():
    print (request.is_json)
    content = request.get_json()
    name=content
    name = {
    "chemicals": ['Amazon', 'Microsoft', 'Google'],
    "symbols": ['I', 'Am', 'cro', 'Na', 'le', 'abc']
           }
    s = name["symbols"]
    t=name["chemicals"]
    a=[]
    for i in s:
        for j in t:
            if(i in j):
                q=j.replace(i,"[" +i+"]")
                a.append(q)
        
    return jsonify(a)    

if __name__ == '__main__':
    app.debug = True
    app.run()