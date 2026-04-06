from django.shortcuts import render

def showStudentPage(request):
    return render(request, 'studentpage/studentpage.html')
