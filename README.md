# 📝 The Shortest ToDo App Ever (with DB & CRUD)

A minimal example of a complete crossplatform database application built with [**q2gui**](https://pypi.org/project/q2gui/) and [**q2db**](https://pypi.org/project/q2db/).  
It demonstrates how to create a working **ToDo list** app with **SQLite**, **CRUD functionality**, **dark/light themes**, **import/export**, and **menu actions** — all in about 40 lines of Python!

---

## 🚀 Features

- ✅ Creates and initializes an in-memory SQLite database  
- 🧱 Defines a schema using `Q2DbSchema`  
- 📋 Provides a CRUD form for editing ToDo items  
- 🌞 Switch between Light and Dark modes  
- 🪶 Ultra-short, fully functional GUI + DB app  

---

## 🧩 Quick Start

```bash
git clone https://github.com/AndreiPuchko/q2-short.git
cd q2-short
python -m venv .venv
.venv\Scripts\activate  # or 'source .venv/bin/activate' on macOS/Linux
pip install q2db q2gui
python app.py
```

---


## 💾 Persistence Tip!

By default, the app uses an in-memory SQLite database, which means all data is lost when you close the app.

To make your data persistent, simply modify line 29 in todo_app.py:
```python
# In-memory (temporary) database:
self.db = Q2Db("sqlite3", database_name=":memory:")

# ➜ Change it to a file-based (persistent) database:
self.db = Q2Db("sqlite3", database_name="todo_database.sqlite")
```
This will store your ToDo data in a file named todo_database.sqlite in the same folder as the script.

---

## Screenshots
### Windows
![win0](https://andreipuchko.github.io/q2-short/docs/windows0.png)
![win1](https://andreipuchko.github.io/q2-short/docs/windows1.png)
### Linux
![lin0](https://andreipuchko.github.io/q2-short/docs/linux0.png)
![lin1](https://andreipuchko.github.io/q2-short/docs/linux1.png)
### Mac
![mac0](https://andreipuchko.github.io/q2-short/docs/mac0.png)
![mac1](https://andreipuchko.github.io/q2-short/docs/mac1.png)

---

## ⚙️ App Structure

### **App.__init__()**
- Initializes the main GUI window.  
- Defines menus and toolbar actions:  
  - Open the ToDo list form  
  - Switch between Light/Dark color modes  
  - Quit the app  
  - Show "About" dialog  

### **App.form()**
- Creates a `Q2Form` for the `todo` table.  
- Defines fields:  
  - `uid` — primary key  
  - `todo` — task text  
  - `bdate` — begin date  
  - `edate` — end date  
  - `done` — checkbox  
- Connects the form to the database via `Q2CursorModel`.  
- Adds a `/crud` action to enable Create, Read, Update, Delete operations.

### **App.create_database()**
- Creates an in-memory SQLite database.  
- Defines schema using `Q2DbSchema`.  
- Adds a table `todo` with fields for task, dates, and status.  
- Applies schema to the database.

### **App.run()**
- Starts the event loop and runs the GUI app.

---

## 🧰 Tech Stack

- [q2gui](https://pypi.org/project/q2gui/) – GUI framework (PyQt6)  
- [q2db](https://pypi.org/project/q2db/) – lightweight DB abstraction layer  
- SQLite – in-memory database  

---

## 📜 License

MIT License © [Andrei Puchko](https://github.com/AndreiPuchko)

---

## ⭐️ Why This Matters

This example shows how **little code** you need with **Q2** to make powerful database tools, admin panels, or utilities — all with a consistent GUI and no boilerplate.

> It’s arguably *the shortest fully functional CRUD + DB app ever written in Python.*
