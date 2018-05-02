from flask import jsonify, request
from todo import app
from todo import Db as db
from datetime import datetime
from models import Task
import json



@app.route('/', methods=['GET'])
def index():
  return jsonify({ 'hello': 'world' })

@app.route('/tasks', methods=['POST'])
def tasks():
	name = request.args.get('name')
	description = request.args.get('description')
	due_date = int(request.args.get('due_date'))
	tags = request.args.get('tags')
	t = Task(name, description, tags, due_date).to_dict()
	db.insert_task(t["id"], t["name"], t["created_at"], t["description"], t["due_date"], t["tags"])
	return jsonify(t)

@app.route('/tasks', methods=['GET'])
def gettasks():
    taskid = request.args.get("id")
    if taskid == None:
        return jsonify(db.query())
    return jsonify(db.query_id(taskid))


@app.route('/tasks', methods=['DELETE'])
def delete_id():
    id = request.args.get('id')
    db.delete_task_id(id)
    return jsonify(success="true")

@app.route('/tasks/all', methods=['DELETE'])
def delete_all():
    db.delete_all_tasks()
    return jsonify(success="true")

@app.route('/tasks/deltable', methods=['DELETE'])
def delete_table():
	db.__init__()
	db.delete_task_table()
	return jsonify(success="true")
