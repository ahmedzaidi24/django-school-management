# School Management System – Django Web Application

## 📚 Overview
This Django-based web application was developed for the **COMP6006: Web Application Frameworks** unit at Curtin University. The system manages student and course data within a university’s School of Computer Science. It demonstrates foundational concepts in Django development including relational modeling, templating, URL routing, view creation, and role-based access logic.

---

## 🎯 Project Goal
To build a clean, modular, and secure Django application that allows:
- 🧑‍🏫 Viewing a list of courses and students
- 🧾 Displaying course details including enrolled students
- 🔄 CRUD operation planning based on user roles (coordinators, students, visitors)

---

## 🧩 Models
### Course
- `name`: CharField – course title
- `coordinator`: CharField – course leader name
- `size`: PositiveIntegerField – maximum number of students allowed

### Student
- `name`: CharField
- `email`: EmailField – with auto-validation
- `student_id`: CharField – supports alphanumeric IDs
- `date_of_birth`: DateField – stores DOB only (no time)
- `course`: ForeignKey – each student is enrolled in exactly one course

Includes a method `total_students()` to compute enrolled count.

---

## 🔁 URL Endpoints
| URL | Functionality |
|-----|----------------|
| `/schoolmanagement/courses/` | Lists all available courses |
| `/schoolmanagement/students/` | Lists all students enrolled in the school |
| `/schoolmanagement/courses/<id>/` | Shows detailed view of a single course and its enrolled students |

---

## 🧱 Template Structure
- Built with **base.html** inheritance
- Navigation links to students and courses on every page
- Templates include:
  - `course_list.html`
  - `student_list.html`
  - `single_course.html`

---

## 🔐 Role-Based CRUD Planning
| Role | Allowed Operations | Justification |
|------|---------------------|----------------|
| **Course Coordinator** | Create, Read, Update, Delete | Owns and manages course data |
| **Student** | Create (self), Read (own/course info), Update (own info) | Must access/update personal info but not others |
| **Visitor** | Read (course info only) | Restricted from creating, editing, or deleting any data |

---

## 🛡️ Security & Dev Benefits
- ✅ Built-in Django admin for ease of data entry
- ✅ CSRF protection, email validation, and secure password handling
- ✅ Simplified structure using models, views, and templates separation

---

## 🚀 Getting Started
1. Clone the project
```bash
git clone https://github.com/yourusername/django-school-management.git
cd schoolmanagement
```
2. Run migrations
```bash
python manage.py makemigrations
python manage.py migrate
```
3. Run the server
```bash
python manage.py runserver
```
4. Access locally:
- `http://127.0.0.1:8000/schoolmanagement/courses/`
- `http://127.0.0.1:8000/schoolmanagement/students/`

---

## 📁 Project Files
| File | Description |
|------|-------------|
| `manage.py` | Django project manager file |
| `db.sqlite3` | SQLite database storing project data |
| `Requirements.pdf` | Project specification |
| `20972008_Word_File.docx` | Design explanations, CRUD rules, and justification |

---

## 👤 Author
**Syed Muhammad Ahmed Zaidi**  
Curtin University | Student ID: 20972008  
Unit: COMP6006 – Web Application Frameworks

---

## 📝 License
Academic use only. For commercial use or reproduction, contact the author.

---
