# 📊 Subscription Manager System

A menu-driven **Python CRUD application** for managing digital subscriptions like Netflix, Spotify, Amazon Prime, etc.

The application runs in the terminal and uses the **Rich library** to provide an attractive and user-friendly interface. Subscription records are stored in memory and can be exported to Excel.

---

## 📌 Project Overview

Managing multiple subscriptions manually can be difficult when tracking renewal dates, costs, and usage.

The **Subscription Manager System** provides a simple solution to:

* Track all subscriptions in one place
* Monitor renewal dates
* Analyze expenses
* Get smart suggestions

---

## ✨ Features

### 1. Add Subscription

Users can add a new subscription with details such as:

* Service Name
* Plan Type (Monthly/Yearly)
* Cost
* Renewal Date
* Last Used Date

---

### 2. View Subscriptions

Displays all subscriptions in a formatted table using Rich.

The table includes:

* ID
* Name
* Plan
* Cost
* Renewal Date
* Status

Menu UI example:

---

### 3. Update Subscription

Users can update:

* Name
* Plan
* Cost
* Renewal Date
* Status (Active/Cancelled)

---

### 4. Delete Subscription

Users can delete a subscription using its ID.

---

### 5. Export to Excel

The system exports all subscription data to an Excel file.

* File name: `subscriptions.xlsx`

Export logic:

---

### 6. Smart Suggestions

The system provides intelligent suggestions such as:

* ⚠️ Expired subscriptions
* ⏳ Expiring soon
* 📉 Not used recently
* 💰 Expensive subscriptions

---

### 7. Total Expense

Calculates total cost of all active subscriptions.

---

## 🛠️ Technologies Used

| Technology | Purpose          |
| ---------- | ---------------- |
| Python     | Core programming |
| Rich       | CLI UI           |
| Pandas     | Data handling    |
| OpenPyXL   | Excel export     |

Dependencies:

---

## 📂 Project Structure

```text
subscription-manager/
│
├── main.py              # Main menu & control flow
├── subscription.py      # CRUD operations
├── storage.py           # Data storage (list-based)
├── export_excel.py      # Excel export
├── requirements.txt     # Dependencies
├── subscriptions.xlsx   # Output file
```

---

## 🧩 Project Architecture

```text
            main.py
               │
   ┌───────────┼───────────┐
   │           │           │
   ▼           ▼           ▼
subscription  storage   export_excel
     │           │           │
     ▼           ▼           ▼
 CRUD Ops     Data List    Excel File
```

---

## 💾 Data Storage

The application stores data in memory using a Python list.

Storage logic:

⚠️ Data will be lost after program exit.

---

## 🔄 CRUD Operations

The project implements full CRUD:

* Create → Add subscription
* Read → View subscriptions
* Update → Modify subscription
* Delete → Remove subscription

Example structure:

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/subscription-manager.git
```

### 2. Open project folder

```bash
cd subscription-manager
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

```bash
python main.py
```

Menu will appear:

```text
1. Add Subscription
2. View Subscriptions
3. Update Subscription
4. Delete Subscription
5. Export to Excel
6. Smart Suggestion
7. Show Total Expense
8. Exit
```

---

## 📊 Smart Logic

The system analyzes subscription data using:

* Days left for renewal
* Days since last use
* Cost comparison

This helps users make better decisions.

---

## ⚠️ Limitations

* No database (data not saved permanently)
* No authentication system
* Manual date input

---

## 🚀 Future Improvements

* Add database (SQLite / MongoDB)
* Add notification system
* Add GUI (Tkinter / Web App)
* Add automatic reminders
* Add login system

---

## 🎯 Learning Objectives

This project demonstrates:

* Python fundamentals
* CRUD operations
* Modular programming
* CLI UI using Rich
* Excel export using Pandas
* Project structuring

---

## 👨‍💻 Author

**Subscription Manager Project**

Built as a Python CRUD project for learning and practical implementation.

---