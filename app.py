# app.py
from flask import Flask, redirect, render_template, request, session, url_for
from psutil import users

app = Flask(__name__)

# Sample data for blog posts
blog_posts = [
    {"username": "JohnDoe", "date": "2023-12-01", "time": "14:30", "topic": "Python", "description": "Introduction to Python Programming."},
    {"username": "JaneSmith", "date": "2023-12-02", "time": "10:45", "topic": "Web Development", "description": "Building responsive websites with HTML, CSS, and JavaScript."},
]

# Sample data for projects
projects_data = [
    {"name": "Project 1", "description": "Description of Project 1"},
    {"name": "Project 2", "description": "Description of Project 2"},
]

# Social links
social_links = {
    "twitter": "https://twitter.com/your_twitter",
    "linkedin": "https://linkedin.com/in/your_linkedin",
    "github": "https://github.com/your_github",
}

# Image filenames
logo_filename = "images/Code Cafe Logo.png"  # Adjust the filename accordingly
coffee_mug_filename = "images/Code Cafe Logo.png"  # Adjust the filename accordingly

# Sample user data (replace with a database in a real application)
users = {
    'john_doe': {'password': 'password123'},
    'jane_smith': {'password': 'secret'},
}

@app.route('/')
def home():
    show_buttons = 'username' not in session
    return render_template('home.html', logo_filename=logo_filename, coffee_mug_filename=coffee_mug_filename, show_buttons=show_buttons)


@app.route('/signin', methods=['GET', 'POST'])
def signin():
    error_message = None  # Initialize error_message to None

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Check if the provided username exists and the password is correct
        if username in users and users[username]['password'] == password:
            # For simplicity, you can consider the user as signed in by setting a session variable
            # In a real application, use a proper user authentication system
            session['username'] = username
            return redirect(url_for('home'))

        # If the username or password is incorrect, show an error message
        error_message = 'Invalid username or password'

    return render_template('signin.html', error_message=error_message)

@app.route('/register', methods=['GET', 'POST'])
def register():
    # Add logic for handling registration form submission (to be implemented)
    if request.method == 'POST':
        # Retrieve username, email, and password from the form data
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        # Add your registration logic here (e.g., store user data in a database)

        # Assuming successful registration, set session variable and redirect to the user's profile
        session['username'] = username
        return redirect(url_for('profile'))

         

    return render_template('register.html')

@app.route('/projects')
def projects():
    return render_template('projects.html', projects=projects_data)

@app.route('/project_details/<project_name>')
def project_details(project_name):
    # Add logic to fetch project details based on the project_name
    # This could involve querying a database or fetching data from another source
    # For now, let's just display a simple message
    return f"Details for {project_name}"

@app.route('/blog')
def blog():
    return render_template('blog.html', posts=blog_posts)

@app.route('/blog_post_details/<post_date>/<post_topic>')
def blog_post_details(post_date, post_topic):
    # Add logic to fetch blog post details based on the post_date and post_topic
    # This could involve querying a database or fetching data from another source
    # For now, let's just display a simple message
    return f"Details for the blog post on {post_date} with the topic {post_topic}"

@app.route('/about')
def about():
    return render_template('about.html', social_links=social_links)

@app.route('/profile')
def profile():
    # Assume user data is fetched from a database
    user_data = {
        "username": "JohnDoe",
        "email": "john@example.com",
        "bio": "A passionate coder exploring the world of technology.",
    }
        # Check if the user is logged in
    if 'username' in session:
        return render_template('profile.html', user_data=user_data, show_logout=True)
    else:
        return redirect(url_for('signin'))
        # Add more fields as needed

    return render_template('profile.html', user_data=user_data)

@app.route('/edit_profile')
def edit_profile():
    # Logic for editing the profile (to be implemented)
    return "This is the page for editing the profile."

@app.route('/logout')
def logout():
    # Clear the session to log out the user
    session.pop('username', None)
    return redirect(url_for('home'))

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/forgot_password')
def forgot_password():
    # Implement the logic for the "Forgot Password" page
    return render_template('forgot_password.html')

@app.route('/register')
def register():
    # Implement the logic for the "Create an Account" page
    return render_template('register.html')

# Other routes...

if __name__ == '__main__':
    app.run(debug=True)
