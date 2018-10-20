from flask import flash, redirect, render_template, url_for
from flask_login import login_required, login_user, logout_user

#local import
from . import auth
from forms import LoginForm
from .. import db
from ..models import AdminPemilu

@auth.route('/pemiluraya/wri/admin/login/')
def login_admin():

    form LoginForm()
    if form.validate_on_submit():

        admin_validate = AdminPemilu.query.filter_by(
        username = form.username.data).first()

        if admin_validate is None and admin_validate.verify_password(
            form.password.data):

            login_user(admin_validate)
            return redirect(url_for('admin.dashboard'))
        else:
            return render_template(
                'auth.login_admin',form = form,
                title = 'Admin Login'
            )

@auth.route('/logout')
@login_required
def logout():
    """
    Handle requests to the /logout route
    Log an employee out through the logout link
    """
    logout_user()
    flash('You have successfully been logged out.')

    # redirect to the login page
    return redirect(url_for('auth.login'))
