from flask import *
from database import *
import uuid


admin=Blueprint('admin',__name__)


@admin.route('/adminhome')
def adminhome():
	return render_template("adminhome.html")


@admin.route('/viewuser')
def viewuser():
	data={}
	q="select * from user inner join event using(user_id)"
	res=select(q)
	data['user']=res

	return render_template('adminviewuser.html',data=data)

@admin.route('/viewsecurity')
def viewsecurity():
	data={}
	q="select * from security"
	res=select(q)
	data['security']=res

	return render_template('adminviewsecurity.html',data=data)




