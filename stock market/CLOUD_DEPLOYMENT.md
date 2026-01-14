# Cloud Deployment Guide

Here are the two best ways to run your **Stock Insight Tool** automatically 24/7 (well, once a week) without your computer being on.

---

## Option 1: GitHub Actions (Recommended - Easiest & Free)

GitHub Actions allows you to run this script on GitHub's servers for free.

### Steps:

1.  **Push your code to GitHub**:
    - Create a new repository on GitHub.
    - Upload all your files (`main.py`, `requirements.txt`, `src/`, etc.).

2.  **Add Your Secrets (Passwords)**:
    - Go to your GitHub Repository **Settings** > **Secrets and variables** > **Actions**.
    - Click **New repository secret**.
    - Add these two secrets:
        - Name: `GMAIL_USER` -> Value: `varunlakebright04@gmail.com`
        - Name: `GMAIL_PASS` -> Value: `nlor yqzy rtxe jjow`

3.  **The Workflow File is already created!**
    - I have created the file `.github/workflows/weekly_report.yml` for you.
    - This file tells GitHub to:
        - Wake up every Monday at 9:00 AM IST (3:30 AM UTC).
        - Install Python and dependencies.
        - Run `main.py --auto`.
        - Send the email.

---

## Option 2: Google Cloud Functions (Advanced)

This approach uses Google's serverless platform. It's robust but requires a billing account (though often stays within the free tier).

### Steps:

1.  **Prepare a GCP Wrapper**:
    - Cloud Functions need a specific function to "trigger". I have created `src/gcp_main.py` for this purpose.

2.  **Create the Function**:
    - Go to **Google Cloud Console** > **Cloud Functions**.
    - Click **Create Function**.
    - **Trigger**: Choose "Cloud Pub/Sub" (create a new topic named `weekly-stock-trigger`).
    - **Runtime**: Python 3.10 (or newer).
    - **Source Code**: Upload your files.
        - **Entry point**: `entry_point` (this matches the function in `src/gcp_main.py`).
    - **Environment Variables**:
        - Add `GMAIL_USER` and `GMAIL_PASS` under "Runtime, build, connections and security settings".

3.  **Schedule it**:
    - Go to **Cloud Scheduler**.
    - Create a Job.
    - **Frequency**: `30 9 * * 1` (Every Monday at 9:30 AM).
    - **Target**: Pub/Sub.
    - **Topic**: `weekly-stock-trigger`.

This will "ping" your function once a week, and it will run your script.
