from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, URLField, SelectField, SelectMultipleField, SubmitField
from wtforms.validators import DataRequired, URL, Email

PHASE_CHOICES = [('','select a Phase'),(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')]
ROLE_CHOICES = [
    ('','select a Role'),
    ('public', 'public'),
    ('private', 'private'),
    ('demo', 'demo'),
    ('staging', 'staging'),
    ('offboarded', 'offboarded'),
    ('poc', 'poc')
]
DATACENTERS_CHOICES = [
    ('', 'Select a Datacenter'),
    ('US1', 'US1'),
    ('US2', 'US2'),
    ('SG', 'SG'),
    ('AU', 'AU'),
    ('DE', 'DE'),
    ('UK', 'UK'),
    ('IL', 'IL'),
    ('CA', 'CA'),
]
CLOUD_STATUS = [
    ('','select a Status '),
    ('Online', 'Online'),
    ('Offline', 'Offline'),
    ('Maintenance', 'Maintenance'),
]

class CloudForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(message='Name is required.')])
    email = StringField('Email', validators=[
        DataRequired(message='Email is required.'),
        Email(message='Invalid email address.')
    ])
    cc_mail_ids = StringField('CC Mail IDs', validators=[DataRequired(message='CC Mail IDs are required.')])
    url = StringField('URL', validators=[
        DataRequired(message='URL is required.'),
        URL(message='Invalid URL.')
    ])
    datacenter_main = SelectField('Datacenter Main', choices=DATACENTERS_CHOICES, validators=[DataRequired(message='Datacenter Main is required.')])
    datacenters_remote = SelectMultipleField('Datacenters Remote', choices=DATACENTERS_CHOICES, validators=[DataRequired(message='Datacenters Remote is required.')])
    role = SelectField('Role', choices=ROLE_CHOICES, validators=[DataRequired(message='Role is required.')])
    status = SelectField('Status', choices=CLOUD_STATUS, validators=[DataRequired(message='Status is required.')])
    sfdc_name = StringField('SFDC Name', validators=[DataRequired(message='SFDC Name is required.')])
    sfdc_id = StringField('SFDC ID', validators=[DataRequired(message='SFDC ID is required.')])
    private_device_licenses = StringField('Private Device Licenses', validators=[DataRequired(message='Private Device Licenses are required.')])
    shared_devices_licenses = StringField('Shared Devices Licenses', validators=[DataRequired(message='Shared Devices Licenses are required.')])
    browser_licenses = StringField('Browser Licenses', validators=[DataRequired(message='Browser Licenses are required.')])
    virtual_device_licenses = StringField('Virtual Device Licenses', validators=[DataRequired(message='Virtual Device Licenses are required.')])
    cloud_build = StringField('Cloud Build', validators=[DataRequired(message='Cloud Build is required.')])
    reporter_build = StringField('Reporter Build', validators=[DataRequired(message='Reporter Build is required.')])
    nv_build = StringField('NV Build', validators=[DataRequired(message='NV Build is required.')])
    selenium_build = StringField('Selenium Build', validators=[DataRequired(message='Selenium Build is required.')])
    phase = SelectField('Phase', choices=PHASE_CHOICES, validators=[DataRequired(message='Phase is required.')])
    submit = SubmitField('Submit')
