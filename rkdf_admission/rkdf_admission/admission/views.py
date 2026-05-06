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
from django.http import JsonResponse
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
def get_course_recommendations(profile):
    education_level = profile.get('education_level', '')
    stream = profile.get('stream', '')
    marks = profile.get('marks', 0)
    budget = profile.get('budget', 999999999)
    interests = profile.get('interests', '').strip().lower()

    eligible_courses = []
    for course in Course.objects.all():
        if course.education_level != education_level:
            continue
        if course.required_stream != 'ANY' and course.required_stream != stream:
            continue
        if marks < float(course.min_percentage):
            continue
        if course.annual_fee > budget:
            continue
        eligible_courses.append(course)

    scored_courses = []
    for course in eligible_courses:
        score = 0
        reasons = []
        if course.required_stream == stream:
            score += 30
            reasons.append('Perfect stream match')
        marks_above_min = marks - float(course.min_percentage)
        if marks_above_min > 0:
            score += min(marks_above_min, 20)
            reasons.append(f'Excellent marks ({marks}% vs min {course.min_percentage}%)')
        if course.annual_fee <= budget * 0.7:
            score += 15
            reasons.append('Good budget fit')
        if interests:
            interest_text = (course.description + ' ' + course.name).lower()
            if any(keyword in interest_text for keyword in interests.split()):
                score += 20
                reasons.append(f'Matches your interests ({profile.get("interests")})')
        scored_courses.append({'course': course, 'score': score, 'reasons': reasons})

    scored_courses.sort(key=lambda x: x['score'], reverse=True)
    return scored_courses[:3]


def serialize_recommendation(item):
    course = item['course']
    return {
        'code': course.code,
        'name': course.name,
        'full_name': course.full_name,
        'duration': course.duration,
        'seats': course.seats,
        'eligibility': f'{course.get_education_level_display()} / {course.get_required_stream_display()} / {course.min_percentage}%',
        'annual_fee': float(course.annual_fee),
        'total_fee': float(course.total_fee),
        'description': course.description,
        'career_opportunities': course.career_opportunities,
        'average_salary': course.average_salary,
        'score': item['score'],
        'reasons': item['reasons'],
        'apply_url': f'/apply/?course={course.code}',
    }


def course_recommendation(request):
    """
    AI-powered Course Recommendation System.
    Recommends top 3 courses based on student profile.
    """

    recommendations = []
    student_data = {}
    no_match = False
    message = ''
    suggestions = []

    if request.method == 'POST':
        education_level = request.POST.get('education_level', '').strip()
        stream = request.POST.get('stream', '').strip()
        marks = request.POST.get('marks', '') or 0
        budget = request.POST.get('budget', '') or 999999999
        interests = request.POST.get('interests', '').strip()

        try:
            marks = float(marks)
        except Exception:
            marks = 0
        try:
            budget = float(budget)
        except Exception:
            budget = 999999999

        student_data = {
            'education_level': education_level,
            'stream': stream,
            'marks': marks,
            'budget': budget,
            'interests': interests,
        }

        recommendations = get_course_recommendations(student_data)
        if not recommendations:
            no_match = True
            message = 'No courses match your current criteria. Please consider:'
            suggestions = [
                '✓ Lower your budget expectations',
                '✓ Consider different educational streams',
                '✓ Check if you meet the minimum percentage requirement',
                '✓ Explore alternative courses at other education levels',
            ]

        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            data = {
                'recommendations': [serialize_recommendation(item) for item in recommendations],
                'no_match': no_match,
                'message': message,
                'suggestions': suggestions,
            }
            return JsonResponse(data)

    context = {
        'page_title': 'Course Recommendation',
        'recommendations': recommendations,
        'student_data': student_data,
        'no_match': no_match,
        'message': message,
        'suggestions': suggestions,
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
