from django.shortcuts import render, redirect
from .models import student

def student_registration(request):
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        gender = request.POST.get('gender')
        date_of_birth = request.POST.get('date_of_birth')
        contact_number = request.POST.get('contact_number')

        # Create a new student instance and save it to the database
        student.objects.create(
            student_id=student_id,
            first_name=first_name,
            last_name=last_name,
            gender=gender,
            date_of_birth=date_of_birth,
            contact_number=contact_number
        )

        return redirect('registration_success')  # Redirect to a success page after registration

    return render(request, 'registration/student_registration.html')

def registration_success(request):
    return render(request, 'registration/success.html')
