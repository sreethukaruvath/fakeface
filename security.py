from flask import *
from database import *
import uuid
from core import *
from facedetection import *
from face_recognition_liveness_app import *


security=Blueprint('security',__name__)


@security.route('/securityhome')
def securityhome():
	return render_template("securityhome.html")


@security.route('/securityviewevent')
def securityviewevent():
	data={}
	q="select * from event"
	res=select(q)
	data['event']=res

	return render_template('securityviewevent.html',data=data)


@security.route('/checkface')
def checkface():
	eid=request.args['eid']
	out=startChecking()
	print("2D result: ................................................................",out)
	if out['status'] == "real":
		spoofingtest=start3DSpoofing()
		print(f"3D result .....................................{spoofingtest}")
		if spoofingtest == "fake":
			flash("Fake Face detected!")
			return redirect(url_for('security.securityhome'))
		else:
			s=vallogin()
			print("valuee..........",s)
			if s['stat'] == "No face detected, Try register again...":
				q="insert into request values(null,'%s',curdate(),'%s','pending')"%(eid,out['path'])
				insert(q)
				flash(s['stat'])
				return redirect(url_for('security.add_unknown'))
			else:
				pid=s['id']
				flash("Verification Completed.")
				return redirect(url_for('security.view_verified_participant',pid=pid))
	else:
		flash("Fake person.")
		return redirect(url_for('security.add_unknown')) 
	return render_template("securityhome.html")


@security.route('/add_unknown',methods=['get','post'])
def add_unknown():
	if 'submit' in request.form:
		fname =request.form['fname']
		lname= request.form['lname']
		place =request.form['place']
		gender= request.form['gender']
		# image =request.files['image']
		# path="static/uploads/"+str(uuid.uuid4())+image.filename
		# image.save(path)
		s=partLogin()
		if s == "No face detected, Try register again...":
			q="insert into participant values(null,'%s','%s','%s','%s','pending','pending')"%(fname,lname,place,gender)
			id=insert(q)
			path=captures(id)
			q="update participant set image='%s' where participant_id='%s'"%(path,uid)
			update(q)
			enf("static/trainimages/")
			flash("Registration Completed")
			return redirect(url_for('security.securityhome'))
		else:
			flash("This Participant is already registered...!")
			return redirect(url_for('security.add_unknown'))

		
		

	return render_template('add_unknown.html')


@security.route('/view_verified_participant')
def view_verified_participant():
	data={}
	pid=request.args['pid']
	q="select * from participant where participant_id='%s'"%(pid)
	data['user']=select(q)
	return render_template('view_verified_participant.html',data=data)

@security.route('/view_userdetail')
def view_userdetail():
	data={}
	q="select * from user"
	data['user']=select(q)
	return render_template('view_userdetail.html',data=data)