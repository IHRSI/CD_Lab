# Lab 8 - Django Form Processing Summary

## ✅ Project Completion Status

All lab exercises have been successfully created and tested.

### Project Name: **lab8**
### Framework: **Django 5.2.12**
### Python Version: **3.11**

---

## 📋 Questions & Additional Questions Summary

### **QUESTIONS (Q)** - Main Lab Exercises

#### **Q1: Register & Success Page** ✅
- **Theme Color:** Blue (#007bff)
- **Location:** `/q1/register/`
- **Files Created:**
  - `q1/forms.py` - RegisterForm with 4 fields
  - `q1/views.py` - register() and success() views
  - `q1/urls.py` - URL routing
  - `q1/templates/q1/register.html` - Registration form
  - `q1/templates/q1/success.html` - Success page
  
- **Requirements Met:**
  - ✅ 4 input fields: Username (required), Password, Email, Contact Number (optional)
  - ✅ Submit button
  - ✅ Success page shows "Welcome {UserName}"
  - ✅ Email and Contact Number displayed
  - ✅ Uses CSRF token for security
  - ✅ Two-page design as requested

#### **Q2: Voting System** ✅
- **Theme Color:** Red (#dc3545)
- **Location:** `/q2/vote/`
- **Files Created:**
  - `q2/views.py` - vote() and results() views
  - `q2/urls.py` - URL routing
  - `q2/templates/q2/vote.html` - Voting form
  - `q2/templates/q2/results.html` - Results page

- **Requirements Met:**
  - ✅ Question: "How is the book ASP.NET with C# by Vipul Prakashan?"
  - ✅ Three choices: Good, Satisfactory, Bad
  - ✅ VOTE button
  - ✅ Results shown in percentage using labels
  - ✅ Two-page design

#### **Q3: CGPA Calculator** ✅
- **Theme Color:** Pink (#e75480)
- **Location:** `/q3/calculate/`
- **Files Created:**
  - `q3/forms.py` - CGPAForm
  - `q3/views.py` - calculate() and result() views
  - `q3/urls.py` - URL routing
  - `q3/templates/q3/calculate.html` - Input form
  - `q3/templates/q3/result.html` - Result page

- **Requirements Met:**
  - ✅ Page 1: Two TextBoxes (name, total marks) and Calculate button
  - ✅ Page 2: CGPA (total marks/50) with student name
  - ✅ Django sessions used to store information
  - ✅ Two-page design

---

### **ADDITIONAL QUESTIONS (A)** - Extra Exercises

#### **A1: Bill Generator** ✅
- **Theme Color:** Orange (#fd7e14)
- **Location:** `/a1/bill/`
- **Files Created:**
  - `a1/forms.py` - BillForm
  - `a1/views.py` - bill() and result() views
  - `a1/urls.py` - URL routing
  - `a1/templates/a1/bill.html` - Bill input form
  - `a1/templates/a1/result.html` - Bill result

- **Requirements Met:**
  - ✅ Page 1: RadioButtons (HP, Nokia, Samsung, Motorola, Apple)
  - ✅ CheckBoxes (Mobile, Laptop)
  - ✅ TextBox for quantity
  - ✅ "Produce Bill" button
  - ✅ Page 2: Item display with total amount
  - ✅ Two-page design

#### **A2: Feedback Form** ✅
- **Theme Color:** Green (#28a745)
- **Location:** `/a2/feedback/`
- **Files Created:**
  - `a2/forms.py` - FeedbackForm
  - `a2/views.py` - feedback() and thank_you() views
  - `a2/urls.py` - URL routing
  - `a2/templates/a2/feedback.html` - Feedback form
  - `a2/templates/a2/thank_you.html` - Thank you page

- **Requirements Met:**
  - ✅ Heading: "Coursework Feedback Form"
  - ✅ Section: Student name, Gender
  - ✅ Dropdown options: ASP-XML, DotNET, JavaPro, Unix, C, C++
  - ✅ Suggestion box
  - ✅ Submit button
  - ✅ Display thank you message: "Thanks {Name} for your feedback."
  - ✅ Two-page design

---

## 🎨 Color Theme Implementation

Each exercise has its own color theme:

| Exercise | Color | Hex Code | Theme Applied To |
|----------|-------|----------|------------------|
| Q1 | Blue | #007bff | Borders, headings, buttons, links |
| Q2 | Red | #dc3545 | Borders, headings, buttons, links |
| Q3 | Pink | #e75480 | Borders, headings, buttons, links |
| A1 | Orange | #fd7e14 | Borders, headings, buttons, links |
| A2 | Green | #28a745 | Borders, headings, buttons, links |

---

## 📁 Project Structure

```
L8/
├── manage.py                           # Django management
├── db.sqlite3                          # SQLite database
├── README.md                           # Full documentation
├── QUICKSTART.md                       # Quick start guide
│
├── lab8/                               # Main Django project
│   ├── __init__.py
│   ├── settings.py                     # Settings with all apps configured
│   ├── urls.py                         # Main URL configuration
│   ├── asgi.py
│   └── wsgi.py
│
├── q1/                                 # Lab Exercise 1
│   ├── forms.py                        # RegisterForm
│   ├── views.py                        # register(), success()
│   ├── urls.py
│   └── templates/q1/
│       ├── register.html
│       └── success.html
│
├── q2/                                 # Lab Exercise 2
│   ├── views.py                        # vote(), results()
│   ├── urls.py
│   └── templates/q2/
│       ├── vote.html
│       └── results.html
│
├── q3/                                 # Lab Exercise 3
│   ├── forms.py                        # CGPAForm
│   ├── views.py                        # calculate(), result()
│   ├── urls.py
│   └── templates/q3/
│       ├── calculate.html
│       └── result.html
│
├── a1/                                 # Additional Exercise 1
│   ├── forms.py                        # BillForm
│   ├── views.py                        # bill(), result()
│   ├── urls.py
│   └── templates/a1/
│       ├── bill.html
│       └── result.html
│
├── a2/                                 # Additional Exercise 2
│   ├── forms.py                        # FeedbackForm
│   ├── views.py                        # feedback(), thank_you()
│   ├── urls.py
│   └── templates/a2/
│       ├── feedback.html
│       └── thank_you.html
│
├── templates/
│   └── index.html                      # Home page with navigation
│
├── static/css/
│   ├── q1.css                          # Main stylesheet (all themes)
│   ├── q2.css                          # Imports q1.css
│   ├── q3.css                          # Imports q1.css
│   ├── a1.css                          # Imports q1.css
│   └── a2.css                          # Imports q1.css
│
└── venv/                               # Python virtual environment
```

---

## 🔐 Security Features Implemented

1. **CSRF Token Protection**
   - All forms include `{% csrf_token %}`
   - Prevents Cross-Site Request Forgery attacks

2. **Django Sessions**
   - Data stored securely in sessions
   - Cleared automatically when browser closes
   - Session middleware configured in settings

3. **Form Validation**
   - Django Forms validate all inputs
   - Server-side validation ensures data integrity
   - Email field uses EmailField for validation

---

## ✨ Key Features

### Forms & Validation
- Custom Django Form classes for each exercise
- Required and optional field validation
- Email field validation in Q1
- Integer validation for quantity in A1 and Q3

### Views & Templates
- Clean separation of concerns (MTV architecture)
- Reusable template structure
- Consistent styling across all exercises

### Sessions & Data Storage
- Q1: username, email, contact stored in session
- Q2: vote counts stored in session
- Q3: student name, marks, CGPA stored in session
- A1: brand, devices, quantity stored in session
- A2: feedback data stored in session

### Styling
- Minimal and clean CSS as per requirement
- Color-coded by exercise
- Responsive design
- Consistent form styling
- Clear visual hierarchy

---

## 🚀 How to Run

### 1. Activate Virtual Environment
```bash
cd /home/WP_C1/Documents/230905152_WP/L8
source venv/bin/activate
```

### 2. Run Migrations (already done)
```bash
python manage.py migrate
```

### 3. Start Development Server
```bash
python manage.py runserver
```

### 4. Access Application
- Home: `http://localhost:8000/`
- Q1: `http://localhost:8000/q1/register/`
- Q2: `http://localhost:8000/q2/vote/`
- Q3: `http://localhost:8000/q3/calculate/`
- A1: `http://localhost:8000/a1/bill/`
- A2: `http://localhost:8000/a2/feedback/`

---

## 📊 Data Flow

### Q1 - Register Flow
```
register.html (form) → POST → views.register() → 
Store in session → Redirect → success.html (display data)
```

### Q2 - Voting Flow
```
vote.html (radio buttons) → POST → views.vote() → 
Store votes in session → Redirect → results.html (show percentages)
```

### Q3 - CGPA Flow
```
calculate.html (name, marks) → POST → views.calculate() → 
Calculate CGPA → Store in session → Redirect → result.html (display CGPA)
```

### A1 - Bill Flow
```
bill.html (brand, device, qty) → POST → views.bill() → 
Calculate prices → Store in session → Redirect → result.html (show bill)
```

### A2 - Feedback Flow
```
feedback.html (form) → POST → views.feedback() → 
Store feedback in session → Redirect → thank_you.html (show message)
```

---

## ✅ Requirements Checklist

### Q1
- [x] Register page with 4 input TextBoxes
- [x] Username is compulsory (marked with *)
- [x] Other fields are optional
- [x] Submit button
- [x] Success page with "Welcome {UserName}"
- [x] Email and Contact Number displayed
- [x] CSRF token used for security
- [x] Two pages design

### Q2
- [x] Two pages design
- [x] Title: "How is the book ASP.NET with C# by Vipul Prakashan?"
- [x] Three choices: Good, Satisfactory, Bad
- [x] VOTE button
- [x] Results in percentage using labels

### Q3
- [x] Two pages design
- [x] Page 1: Two TextBoxes (name, total marks), Calculate button
- [x] Page 2: CGPA display with student name
- [x] CGPA formula: total marks / 50
- [x] Django sessions used

### A1
- [x] Two pages design
- [x] RadioButtons: HP, Nokia, Samsung, Motorola, Apple
- [x] CheckBoxes: Mobile, Laptop
- [x] TextBox for quantity
- [x] "Produce Bill" button
- [x] Item display with total amount on another page

### A2
- [x] Heading: "Coursework Feedback Form"
- [x] Section: Student name, Gender
- [x] Dropdown options: ASP-XML, DotNET, JavaPro, Unix, C, C++
- [x] Suggestion box
- [x] Submit Form button
- [x] Thank you message: "Thanks {Name} for your feedback."

### General
- [x] Project name: lab8
- [x] App names: q1, q2, q3, a1, a2
- [x] Minimal styling (no over-design)
- [x] Color theme for each exercise
- [x] Simple and clean design

---

## 📝 Notes

1. **Session Data:** All data is temporary and stored in Django sessions
2. **No Database Models:** No database records are created (as required)
3. **Minimal Styling:** CSS is kept basic and clean
4. **CSRF Protection:** All forms are CSRF token protected
5. **Form Validation:** All inputs validated on server-side
6. **Responsive Design:** Works on desktop and mobile browsers

---

## 🎓 Learning Outcomes

This lab demonstrates:
- Django form creation and validation
- URL routing in Django
- Template rendering
- Session management
- CSRF protection
- Multi-page form workflow
- CSS theming
- HTML form elements (radio, checkbox, select, textarea, text input)

---

**Project Completion Date:** 18 March 2026
**Status:** ✅ COMPLETE

All exercises are fully functional and ready for testing/grading.
