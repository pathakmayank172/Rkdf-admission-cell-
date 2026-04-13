# 🎓 RKDF University Ranchi — MIS Admission Cell Website

A complete full-stack web application for managing university admissions,
built with **Django** (backend) + **HTML, CSS, JavaScript** (frontend).

---

## 📁 Project Structure

```
rkdf_admission/                        ← Root project folder
│
├── manage.py                          ← Django command-line tool
├── requirements.txt                   ← Python dependencies
├── db.sqlite3                         ← SQLite database (auto-created)
│
├── rkdf_admission/                    ← Django project configuration
│   ├── __init__.py
│   ├── settings.py                    ← All project settings
│   ├── urls.py                        ← Root URL routing
│   └── wsgi.py                        ← WSGI server entry point
│
└── admission/                         ← Main Django app
    ├── __init__.py
    ├── apps.py                        ← App configuration
    ├── models.py                      ← Database models (AdmissionForm)
    ├── views.py                       ← Page logic & form handling
    ├── urls.py                        ← App-level URL patterns
    ├── admin.py                       ← Admin panel configuration
    │
    ├── templates/
    │   └── admission/
    │       ├── base.html              ← Base template (navbar + footer)
    │       ├── home.html              ← Home page
    │       ├── about.html             ← About University page
    │       ├── courses.html           ← Courses listing page
    │       ├── admission_form.html    ← Student admission form
    │       ├── dashboard.html         ← MIS dashboard (all records)
    │       └── contact.html           ← Contact page
    │
    └── static/
        └── admission/
            ├── css/
            │   └── style.css          ← All styles (responsive design)
            └── js/
                └── main.js            ← Form validation + interactions
```

---

## 🗄️ Database Model

The `AdmissionForm` model stores:

| Field               | Type          | Description                          |
|---------------------|---------------|--------------------------------------|
| `name`              | CharField     | Student's full name                  |
| `email`             | EmailField    | Unique email address                 |
| `phone`             | CharField     | 10-digit mobile number               |
| `course`            | CharField     | Selected course (BCA, BBA, etc.)     |
| `address`           | TextField     | Residential address                  |
| `father_name`       | CharField     | Father's name                        |
| `date_of_birth`     | DateField     | Date of birth                        |
| `tenth_percentage`  | DecimalField  | 10th board percentage                |
| `twelfth_percentage`| DecimalField  | 12th board percentage                |
| `status`            | CharField     | pending / approved / rejected        |
| `submitted_at`      | DateTimeField | Auto-set on submission               |

---

## 🌐 URL Routes

| URL                | View Function    | Page                    |
|--------------------|------------------|-------------------------|
| `/`                | `home`           | Home page               |
| `/about/`          | `about`          | About University        |
| `/courses/`        | `courses`        | Courses listing         |
| `/apply/`          | `admission_form` | Admission form          |
| `/dashboard/`      | `dashboard`      | MIS Student Dashboard   |
| `/contact/`        | `contact`        | Contact page            |
| `/admin/`          | Django Admin     | Admin panel             |

---

## 🚀 How to Run the Project Locally

Follow these steps exactly. Each step is explained clearly.

---

### ✅ STEP 1 — Install Python

Make sure Python 3.8 or higher is installed.

Check your version:
```bash
python --version
# or
python3 --version
```

Download Python from: https://www.python.org/downloads/

---

### ✅ STEP 2 — Create a Virtual Environment

A virtual environment keeps your project's packages separate from other projects.

```bash
# Navigate to the project folder
cd rkdf_admission

# Create virtual environment named "venv"
python -m venv venv

# Activate virtual environment:

# On Windows:
venv\Scripts\activate

# On Mac/Linux:
source venv/bin/activate
```

You will see `(venv)` appear in your terminal — this means it's active.

---

### ✅ STEP 3 — Install Django

```bash
pip install -r requirements.txt
```

This installs Django. Verify with:
```bash
python -m django --version
# Should print: 4.x.x
```

---

### ✅ STEP 4 — Create Database Tables (Migrations)

Django needs to create tables in SQLite based on our models.

```bash
# Step 4a: Generate migration files
python manage.py makemigrations

# Step 4b: Apply migrations to create the actual tables
python manage.py migrate
```

