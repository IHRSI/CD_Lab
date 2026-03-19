# QUICK START GUIDE

## Starting the Application

1. **Navigate to project folder:**
   ```bash
   cd /home/WP_C1/Documents/230905152_WP/L8
   ```

2. **Activate virtual environment:**
   ```bash
   source venv/bin/activate
   ```

3. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

4. **Open in browser:**
   ```
   http://localhost:8000/
   ```

## Application URLs

| Exercise | URL | Purpose |
|----------|-----|---------|
| Home | `http://localhost:8000/` | Index page with all exercises |
| Q1 | `http://localhost:8000/q1/register/` | Register & Success Page |
| Q2 | `http://localhost:8000/q2/vote/` | Voting System |
| Q3 | `http://localhost:8000/q3/calculate/` | CGPA Calculator |
| A1 | `http://localhost:8000/a1/bill/` | Bill Generator |
| A2 | `http://localhost:8000/a2/feedback/` | Feedback Form |

## Exercise Details

### Q1: Register & Success (BLUE)
- **Location:** q1/
- **Key Features:**
  - Register.html - Form with 4 fields
  - Success.html - Welcome message with user details
  - Uses CSRF token for security
  - Stores data in sessions

- **Test:**
  1. Go to http://localhost:8000/q1/register/
  2. Enter username (required), optional password, email, contact
  3. Click Submit
  4. See welcome message with your details

### Q2: Voting System (RED)
- **Location:** q2/
- **Key Features:**
  - Vote.html - Radio buttons for Good/Satisfactory/Bad
  - Results.html - Shows vote counts and percentages
  - Stores votes in sessions

- **Test:**
  1. Go to http://localhost:8000/q2/vote/
  2. Select a voting option
  3. Click VOTE
  4. See results with percentages

### Q3: CGPA Calculator (PINK)
- **Location:** q3/
- **Key Features:**
  - Calculate.html - Input name and marks
  - Result.html - Shows CGPA (marks/50)
  - Uses Django sessions

- **Test:**
  1. Go to http://localhost:8000/q3/calculate/
  2. Enter name and total marks
  3. Click Calculate
  4. See calculated CGPA

### A1: Bill Generator (ORANGE)
- **Location:** a1/
- **Key Features:**
  - Bill.html - Select brand, device, quantity
  - Result.html - Itemized bill with total
  - Brands: HP, Nokia, Samsung, Motorola, Apple
  - Devices: Mobile, Laptop

- **Test:**
  1. Go to http://localhost:8000/a1/bill/
  2. Select brand and device(s)
  3. Enter quantity
  4. Click Produce Bill
  5. View itemized bill

### A2: Feedback Form (GREEN)
- **Location:** a2/
- **Key Features:**
  - Feedback.html - Student info form
  - Thank_you.html - Thank you message
  - Includes gender dropdown and course selection
  - Suggestion text area

- **Test:**
  1. Go to http://localhost:8000/a2/feedback/
  2. Fill in all fields (name, gender, course, suggestion)
  3. Click Submit Form
  4. See thank you message

## Project Structure

```
L8/
├── manage.py                    # Django management script
├── db.sqlite3                   # Database file
├── README.md                    # Project documentation
├── QUICKSTART.md               # This file
│
├── lab8/                        # Main project folder
│   ├── settings.py             # Django settings
│   ├── urls.py                 # Main URL configuration
│   └── ...
│
├── q1/, q2/, q3/              # Lab exercises
├── a1/, a2/                    # Additional exercises
│
├── templates/
│   ├── index.html              # Home page
│   ├── q1, q2, q3/            # App templates
│   └── a1, a2/
│
├── static/css/
│   ├── q1.css                  # Main stylesheet
│   └── q2.css, q3.css, a1.css, a2.css  # Theme imports
│
└── venv/                        # Virtual environment

```

## Key Files

### Forms (Django Form Classes)
- `q1/forms.py` - RegisterForm
- `q3/forms.py` - CGPAForm
- `a1/forms.py` - BillForm
- `a2/forms.py` - FeedbackForm

### Views (Backend Logic)
- `q1/views.py` - register(), success()
- `q2/views.py` - vote(), results()
- `q3/views.py` - calculate(), result()
- `a1/views.py` - bill(), result()
- `a2/views.py` - feedback(), thank_you()

### URLs
- `q1/urls.py` - Routes for Q1
- `q2/urls.py` - Routes for Q2
- `q3/urls.py` - Routes for Q3
- `a1/urls.py` - Routes for A1
- `a2/urls.py` - Routes for A2

### Templates
Each exercise has HTML templates:
- Forms for data input
- Result/Success pages for output display

## Color Scheme

| Exercise | Color | Hex Code |
|----------|-------|----------|
| Q1 | Blue | #007bff |
| Q2 | Red | #dc3545 |
| Q3 | Pink | #e75480 |
| A1 | Orange | #fd7e14 |
| A2 | Green | #28a745 |

## Important Notes

1. **Sessions:** Data is stored in Django sessions and will be cleared when the browser closes
2. **CSRF Token:** All forms include CSRF token for security
3. **No Database Records:** All data is session-based, no models are used
4. **Static Files:** CSS is minimal and clean as per lab requirement
5. **Validation:** Form fields are validated using Django forms

## Troubleshooting

**Issue:** Port 8000 already in use
```bash
python manage.py runserver 8001
# Then access at http://localhost:8001
```

**Issue:** CSS not loading
```bash
python manage.py collectstatic --noinput
```

**Issue:** Reset sessions
```bash
# Session data clears automatically when browser closes
# Or delete browser cookies for localhost
```

## Testing Each Exercise

### Q1 Test Case:
- Username: john_doe (required)
- Password: (optional - leave empty)
- Email: john@example.com
- Contact: 9876543210

### Q2 Test Case:
- Vote multiple times with different choices
- Check if percentages are calculated correctly

### Q3 Test Case:
- Name: Raj Kumar
- Marks: 45
- Expected CGPA: 0.9

### A1 Test Case:
- Brand: Apple
- Devices: Mobile, Laptop
- Quantity: 2
- Should show: Apple Mobile (₹70000 x 2) + Apple Laptop (₹100000 x 2)

### A2 Test Case:
- Name: Priya Sharma
- Gender: Female
- Course: JavaPro
- Suggestion: Great course, very informative!

---

**Enjoy the lab exercise!**
