# TaskTrack - Task Management Web Application

TaskTrack is a small Flask web app for adding tasks, marking them complete, and deleting them. It demonstrates JIRA task allocation, Git/GitHub version control, Docker containerization, and localhost deployment.

## Requirements
- Python 3.10+ for running without Docker
- Git
- Docker Desktop for the container method
- A GitHub account
- A JIRA account

## Run locally with Python (Windows)
Open a terminal in this folder and run:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

If PowerShell blocks activation, use Command Prompt and run `.venv\Scripts\activate.bat`, then run the install and start commands.

Open http://localhost:5000 in your browser.

## Run using Docker
Start Docker Desktop, then run:

```bash
docker build -t tasktrack .
docker run --name tasktrack-app -p 5000:5000 tasktrack
```

Open http://localhost:5000. Stop the container with `docker stop tasktrack-app`. To remove it, run `docker rm tasktrack-app`.

The demo stores tasks in `tasks.json` in the app's current working directory. Container data may not persist after deleting/recreating the container unless you configure a persistent volume.

## Git and GitHub
Run:

```bash
git init
git add .
git commit -m "Initial TaskTrack application"
git branch -M main
```

Create an empty GitHub repository named `tasktrack`, then connect it (replace the placeholder):

```bash
git remote add origin https://github.com/YOUR-USERNAME/tasktrack.git
git push -u origin main
```

For a new feature, use a branch:

```bash
git checkout -b feature/add-task-validation
git add .
git commit -m "Add task validation"
git push -u origin feature/add-task-validation
```

Open a Pull Request on GitHub to review and merge the branch.

## JIRA task allocation
Create a JIRA project named **TaskTrack Development** using a Kanban template. Add these issues and assign each to an actual group member:

| Issue | Summary | Suggested owner | Acceptance criteria |
|---|---|---|---|
| TT-1 | Create Flask project structure | Member 1 | App starts without errors |
| TT-2 | Build task dashboard UI | Member 2 | Dashboard shows summary and task list |
| TT-3 | Implement add/complete/delete actions | Member 1 | All three actions work |
| TT-4 | Configure Docker container | Member 3 | App opens at localhost:5000 in Docker |
| TT-5 | GitHub repository and README | Member 2 | Code pushed and setup instructions documented |
| TT-6 | Test complete workflow | All members | Add, complete, and delete tasks are tested |

Use statuses **To Do → In Progress → Done**. The TT-1 style identifiers are suggested labels; JIRA will generate its own issue keys.

## Suggested demonstration
1. Add a task on the website.
2. Mark it completed, then delete it.
3. Show the JIRA board and assigned issues.
4. Show Git history with `git log --oneline`.
5. Show Docker status with `docker ps`.
6. Show the website at localhost:5000.

## Limitations
This is a learning/demo project, not a production service. It does not include login, a database server, or a live JIRA API integration. JIRA is used to allocate and track development work separately.
