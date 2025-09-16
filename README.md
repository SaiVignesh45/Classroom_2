# Project Name: EduConnect (Educational Messaging & Assignments Platform)

## Overview

Hey everyone! We're super excited to share our new educational project called EduConnect. It's basically a messaging system between teachers and students with some assignment features 
thrown in for good measure. So far, we've managed to get the login working and assignments being saved.

We know this is still very much in development mode right now – just enough functionality to show how cool it could be once finished. Our main goal was to create a proof-of-concept 
that demonstrates what EduConnect could become with proper planning!

## Current Features

### Login System
```
@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username]['password'] == password:
            session['username'] = username  
            flash('Logged in successfully!')
            return redirect(url_for('dashboard', username=username))
        else:
            flash('Invalid username or password!')
    return render_template('login.html')
```

### Dashboard View
```
@app.route('/dashboard/<username>')
def dashboard(username):
    user = users.get(username)
    if user:
        return render_template('dashboard.html', user=user)
    else:
        flash('Invalid user or user not logged in!')
        return redirect(url_for('login'))
```

### Assignment Creation
```
@app.route('/create_assignment', methods=['GET', 'POST'])
def create_assignment():
    if request.method == 'POST':
        
        name = request.form['name']
        description = request.form['description']
        due_date = request.form['due_date']
        save_assignment(name, description, due_date)
        flash('Assignment created successfully')
        return redirect(url_for('view_assignments'))
    return render_template('create_assignment.html')
```

### Assignment Viewing
```
@app.route('/view_assignments')
def view_assignments():
    
    assignments = load_assignments()
    return render_template('view_assignments.html', assignments=assignments)
```

## Implementation Details

For storage, we're currently saving users in a dictionary and using JSON files for messages and assignments. We have two folders:
- `templates/` contains our HTML files
- `static/` holds any CSS or JS files (though not much there yet)

The assignment functionality is pretty basic right now – it just saves the assignment data to separate JSON files.

## Room for Growth

We've got so many ideas for this project, but we're still figuring out how to properly organize everything. Here are some of our big plans:

### Core Functionality
1. Add user registration instead of hardcoded users
2. Implement proper message sending and receiving system
3. Create a way to view past assignments

### UI/UX Improvements
We need to redesign the dashboard page completely! It's currently just showing one assignment block per line, which isn't very efficient.

Also, we haven't implemented any search functionality yet – that would be awesome for finding specific messages or assignments!

### Security Enhancements
Oh man, this is a big one. We're using plaintext passwords right now because we didn't know about hashing and salting back then. We also need to fix session management completely.

### Architecture Improvements
We should break up the code into separate modules – currently everything's in one file which makes it hard to manage as our project grows.

## Getting Started

To run this application, you'll need:

1. Python installed on your computer (we used version 3.x)
2. Flask framework set up
3. Basic knowledge of how web applications work

The current code is just scratching the surface but demonstrates some core functionality patterns that could be expanded upon once we have a better architecture in place.

---

# Later Update - From Our Current Experienced Perspective

> *[This section written much later]*

Wow, looking back at our initial README for this project feels like reading something from another person! Back then when we were just starting out with Flask and web development, we 
didn't realize how many technical debt problems we'd be creating.

Here's what we wish we had known better:

## Security Issues
We completely overlooked security concerns. The current password storage is insecure (we used plaintext!), session management needs serious work, and our authentication system lacks 
proper hashing algorithms.

## Architecture Problems
Our monolithic approach to the application design will cause maintenance nightmares as it grows. We really should have broken this up into microservices or at least organized by 
functionality from the beginning.

## Scalability Concerns
The JSON storage solution is fundamentally flawed for anything beyond a simple demo project. We need proper database integration with SQLAlchemy and SQLite support.

## User Experience Flaws
Our initial design choices were purely functional – we didn't think about usability enough. The dashboard layout needs restructuring, there should be better navigation between pages, 
and the overall aesthetic could use some work!

But hey, at least we knew to document these limitations for future reference. We're looking forward to properly revisiting this project once we've gained more experience with Flask 
development and best practices!
