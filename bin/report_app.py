import peewee
from models import *
from flask import Flask, request, jsonify, make_response, Response
from flask_restful import Resource, Api
import config


app = Flask(__name__)
app.config.from_object(config.Config)
api = Api(app)
app.config['DEBUG'] = True
app.json.sort_keys = False


def db_data(order):
    result = {}

    if order == 'desc':
        res = -ReportBase.time

    else:
        res = ReportBase.time

    for items in ReportBase.select().order_by(res):
        result.update({items.abbreviation: {
            'place': str(items.place),
            'name': str(items.name),
            'team': str(items.team),
            'time': str(items.time)}})

    return result


class Report(Resource):
    def get(self):
        request_order = request.args.get('order', type=str)

        if request_order == 'desc':
            return jsonify(db_data(request_order))

        if request_order == 'asc':
            return jsonify(db_data(request_order))


class DriverID(Resource):
    def get(self, driver_id):
        result = db_data("asc")
        if driver_id in result:
            return result[driver_id]

        else:
            return 'Error Wrong format', 400


api.add_resource(Report, '/api/v1/report/')
api.add_resource(DriverID, '/api/v1/report/<driver_id>/')


if __name__ == "__main__":
    app.run(debug=True)
