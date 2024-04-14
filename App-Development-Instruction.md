# Python-App-Deployment-Project

To expose the To-Do application as a REST service and interact with it from a front end, we can utilize a framework like Flask to create a web server and handle HTTP requests. Here's how you can modify the To-Do application to expose it as a REST service and create a basic front end to interact with it:

1. **Install Flask:**
   Before proceeding, make sure you have Flask installed. You can install it via pip:
   ```
   pip install Flask
   ```

2. **Modify the To-Do App:**
   Update the To-Do application to handle HTTP requests using Flask. Here's a modified version:

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

tasks = []

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    task = data.get('task')
    tasks.append(task)
    return jsonify({'message': 'Task added successfully!'})

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def complete_task(task_id):
    if task_id >= 0 and task_id < len(tasks):
        tasks[task_id] = "[X] " + tasks[task_id]
        return jsonify({'message': 'Task marked as completed!'})
    else:
        return jsonify({'error': 'Invalid task index.'}), 400

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    if task_id >= 0 and task_id < len(tasks):
        del tasks[task_id]
        return jsonify({'message': 'Task deleted successfully!'})
    else:
        return jsonify({'error': 'Invalid task index.'}), 400

if __name__ == "__main__":
    app.run(debug=True)
```

3. **Create a Basic Front End:**
   Now, you can create a basic front end using HTML and JavaScript to interact with the To-Do application. You can use AJAX to send requests to the REST endpoints created by Flask.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>To-Do App</title>
</head>
<body>
    <h1>To-Do App</h1>
    <input type="text" id="taskInput" placeholder="Enter task">
    <button onclick="addTask()">Add Task</button>
    <ul id="taskList"></ul>

    <script>
        function addTask() {
            var taskInput = document.getElementById("taskInput");
            var task = taskInput.value;
            taskInput.value = "";

            fetch('/tasks', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ task: task })
            })
            .then(response => response.json())
            .then(data => {
                alert(data.message);
                getTasks();
            });
        }

        function getTasks() {
            fetch('/tasks')
            .then(response => response.json())
            .then(data => {
                var taskList = document.getElementById("taskList");
                taskList.innerHTML = "";
                data.tasks.forEach(function(task, index) {
                    var listItem = document.createElement("li");
                    listItem.textContent = task;
                    taskList.appendChild(listItem);
                });
            });
        }

        getTasks();
    </script>
</body>
</html>
```

To configure the Flask application to be accessible at `http://127.0.0.1:5000/`, you don't need to make any changes to the code. By default, when you run a Flask application, it listens on `127.0.0.1` (localhost) and port `5000`.

Here's what you need to do:

1. **Run the Flask Application:**
   Save the Flask code to a Python file (e.g., `app.py`). Open a terminal or command prompt, navigate to the directory containing `app.py`, and run the Flask application by executing the command:
   ```
   python app.py
   ```
   This will start the Flask application, and it will be accessible at `http://127.0.0.1:5000/`.

2. **Access the API:**
   Once the Flask application is running, you can access the API endpoints defined in the application using any HTTP client (such as a web browser, cURL, or tools like Postman). For example:
   - To view tasks, you can access `http://127.0.0.1:5000/tasks` in a web browser or use cURL:
     ```
     curl http://127.0.0.1:5000/tasks
     ```
   - To add a task, you can send a POST request to `http://127.0.0.1:5000/tasks` with a JSON payload containing the task data.

3. **Access the Front End:**
   To access the front end of the application, open a web browser and navigate to `http://127.0.0.1:5000/`. You should see the To-Do App interface where you can add, view, complete, and delete tasks.

Since the Flask application is running on `127.0.0.1` (localhost) and port `5000`, you can access it locally using that URL. If you want to access it from other devices on the same network, you can use your computer's IP address instead of `127.0.0.1` (e.g., `http://192.168.1.100:5000/`). Just make sure any firewall settings allow access to port `5000`.
