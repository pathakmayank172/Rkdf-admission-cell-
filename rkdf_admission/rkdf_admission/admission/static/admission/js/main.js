/**
 * RKDF University Ranchi - Admission Cell
 * Main JavaScript File
 * 
 * Contains:
 * - Navigation toggle (mobile menu)
 * - Scroll-to-top button
 * - Admission form validation
 * - Contact form validation
 * - Counter animation
 * - Active nav link highlighting
 */

// ================================================================
// 1. RUN EVERYTHING WHEN THE PAGE IS FULLY LOADED
// ================================================================
document.addEventListener('DOMContentLoaded', function () {

    initNavigation();
    initScrollTop();
    initAdmissionFormValidation();
    initCourseRecommendation();
    initChatbot();
    initContactFormValidation();
    initCounterAnimation();
    setActiveNavLink();
    initTableSearch();

    console.log('✅ RKDF Admission Cell - JS Loaded');
});


// ================================================================
// 2. NAVIGATION (Mobile Menu Toggle)
// ================================================================
function initNavigation() {
    const toggle = document.getElementById('navToggle');
    const navMenu = document.getElementById('navMenu');

    if (!toggle || !navMenu) return;

    // Toggle mobile menu open/close
    toggle.addEventListener('click', function () {
        toggle.classList.toggle('open');
        navMenu.classList.toggle('open');
    });

    // Close menu when a link is clicked
    navMenu.querySelectorAll('.nav-link').forEach(function (link) {
        link.addEventListener('click', function () {
            toggle.classList.remove('open');
            navMenu.classList.remove('open');
        });
    });

    // Close menu on outside click
    document.addEventListener('click', function (e) {
        if (!toggle.contains(e.target) && !navMenu.contains(e.target)) {
            toggle.classList.remove('open');
            navMenu.classList.remove('open');
        }
    });
}


// ================================================================
// 3. SET ACTIVE NAV LINK
// Highlights the current page's nav link
// ================================================================
function setActiveNavLink() {
    // Get the current page URL path (e.g., "/about/")
    var currentPath = window.location.pathname;

    document.querySelectorAll('.nav-link').forEach(function (link) {
        var linkPath = link.getAttribute('href');

        // Exact match for home, prefix match for others
        if (currentPath === linkPath ||
            (linkPath !== '/' && currentPath.startsWith(linkPath))) {
            link.classList.add('active');
        } else {
            link.classList.remove('active');
        }
    });
}


// ================================================================
// 4. SCROLL-TO-TOP BUTTON
// ================================================================
function initScrollTop() {
    var btn = document.getElementById('scrollTopBtn');
    if (!btn) return;

    // Show/hide button based on scroll position
    window.addEventListener('scroll', function () {
        if (window.scrollY > 400) {
            btn.classList.add('visible');
        } else {
            btn.classList.remove('visible');
        }
    });

    // Scroll to top smoothly on click
    btn.addEventListener('click', function () {
        window.scrollTo({ top: 0, behavior: 'smooth' });
    });
}


