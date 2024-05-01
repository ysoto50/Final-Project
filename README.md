# NoteKeeper
#### Video Demo: https://youtu.be/80s-vm5jZF8
#### **Description**: Note-Journal is a web application built with Bootstrap, JavaScript, Python, HTML, and CSS. It provides functionalities such as user authentication, note management, and password validation. Users can sign up, log in, create notes, delete notes, and log out securely.

### Features
- **User Authentication**: Users can sign up with a unique username and password, ensuring secure access to their notes.
- **Login and Logout**: Secure login and logout functionalities are implemented to manage user sessions.
- **Note Management**: Users can create, view, and delete notes. Notes are stored in a database and displayed on the user's dashboard.
- **Password Security**: Passwords are hashed and must meet specific requirements (capital letters, numbers, and punctuations) to ensure security.

### Web application:
My final project is called Note-Journal, I made an app.py and a helper.py this was for my login required function to import it into my app.py. Then I used it for certain functions such as (Home, Notes, and Logout functions). This is so when my web app opens users are first directed to the login screen and if they are new, they can click on the sign-up link in the nav bar. Next, I built my database using cs50s SQLite. Lastly, I used flash messages for errors and successes, throughout my code.

### Home Function and Home.HTML:
My home function is the main page for my site, it is where you can add notes to the database. My home function renders to my Home.html file. In my Home.html I use jinja2 to extend from my index.html. Also, I used "textarea" to create the area for users to write their notes down and save them.

### Login - Logout Function and Login.HTML:
In my login function I make sure that all new and old users need a username and password to access my web app, or the login button does not work, and flash errors for incorrect username and password. When successfully logged in they are redirected to the home page. The login function renders to my login.html. The login.html extends from my index.html using jinja2 and it has a username label and input, a password label and input as well as a login button. Once logged in you have access to the log out function that uses session.clear and redirect to the login page.

### Sign-up Function and Sign-up.HTML:
The sign-up function uses everything the log in function has except I added a confirmation to confirm the password and I tie my password meets requirement function to this code. I also use a “if len() loop” to check the database if usernames already exists and have flash messages set up for all errors, password does not match, and password does not meet requirements. I also used generate_password_hash to hash all passwords upon sign-up and I used db.execute to store all new sign-ups in the database. At the end I return and render this function to the sign-up.html which has username label and input, a password label and input, and a confirmation label and input with a sign-up button and it all extends to index through jinja2.

### Notes and Delete-Notes Function and Notes.HTML:
Next, I have my notes function this displays the notes stored in my note table of my database to allow users to see their notes. This function renders to notes.html. In my notes.html I use jnija2 and html syntax to build a table for users to see their notes stored in three columns id, notes, and date. I added a delete button to delete any note the user chooses to delete, and this extends from index.html as well. Next is my delete notes function that deletes the notes users want to delete and it deletes from the page and the database using db.execute. and flashes a success message to show it was deleted successfully. This function redirects to the notes page so once you press delete it, it keeps you in the notes page, so you see the note was deleted.

### Password Meets Requirments:
Last function in my app.py is the password meets requirements and this just makes sure to check for a capital letter, a number, and punctuation for the password and I use a for loop to check if each one is true. If even one is false, it returns false for the whole password and sends a flash message error. For my loop to work I had to import str from str_module into this function specifically for punctuation.

### Helper.py and Login Required Function:
Now we are in my helper.py that imports into my app.py and has my login required function. This function makes sure certain pages are only accessible if the user is logged in. This code you’ll since in my code above my def home function and any other functions that make need you to login to have access too.

### Index.HTML and CSS:
In my index.html I use jinja2 to extend to all my html files. This file uses the latest bootstrap CSS and JS, and a link to my static/CSS folder/file. I have my header Note-Journal and a nav bar for my home, notes, login, logout and signup links but I used an if-session to make sure only login and signup show up if the user/new_user is not logged in or signed-up. Once you are logged in the nav bar changes and only the home, notes and logout links show up in the nav bar. After the nav bar, I set my flash messages, and I categorized them as error and success messages. At first, I just had a regular message, but I wanted to have the color correlation for the background to show the difference in messages, so I went with categorizing them to make that effect possible. Next, I have a button in the flash message to close the messages out. After I have my container to extend my index.html to all my html files inside my templates folder. Thereafter I have my jQuery and Java from bootstrap and my JavaScript for my close button. Lastly, I have a CSS file in a static folder to design my code the body, h1, container, nav item, btn, btn hover, notes, form-group and form-control, close and close hover.
