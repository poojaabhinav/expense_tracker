## Expense Tracker 📊💰  

A web-based application to track daily expenses with **user authentication, data visualization, and an intuitive UI**.  

### 🚀 Features  
- **User Authentication** (Login & Signup)  
- **Add, View, and Delete Expenses**  
- **Category-wise Expense Breakdown**  
- **Interactive Charts & Graphs**  
- **SQLite Database Integration**  
- **Secure Password Hashing**  
- **Flask Backend with Jinja Templating**  

---  

## ⚙️ Installation & Setup  

Follow these steps to set up the project locally:  

### 1️⃣ Clone the Repository  
```sh
git clone https://github.com/poojaabhinav/expense_tracker.git
cd expense_tracker
```

### 2️⃣ Create a Virtual Environment  
```sh
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
# OR
.venv\Scripts\activate  # Windows
```

### 3️⃣ Install Dependencies  
```sh
pip install -r requirements.txt
```

### 4️⃣ Set Up the Database  
```sh
python separatedatabase.py
```

### 5️⃣ Run the Application  
```sh
python app.py
```
Now, open [http://127.0.0.1:5000/](http://127.0.0.1:5000/) in your browser.  

---  

## 🛠️ Technologies Used  

- **Backend:** Flask (Python)  
- **Database:** SQLite  
- **Frontend:** HTML, CSS, JavaScript  
- **Libraries:** Flask, Jinja2, SQLAlchemy, SQLite3, Chart.js  

---  

## 🎮 Screenshots  

*(Add screenshots of your app, such as login, dashboard, expense entries, etc.)*  

---  

## 👤 User Guide  

1. **Sign Up** for an account.  
2. **Log In** with your credentials.  
3. **Add expenses** by selecting category, amount, and date.  
4. **View expense summary** in an interactive chart.  
5. **Delete or modify** expenses as needed.  
6. **Logout** securely.  

---  

## 📂 Folder Structure  

```
expense_tracker/
│── static/
│   ├── css/
│   │   ├── styles.css
│   ├── js/
│   │   ├── script.js
│── templates/
│   ├── base.html
│   ├── index.html
│   ├── login.html
│   ├── signup.html
│── app.py
│── separatedatabase.py
│── requirements.txt
│── README.md
│── .gitignore
```

---  

## 🤝 Contributing  

Feel free to **fork** this repository and submit a **pull request** with improvements! 🚀  

---  

## 📝 License  

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.  

