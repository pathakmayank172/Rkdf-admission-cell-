"""
Views for the RKDF University Admission Cell
A "view" is a Python function that:
  1. Receives a web request
  2. Does some processing (save data, fetch data, etc.)
  3. Returns an HTML response
"""

from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Count
from .models import AdmissionForm, COURSE_CHOICES, Course
from decimal import Decimal


# -------------------------------------------------------
# HOME PAGE VIEW
# -------------------------------------------------------
def home(request):
    """
    Renders the Home page.
    Passes some statistics to display on the homepage.
    """
    # Get some basic stats for the homepage
    total_applications = AdmissionForm.objects.count()

    context = {
        'total_applications': total_applications,
        'page_title': 'Home',
    }
    return render(request, 'admission/home.html', context)


# -------------------------------------------------------
# ABOUT PAGE VIEW
# -------------------------------------------------------
def about(request):
    """Renders the About RKDF University page."""
    context = {
        'page_title': 'About Us',
    }
    return render(request, 'admission/about.html', context)


# -------------------------------------------------------
# COURSES PAGE VIEW
# -------------------------------------------------------
def courses(request):
    """
    Renders the Courses page.
    Passes course data to display.
    """
    # Detailed course information
    course_data = [
        {
            'code': 'BTECH',
            'name': 'B.Tech',
            'full_name': 'Bachelor of Technology',
            'duration': '4 Years',
            'seats': 120,
            'eligibility': '10+2 with PCM, Min 50%',
            'icon': '🔧',
            'description': 'Engineering programs in CSE, ECE, ME, CE branches with industry-ready curriculum.',
        },
        {
            'code': 'BCA',
            'name': 'BCA',
            'full_name': 'Bachelor of Computer Applications',
            'duration': '3 Years',
            'seats': 60,
            'eligibility': '10+2 with Mathematics, Min 45%',
            'icon': '💻',
            'description': 'Comprehensive computer science program covering programming, databases and web development.',
        },
        {
            'code': 'BBA',
            'name': 'BBA',
            'full_name': 'Bachelor of Business Administration',
            'duration': '3 Years',
            'seats': 60,
            'eligibility': '10+2 from any stream, Min 45%',
            'icon': '📊',
            'description': 'Management fundamentals, marketing, finance and entrepreneurship skills.',
        },
        {
            'code': 'MBA',
            'name': 'MBA',
            'full_name': 'Master of Business Administration',
            'duration': '2 Years',
            'seats': 60,
            'eligibility': 'Graduation in any stream, Min 50%',
            'icon': '🏢',
            'description': 'Advanced management education with specializations in Finance, HR, Marketing.',
        },
        {
            'code': 'MTECH',
            'name': 'M.Tech',
            'full_name': 'Master of Technology',
            'duration': '2 Years',
            'seats': 30,
            'eligibility': 'B.Tech/BE, Min 55%',
            'icon': '⚙️',
            'description': 'Advanced technical specialization with research opportunities.',
        },
        {
            'code': 'BCOM',
            'name': 'B.Com',
            'full_name': 'Bachelor of Commerce',
            'duration': '3 Years',
            'seats': 60,
            'eligibility': '10+2 with Commerce, Min 45%',
            'icon': '💰',
            'description': 'Accounting, taxation, business law and financial management.',
        },
        {
            'code': 'BSC',
            'name': 'B.Sc',
            'full_name': 'Bachelor of Science',
            'duration': '3 Years',
            'seats': 60,
            'eligibility': '10+2 with Science, Min 45%',
            'icon': '🔬',
            'description': 'Physics, Chemistry, Mathematics, Biology specializations available.',
        },
        {
            'code': 'BPHARM',
            'name': 'B.Pharm',
            'full_name': 'Bachelor of Pharmacy',
            'duration': '4 Years',
            'seats': 60,
            'eligibility': '10+2 with PCB/PCM, Min 50%',
            'icon': '💊',
            'description': 'Pharmaceutical sciences with hands-on lab training and clinical exposure.',
        },
    ]

    context = {
        'page_title': 'Courses',
        'courses': course_data,
    }
    return render(request, 'admission/courses.html', context)


