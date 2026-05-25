import streamlit as st
import requests
import pandas as pd

API_URL = "http://127.0.0.1:8000/api/tasks/"

st.set_page_config(page_title="Smart Task Manager", layout="wide")

st.title("Smart Task & Productivity Manager")

# Sidebar
st.sidebar.header("Create New Task")

with st.sidebar.form("task_form", clear_on_submit=True):
    title = st.text_input("Task Title")
    description = st.text_area("Description")
    priority = st.selectbox("Priority", ["Low", "Medium", "High"])

    submitted = st.form_submit_button("Add Task")

    if submitted:
        if title.strip() == "":
            st.sidebar.error("Task title cannot be empty")
        else:
            payload = {
                "title": title,
                "description": description,
                "priority": priority,
                "completed": False
            }

            response = requests.post(API_URL, json=payload)

            if response.status_code == 201:
                st.sidebar.success("Task Added Successfully")
            else:
                st.sidebar.error("Failed to add task")

# Fetch tasks
response = requests.get(API_URL)

if response.status_code == 200:
    tasks = response.json()
else:
    tasks = []

# Statistics
st.subheader("Dashboard")

search = st.text_input("Search Tasks")

completed_count = len([t for t in tasks if t['completed']])
pending_count = len([t for t in tasks if not t['completed']])
high_priority = len([t for t in tasks if t['priority'] == 'High'])
filtered_tasks = [
    task for task in tasks
    if search.lower() in task['title'].lower()
]

metric_col1, metric_col2, metric_col3 = st.columns(3)

metric_col1.metric("Completed", completed_count)
metric_col2.metric("Pending", pending_count)
metric_col3.metric("High Priority", high_priority)

st.divider()

# Display Tasks
st.subheader("All Tasks")

for task in filtered_tasks:
    with st.container(border=True):
        task_col1, task_col2, task_col3 = st.columns([5, 2, 2])

        with task_col1:
            st.markdown(f"### {task['title']}")
            st.write(task['description'])
            st.write(f"Priority: {task['priority']}")

        with task_col2:
            if task['completed']:
                st.success("Completed")
            else:
                if st.button(f"Mark Done {task['id']}"):
                    update_payload = {
                        "title": task['title'],
                        "description": task['description'],
                        "priority": task['priority'],
                        "completed": True
                    }

                    requests.put(f"{API_URL}{task['id']}/", json=update_payload)
                    st.rerun()

        with task_col3:
            if st.button(f"Delete {task['id']}"):
                requests.delete(f"{API_URL}{task['id']}/")
                st.rerun()