// ================================================================
// 5. ADMISSION FORM VALIDATION
// Validates each field before allowing form submission
// ================================================================
function initAdmissionFormValidation() {
    var form = document.getElementById('admissionForm');
    if (!form) return;

    // Validate on form submit
    form.addEventListener('submit', function (e) {
        // Clear previous errors first
        clearAllErrors();

        var isValid = true;

        // --- Validate Full Name ---
        var nameInput = document.getElementById('name');
        if (nameInput) {
            var nameVal = nameInput.value.trim();
            if (nameVal === '') {
                showError('name', 'Full Name is required.');
                isValid = false;
            } else if (nameVal.length < 3) {
                showError('name', 'Name must be at least 3 characters.');
                isValid = false;
            } else if (!/^[a-zA-Z\s]+$/.test(nameVal)) {
                showError('name', 'Name should contain only letters and spaces.');
                isValid = false;
            }
        }

        // --- Validate Email ---
        var emailInput = document.getElementById('email');
        if (emailInput) {
            var emailVal = emailInput.value.trim();
            var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (emailVal === '') {
                showError('email', 'Email address is required.');
                isValid = false;
            } else if (!emailRegex.test(emailVal)) {
                showError('email', 'Please enter a valid email address.');
                isValid = false;
            }
        }

        // --- Validate Phone ---
        var phoneInput = document.getElementById('phone');
        if (phoneInput) {
            var phoneVal = phoneInput.value.trim();
            var phoneRegex = /^[6-9]\d{9}$/; // Indian mobile number
            if (phoneVal === '') {
                showError('phone', 'Phone number is required.');
                isValid = false;
            } else if (!phoneRegex.test(phoneVal)) {
                showError('phone', 'Enter a valid 10-digit Indian mobile number.');
                isValid = false;
            }
        }

        // --- Validate Father's Name ---
        var fatherInput = document.getElementById('father_name');
        if (fatherInput) {
            var fatherVal = fatherInput.value.trim();
            if (fatherVal === '') {
                showError('father_name', "Father's Name is required.");
                isValid = false;
            }
        }

        // --- Validate Date of Birth ---
        var dobInput = document.getElementById('date_of_birth');
        if (dobInput) {
            var dobVal = dobInput.value;
            if (dobVal === '') {
                showError('date_of_birth', 'Date of Birth is required.');
                isValid = false;
            } else {
                var dob = new Date(dobVal);
                var today = new Date();
                var age = today.getFullYear() - dob.getFullYear();
                if (age < 15 || age > 50) {
                    showError('date_of_birth', 'Age must be between 15 and 50 years.');
                    isValid = false;
                }
            }
        }

        // --- Validate Course ---
        var courseInput = document.getElementById('course');
        if (courseInput) {
            if (courseInput.value === '') {
                showError('course', 'Please select a course.');
                isValid = false;
            }
        }

        // --- Validate Address ---
        var addressInput = document.getElementById('address');
        if (addressInput) {
            var addrVal = addressInput.value.trim();
            if (addrVal === '') {
                showError('address', 'Residential address is required.');
                isValid = false;
            } else if (addrVal.length < 15) {
                showError('address', 'Please enter a complete address (at least 15 characters).');
                isValid = false;
            }
        }

        // --- Validate 10th Percentage ---
        var tenthInput = document.getElementById('tenth_percentage');
        if (tenthInput && tenthInput.value !== '') {
            var tenthVal = parseFloat(tenthInput.value);
            if (isNaN(tenthVal) || tenthVal < 0 || tenthVal > 100) {
                showError('tenth_percentage', 'Percentage must be between 0 and 100.');
                isValid = false;
            }
        }

        // --- Validate 12th Percentage ---
        var twelfthInput = document.getElementById('twelfth_percentage');
        if (twelfthInput && twelfthInput.value !== '') {
            var twelfthVal = parseFloat(twelfthInput.value);
            if (isNaN(twelfthVal) || twelfthVal < 0 || twelfthVal > 100) {
                showError('twelfth_percentage', 'Percentage must be between 0 and 100.');
                isValid = false;
            }
        }

        // If validation failed, stop form submission
        if (!isValid) {
            e.preventDefault(); // Prevent form from being sent

            // Scroll to the first error
            var firstError = form.querySelector('.error');
            if (firstError) {
                firstError.scrollIntoView({ behavior: 'smooth', block: 'center' });
            }

            // Show a top-level error message
            showFormAlert('Please fix the errors below before submitting.', 'error');
        } else {
            // Show loading state on submit button
            var submitBtn = form.querySelector('button[type="submit"]');
            if (submitBtn) {
                submitBtn.textContent = '⏳ Submitting...';
                submitBtn.disabled = true;
            }
        }
    });

    // Real-time validation: validate each field as user types
    form.querySelectorAll('input, select, textarea').forEach(function (field) {
        field.addEventListener('blur', function () {
            // Clear the error for this specific field on blur
            clearError(field.id);
        });
    });
}


// ================================================================
// 6. CONTACT FORM VALIDATION
// ================================================================
function initContactFormValidation() {
    var form = document.getElementById('contactForm');
    if (!form) return;

    form.addEventListener('submit', function (e) {
        clearAllErrors();
        var isValid = true;

        var nameInput = document.getElementById('contact_name');
        if (nameInput && nameInput.value.trim() === '') {
            showError('contact_name', 'Your name is required.');
            isValid = false;
        }

        var emailInput = document.getElementById('contact_email');
        if (emailInput) {
            var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!emailRegex.test(emailInput.value.trim())) {
                showError('contact_email', 'Valid email is required.');
                isValid = false;
            }
        }

        var msgInput = document.getElementById('contact_message');
        if (msgInput && msgInput.value.trim().length < 10) {
            showError('contact_message', 'Message must be at least 10 characters.');
            isValid = false;
        }

        if (!isValid) e.preventDefault();
    });
}