After this, a `db.sqlite3` file will appear in the project folder.
This is your database.

---

### ✅ STEP 5 — Create a Superuser (Admin Account)

This lets you log into the admin panel at `/admin/`.

```bash
python manage.py createsuperuser
```

It will prompt you for:
```
Username: admin
Email address: admin@example.com
Password: (type a strong password)
Password (again): (confirm)
```

---

### ✅ STEP 6 — Run the Development Server

```bash
python manage.py runserver
```

You should see:
```
Starting development server at http://127.0.0.1:8000/
```

---

### ✅ STEP 7 — Open in Browser

| Page             | URL                                  |
|------------------|--------------------------------------|
| Home             | http://127.0.0.1:8000/               |
| About            | http://127.0.0.1:8000/about/         |
| Courses          | http://127.0.0.1:8000/courses/       |
| Apply            | http://127.0.0.1:8000/apply/         |
| Dashboard        | http://127.0.0.1:8000/dashboard/     |
| Contact          | http://127.0.0.1:8000/contact/       |
| **Admin Panel**  | http://127.0.0.1:8000/admin/         |

---

## 🛠️ Admin Panel Guide

1. Go to: http://127.0.0.1:8000/admin/
2. Login with the superuser credentials you created
3. Click on **"Admission Applications"**
4. You can:
   - View all submitted applications
   - Search by name, email, phone
   - Filter by course, status, date
   - **Change status** (pending → approved/rejected) directly in the list
   - View full application details

---

## 🔧 Common Commands Reference

```bash
# Start server
python manage.py runserver

# Create migrations after changing models.py
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create admin user
python manage.py createsuperuser

# Open Django shell (Python REPL with Django loaded)
python manage.py shell

# View all registered URL patterns
python manage.py show_urls   # (requires django-extensions)

# Collect static files (for production)
python manage.py collectstatic
```

---

## 💡 How Django Works — Quick Explanation for Beginners

```
Browser                     Django
  |                            |
  |  GET /courses/             |
  |--------------------------->|
  |                            |  1. urls.py matches "/courses/"
  |                            |  2. Calls courses() in views.py
  |                            |  3. views.py fetches data
  |                            |  4. Renders courses.html template
  |  HTML Page Response        |  5. Returns completed HTML
  |<---------------------------|
```

**Key Files:**
- `models.py` → Defines what data to store (tables)
- `views.py`  → Contains logic for each page
- `urls.py`   → Maps URLs to view functions
- `templates/`→ Contains HTML files with `{{ variable }}` placeholders
- `static/`   → CSS, JS, images

---

## 📱 Features Summary

| Feature                    | Technology Used           |
|----------------------------|---------------------------|
| Responsive navigation      | HTML + CSS + JavaScript   |
| Mobile hamburger menu      | JavaScript                |
| Form validation (frontend) | JavaScript                |
| Form validation (backend)  | Python / Django views     |
| Database storage           | Django ORM + SQLite       |
| Admin panel                | Django Admin              |
| Flash messages             | Django Messages Framework |
| CSRF protection            | Django middleware          |
| Counter animations         | JavaScript (Intersection Observer) |
| Filter/search dashboard    | Django ORM + JavaScript   |
| Responsive design          | CSS3 (Flexbox + Grid)     |

---

## ❓ Troubleshooting

**Problem:** `ModuleNotFoundError: No module named 'django'`
**Fix:** Make sure your virtual environment is activated (`source venv/bin/activate`)

**Problem:** `OperationalError: no such table`
**Fix:** Run `python manage.py migrate`

**Problem:** Static files (CSS/JS) not loading
**Fix:** Make sure `DEBUG = True` in settings.py during development

**Problem:** Port 8000 already in use
**Fix:** `python manage.py runserver 8080` (use a different port)

---

## 👨‍💻 Technologies Used

- **Backend:** Python 3.x, Django 4.2
- **Frontend:** HTML5, CSS3, JavaScript (Vanilla)
- **Database:** SQLite (via Django ORM)
- **Fonts:** Google Fonts (Playfair Display + DM Sans)
- **Design:** Custom CSS with CSS Variables

---

*Built for RKDF University Ranchi — MIS Admission Cell Project*
