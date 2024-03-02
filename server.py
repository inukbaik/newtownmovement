from flask import Flask, render_template, request
from flask_mail import Mail, Message
import smtplib

app = Flask(__name__)
mail = Mail(app)

# Configuration of the email server
my_email = 'xxxi30cw@gmail.com'
my_password = 'xrhmggiljizxqilc'

@app.route('/')
@app.route('/index.html')
def main():
    return render_template('index.html')


@app.route('/cutting_project.html')
def about():
    return render_template('cutting_project.html')


@app.route('/denim_project.html')
def denim():
    return render_template('denim_project.html')


@app.route('/jersey_project.html')
def jersey():
    return render_template('jersey_project.html')


@app.route('/LVMH_sustainability_project.html')
def lvmh():
    return render_template('LVMH_sustainability_project.html')


@app.route('/send_email', methods=['POST'])
def send_email():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(my_email, my_password)
        smtp.sendmail(my_email,
                      'youngbean9808@gmail.com',
                      f'Subject: New message from your website\n\nName: {name}\nEmail: {email}\nMessage: {message}')

    return 'OK'


if __name__ == '__main__':
    app.run(debug=True)
