from flask import Flask, render_template, request, redirect, url_for, flash, session
import os
import json

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

users = {
    'teacher': {'username': 't@a.com', 'password': 'tss', 'role': 'teacher'},
    'student': {'username': 's@b.com', 'password': 'spass', 'role': 'student'}
}

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

@app.route('/dashboard/<username>')


@app.route('/dashboard/<username>')
def dashboard(username):
    user = users.get(username)
    if user:
        return render_template('dashboard.html', user=user)
    else:
        flash('Invalid user or user not logged in!')
        return redirect(url_for('login'))

@app.route('/message_form', methods=['GET', 'POST'])
def message_form():
    if request.method == 'POST':
        recipient = request.form['recipient']
        content = request.form['content']
        sender = session['username']
        save_message(sender, recipient, content)
        flash('Message sent successfully!')
        return redirect(url_for('dashboard', username=session['username']))
    return render_template('message_form.html')

def save_message(sender, recipient, content):
    message = {
        'sender': sender,
        'recipient': recipient,
        'content': content
    }
    with open('messages.json', 'a') as f:
        json.dump(message, f)
        f.write('\n')

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

@app.route('/view_assignments')
def view_assignments():
    
    assignments = load_assignments()
    return render_template('view_assignments.html', assignments=assignments)

def save_assignment(name, description, due_date):
    if not os.path.exists('assignments'):
        os.makedirs('assignments')
    assignment = {
        'name': name,
        'description': description,
        'due_date': due_date
    }
    assignment_id = len(os.listdir('assignments')) + 1
    filename = os.path.join('assignments', f'assignment_{assignment_id}.json')
    with open(filename, 'w') as f:
        json.dump(assignment, f)

def load_assignments():
    assignments = []
    if os.path.exists('assignments'):
        files = os.listdir('assignments')
        for file in files:
            with open(os.path.join('assignments', file), 'r') as f:
                assignment = json.load(f)
                assignments.append(assignment)
    return assignments

@app.route('/answer_assignment')
def answer_assignment():
    
    return render_template('answer_assignment.html')

if __name__ == '__main__':
    app.run(debug=True)
