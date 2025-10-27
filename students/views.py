from django.shortcuts import render,redirect,get_object_or_404
from .models import Student
from .forms import StudentForm,UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

# Create your views here.

@login_required
def student_list(request):
    students =  Student.objects.filter(user=request.user)
    return render(request,'students/student_list.html',{'students':students})

@login_required
def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST,request.FILES)
        if form.is_valid():
            std = form.save(commit=False)
            std.user = request.user
            std.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request,'students/student_form.html',{'form':form})

@login_required
def student_edit(request,pk):
    student = get_object_or_404(Student,pk=pk,user=request.user)
    if request.method == 'POST':
        form = StudentForm(request.POST,request.FILES,instance=student)
        if form.is_valid():
            std = form.save(commit=False)
            std.user = request.user
            std.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request,'students/student_form.html',{'form':form})

@login_required
def student_delete(request,pk):
    student = get_object_or_404(Student,pk=pk,user=request.user)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request,'students/student_confirm_delete.html',{'student':student})


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request,user)
            return redirect('student_list')
    else:
        form = UserRegistrationForm()
    return  render(request,'registration/registration.html',{'form':form})
