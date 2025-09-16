# EventHub 🎉
A full-featured event management web application built with **Django** and **SQLite**, where users can discover, create, and register for events. 

---

## ✨ Features  
- Browse events with images, descriptions, dates, and locations 📅  
- User registration & authentication 🔑  
- Create and manage events (for logged-in users) 📝  
- Register / cancel registration for events   
- Responsive event cards UI (Bootstrap 5 + custom CSS)   
- Event calendar view 
- Admin dashboard for managing events & users ⚙️  

---

## 🚀 Getting Started  

### Prerequisites  
- Python 3.10+ (tested with 3.13.7) 🐍  
- pip (Python package manager)  
- Virtual environment (recommended)  

### Installation  

1. **Clone the repository**  
```bash
git clone https://github.com/subashkatwal/Event-Hub.git
cd EventHub
```

2. **Set up a virtual environment**  
```bash
python -m venv env
# Windows
env\Scripts\activate
# macOS / Linux
source env/bin/activate
```

3. **Install dependencies**  
```bash
pip install -r requirements.txt
```

4. **Run migrations**  
```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Create a superuser**  
```bash
python manage.py createsuperuser
```

6. **Run the development server**  
```bash
python manage.py runserver
```

7. **Open in browser**  
- Site → `http://127.0.0.1:8000/`  
- Admin → `http://127.0.0.1:8000/admin/`  

---

## 📂 Project Structure  

```
EventHub/
├─ event/                 # Django app
│  ├─ templates/event/    # HTML templates
│  ├─ static/event/       # CSS/JS/Images
│  ├─ migrations/
│  ├─ models.py           # Event & Registration models
│  ├─ views.py            # Views (list, create, detail, etc.)
│  ├─ urls.py             # App routes
├─ media/                 # Uploaded images
├─ static/                # Static files
├─ db.sqlite3             # SQLite database
├─ manage.py
└─ requirements.txt
```

---

## ⚡ How It Works  
- **View Events** → Browse all events with details.  
- **Create Event** → Admins can create events.  
- **Register** → Click “Register” to join an event.    
- **Admin Panel** → Manage users, events, and registrations.  

---

## 🛠️ Technologies Used  
- **Backend:** Django (5.2.6)  
- **Database:** SQLite (default)  
- **Frontend:** Bootstrap 5, Bootstrap Icons, Font Awesome  
- **Other:** Pillow (for image upload support)  

---

## 💡 Future Improvements  
- Cancel Registration → Unregister anytime.
- Event categories & search functionality 🔍  
- Persistent registrations with notifications 🔔  
- Improved calendar with filters 📅  
- Deployment on cloud platforms (Heroku / Render) 🌐  
- REST API for mobile integration 📱 
 

---

## 📖 Documentation  
- [Django Official Docs](https://docs.djangoproject.com/en/5.0/)  
- Project Report (detailed) → [View Report](https://drive.google.com/file/d/17eRSBLOWD34Hhh2BLQhUzqQEiiimc18h/view?usp=sharing)  

---

## 👨‍💻 Author  
**Subash Katwal**  