// ================================================================
// 7. HELPER FUNCTIONS FOR VALIDATION
// ================================================================

/**
 * Show an error message below a specific field
 * @param {string} fieldId - The ID of the input field
 * @param {string} message - The error message to display
 */
function showError(fieldId, message) {
    var field = document.getElementById(fieldId);
    var errorEl = document.getElementById(fieldId + '_error');

    if (field) {
        field.classList.add('error');
    }

    if (errorEl) {
        errorEl.textContent = message;
        errorEl.style.display = 'block';
    }
}

/**
 * Clear the error for a specific field
 * @param {string} fieldId - The ID of the input field
 */
function clearError(fieldId) {
    var field = document.getElementById(fieldId);
    var errorEl = document.getElementById(fieldId + '_error');

    if (field) {
        field.classList.remove('error');
    }

    if (errorEl) {
        errorEl.style.display = 'none';
        errorEl.textContent = '';
    }
}

/**
 * Clear ALL error messages on the page
 */
function clearAllErrors() {
    document.querySelectorAll('.error').forEach(function (el) {
        el.classList.remove('error');
    });
    document.querySelectorAll('.field-error').forEach(function (el) {
        el.style.display = 'none';
        el.textContent = '';
    });
}

/**
 * Show a global alert at the top of the form
 * @param {string} message - Alert message
 * @param {string} type    - 'error', 'success', 'info'
 */
function showFormAlert(message, type) {
    var alertContainer = document.getElementById('formAlerts');
    if (!alertContainer) return;

    var icon = type === 'error' ? '⚠️' : type === 'success' ? '✅' : 'ℹ️';
    alertContainer.innerHTML =
        '<div class="alert alert-' + type + '">' +
        '<span>' + icon + '</span>' +
        '<span>' + message + '</span>' +
        '</div>';

    alertContainer.scrollIntoView({ behavior: 'smooth', block: 'center' });
}


// ================================================================
// 8. ANIMATED NUMBER COUNTER (for homepage stats)
// ================================================================
function initCounterAnimation() {
    var counters = document.querySelectorAll('[data-counter]');
    if (counters.length === 0) return;

    /**
     * Animate a counter from 0 to its target value
     * @param {HTMLElement} el - The element to animate
     */
    function animateCounter(el) {
        var target = parseInt(el.getAttribute('data-counter'), 10);
        var duration = 2000; // 2 seconds
        var start = 0;
        var startTime = null;

        function step(timestamp) {
            if (!startTime) startTime = timestamp;
            var progress = Math.min((timestamp - startTime) / duration, 1);

            // Ease-out formula for smoother animation
            var eased = 1 - Math.pow(1 - progress, 3);
            el.textContent = Math.floor(eased * target).toLocaleString();

            if (progress < 1) {
                requestAnimationFrame(step);
            } else {
                el.textContent = target.toLocaleString() + (el.dataset.suffix || '');
            }
        }

        requestAnimationFrame(step);
    }

    // Use Intersection Observer to start animation when element is visible
    var observer = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
            if (entry.isIntersecting) {
                animateCounter(entry.target);
                observer.unobserve(entry.target); // Only animate once
            }
        });
    }, { threshold: 0.5 });

    counters.forEach(function (counter) {
        observer.observe(counter);
    });
}


