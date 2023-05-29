from flask import Flask 
from public import public
from admin import admin
from user import user
from security import security

 
app=Flask(__name__)
app.secret_key="hello"
app.register_blueprint(admin)
app.register_blueprint(public)
app.register_blueprint(user)
app.register_blueprint(security)

app.run(debug=True,port=5003)
