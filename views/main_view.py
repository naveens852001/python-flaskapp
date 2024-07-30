from flask import render_template, request, redirect, url_for, flash, jsonify
from flask.views import View, MethodView
from forms import CloudForm
from sqlalchemy.sql import func,text
from models import Cloud
from app import app ,db

# View/Render base.html
class BaseHtmlView(MethodView):
    def get(self):
        return render_template('base.html')

# View/Home Page Render
class HomepageHandler(View):
    def dispatch_request(self):
        count = db.session.query(func.count(Cloud.id)).scalar()
        return render_template('index.html', cloud_count=count)

# View/Search specific cloud details
class SearchView(MethodView):
    def get(self):
        return render_template('index.html', results=[])

    def post(self):
        name = request.form.get('cloudsearch')
        results = []
        if name:
            try:
                results = Cloud.query.filter_by(name=name).all()
            except Exception as e:
                print(f"Error: {e}")  # Debugging line
        return render_template('index.html', results=results)

# View/Update Cloud Details
class CloudDetailsUpdate(View):
    def dispatch_request(self):
        return render_template('updatecloud.html')

# View/Login-Logout Details
class Authentication(View):
    def dispatch_request(self):
        return render_template('updatecloud.html')

# View/Profile
class Profile(View):
    def dispatch_request(self):
        return render_template('profile.html')

# View/Total Cloud Registered
class TotalCloud(MethodView):
    def get(self):
        try:
            cloud_count = db.session.query(func.count(Cloud.id)).scalar()
        except Exception as e:
            cloud_count = None
        return render_template('index.html', cloud_count=cloud_count)

# View/Create Cloud Form Register
class CloudCreateHandler(View):
    methods = ['GET', 'POST']

    def dispatch_request(self):
        form = CloudForm()
        if request.method == 'POST':
            if form.validate_on_submit():
                existing_cloud = Cloud.query.filter_by(
                    name=form.name.data,
                    url=form.url.data
                ).first()
                if existing_cloud:
                    flash('Cloud entry already exists!', 'warning')
                    return redirect(url_for('home'))
                else:
                    new_cloud = Cloud(
                        name=form.name.data,
                        email=form.email.data,
                        cc_mail_ids=form.cc_mail_ids.data,
                        url=form.url.data,
                        datacenter_main=form.datacenter_main.data,
                        datacenters_remote=form.datacenters_remote.data,
                        role=form.role.data,
                        status=form.status.data,
                        sfdc_name=form.sfdc_name.data,
                        sfdc_id=form.sfdc_id.data,
                        private_device_licenses=form.private_device_licenses.data,
                        shared_devices_licenses=form.shared_devices_licenses.data,
                        browser_licenses=form.browser_licenses.data,
                        virtual_device_licenses=form.virtual_device_licenses.data,
                        cloud_build=form.cloud_build.data,
                        reporter_build=form.reporter_build.data,
                        nv_build=form.nv_build.data,
                        selenium_build=form.selenium_build.data,
                        phase=form.phase.data
                    )
                    db.session.add(new_cloud)
                    db.session.commit()
                    flash('Cloud entry successfully created!', 'success')
                    return redirect(url_for('home'))
            else:
                
                pass
        
        return render_template('cloud_form.html', form=form)

# View/Success redirection after form-submission
class SuccessReDirect(View):
    def dispatch_request(self):
        return render_template('success.html')

class TestConnectionView(MethodView):
    def get(self):
        try:
            # Use text() function to wrap the raw SQL query
            with app.app_context():
                db.session.execute(text('SELECT 1'))
            return jsonify(message='Database connection successful!'), 200
        except Exception as e:
            return jsonify(error=str(e)), 500

