# DBlog

<p align="center">
<a href="https://www.python.org/"><img src="https://forthebadge.com/images/badges/made-with-python.svg" border="0" title="Made with Python" />
</p>

<p align="center">
<a href="http://www.djangoproject.com/"><img src="https://www.djangoproject.com/m/img/badges/djangopowered126x54.gif" border="0" alt="Powered by Django." title="Powered by Django." /></a>
</p>

### ER Diagram

![ER-diagram](https://user-images.githubusercontent.com/84091455/206548715-d5fe1491-1ced-4f57-b572-30ef62d3c372.png)

<br/>

### Pages

- Home page
- Article Detail page
- Add Post Page
- Add Category Page
- Update Post
- Delete Post
- Add Comment page
- Blogs filtered by category page
- Category List Page
- Register Page
- Login Page
- Edit Profile Page
- Password Change page
- Show Profile Page
- Edit Profile Page
- Create profile page

### Installation

1. - Fork the [repo](https://github.com/pkini2002/DBlog-Application)
   - Clone the repo to your local system
   ```git
   git clone https://github.com/pkini2002/DBlog-Application.git
   cd DBlog-Application
   ```
   Make sure you have python installed on your system.
2. Create a Virtual Environment for the Project

   If u don't have a virtualenv installed

   ```bash
   pip install virtualenv
   ```
   **For Windows Users**
   `Initially when you clone the project run` 

   ```bash
   virtualenv env
   source env/Scripts/activate
   ```

   `For subsequent run of the project you can simply use`
   ```bash
   virtualenv env
   env/Scripts/activate
   ```

   **For Linux Users**
   ```bash
   virtualenv env
   source env/Scripts/activate
   ```

   If you are giving a different name than `env`, mention it in `.gitignore` first

3. Install all the requirements

   ```bash
   pip install -r requirements.txt
   ```

4. Make migrations/ Create db.sqlite3

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Create a super user.
   This is to access Admin panel and admin specific pages.

   ```djangotemplate
   python manage.py createsuperuser
   ```
   
   Enter your username, email and password.

6. Run server
   ```bash
   python manage.py runserver
   ```
   
### Snapshots

**Home Page**

![Home](https://user-images.githubusercontent.com/84091455/208229840-188ab65e-853f-46b3-83d2-79e6860f4b02.png)

**Article Detail Page**

![article details](https://user-images.githubusercontent.com/84091455/208229849-3089dcc4-612b-4eeb-97db-fdf71eabda5d.png)

**Blogs filtered by category page**

![category filtering](https://user-images.githubusercontent.com/84091455/208229845-e517838e-8c9a-42b7-9827-c0dd9e4bacaf.png)
