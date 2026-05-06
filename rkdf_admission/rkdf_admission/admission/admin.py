"""
Admin panel configuration for the Admission app.
Register models here to manage them in the Django admin panel.
Access at: http://localhost:8000/admin/
"""

from django.contrib import admin
from .models import AdmissionForm, Course


# -------------------------------------------------------
# Custom Admin View for AdmissionForm
# -------------------------------------------------------
@admin.register(AdmissionForm)
class AdmissionFormAdmin(admin.ModelAdmin):
    """
    Customize how AdmissionForm records appear in the admin panel.
    """

    # Columns shown in the list view
    list_display = ('id', 'name', 'email', 'phone', 'course', 'status', 'submitted_at')

    # Filters on the right sidebar
    list_filter = ('course', 'status', 'submitted_at')

    # Search box - search by these fields
    search_fields = ('name', 'email', 'phone')

    # Fields that can be edited directly in the list view
    list_editable = ('status',)

    # Default ordering: newest first
    ordering = ('-submitted_at',)

    # Read-only fields (cannot be changed after submission)
    readonly_fields = ('submitted_at',)

    # Group fields in the detail view
    fieldsets = (
        ('Personal Information', {
            'fields': ('name', 'father_name', 'date_of_birth', 'email', 'phone', 'address')
        }),
        ('Academic Details', {
            'fields': ('course', 'tenth_percentage', 'twelfth_percentage')
        }),
        ('Application Status', {
            'fields': ('status', 'submitted_at')
        }),
    )


# -------------------------------------------------------
# Custom Admin View for Course
# -------------------------------------------------------
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    """
    Customize how Course records appear in the admin panel.
    """

    list_display = ('code', 'name', 'education_level', 'required_stream', 'min_percentage', 'annual_fee', 'seats')
    list_filter = ('education_level', 'required_stream')
    search_fields = ('code', 'name', 'full_name')
    ordering = ('name',)

    fieldsets = (
        ('Basic Information', {
            'fields': ('code', 'name', 'full_name', 'icon', 'duration', 'seats')
        }),
        ('Eligibility Requirements', {
            'fields': ('education_level', 'required_stream', 'min_percentage')
        }),
        ('Fees', {
            'fields': ('annual_fee', 'total_fee')
        }),
        ('Description & Career', {
            'fields': ('description', 'career_opportunities', 'average_salary')
        }),
    )
