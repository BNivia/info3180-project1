"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""
import os
from app import app,db
from flask import render_template, request, redirect, url_for,flash, session, abort, send_from_directory
from werkzeug.utils import secure_filename
from app.models import Properties
from .forms import NewProperty


###
# Helpers
###
def get_uploaded_images():
    flist = []
    for subdir,dirs,files in os.walk(os.path.join(app.config['UPLOAD_FOLDER'])):
        for file in files:
            flist.append(file)
    return flist
###


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")

@app.route('/propertyy', methods=['POST','GET'])
def propertyy():
    form = NewProperty()
    if (request.method == 'POST'):
        if (form.validate_on_submit()):
            img = form.img.data
            filename = secure_filename(img.filename)
            img.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            db.session.add(Properties(form.title.data, form.description.data, form.beds.data, form.baths.data, form.location.data, form.price.data, form.ptype.data,filename))
            db.session.commit()
            flash('Property added!', 'success')
            return redirect(url_for('properties'))
        else:
            flash_errors(form)
    return render_template('propertyy.html',form=form)

@app.route('/properties')
def properties():
    prop = Properties.query.all()
    return render_template('properties.html', prop=prop)

@app.route('/propertyy/<pid>')
def getProperty(pid):
    result = Properties.query.filter_by(pid=pid).first()
    return render_template('iproperty.html', result=result)

@app.route('/uploads/<filename>')
def get_image(filename):
    rootdir = os.getcwd()
    return  send_from_directory(os.path.join(rootdir,app.config['UPLOAD_FOLDER']),filename)

###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
