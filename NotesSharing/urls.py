from django.contrib import admin
from django.urls import path
from notes.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", index, name="index"),
    path("admin/", admin.site.urls),
    path("about-us/", about, name="about"),
    path("contact-us/", contact, name="contact"),
    path("user-login/", userLogin, name="userLogin"),
    path("profile/", profile, name="profile"),
    path("sign-up/", signUpPage, name="signUpPage"),
    path("admin-login/", adminLogin, name="adminLogin"),
    path("users/", viewUsers, name="viewUsers"),
    path("del-user/<int:uid>", delUser, name="delUser"),
    path("admin-home/", adminHome, name="adminHome"),
    path("admin-logout/", adminLogout, name="adminLogout"),
    path("user-logout/", userLogout, name="userLogout"),
    path("profile/change-pwd/", changePwd, name="changePwd"),
    path("user-home/", userHome, name="userHome"),
    path("user-home/All-Notes", userAllNotes, name="userAllNotes"),
    path("view-notes/user-pending", userPendingNotes, name="userPendingNotes"),
    path("view-notes/user-rejected", userRejectedNotes, name="userRejectedNotes"),
    path("uopload-notes/", uploadNotes, name="uploadNotes"),
    path("edit-profile/", editProfile, name="editProfile"),
    path("view-notes/", viewNotes, name="viewNotes"),
    path("view-notes/pending", pendingNotes, name="pendingNotes"),
    path("view-notes/accepted", acceptedNotes, name="acceptedNotes"),
    path("view-notes/rejected", rejectedNotes, name="rejectedNotes"),
    path("view-notes/All", allNotes, name="allNotes"),
    path("del-notes/<int:uid>", delNotes, name="delNotes"),
    path("del-pending-notes/<int:uid>", delPendingNotes, name="delPendingNotes"),
    path("assign-status/<int:uid>", assignStatus, name="assignStatus"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
