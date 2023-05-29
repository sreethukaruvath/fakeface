from flask import*
from database import *
from capture import *
from facedetection import *
from model_manager import *

import uuid

public=Blueprint('public',__name__)

@public.route('/')
def home():
    return render_template("home.html")

@public.route('/login',methods=['get','post'])
def login():
    if 'login' in request.form:
        email =request.form['email']
        password= request.form['password']
        q="select * from login where username='%s' and password='%s'"%(email,password)
        res=select(q)

        if res:
            session['login_id']=res[0]['login_id']
            if res[0]['usertype']=='admin':
                return redirect(url_for('admin.adminhome'))
            if res[0]['usertype']=='user':
                q="select * from user where login_id='%s'"%(session['login_id'])
                res=select(q)
                if res:
                    session['uid']=res[0]['user_id']
                return redirect(url_for('user.userhome'))
            if res[0]['usertype']=='security':
                q="select * from security where login_id='%s'"%(session['login_id'])
                res=select(q)
                if res:
                    session['sid']=res[0]['security_id']
                return redirect(url_for('security.securityhome'))
    return render_template("login.html")
       

@public.route('/reg',methods=['get','post'])
def reg():
    if 'submit' in request.form:
        fname =request.form['fname']
        lname= request.form['lname']
        password= request.form['password']
        cpassword= request.form['cpassword']
        place =request.form['place']
        # gender= request.form['gender']
        # dob =request.form['dob']
        phone= request.form['phone']
        email =request.form['email']
        # image =request.files['image']
        # path="static/uploads/"+str(uuid.uuid4())+image.filename
        # image.save(path)

        if password==cpassword:
            q="insert into login values(null,'%s','%s','user')"%(email,password)
            id=insert(q)
            q="insert into user values(null,'%s','%s','%s','%s','%s','%s','pending')"%(id,fname,lname,place,phone,email)   
            uid=insert(q)
            path=captures(id)
            q="update user set image='%s' where user_id='%s'"%(path,uid)
            update(q)
            enf("static/trainimages/")
            return redirect(url_for("public.login"))
        else:
            flash("password Mismatch")
        # print(fname,lname,password,cpassword,place,gender,dob,phone,email,image)
    return render_template("reg.html")

@public.route('/forgot',methods=['get','post'])
def forgot():
    return render_template("forgot.html")

@public.route('/securitypage',methods=['get','post'])
def security():
    if 'submit' in request.form:
        fname =request.form['fname']
        lname= request.form['lname']
        password= request.form['password']
        cpassword= request.form['cpassword']
        # place= request.form['place']
        phone= request.form['phone']
        email =request.form['email']


    
        if password==cpassword:
            q="insert into login values(null,'%s','%s','security')"%(email,password)
            id=insert(q)
            q="insert into security values(null,'0','%s','%s','%s','%s','%s')"%(fname,lname,phone,email,id)   
            insert(q)
            return redirect(url_for("public.login"))
        else:
            flash("password dismatch")
    return render_template("securityregistration.html")