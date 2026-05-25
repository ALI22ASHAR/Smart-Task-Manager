# Smart-Task-Manager

Smart Task & Productivity Manager

Run it on a fresh machine:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r backend\requirements.txt
pip install -r frontend\requirements.txt
python manage.py migrate
python manage.py runserver
```

In a second terminal:

```powershell
cd frontend
streamlit run app.py
```

This starts the Django REST API on `http://127.0.0.1:8000` and the Streamlit UI on its default local port.

Additional notes:
- Backend is a Django REST Framework API under the `backend/` folder.
- Frontend is a Streamlit app at `frontend/app.py` that calls the API at `http://127.0.0.1:8000/api/tasks/`.