// ================================================================
// 9. DASHBOARD TABLE SEARCH
// Client-side filtering of the table rows
// ================================================================
function initCourseRecommendation() {
    var form = document.getElementById('recommendationForm');
    var resultSection = document.getElementById('recommendationSection');
    if (!form || !resultSection) return;

    form.addEventListener('submit', function (e) {
        e.preventDefault();
        clearAllErrors();

        var education = document.getElementById('education_level');
        var stream = document.getElementById('stream');
        var marks = document.getElementById('marks');
        var budget = document.getElementById('budget');

        var valid = true;

        if (!education || education.value.trim() === '') {
            showError('education_level', 'Please select your education level.');
            valid = false;
        }
        if (!stream || stream.value.trim() === '') {
            showError('stream', 'Please select your stream.');
            valid = false;
        }
        if (!marks || marks.value.trim() === '' || isNaN(parseFloat(marks.value)) || parseFloat(marks.value) < 0 || parseFloat(marks.value) > 100) {
            showError('marks', 'Please enter a valid percentage between 0 and 100.');
            valid = false;
        }
        if (!budget || budget.value.trim() === '') {
            showError('budget', 'Please choose a budget range.');
            valid = false;
        }

        if (!valid) {
            showFormAlert('Please fix the highlighted fields and try again.', 'error');
            return;
        }

        resultSection.innerHTML = '<div class="recommendation-loading">⏳ Generating your personalized course recommendations...</div>';

        var formData = new FormData(form);

        fetch(form.action || window.location.pathname, {
            method: 'POST',
            body: formData,
            headers: {
                'X-Requested-With': 'XMLHttpRequest'
            }
        })
        .then(function (response) {
            if (!response.ok) {
                throw new Error('Server error');
            }
            return response.json();
        })
        .then(function (data) {
            if (data.no_match) {
                resultSection.innerHTML = renderNoMatch(data);
            } else {
                resultSection.innerHTML = renderRecommendations(data.recommendations);
            }
            resultSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
        })
        .catch(function () {
            resultSection.innerHTML = '<div class="recommendation-error">Unable to load recommendations right now. Please try again.</div>';
        });
    });
}

function renderRecommendations(recommendations) {
    if (!recommendations || recommendations.length === 0) {
        return '<div class="recommendation-error">No recommendations were found.</div>';
    }

    var html = '<div style="text-align: center; margin-bottom: 40px;"><h2>✅ Best Course Matches</h2><p>These courses fit your profile and budget.</p></div>';
    recommendations.forEach(function (item, index) {
        var rankLabel = index === 0 ? '🥇 Rank #1 - Best Match' : index === 1 ? '🥈 Rank #2 - Strong Match' : '🥉 Rank #3 - Good Match';
        html += '<div class="course-card" style="margin-bottom: 30px; padding: 24px; border: 2px solid #e8f0f7; border-radius: 12px; background: linear-gradient(135deg, #f8fbff 0%, #f0f8ff 100%);">';
        html += '<div style="display: inline-block; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 6px 12px; border-radius: 20px; font-weight: bold; margin-bottom: 12px;">' + rankLabel + '</div>';
        html += '<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px;">';
        html += '<div><h3 style="margin: 0 0 8px 0; color: #333;">' + item.name + '</h3>';
        html += '<p style="margin: 0 0 12px 0; color: #666; font-size: 14px;">' + item.full_name + '</p>';
        html += '<div style="background: white; padding: 12px; border-radius: 8px; margin-bottom: 12px;">';
        html += '<p style="margin: 0; font-size: 14px; line-height: 1.6;"><strong>Duration:</strong> ' + item.duration + '<br>';
        html += '<strong>Seats:</strong> ' + item.seats + '<br>';
        html += '<strong>Eligibility:</strong> ' + item.eligibility + '<br>';
        html += '<strong>Annual Fee:</strong> ₹' + Math.round(item.annual_fee) + '<br>';
        html += '<strong>Total Fee:</strong> ₹' + Math.round(item.total_fee) + '</p></div>';
        html += '<p style="margin: 0; color: #555; font-size: 14px; line-height: 1.6;"><strong>About:</strong> ' + item.description + '</p></div>';
        html += '<div><h4 style="color: #667eea; margin-top: 0;">Why It Suits You</h4>';
        html += '<div style="background: white; padding: 12px; border-radius: 8px; margin-bottom: 12px;"><ul style="margin: 0; padding-left: 20px; font-size: 14px; line-height: 1.8;">';
        item.reasons.forEach(function (reason) {
            html += '<li style="margin-bottom: 6px;">✓ ' + reason + '</li>';
        });
        html += '</ul></div>';
        html += '<h4 style="color: #667eea;">Career Opportunities</h4>';
        html += '<p style="margin: 0; color: #555; font-size: 14px; line-height: 1.6;">' + item.career_opportunities + '</p>';
        html += '<h4 style="color: #667eea; margin-top: 12px;">Expected Salary</h4>';
        html += '<div style="background: #d4e8f0; padding: 10px; border-radius: 6px; font-weight: bold; color: #333; font-size: 14px;">💰 ' + item.average_salary + '</div>';
        html += '<div style="margin-top: 16px;"><a href="' + item.apply_url + '" class="btn btn-primary" style="display: inline-block; padding: 10px 20px; background: #667eea; color: white; text-decoration: none; border-radius: 6px; font-size: 14px; text-align: center;">Apply for ' + item.name + '</a></div>';
        html += '</div></div></div>';
    });
    return html;
}