# -------------------------------------------------------
# ADMISSION FORM VIEW
# -------------------------------------------------------
def admission_form(request):
    """
    Handles the Admission Form page.
    - GET request: Shows the empty form
    - POST request: Saves the submitted form data
    """

    if request.method == 'POST':
        # The form was submitted - extract the data
        name            = request.POST.get('name', '').strip()
        email           = request.POST.get('email', '').strip()
        phone           = request.POST.get('phone', '').strip()
        course          = request.POST.get('course', '').strip()
        address         = request.POST.get('address', '').strip()
        father_name     = request.POST.get('father_name', '').strip()
        date_of_birth   = request.POST.get('date_of_birth', '') or None
        tenth_pct       = request.POST.get('tenth_percentage', '') or None
        twelfth_pct     = request.POST.get('twelfth_percentage', '') or None

        # Server-side validation
        errors = []

        if not name:
            errors.append("Full Name is required.")
        if not email:
            errors.append("Email is required.")
        if not phone or len(phone) < 10:
            errors.append("Valid Phone Number is required.")
        if not course:
            errors.append("Please select a course.")
        if not address:
            errors.append("Address is required.")

        # Check if email already exists
        if AdmissionForm.objects.filter(email=email).exists():
            errors.append("An application with this email already exists.")

        if errors:
            # Errors found - show form again with error messages
            for error in errors:
                messages.error(request, error)
            # Pass back submitted data so user doesn't retype everything
            context = {
                'page_title': 'Apply Now',
                'course_choices': COURSE_CHOICES,
                'submitted_data': request.POST,
            }
            return render(request, 'admission/admission_form.html', context)

        # No errors - save the data to the database
        try:
            admission = AdmissionForm(
                name=name,
                email=email,
                phone=phone,
                course=course,
                address=address,
                father_name=father_name,
                date_of_birth=date_of_birth,
                tenth_percentage=tenth_pct,
                twelfth_percentage=twelfth_pct,
            )
            admission.save()  # This writes to the SQLite database

            # Success message
            messages.success(
                request,
                f"🎉 Application submitted successfully! "
                f"Your Application ID is #{admission.id}. "
                f"Keep this for future reference."
            )
            # Redirect to home page to see the application
            return redirect('home')

        except Exception as e:
            messages.error(request, f"Error saving application: {str(e)}")

    # GET request - just show the empty form
    context = {
        'page_title': 'Apply Now',
        'course_choices': COURSE_CHOICES,
        'submitted_data': {},
    }
    return render(request, 'admission/admission_form.html', context)


# -------------------------------------------------------
# STUDENT DASHBOARD VIEW (MIS View)
# -------------------------------------------------------
def dashboard(request):
    """
    Student Dashboard - shows all admission records.
    This is the MIS (Management Information System) view.
    Allows filtering by course and status.
    """

    # Get all admission records
    admissions = AdmissionForm.objects.all()

    # Apply filters if provided in URL query parameters
    # Example: /dashboard/?course=BCA&status=pending
    filter_course = request.GET.get('course', '')
    filter_status = request.GET.get('status', '')

    if filter_course:
        admissions = admissions.filter(course=filter_course)
    if filter_status:
        admissions = admissions.filter(status=filter_status)

    # Statistics for the dashboard summary cards
    total         = AdmissionForm.objects.count()
    pending_count = AdmissionForm.objects.filter(status='pending').count()
    approved_count= AdmissionForm.objects.filter(status='approved').count()
    rejected_count= AdmissionForm.objects.filter(status='rejected').count()

    # Course-wise breakdown for chart/table
    course_stats = AdmissionForm.objects.values('course').annotate(
        count=Count('id')
    ).order_by('-count')

    context = {
        'page_title': 'Student Dashboard',
        'admissions': admissions,
        'total': total,
        'pending_count': pending_count,
        'approved_count': approved_count,
        'rejected_count': rejected_count,
        'course_stats': course_stats,
        'course_choices': COURSE_CHOICES,
        'filter_course': filter_course,
        'filter_status': filter_status,
    }
    return render(request, 'admission/dashboard.html', context)


# -------------------------------------------------------
# CONTACT PAGE VIEW
# -------------------------------------------------------
def contact(request):
    """Renders the Contact page."""
    if request.method == 'POST':
        # In a real project, you'd send this as an email
        cname    = request.POST.get('name', '')
        cemail   = request.POST.get('email', '')
        cmessage = request.POST.get('message', '')
        if cname and cemail and cmessage:
            messages.success(
                request,
                "Thank you for reaching out! We will get back to you within 24 hours."
            )
        else:
            messages.error(request, "Please fill all fields.")

    context = {
        'page_title': 'Contact Us',
    }
    return render(request, 'admission/contact.html', context)


