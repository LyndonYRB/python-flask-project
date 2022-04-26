from flask import Flask, request, jsonify
from peewee import *
from playhouse.shortcuts import model_to_dict, dict_to_model

db = PostgresqlDatabase('project', user='postgres',
                        password='0000', host='localhost', port=5432)


class BaseModel(Model):
    class Meta:
        database = db


class MilitaryBase(BaseModel):
    base_name = CharField()
    location = CharField()
    branch_in_controll = CharField()
    year_activated = IntegerField()
    miles_from_dmv = IntegerField()


db.connect()
db.drop_tables([MilitaryBase])
db.create_tables([MilitaryBase])

MilitaryBase(base_name='Kunsan', location="Gunsan", branch_in_controll="Air Force",
             year_activated=1938, miles_from_dmv=140).save()

MilitaryBase(base_name='Osan', location="Songtan", branch_in_controll="Air Force",
             year_activated=1951, miles_from_dmv=48).save()

MilitaryBase(base_name='Camp Carroll', location="Waegwan", branch_in_controll="Army",
             year_activated=1959, miles_from_dmv=134).save()

MilitaryBase(base_name='Camp Castle', location="Dongducheon", branch_in_controll="Army",
             year_activated=1959, miles_from_dmv=20).save()

MilitaryBase(base_name='Camp Eagle', location="Wonju", branch_in_controll="Army",
             year_activated=1955, miles_from_dmv=50).save()

MilitaryBase(base_name='Camp Humphreys', location="Dongducheon", branch_in_controll="Army",
             year_activated=1950, miles_from_dmv=60).save()

MilitaryBase(base_name='Camp Market', location="Yongsan", branch_in_controll="Army",
             year_activated=2003, miles_from_dmv=30).save()

MilitaryBase(base_name='Camp Red Cloud', location="Uijeongbu", branch_in_controll="Army",
             year_activated=1950, miles_from_dmv=20).save()

MilitaryBase(base_name='Camp Stanly', location="Uijeongbu", branch_in_controll="Army",
             year_activated=1955, miles_from_dmv=15).save()

MilitaryBase(base_name='Camp Hovey', location="Dongducheon", branch_in_controll="Army",
             year_activated=1952, miles_from_dmv=15).save()

MilitaryBase(base_name='Camp Casey', location="Dongducheon", branch_in_controll="Army",
             year_activated=1952, miles_from_dmv=10).save()

MilitaryBase(base_name='K 16 Air Base', location="Seongnam", branch_in_controll="Army",
             year_activated=1951, miles_from_dmv=35).save()

MilitaryBase(base_name='USAG Yongsan', location="Daegu", branch_in_controll="Army",
             year_activated=2003, miles_from_dmv=30).save()

MilitaryBase(base_name='USAG Daegu', location="Daegu", branch_in_controll="Army",
             year_activated=1950, miles_from_dmv=150).save()

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
