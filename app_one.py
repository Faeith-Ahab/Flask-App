# Import the libraries

from flask import Flask, render_template, redirect, url_for, request


# Create an instance

app = Flask(__name__)

# Create routes

@app.route('/')
def index():
    return render_template ('index.html')


@app.route('/about')
def about():
   return render_template('about.html') 
           
           
@app.route('/contact')
def home():
    return render_template('contact.html')


# Route that allows for submitting information

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        
        name = request.form.get['name']  
        email = request.form.get['email']  
       
        return render_template('thanksmsg.html', name=name, email=email)
    return render_template('form.html')


@app.route('/thanksmsg')
def thanksmsg():
    return render_template('form.html')

# Debug mode
if __name__ == '__main__':
   app.run(debug=True)