# -------------------------------------------------------
# COURSE RECOMMENDATION VIEW
# -------------------------------------------------------
def course_recommendation(request):
    """
    AI-powered Course Recommendation System.
    Recommends top 3 courses based on student profile.
    
    Student inputs:
    - Education Level (10+2, Graduation, etc.)
    - Stream (PCM, PCB, Commerce, Arts, Any)
    - Marks (12th percentage or graduation percentage)
    - Budget (annual fee preference)
    - Interests (optional - for future enhancement)
    """
    
    recommendations = []
    student_data = {}
    
    if request.method == 'POST':
        # Collect student data
        education_level = request.POST.get('education_level', '').strip()
        stream = request.POST.get('stream', '').strip()
        marks = request.POST.get('marks', '') or 0
        budget = request.POST.get('budget', '') or 999999999
        interests = request.POST.get('interests', '').strip()
        
        # Store for display
        student_data = {
            'education_level': education_level,
            'stream': stream,
            'marks': float(marks) if marks else 0,
            'budget': float(budget) if budget else 0,
            'interests': interests,
        }
        
        try:
            marks = float(marks) if marks else 0
            budget = float(budget) if budget else 999999999
        except:
            marks = 0
            budget = 999999999
        
        # ===============================================
        # STEP 1: FILTER ELIGIBLE COURSES
        # ===============================================
        eligible_courses = []
        
        # Get all courses from database
        all_courses = Course.objects.all()
        
        for course in all_courses:
            # Check education level match
            if course.education_level != education_level:
                continue
            
            # Check stream match
            if course.required_stream != 'ANY' and course.required_stream != stream:
                continue
            
            # Check minimum percentage
            if marks < float(course.min_percentage):
                continue
            
            # Check budget
            if course.annual_fee > budget:
                continue
            
            eligible_courses.append(course)
        
        # ===============================================
        # STEP 2: RANK TOP 3 COURSES
        # ===============================================
        # Simple ranking: courses matching stream/interests get higher scores
        scored_courses = []
        
        for course in eligible_courses:
            score = 0
            reason = []
            
            # Score based on match
            if course.required_stream == stream:
                score += 30
                reason.append("Perfect stream match")
            
            # Score based on marks exceeding minimum
            marks_above_min = marks - float(course.min_percentage)
            if marks_above_min > 0:
                score += min(marks_above_min, 20)  # Max 20 points
                reason.append(f"Excellent marks ({marks}% vs min {course.min_percentage}%)")
            
            # Score based on budget comfort
            if course.annual_fee <= budget * 0.7:
                score += 15
                reason.append("Good budget fit")
            
            # Score based on interest keywords (simple matching)
            if interests.lower():
                interest_keywords = course.description.lower() + course.name.lower()
                if any(keyword in interest_keywords for keyword in interests.lower().split()):
                    score += 20
                    reason.append(f"Matches your interests ({interests})")
            
            scored_courses.append({
                'course': course,
                'score': score,
                'reasons': reason,
            })
        
        # Sort by score (highest first)
        scored_courses.sort(key=lambda x: x['score'], reverse=True)
        
        # Get top 3
        recommendations = scored_courses[:3]
        
        # If no recommendations, suggest alternatives
        if not recommendations:
            context = {
                'page_title': 'Course Recommendation',
                'student_data': student_data,
                'recommendations': [],
                'no_match': True,
                'message': 'No courses match your current criteria. Please consider:',
                'suggestions': [
                    '✓ Lower your budget expectations',
                    '✓ Consider different educational streams',
                    '✓ Check if you meet the minimum percentage requirement',
                    '✓ Explore alternative courses at other education levels',
                ]
            }
            return render(request, 'admission/course_recommendation.html', context)
    
    context = {
        'page_title': 'Course Recommendation',
        'recommendations': recommendations,
        'student_data': student_data,
        'education_levels': Course.EDUCATION_LEVEL_CHOICES,
        'streams': Course.STREAM_CHOICES,
        'budget_ranges': [
            (50000, '₹50,000/year'),
            (100000, '₹1,00,000/year'),
            (150000, '₹1,50,000/year'),
            (200000, '₹2,00,000/year'),
            (300000, '₹3,00,000/year'),
            (500000, '₹5,00,000+/year'),
        ]
    }
    return render(request, 'admission/course_recommendation.html', context)
