# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return "Hello, World!"+" prakash"

# @app.route('/FaceBook')
# def fb():
# 	return "FB mat chala bhai coding kar le :)"

# if __name__ == '__main__':
#     app.run(debug=True)




from flask import Flask, jsonify,abort,make_response,request,url_for
import json
app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': 'Buy groceries',
        'description': 'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': 'Learn Python',
        'description': 'Need to find a good Python tutorial on the web',
        'done': False
    }
]


#TASK_1 and TASK_7
@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    with open('falsk_data.json','w+')as send_file:
        json.dump({'tasks':[make_public_task(task)for task in tasks]},send_file)
        return jsonify({'tasks':[make_public_task(task)for task in tasks]})

#TASK_3
@app.errorhandler(404)
def not_found(error):
	return make_response(jsonify({'error': 'Not found'}), 404)

#TASK_2
@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_id(task_id):
	task = [task for task in tasks if task['id'] == task_id ]
	if len(task) == 0:
		abort(404)
	return jsonify({'task':task[0]})

#TASK_4

@app.route('/todo/api/v1.0/tasks',methods=['POST'])
def create_new_dict():
	if not request.json or not 'title' in request.json:
		abort(404)
	# if len(tasks) >= 1:
	# 	Id = tasks[-1]['id']+1

	task={

		'id':tasks[-1]['id']+1,
		'title':request.json['title'],
		'description':request.json['description'],
		'done':False
	}
	tasks.append(task)
	return jsonify({"sucess":True})


#TASK_5

@app.route('/todo/api/v1.0/tasks/<int:task_id>',methods=['PUT'])
def update_task(task_id):
    task=[task for task in tasks if task['id'] == task_id]
    if len(task)==0:
        route(404)
    if not request.json:
        route(400)
    if 'title' in request.json and type(request.json['title'])!= str:
        route(400)
    if 'description' in request.json and type(request.json['description'])is not str:
        route(400)
    if 'done' in request.json and type(request.json['done']) is not bool:
        route(400)
    task[0]['title'] = request.json.get('title', task[0]['title'])
    task[0]['description']=request.json.get('description',task[0]['description'])
    task[0]['done'] = request.json.get('done', task[0]['done'])
    return jsonify({'task':task})

#TASK_6

@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    tasks.remove(task[0])
    return jsonify({'result': True})

#TASK_7

def make_public_task(task):
    new_task = {}
    for field in task:
        if field == 'id':
            new_task['uri']= url_for('get_id',task_id=task['id'],_external=True)
        else:
            new_task[field] = task[field]
    return new_task


if __name__ == '__main__':
    app.run(debug=True,port=8000)
