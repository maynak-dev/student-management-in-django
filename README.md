
# Student Management System (Django)

A web‑based Student Management System built with Django, allowing administrators to manage students, their data and related operations via a clean UI and admin backend.

## 🚀 Live Demo  
[https://student-management-in-django.vercel.app/](https://student-management-in-django.vercel.app/)

## 📁 Repository  
[maynak‑dev/student‑management‑in‑django](https://github.com/maynak-dev/student-management-in-django)

---

## 🧩 Features  
- Add, update, delete student records (with photo uploads)  
- Student profile management  
- Admin panel for overview of students  
- Media support (student photos)  
- Static files build for production (via `staticfiles_build`)  
- Simple responsive UI for both admin & student views  
- SQLite used by default for quick setup  
- Deployment ready for Vercel (via `vercel.json`)

---

## 🛠️ Technology Stack  
- Backend: Django (Python)  
- Database: SQLite (default)  
- Frontend: HTML, CSS, JavaScript, Bootstrap  
- Static build: Custom build script (`build_files.sh`) + staticfiles folder  
- Hosting / Deployment: Vercel (configured via `vercel.json`)

---

## 📦 Getting Started  
### Prerequisites  
- Python (3.x recommended)  
- pip (Python package manager)  
- Git  
- (Optional) Virtual environment tool: `venv`, `virtualenv`, etc.

### Installation Steps  
1. Clone the repository  
   ```bash
   git clone https://github.com/maynak-dev/student-management-in-django.git
   cd student-management-in-django
   ```  
2. Create & activate a virtual environment (recommended)  
   ```bash
   python -m venv venv
   source venv/bin/activate    # or: venv\Scripts\activate on Windows
   ```  
3. Install required packages  
   ```bash
   pip install -r requirements.txt
   ```  
4. Apply migrations  
   ```bash
   python manage.py migrate
   ```  
5. Create a superuser (for Django admin)  
   ```bash
   python manage.py createsuperuser
   ```  
6. Run the development server  
   ```bash
   python manage.py runserver
   ```  
   Then open `http://127.0.0.1:8000/` in your browser.

---

## ⚙️ Configuration  
- `db.sqlite3` file is included for demo purposes; for production you may switch to PostgreSQL or MySQL.  
- Static files are built into `staticfiles_build/static/` using the shell script `build_files.sh` — you can adjust for your workflow.  
- Deployment to Vercel is configured via `vercel.json`. Customize settings (environment variables, build command) as required.

---

## 📂 Project Structure  
```
media/                   # Media uploads (student photos)  
sms/                     # Django project root (settings, urls, wsgi)  
students/                # Django app for student management  
templates/               # HTML templates  
staticfiles_build/       # Built static files for production  
manage.py                # Django management script  
requirements.txt         # Python dependencies  
vercel.json              # Deployment config for Vercel  
build_files.sh           # Script to build static files  
db.sqlite3               # SQLite DB (demo)  
```  

---

## ✅ Usage  
- Navigate to the Django admin panel (`/admin/`) and login with the superuser created.  
- Add student entries with required fields, upload photos.  
- Explore the front‑end views to list/view students.  
- For production deployment: build static files, configure your database & environment variables, then deploy.

---

## 🔧 Customization & Extensibility  
- You can replace SQLite with PostgreSQL or MySQL by changing `DATABASES` in `settings.py`.  
- Extend the `students` app to include additional models such as Courses, Attendance, Grades.  
- Enhance UI using modern front‑end frameworks (e.g., React, Vue) or add REST API endpoints with `django-rest-framework`.  
- Add authentication for student users and role‑based access (admin vs student vs teacher).  
- Implement file storage (AWS S3, Google Cloud Storage) for media in production.

---

## 📝 License  
This project is open‑source (specify license if you have one, e.g., MIT). Feel free to use, modify, and distribute.

---

## 👤 Author  
- **Maynak Dey**  
- GitHub: [@maynak‑dev](https://github.com/maynak-dev)  
- Created this project as part of learning/development in Django and deployment workflows.

---

## 🎯 Acknowledgments  
- Thanks to the Django community for the excellent framework and documentation.  
- Inspired by various student/education management system tutorials and open‑source projects.
