# Django Form Processing Lab Exercise

A comprehensive Django web application demonstrating form processing with multiple lab exercises.

## Project Structure

```
lab8/
├── manage.py
├── lab8/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── q1/                 # Register & Success
├── q2/                 # Voting System
├── q3/                 # CGPA Calculator
├── a1/                 # Bill Generator
├── a2/                 # Feedback Form
├── templates/          # HTML templates
├── static/
│   └── css/           # Stylesheets
└── venv/              # Virtual environment
```

## Setup Instructions

### 1. Create Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 2. Install Django
```bash
pip install django
```

### 3. Run Migrations
```bash
python manage.py migrate
```

### 4. Start Development Server
```bash
python manage.py runserver
```

The server will run on `http://localhost:8000`

## Questions Overview

### **Q1: Register & Success Page** (Blue Theme)
- **URL:** `http://localhost:8000/q1/register/`
- **Features:**
  - Register form with 4 fields: Username, Password, Email, Contact Number
  - Username is compulsory field (marked with *)
  - Other fields are optional
  - Uses CSRF token for security
  - Stores data in Django sessions
  - Success page displays welcome message with stored information

### **Q2: Voting System** (Red Theme)
- **URL:** `http://localhost:8000/q2/vote/`
- **Features:**
  - Title: "How is the book ASP.NET with C# by Vipul Prakashan?"
  - Three voting options: Good, Satisfactory, Bad (Radio buttons)
  - VOTE button to submit choice
  - Results page shows vote count and percentage for each option
  - Stores votes in session

### **Q3: CGPA Calculator** (Pink Theme)
- **URL:** `http://localhost:8000/q3/calculate/`
- **Features:**
  - Two text input fields: Student Name and Total Marks
  - Calculate button to compute CGPA
  - CGPA formula: Total Marks / 50
  - Result page displays name, marks, and calculated CGPA
  - Uses Django sessions to store and retrieve information

### **A1: Bill Generator** (Orange Theme)
- **URL:** `http://localhost:8000/a1/bill/`
- **Features:**
  - Radio buttons for brand selection: HP, Nokia, Samsung, Motorola, Apple
  - Checkboxes for device type: Mobile, Laptop
  - Number input for quantity
  - Produce Bill button generates an itemized bill
  - Bill shows Brand, Device, Unit Price, Quantity, and Total
  - Grand total amount displayed

### **A2: Feedback Form** (Green Theme)
- **URL:** `http://localhost:8000/a2/feedback/`
- **Features:**
  - Heading: "Coursework Feedback Form"
  - Student Name text input
  - Gender dropdown selector
  - Course selection dropdown: ASP-XML, DotNET, JavaPro, Unix, C, C++
  - Suggestion box (large text area)
  - Submit Form button
  - Thank you page displays: "Thanks [Name] for your feedback."

## Theme Colors

- **Q1:** Blue (#007bff)
- **Q2:** Red (#dc3545)
- **Q3:** Pink (#e75480)
- **A1:** Orange (#fd7e14)
- **A2:** Green (#28a745)

## Key Technologies Used

- **Django 5.2.12** - Web framework
- **Python 3.11** - Programming language
- **SQLite** - Database (default)
- **Django Sessions** - For storing user data across pages
- **CSRF Token** - For secure form submissions
- **HTML5 & CSS3** - Frontend

## Security Features

- CSRF Token protection on all forms
- Session-based data storage
- Secure form validation
- Input type validation using Django forms

## UI/UX Features

- Responsive design
- Clean and minimal styling as per requirement
- Color-coded sections for easy navigation
- Easy-to-use forms with clear labels
- Success/result pages with navigation links
- Index page linking to all lab exercises

## File Organization

### Templates
- `templates/index.html` - Home page with links to all exercises
- `q1/templates/q1/register.html` - Registration form
- `q1/templates/q1/success.html` - Success page
- `q2/templates/q2/vote.html` - Voting form
- `q2/templates/q2/results.html` - Vote results
- `q3/templates/q3/calculate.html` - CGPA input form
- `q3/templates/q3/result.html` - CGPA result
- `a1/templates/a1/bill.html` - Bill form
- `a1/templates/a1/result.html` - Bill summary
- `a2/templates/a2/feedback.html` - Feedback form
- `a2/templates/a2/thank_you.html` - Thank you page

### CSS
- `static/css/q1.css` - Main stylesheet with all theme definitions
- `static/css/q2.css` - Imports q1.css
- `static/css/q3.css` - Imports q1.css
- `static/css/a1.css` - Imports q1.css
- `static/css/a2.css` - Imports q1.css

## Testing the Application

1. Open Home Page:
   ```
   http://localhost:8000/
   ```

2. Click on any exercise to access its form

3. Fill in the required fields and submit

4. View the results on the results/success page

## Accessing Admin Panel

```bash
python manage.py createsuperuser  # Create admin user
```

Then visit `http://localhost:8000/admin/`

## Notes

- All data is stored in session and cleared when the browser closes
- Username field in Q1 is required; all others are optional
- Bill amounts in A1 are predefined for each brand-device combination
- No database records are created (pure session-based storage)

## Author
Lab Exercise for Django Form Processing

---

**Happy Learning!** 📚
