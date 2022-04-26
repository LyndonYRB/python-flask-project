from flask import Flask, request, jsonify
from peewee import *
from playhouse.shortcuts import model_to_dict, dict_to_model

db = PostgresqlDatabase('project', user='postgres',
                        password='0000', host='localhost', port=5432)


class BaseModel(Model):
    class Meta:
        database = db


class MilitaryBase(BaseModel):
    name = CharField()
    location = CharField()
    branch = CharField()
    year_activated = IntegerField()
    miles_from_dmv = IntegerField()


db.connect()
db.drop_tables([MilitaryBase])
db.create_tables([MilitaryBase])

MilitaryBase(name='Kunsan', location="Gunsan", branch="Air Force",
             year_activated=1938, miles_from_dmv=140).save()

MilitaryBase(name='Osan', location="Songtan", branch="Air Force",
             year_activated=1951, miles_from_dmv=48).save()

app = Flask(__name__)


@app.route('/militarybase/', methods=['GET', 'POST'])
@app.route('/militarybase/<id>', methods=['GET', 'PUT', 'DELETE'])
def endpoint(id=None):
    if request.method == 'GET':
        if id:
            return jsonify(model_to_dict(MilitaryBase.get(MilitaryBase.id == id)))
        else:
            militarybasesList = []
            for militarybase in MilitaryBase.select():
                militarybasesList.append(model_to_dict(militarybase))
            return jsonify(militarybasesList)

    if request.method == 'PUT':
        return 'PUT request'

    if request.method == 'POST':
        new_militarybase = dict_to_model(MilitaryBase, request.get_json())
        new_militarybase.save()
        return jsonify({"success": True})

    if request.method == 'DELETE':
        return 'DELETE request'


app.run(debug=True)
