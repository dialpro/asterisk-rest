#! /usr/bin/python3
from flask import Flask, jsonify, make_response
from datetime import datetime, timedelta
from subprocess import check_output
import csv


def last3month( date_to_parse):
    datetime_object = datetime.strptime(date_to_parse, '%Y-%m-%d %H:%M:%S')
    return datetime.now() - timedelta(days=90) < datetime_object 

fieldnames = ['accountcode', 'src', 'dst', 'dcontext', 'clid', 'channel', 'dstchannel', 'lastapp', 'lastdata', 'start', 'answer', 'end', 'duration', 'billsec', 'disposition', 'amaflags', 'uniqueid']


app = Flask(__name__)

@app.route('/api/v1.0/calls', methods=['GET'])
def get_tasks():
    calls_dict = []
    with open('/var/log/asterisk/cdr-csv/Master.csv') as csvfile:
        callreader = csv.reader(csvfile)
        for row in callreader:
            call = dict(zip( fieldnames, row));
            if last3month(call['start']):
                calls_dict.append( call)
    return jsonify({'calls': calls_dict})

@app.errorhandler(404)
def not_found(error):
        return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)

