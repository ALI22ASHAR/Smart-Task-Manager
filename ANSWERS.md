1. How to run

Install Python 3.14+, then from the repo root run:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r backend\requirements.txt
pip install -r frontend\requirements.txt
python manage.py migrate
python manage.py runserver
```

In another terminal:

```powershell
cd frontend
streamlit run app.py
```

2. Stack choice

I used Python with Django REST Framework for the backend and Streamlit for the UI because the project is small, fast to iterate, and already fits the repo layout. A heavier choice like React + Node would have added more setup and more moving parts without helping this task.

3. One real edge case

The frontend blocks blank task titles in [frontend/app.py](frontend/app.py#L21-L23). Without that check, the app would still try to send an empty task to the API, which would either fail later or create a bad user experience with a useless submission.

4. AI usage

I used Copilot tools to inspect files, fix code, and verify the app:

* `read_file` to inspect `frontend/app.py`, `backend/backend/settings.py`, `backend/backend/wsgi.py`, and the task API files.
* `get_errors` to surface the broken lines in `frontend/app.py`.
* `apply_patch` to repair `frontend/app.py`, `manage.py`, `backend/backend/settings.py`, `backend/backend/wsgi.py`, `README.md`, and this file.
* `run_in_terminal` to verify pip, install requirements, run Django checks, create migrations, apply migrations, and test task creation.
* `manage_todo_list` to track the work stages.

I changed one AI-suggested direction after checking the actual backend traceback: the first suspicion was the Streamlit UI, but the real issue was the missing `tasks_task` table, so I switched to fixing migrations instead.

5. Honest gap

The app still depends on a hard-coded local API URL in `frontend/app.py`, so it is not portable across environments without editing code. With another day, I would move that to an environment variable and add friendlier request error handling in the UI.
