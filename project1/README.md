## Project 1

Web Programming with Python and JavaScript

# 15-04
Task 1:
Created a registration page using a std layout to be used for all pages.

Task 2:
Added the page to flask.

Task 3:
The page can take values in the form and can be read in flask as well as sent
to page via 'POST' method.

# 16-04
Task 1:
Completed the task by creating a table in the adminer website given to us.

Task 2:
Designed the 'register' page in 3 forms -
1) the form page for 'GET' request method(act = 0)
2) the form page if the username is already taken(act = -1)
3) page if the registration is successful(act = 1)

Task 3:
Designed 'admin' page which gives the details of all the users in the database in a table.

# 17-04
Task 1:
Added the login button adjacent to the register button on the /register page. Users can register or login from the same page and the same form. Changed the button to input tag from the form tag, and changed the form action from the form tag to this input tag.
Login button posts the form inputs to the /auth page, whereas register button posts it to the same page.

Task 2:
Added the session variable on "username", it is None. Everytime a user logs in, it is changed to his name and when no user is logged in. When logged out, it is None again.

Task 3:
Read the contents of the books.csv file and uploaded in the database. ORM has been used. The class has been defined in the models.py file.