from django.shortcuts import render,redirect
from django.http import HttpResponse
from student_grievance.models import first,report_data,login_data,register_data
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail


def main(request):

    return render(request, 'main.html')

@login_required
def main2(request):
    return render(request, 'main2.html')


def register(request):
    raise_massage = None  # Always define this variable
    if request.method == 'POST':
        register_form = request.POST
        firstname = register_form.get('first_name')
        lastname = register_form.get('last_name')
        email = register_form.get('email')
        phone = register_form.get('phone')
        username = register_form.get('username')
        password = register_form.get('password')
        cpassword = register_form.get('cpassword')

        if register_data.objects.filter(email=email).exists():
            raise_massage = "Email already exists"
        elif len(password) < 8:
            raise_massage = "Password must be at least 8 characters long."
        elif not any(char.isdigit() for char in password):
            raise_massage = "Password must contain at least one digit."
        elif not any(char.isalpha() for char in password):
            raise_massage = "Password must contain at least one letter."
        elif not any(char in '!@#$%^&*()_+' for char in password):
            raise_massage = "Password must contain at least one special character (!@#$%^&*()_+)."
        elif not username.isalnum():
            raise_massage = "Username must be alphanumeric (letters and numbers only)."
        elif password != cpassword:
            raise_massage = "Password and Confirm Password do not match. Please try again."
        else:
            # Save the user data
            user = User.objects.create_user(username=username, password=password, email=email)
            user.first_name = firstname
            user.last_name = lastname
            user.save()
            rd = register_data(
                first_name=firstname, 
                last_name=lastname, 
                email=email, 
                phone=phone, 
                username=username
            )
            rd.save()
            # Send confirmation email
            send_mail(
                'Registration Successful',
                f'Hello {firstname},\n\nThank you for registering on our platform. Your account has been created successfully.\n\nBest regards,\nStudent Grievance Team',
                'karljackhob@gmail.com',
                [email],
                fail_silently=False,
            )
            return render(request, 'login.html')
    return render(request, 'register.html', {'raise_massage': raise_massage})


def user_login(request):
    error_message = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main2')
        else:
           error_message = {
                'error': 'Invalid username or password. Please try again.'
            }
           return render(request, 'login.html', error_message)
    else:
        return render(request, 'login.html')        

def aboutus(request):
    return render(request,'about.html')

@login_required
def about_us(request):
    return render(request, 'about_us.html')

@login_required
def report(request):
    if request.method == 'POST':
        report_form = request.POST
        firstname = report_form.get('first-name')
        lastname = report_form.get('last-name')
        email = report_form.get('email')
        phone = report_form.get('number')
        course = report_form.get('course')
        description = report_form.get('description')
        images = request.FILES.get('media')
        rd = report_data(
            first_name=firstname, 
            last_name = lastname,
            email=email, 
            phone=phone, 
            Course=course, 
            description=description, 
            images=images
            )
        rd.save()
    return render(request,'report.html')


def user_data(request):
    return render(request, 'login.html')

def testpage(request):
    firstdata = first.objects.all()
    pager = Paginator(firstdata, 2)  
    page_num = request.GET.get('page')
    pagedeta = pager.get_page(page_num)
    totalpage = pager.num_pages

    if request.method == "GET":
        ft = request.GET.get('search_name')
        if ft != None:
            firstdata=first.objects.filter(name__icontains = ft)




def user_logout(request):
    logout(request)
    request.session.flush()  # Clear the session data
    return render(request, 'logout.html')


@login_required
def status_track(request):
    status = None
    if request.method == 'POST':
        complain_id =int(request.POST.get('complain_id'))
        try:
            report = report_data.objects.get(status_id=complain_id)
            status = report.status
        except report_data.DoesNotExist:
            status = "Invalid Complain ID. Please try again."
    return render(request, 'status.html', {'status': status})
    


