from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/home')
def home():
    return render_template ('home.html')


@app.route('/about')
def about():
   return render_template('about.html') 
           
           
@app.route('/contact')
def home():
    return render_template('contact.html')


@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        
        name = request.form['name']  
        email = request.form['email']  
       
        return render_template('thankyou.html', name=name, email=email)
    return render_template('form.html')


@app.route('/thank_you')
def thank_you():
    return render_template('form.html')


#if __name__ == '__main__':
#   app.run(debug=True)