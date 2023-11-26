import os
import uuid

from flask import Flask, render_template, flash, redirect, url_for, request, send_from_directory, session
from flask_ckeditor import CKEditor, upload_success, upload_fail
from flask_dropzone import Dropzone
from flask_wtf.csrf import validate_csrf
from wtforms import ValidationError

# from forms import LoginForm, FortyTwoForm, NewPostForm, UploadForm, MultiUploadForm, SigninForm, \
#    RegisterForm, SigninForm2, RegisterForm2, RichTextForm

from forms import LoginForm

app = Flask(__name__)

app.secret_key = 'secret_string'


@app.route('/')
def index():
    return '<H1>Test</H1>'


@app.route('/html')
def html():
    return render_template('pure_html.html')


@app.route('/basic')
def basic():
    form = LoginForm()
    return render_template('basic.html', form=form)


@app.route('/bootstrap', methods=['GET', 'POST'])
def bootstrap():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        flash('Welcome home, %s!' % username)
        return redirect(url_for('index'))
    return render_template('bootstrap.html', form=form)
