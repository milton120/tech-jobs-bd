﻿# tech-jobs-bd
 
 A simple technical job posting site using Django. 
 
 ## Description
 
 The main objective of this project is to learn about **Cutom Authentication** in django. Django by default authenticates with a **username** field and **password** field. But that is not the case we always want. So, i tried to implement a [CustomUser](https://github.com/milton120/tech-jobs-bd/tree/master/custom_user) app which uses **Email** and **Password** to authenticate a user. 
 
 
 ## Editing Settings.py
 
 We need to tell django that we are using a custom authentication not the default one. So, we need to add **AUTH_USER_MODEL** in settings.py like this
 > AUTH_USER_MODEL = 'app_name.custom_user_class_name'
 
 In this project, i have a [custom_user](https://github.com/milton120/tech-jobs-bd/tree/master/custom_user) app. Inside custom_user's **models.py** i have a **CustomUser** class for custom authentication. So, this projects **AUTH_USER_MODEL** is
 > AUTH_USER_MODEL = 'custom_user.CustomUser'
 
 
 
 ## Contribution
 
 I am a big fan of clean code and always try to write clean code and follow standard coding style. If there is any more **pythonic** way to write [custom_user](https://github.com/milton120/tech-jobs-bd/tree/master/custom_user) or if some security issues can arise in the existing code or anything you may feel that needed to be change, you can suggest me. I will really appreciate your contribution. 
