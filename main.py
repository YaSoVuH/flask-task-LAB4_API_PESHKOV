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
        case "Task1": #Из 6 в 10
            return funcNice.ConvertFrom6to10(value)
        case "Task2": #Умножение матриц по алгоритму Штрассена 
            return funcNice.multiplyMatrixAlgStrasen(data['matrix1'], data['matrix2'])
        case "Task3": #Сколько включений данной буквы в тексте
            return funcNice.SkolkoRazBukvVTexte(value, data['letter'])
        case "Task4": #Удаление гласных букв (анлийский и русский)
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

@app.route("/list",methods=['GET'])
def getWorks():
    limit = request.args.get('limit')

    if not (limit == None) and limit.isdigit():
        limit = int(limit)
        works = WorkModel.query.order_by(WorkModel.id.desc()).limit(limit)
        return jsonify(works=[i.serialize for i in works])
    
    if not limit.isdigit():
        return {"data": f"Введите ID работы которую хотите посмотреть!"}
    works = WorkModel.query.order_by(WorkModel.id.desc())
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
    
@app.route('/work', methods=['GET'])
def viewTask():
    WorkId = request.args.get('WorkId')
    if not WorkId == None:
        if not WorkId.isdigit():
            return {"data": f"Введите ID работы которую хотите посмотреть!"}
        WorkId = int(WorkId)

        try:
            return WorkModel.query.get(WorkId).serialize
        except AttributeError:
            return {"data": f"Работы под ID: {WorkId} не существует!"}
    return {"data": "Введите обязательный параметр: WorkId"}

@app.route('/work', methods=['DELETE'])
def deleteTask():
    WorkId = request.args.get('WorkId')
    if not WorkId == None:
        try:
            WorkId = int(WorkId)
        except ValueError:
            return {"data": "Введите число!"}, 404
        s = "not found"
        code = 404
        if(WorkModel.query.get(WorkId)):
            db.session.delete(WorkModel.query.get(WorkId))
            db.session.commit()
            code = 200 
            s = "successfully deleted"       
        return {"data": f"id={WorkId} {s}"}, code
    return {"data": "Введите обязательный параметр: WorkId"}
    
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=2001)

