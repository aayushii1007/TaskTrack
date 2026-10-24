from flask import Flask, render_template, request, redirect, url_for
import json
import os
from uuid import uuid4

app = Flask(__name__)
DATA_FILE = os.environ.get("TASK_DATA_FILE", "tasks.json")

def load_tasks():
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        return []

def save_tasks(tasks):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=2)

@app.route("/")
def index():
    tasks = load_tasks()
    total = len(tasks)
    completed = sum(1 for task in tasks if task["completed"])
    return render_template("index.html", tasks=tasks, total=total,
                           completed=completed, pending=total-completed)

@app.route("/add", methods=["POST"])
def add_task():
    title = request.form.get("title", "").strip()
    if title:
        tasks = load_tasks()
        tasks.insert(0, {"id": str(uuid4()), "title": title, "completed": False})
        save_tasks(tasks)
    return redirect(url_for("index"))

@app.route("/toggle/<task_id>", methods=["POST"])
def toggle_task(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = not task["completed"]
            break
    save_tasks(tasks)
    return redirect(url_for("index"))

@app.route("/delete/<task_id>", methods=["POST"])
def delete_task(task_id):
    tasks = [task for task in load_tasks() if task["id"] != task_id]
    save_tasks(tasks)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
