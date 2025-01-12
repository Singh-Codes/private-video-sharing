import os
from flask import Blueprint, render_template, request, current_app, send_from_directory, abort, flash, redirect, url_for
from flask_login import login_required, current_user
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField
from wtforms.validators import DataRequired
from werkzeug.utils import secure_filename
from app import db
from app.models import File, FileAccess
import uuid

files = Blueprint('files', __name__)

class UploadForm(FlaskForm):
    file = FileField('File', validators=[
        FileRequired(),
        FileAllowed(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'mp4', 'avi', 'mov'], 
                   'Please upload an allowed file type.')
    ])

class KeyForm(FlaskForm):
    key = StringField('Key', validators=[DataRequired()])

@files.route('/upload', methods=['GET', 'POST'])
@login_required
def upload_file():
    form = UploadForm()
    if form.validate_on_submit():
        file = form.file.data
        if file:
            filename = secure_filename(file.filename)
            # Generate unique filename
            unique_filename = f"{uuid.uuid4().hex}_{filename}"
            
            # Save file
            file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], unique_filename))
            
            # Create file record
            new_file = File(
                filename=unique_filename,
                original_filename=filename,
                file_type=file.content_type,
                file_size=os.path.getsize(os.path.join(current_app.config['UPLOAD_FOLDER'], unique_filename)),
                private_key=File.generate_private_key(),
                user_id=current_user.id
            )
            
            db.session.add(new_file)
            db.session.commit()
            
            flash(f'File uploaded successfully. Private key: {new_file.private_key}', 'success')
            return redirect(url_for('files.file_list'))
        
    return render_template('files/upload.html', title='Upload File', form=form)

@files.route('/files')
@login_required
def file_list():
    user_files = File.query.filter_by(user_id=current_user.id).all()
    return render_template('files/list.html', files=user_files)

@files.route('/access/<private_key>')
def access_file(private_key):
    file = File.query.filter_by(private_key=private_key).first_or_404()
    
    # Log access attempt
    access_log = FileAccess(
        file_id=file.id,
        ip_address=request.remote_addr,
        user_agent=request.user_agent.string,
        successful=True
    )
    db.session.add(access_log)
    
    # Update access count
    file.access_count += 1
    db.session.commit()
    
    return send_from_directory(
        current_app.config['UPLOAD_FOLDER'],
        file.filename,
        as_attachment=True,
        download_name=file.original_filename
    )

@files.route('/share/<file_id>')
def share_file(file_id):
    return render_template('files/share.html', file_id=file_id)

@files.route('/view/<file_id>', methods=['GET', 'POST'])
def view_file(file_id):
    form = KeyForm()
    if form.validate_on_submit():
        key = form.key.data
        file = File.query.filter_by(id=file_id, private_key=key).first()
        
        if file:
            # Log access attempt
            access_log = FileAccess(
                file_id=file.id,
                ip_address=request.remote_addr,
                user_agent=request.user_agent.string,
                successful=True
            )
            db.session.add(access_log)
            
            # Update access count
            file.access_count += 1
            db.session.commit()
            
            return send_from_directory(
                current_app.config['UPLOAD_FOLDER'],
                file.filename,
                as_attachment=True,
                download_name=file.original_filename
            )
        else:
            flash('Invalid key', 'error')
            
    return render_template('files/view.html', file_id=file_id, form=form)
