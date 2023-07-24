from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Note, signUp
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import check_password
from datetime import date

## Create your views here.


# About Us Page
def about(request):
    return render(request, "about.html")


# Index Page
def index(request):
    return render(request, "index.html")


# Contact Page
def contact(request):
    return render(request, "contact.html")


# Uaer Login Page
def userLogin(request):
    error = ""
    if request.method == "POST":
        u = request.POST.get("userEmail")
        p = request.POST.get("userPwd")
        user = authenticate(username=u, password=p)
        try:
            if user:
                login(request, user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    d = {"error": error}
    return render(request, "userLogin.html", d)


# Admin Login Page
def adminLogin(request):
    error = ""
    if request.method == "POST":
        u = request.POST.get("adminEmail")
        p = request.POST.get("adminPwd")
        admin = authenticate(username=u, password=p)
        try:
            if admin.is_staff:
                login(request, admin)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    d = {"error": error}
    return render(request, "adminLogin.html", d)


# SignUp Page
def signUpPage(request):
    error = ""
    if request.method == "POST":
        fn = request.POST.get("fn")
        ln = request.POST.get("ln")
        c = request.POST.get("contact")
        e = request.POST.get("email")
        pwd = request.POST.get("Pwd")
        b = request.POST.get("branch")
        r = request.POST.get("role")
        try:
            u = User.objects.create_user(
                username=e, password=pwd, first_name=fn, last_name=ln, email=e
            )
            signUp.objects.create(user=u, contact=c, branch=b, role=r)
            error = "no"
        except:
            error = "yes"
    d = {"error": error}
    return render(request, "signUpPage.html", d)


# Admin Home Page
def adminHome(request):
    if not request.user.is_staff:
        return redirect("adminLogin")

    pn = Note.objects.filter(status="pending").count()
    ac = Note.objects.filter(status="accepted").count()
    re = Note.objects.filter(status="rejected").count()
    all = Note.objects.all().count()

    d = {"pn": pn, "ac": ac, "re": re, "all": all}
    return render(request, "adminHome.html", d)


# view users
def viewUsers(request):
    if not request.user.is_authenticated:
        return render("adminLogin")
    users = signUp.objects.all()
    d = {"users": users}
    return render(request, "viewUsers.html", d)


# delete user uploaded notes
def delUser(request, uid):
    if not request.user.is_authenticated:
        return render("adminLogin")
    user = User.objects.get(id=uid)
    user.delete()
    return redirect("viewUsers")


# pending notes
def pendingNotes(request):
    if not request.user.is_authenticated:
        return render("adminLogin")
    notes = Note.objects.filter(status="pending")
    d = {"notes": notes}
    return render(request, "pendingNotes.html", d)


# accepted notes
def acceptedNotes(request):
    if not request.user.is_authenticated:
        return render("adminLogin")
    notes = Note.objects.filter(status="accepted")
    d = {"notes": notes}
    return render(request, "acceptedNotes.html", d)


# rejected notes
def rejectedNotes(request):
    if not request.user.is_authenticated:
        return render("adminLogin")
    notes = Note.objects.filter(status="rejected")
    d = {"notes": notes}
    return render(request, "rejectedNotes.html", d)


# view all notes
def allNotes(request):
    if not request.user.is_authenticated:
        return render("adminLogin")
    notes = Note.objects.all()
    d = {"notes": notes}
    return render(request, "allNotes.html", d)


# assign status
def assignStatus(request, uid):
    if not request.user.is_authenticated:
        return render("adminLogin")
    notes = Note.objects.get(id=uid)
    error = ""
    if request.method == "POST":
        s = request.POST.get("status")
        try:
            notes.status = s
            notes.save()
            error = "no"
        except:
            error = "yes"
    d = {"notes": notes, "error": error}
    return render(request, "assignStatus.html", d)


# Admin Logout
def adminLogout(request):
    logout(request)
    return render(request, "adminLogin.html")


# User Home Page
def userHome(request):
    return render(request, "userHome.html")


# Upload Notes
def uploadNotes(request):
    if not request.user.is_authenticated:
        return render("userLogin")
    error = ""
    if request.method == "POST":
        b = request.POST.get("Branch")
        s = request.POST.get("Subject")
        nf = request.FILES.get("uploadFile")
        ft = request.POST.get("FileType")
        d = request.POST.get("Description")
        u = User.objects.filter(username=request.user.username)
        try:
            newNote=Note.objects.create(
                user=u,
                uploadDate=date.today(),
                branch=b,
                subject=s,
                NotesFile=nf,
                type=ft,
                Description=d,
                status="pending",
            )
            newNote.save()
            error = "no"
        except:
            error = "yes"
    d = {"error": error}
    return render(request, "uploadNotes.html", d)


# view user uploaded notes
def viewNotes(request):
    if not request.user.is_authenticated:
        return render("userLogin")
    notes = Note.objects.filter(status="accepted", user=request.user.id)
    d = {"notes": notes}
    return render(request, "viewNotes.html", d)


# view all notes
def userAllNotes(request):
    if not request.user.is_authenticated:
        return render("userLogin")

    notes = Note.objects.filter(status="accepted")
    d = {"notes": notes}
    return render(request, "userAllNotes.html", d)


# user pending Notes
def userPendingNotes(request):
    if not request.user.is_authenticated:
        return render("adminLogin")
    notes = Note.objects.filter(status="pending", user=request.user.id)
    d = {"notes": notes}
    return render(request, "userPendingNotes.html", d)


# user pending Notes
def userRejectedNotes(request):
    if not request.user.is_authenticated:
        return render("adminLogin")
    notes = Note.objects.filter(status="rejected", user=request.user.id)
    d = {"notes": notes}
    return render(request, "userRejectedNotes.html", d)


# delete user uploaded notes
def delNotes(request, uid):
    if not request.user.is_authenticated:
        return render("userLogin")
    notes = Note.objects.get(id=uid)
    notes.delete()
    return redirect("viewNotes")


# remove or delete pending notes
def delPendingNotes(request, uid):
    if not request.user.is_authenticated:
        return render("userLogin")
    notes = Note.objects.get(id=uid)
    notes.delete()
    return redirect("adminHome")


# User Logout Page
def userLogout(request):
    logout(request)
    return render(request, "userLogin.html")


# User Profile Page
def profile(request):
    if not request.user.is_authenticated:
        return render("userLogin")
    user = User.objects.get(id=request.user.id)
    data = signUp.objects.get(user=user)
    d = {"data": data, "user": user}

    error = ""
    if request.method == "POST":
        fn = request.POST.get("fn")
        ln = request.POST.get("ln")
        c = request.POST.get("contact")
        e = request.POST.get("email")
        pwd = request.POST.get("Pwd")
        b = request.POST.get("branch")
        r = request.POST.get("role")
        try:
            u = User.objects.create_user(
                username=e, password=pwd, first_name=fn, last_name=ln, email=e
            )
            signUp.objects.create(user=u, contact=c, branch=b, role=r)
            error = "no"
        except:
            error = "yes"
    return render(request, "profile.html", d)


# Edit User Profile
def editProfile(request):
    if not request.user.is_authenticated:
        return render("userLogin")

    user = User.objects.get(id=request.user.id)
    data = signUp.objects.get(user=user)
    d = {"data": data, "user": user}
    error = ""
    if request.method == "POST":
        fn = request.POST.get("fn")
        ln = request.POST.get("ln")
        c = request.POST.get("contact")
        b = request.POST.get("branch")
        r = request.POST.get("role")
        user.first_name = fn
        user.last_name = ln
        data.contact = c
        data.branch = b
        data.role = r
        try:
            user.save()
            data.save()
            error = "no"
        except:
            error = "yes"
    d = {"data": data, "user": user, "error": error}

    return render(request, "userEditProfile.html", d)


# Change User Password
def changePwd(request):
    if not request.user.is_authenticated:
        return redirect("profile")
    error = ""
    u = User.objects.get(username__exact=request.user.username)
    pwd = request.user.password
    if request.method == "POST":
        oldPwd = request.POST.get("oldPwd")
        newPwd = request.POST.get("newPwd")
        confirmPwd = request.POST.get("confirmPwd")
        checkPwd = check_password(oldPwd, pwd)
        try:
            if checkPwd:
                if confirmPwd == newPwd:
                    u.set_password(newPwd)
                    u.save()
                    error = "no"
                else:
                    error = "yes"
            else:
                error = "yes"
        except:
            error = "yes"
    d = {"error": error}
    return render(request, "changePwd.html", d)
