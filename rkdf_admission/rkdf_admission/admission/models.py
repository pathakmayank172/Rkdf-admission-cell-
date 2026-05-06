"""
Models for the Admission Cell App
A "model" in Django represents a database table.
Each class here = one table in the database.
Each attribute = one column in that table.
"""

from django.db import models

# -------------------------------------------------------
# Course Choices
# These are the courses available at RKDF University Ranchi
# -------------------------------------------------------
COURSE_CHOICES = [
    ('BCA',   'BCA - Bachelor of Computer Applications'),
    ('BBA',   'BBA - Bachelor of Business Administration'),
    ('MBA',   'MBA - Master of Business Administration'),
    ('BTECH', 'B.Tech - Bachelor of Technology'),
    ('MTECH', 'M.Tech - Master of Technology'),
    ('BCOM',  'B.Com - Bachelor of Commerce'),
    ('MCOM',  'M.Com - Master of Commerce'),
    ('BSC',   'B.Sc - Bachelor of Science'),
    ('MSC',   'M.Sc - Master of Science'),
    ('BA',    'BA - Bachelor of Arts'),
    ('MA',    'MA - Master of Arts'),
    ('LLB',   'LLB - Bachelor of Laws'),
    ('BPHARM','B.Pharm - Bachelor of Pharmacy'),
]

# -------------------------------------------------------
# Course Model
# Stores detailed course information for recommendations
# -------------------------------------------------------
class Course(models.Model):
    """
    Comprehensive course database with eligibility,
    fees, and career information.
    """
    EDUCATION_LEVEL_CHOICES = [
        ('10+2', '10+2 (12th Pass)'),
        ('GRADUATION', 'Graduation'),
        ('POST_GRADUATION', 'Post Graduation'),
    ]
    
    STREAM_CHOICES = [
        ('PCM', 'Science (PCM)'),
        ('PCB', 'Science (PCB)'),
        ('COMMERCE', 'Commerce'),
        ('ARTS', 'Arts'),
        ('ANY', 'Any Stream'),
    ]
    
    code = models.CharField(max_length=20, unique=True, verbose_name="Course Code")
    name = models.CharField(max_length=100, verbose_name="Course Name")
    full_name = models.CharField(max_length=200, verbose_name="Full Course Name")
    duration = models.CharField(max_length=50, verbose_name="Duration (Years)")
    seats = models.IntegerField(verbose_name="Available Seats")
    
    # Eligibility
    education_level = models.CharField(
        max_length=20,
        choices=EDUCATION_LEVEL_CHOICES,
        verbose_name="Required Education Level"
    )
    required_stream = models.CharField(
        max_length=20,
        choices=STREAM_CHOICES,
        verbose_name="Required Stream"
    )
    min_percentage = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        verbose_name="Minimum Percentage"
    )
    
    # Fees & Budget
    annual_fee = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Annual Fee (INR)"
    )
    total_fee = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Total Course Fee (INR)"
    )
    
    # Description
    description = models.TextField(verbose_name="Course Description")
    
    # Career Info
    career_opportunities = models.TextField(
        verbose_name="Career Opportunities",
        help_text="List of job roles and industries"
    )
    average_salary = models.CharField(
        max_length=100,
        verbose_name="Average Salary Range",
        help_text="e.g., 4-8 LPA"
    )
    
    icon = models.CharField(max_length=10, default="📚", verbose_name="Icon")
    
    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"
        ordering = ['name']
    
    def __str__(self):
        return f"{self.name} ({self.code})"

# -------------------------------------------------------
# AdmissionForm Model
# This stores all the data submitted by students
# -------------------------------------------------------
class AdmissionForm(models.Model):
    """
    Stores student admission application details.
    When a student submits the admission form,
    a new row is created in this table.
    """

    # Student's full name (max 200 characters)
    name = models.CharField(max_length=200, verbose_name="Full Name")

    # Student's email address (must be unique - no duplicates)
    email = models.EmailField(unique=True, verbose_name="Email Address")

    # Student's phone number (stored as text to allow leading zeros)
    phone = models.CharField(max_length=15, verbose_name="Phone Number")

    # Course selected from the COURSE_CHOICES list above
    course = models.CharField(
        max_length=10,
        choices=COURSE_CHOICES,
        verbose_name="Applied Course"
    )

    # Student's residential address
    address = models.TextField(verbose_name="Residential Address")

    # Father's name
    father_name = models.CharField(
        max_length=200,
        verbose_name="Father's Name",
        default=""
    )

    # Date of birth
    date_of_birth = models.DateField(
        verbose_name="Date of Birth",
        null=True,
        blank=True
    )

    # 10th percentage (optional)
    tenth_percentage = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        verbose_name="10th Percentage",
        null=True,
        blank=True
    )

    # 12th percentage (optional)
    twelfth_percentage = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        verbose_name="12th Percentage",
        null=True,
        blank=True
    )

    # Application status - can be updated by admin
    STATUS_CHOICES = [
        ('pending',  'Pending Review'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='pending',
        verbose_name="Application Status"
    )

    # Automatically set to current date/time when record is created
    submitted_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Date of Submission"
    )

    # -------------------------------------------------------
    # Meta class: extra options for this model
    # -------------------------------------------------------
    class Meta:
        verbose_name = "Admission Application"
        verbose_name_plural = "Admission Applications"
        ordering = ['-submitted_at']  # Newest first

    # String representation (shown in admin panel)
    def __str__(self):
        return f"{self.name} - {self.get_course_display()} ({self.status})"
