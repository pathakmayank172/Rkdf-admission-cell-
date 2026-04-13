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
