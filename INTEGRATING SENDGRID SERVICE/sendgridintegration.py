# importing libraries from flask import Flask

from flask_mail import Mail, Message app = Flask(name )
mail = Mail(app) # instantiate the mail class # configuration of mail
app.config['MAlL_SERVER'] = ‘smtp.gmail.com’ app.congig[‘MAIL_PORT’]=465
app.config[‘MAIL_USERNAME’]='yourld@gmail.com’
app.config[‘MAIL_PASSWROD’]= ‘*****’app.config[‘MAIL_USE_TLS’]=False
app.config[‘MAIL_USE_SSL’]= True
mail = Mail(app)
# message object mapped to a particular URL '/'
@app.route("/") def index():
msg = Message(
'Hello’,
sender ='yourld@gmail.com',
recipients = ['receiver'sid@gmail.com']
}
msg.body = 'Hello Flask message sent from Flask-Mail' mail.send(msg)
return 'Sent'
if name == ' main ': app.run(debug = True)
