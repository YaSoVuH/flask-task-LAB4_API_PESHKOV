import datetime
import utils.functions as func
import utils.functionsNice as funcNice

from flask import Flask, request, jsonify, render_template
from sqlalchemy.dialects.postgresql import JSON

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqlite.db'
db = SQLAlchemy(app)

class WorkModel(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)    
    params = db.Column(JSON, nullable=False)
    result = db.Column(JSON)    
    createdat = db.Column(db.DateTime, default=datetime.datetime.now())

    @property
    def serialize(self):
        return {
            'id': self.id,
            'params': self.params,
            'result': self.result,
        }
    
def funcController(inJson):
    data = inJson['data'] 
    value = inJson['data']['value']

    match inJson['method']:
        # Nice functions section ==========================================
        case "matrix-Julia":
            return funcNice.matrixReverse(value)
        case "ceasar":
            return funcNice.caesar(value,data['offset'])
        case "sum":
            return funcNice.getSum(value)   
        # Nice functions section ADD ==========================================
        case "ConvertFrom6to10":
            return funcNice.ConvertFrom6to10(value)
        case "multiplyMatrixAlgByStrasen":
            return funcNice.multiplyMatrixAlgStrasen(data['matrix1'], data['matrix2'])
        case "HowMuchBuckvVTexte":
            print('ser')
            return funcNice.SkolkoRazBukvVTexte(value, data['letter'])
        case "DeleteGlasBukv":
            return funcNice.DeleteGlasBukv(value)

        # Usual functions section =========================================
        case "matrix-reverse":
            return func.matrixReverse(value)
        case "arraySum":
            return func.arraySum(value)
        case "matrix-t":
            return func.matrixTransponse(value)    
    return "method is not supported"

@app.route("/", methods=['GET', 'POST'])
def start():
    return render_template('index.html')

""" BAD
@app.route("/task1", methods=['GET', 'POST'])
def task1():
    try:
        if request.method == 'POST':
            NumberFromInputFrom6To10 = request.form['NumberFromTask1']
            res = funcController(request.get_json())
            res =  {'data': {'result': res}}
            work = WorkModel(params=request.get_json(),result = res)
            db.session.add(work)
            db.session.commit()
            return render_template('task1.html', AnswerFromServer = {"data": work.serialize, }), 200
        else:
            return render_template('task1.html')
    except:
        render_template('task1.html', AnswerFromServer = {"data": 'wrong json-params', }), 400


@app.route("/task2", methods=['GET', 'POST'])
def task2():
    return render_template('task2.html')

@app.route("/task3", methods=['GET', 'POST'])
def task3():
    return render_template('task3.html')

@app.route("/task4", methods=['GET', 'POST'])
def task4():
    return render_template('task4.html')
"""

@app.route("/list",methods=['GET'])
def getWorks():
    works = WorkModel.query.order_by(WorkModel.id.desc()).limit(25)
    return jsonify(works=[i.serialize for i in works])

@app.route("/calc",methods=['POST'])
def index():    
    try:
        res = funcController(request.get_json())
        res =  {'data': {'result': res}}
        work = WorkModel(params=request.get_json(),result = res)
        db.session.add(work)
        db.session.commit()
        return {"data": work.serialize, }, 200
    except:
        return {"data": 'wrong json-params', }, 400
    
@app.route('/work/<id>', methods=['GET'])
def viewTask(id):
    return WorkModel.query.get(id).serialize

@app.route('/work/<id>', methods=['DELETE'])
def deleteTask(id):
    s = "not found"
    code = 404
    if(WorkModel.query.get(id)):
        db.session.delete(WorkModel.query.get(id))
        db.session.commit()
        code = 200 
        s = "successfully deleted"       
    return {"data": f"id={id} {s}"}, code
    
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=2001)
