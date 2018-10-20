from flask import render_template
from flask_login import login_required

from . import admin


@admin.route('/admin/pemiluraya/')
def homepage():

    return render_template('admin/index.html', title = "Welcome")



@admin.route('/admin/dashboard/')
def dashboard()

    return render_template('admin/dashboard.html', title = "Admin Dashboard")