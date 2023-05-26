from django.shortcuts import render

# Create your views here.

def Signup(request):
    return render(request,"Basics/Signup.html")

def Login(request):
    return render(request,"Basics/Login.html")

def Profile(request):
    return render(request,"Basics/Profile.html")

def LandingAfterLogin(request):
    return render(request,"Basics/LandingAfterLogin.html")

def About(request):
    return render(request,"Basics/About.html")

def Courses(request):
    return render(request,"Basics/Courses.html")

def Pythoncourse(request):
    return render(request,"Basics/Pythoncourse.html")

def Javacourse(request):
    return render(request,"Basics/Javacourse.html")

def Cppcourse(request):
    return render(request,"Basics/Cppcourse.html")


def LandingBeforeLogin(request):
    return render(request,"Basics/LandingBeforeLogin.html")

def Contact(request):
    return render(request,"Basics/Contact.html")

def CourseRecommendationPage(request):
    return render(request,"Basics/CourseRecommendationPage.html")






