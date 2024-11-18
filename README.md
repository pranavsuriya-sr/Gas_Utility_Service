# 🌟 Gas Utility Service Project 🚀  

**A Django-powered application for seamless Gas utility service management!**  
Whether you're a user requesting services or an admin managing them, this app has everything you need to simplify the process.  

---

## ✨ Features  

### 🧑‍💻 For Users:
- 🔒 **Login and Signup**:  
  - Create an account by entering your name, mobile number, location, email, and password.  
  - Secure login using your registered credentials.  

- 🛠️ **Service Management**:  
  - View a list of available services (e.g., Gas Installation, Gas Refill, Gas Leak Check).  
  - Select services by clicking checkboxes and request them with a single click.  
  - Track the **status** of your requested services (Pending ✅ / Completed 🎉) directly on the dashboard.  

---

### 🛡️ For Admins:
- 🔑 **Role-based Login**:  
  - Access your admin dashboard using admin credentials.  

- 🗂️ **Service Management**:  
  - Add new services to the list.  
  - View and process pending user service requests.  
  - Mark services as **Completed** 🟢, automatically updating user dashboards.  

---

### 🌍 General:
- 🎭 **Single Login Page**:  
  - One page for users and admins, with **role-based redirection**.  
- 🚫 **No Role Change**:  
  - All new accounts default to the "User" role, ensuring security and integrity.  
- 🌐 **Frontend**: Modern UI with **HTML, CSS, and JavaScript**.  
- 🔧 **Backend**: Powered by **Django** and **SQL** for robust performance.  

---
## 📹 Video Guide  

Here is a demonstration video:

https://github.com/user-attachments/assets/0ffc10a8-a382-4a97-b2e0-a0f9efd57b83

----
## 🛠️ Technology Stack  

| **Component**      | **Technology

**       |
|---------------------|----------------------|
| Frontend           | HTML, CSS, JavaScript |
| Backend            | Django               |
| Database           | SQL                  |

---

## 🎯 How It Works  

### 📌 For Users:  
1. 🔹 Sign up with your details.  
2. 🔹 Log in to your dashboard.  
3. 🔹 Request services and track their status.  

### 📌 For Admins:  
1. 🔸 Log in using admin credentials.  
2. 🔸 Add new services or process pending service requests.  
3. 🔸 Mark services as completed to notify users.  

---

## 📋 Sample Services  
- 🔧 Gas Installation  
- 🔄 Gas Refill  
- 🚨 Gas Leak Check  

---

## 🎯 Future Enhancements  
- 🔔 **Notifications**: Alert users when services are completed.  
- 📊 **Admin Analytics**: Track service trends and user engagement.  
- 🔒 **Enhanced Security**: Add email verification and password recovery.  

---

## 📂 Project Structure  

```plaintext
gas-utility-service-project/
├── app/                     # Main Django app
│   ├── templates/           # HTML templates
│   ├── views.py             # Application views
│   ├── models.py            # Database models
│   ├── urls.py              # URL routes
│   └── admin.py             # Admin configurations
├── manage.py                # Django management script
├── db                       # SQLite database
└── requirements.txt         # Python dependencies 

```
---

## 🚀 Quick Start  

### 1️⃣ Installation  
1. **Clone the repository**:  
 ```bash
  git clone https://github.com/pranavsuriya-sr/Gas_Utility_Service.git
  cd Gas_Utility_Service
   ```
2. **Set up the virtual environment**:
  ```bash
  python -m venv env
  source env/bin/activate  # On Windows: env\Scripts\activate
```

3. **Install dependencies**:
```bash
pip install -r requirements.txt

```
4. **Run migrations to set up the database**:
```bash
python manage.py migrate
```

5. **Start the development server**:
```bash
python manage.py runserver
```

6. **Access the app at: http://127.0.0.1:8000**.


## 👥 Contributors  

- 💡 **[S R Pranav Suriya](https://github.com/pranavsuriya-sr)**  

---

💻 **Feel free to fork, contribute, or suggest improvements!**  
⭐ Don't forget to star this repository if you found it helpful!  