function renderNoMatch(data) {
    var html = '<div class="alert alert-warning" style="max-width: 700px; margin: 40px auto; padding: 24px; border-radius: 12px;">';
    html += '<div style="font-size: 2rem; margin-bottom: 12px;">⚠️</div>';
    html += '<h3 style="margin: 0 0 12px 0;">No Matching Courses Found</h3>';
    html += '<p style="margin: 0 0 16px 0;">' + (data.message || 'No recommendations available.') + '</p>';
    if (data.suggestions && data.suggestions.length) {
        html += '<ul style="margin: 0; padding-left: 20px;">';
        data.suggestions.forEach(function (suggestion) {
            html += '<li style="margin-bottom: 8px;">' + suggestion + '</li>';
        });
        html += '</ul>';
    }
    html += '<div style="margin-top: 20px;"><p style="margin: 0; color: #666; font-size: 14px;">📞 Contact our admission team for personalized guidance: <strong>admissions@rkdf.ac.in</strong></p></div>';
    html += '</div>';
    return html;
}

function initChatbot() {
    var messagesContainer = document.getElementById('chatbotMessages');
    var input = document.getElementById('chatInput');
    var sendButton = document.getElementById('chatSend');
    if (!messagesContainer || !input || !sendButton) return;

    function addMessage(text, sender) {
        var message = document.createElement('div');
        message.className = 'chatbot-message ' + sender;
        message.textContent = text;
        messagesContainer.appendChild(message);
        messagesContainer.scrollTop = messagesContainer.scrollHeight;
    }

    function getBotResponse(query) {
        var normalized = query.toLowerCase();
        if (normalized.includes('eligibility') || normalized.includes('percentage')) {
            return 'Eligibility depends on the selected course. Generally 10+2 with 45-50% is enough for most undergraduate courses, while postgraduate programs need graduation with 50% or more.';
        }
        if (normalized.includes('budget') || normalized.includes('fee')) {
            return 'Annual fees vary by course: B.Com and B.Sc are usually more affordable, while B.Tech, M.Tech, and MBA have higher fees. Choose a course based on your budget range.';
        }
        if (normalized.includes('bca') || normalized.includes('computer')) {
            return 'BCA is ideal if you enjoy programming, web apps, databases and IT careers. It is good for students from any stream with Maths at 10+2.';
        }
        if (normalized.includes('bba') || normalized.includes('business')) {
            return 'BBA suits students interested in management, marketing, finance, or entrepreneurship. It is open to any stream with 45% or more in 10+2.';
        }
        if (normalized.includes('btech') || normalized.includes('engineering')) {
            return 'B.Tech is best for PCM students with at least 50% in 10+2. It leads to engineering and technology careers in CSE, ECE, ME and other branches.';
        }
        if (normalized.includes('mba')) {
            return 'MBA requires graduation in any stream with 50% or higher. It helps build leadership, marketing, finance, and HR careers.';
        }
        return 'I can help you with courses, eligibility, fees, and admission steps. Try asking “Which course suits my stream?” or “What is the eligibility for BCA?”.';
    }

    function sendChat() {
        var text = input.value.trim();
        if (!text) return;
        addMessage(text, 'user');
        input.value = '';
        setTimeout(function () {
            addMessage(getBotResponse(text), 'bot');
        }, 300);
    }

    sendButton.addEventListener('click', sendChat);
    input.addEventListener('keydown', function (event) {
        if (event.key === 'Enter') {
            event.preventDefault();
            sendChat();
        }
    });
}

function initTableSearch() {
    var searchInput = document.getElementById('tableSearch');
    if (!searchInput) return;

    searchInput.addEventListener('input', function () {
        var searchTerm = this.value.toLowerCase();
        var rows = document.querySelectorAll('#admissionTable tbody tr');

        rows.forEach(function (row) {
            var rowText = row.textContent.toLowerCase();
            row.style.display = rowText.includes(searchTerm) ? '' : 'none';
        });
    });
}


// ================================================================
// 10. PRINT DASHBOARD TABLE
// ================================================================
function printDashboard() {
    window.print();
}
