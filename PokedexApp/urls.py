from django.urls import path
from HomeMateApp import views

"""
Define path for HTML pages
"""

urlpatterns=[
    path("", views.home, name="home"),
    path("sign_up", views.sign_up, name="sign_up"),
    path("sign_in", views.sign_in, name="sign_in"),
    path("get_user_info/<str:id>", views.get_user_info, name="get_user_info"),
    path("update_user_info", views.update_user_info, name="update_user_info"),
    path("user", views.user, name="user"),
    path("worker", views.worker, name="worker"),
    
    path("create_job", views.create_job, name="create_job"),
    path("get_job_info/<str:id>", views.get_job_info, name="get_job_info"),
    path("my_job/<str:id>", views.my_job, name="my_job"),
    path("job", views.job, name="job"),
    path("delete_job/<str:id>", views.delete_job, name="delete_job"),
    
    path("create_cv", views.create_cv, name="create_cv"),
    path("get_cv_info/<str:id>", views.get_cv_info, name="get_cv_info"),
    path("cv", views.cv, name="cv"),
    path("delete_cv/<str:id>", views.delete_cv, name="delete_cv"),
    
    path("create_skill", views.create_skill, name="create_skill"),
    path("skill", views.skill, name="skill"),
]