
from app import db

class Cloud(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(24), nullable=False)
    email = db.Column(db.String(120), nullable=True)
    cc_mail_ids = db.Column(db.String(1024), nullable=True)
    url = db.Column(db.String(200), nullable=True)
    datacenter_main = db.Column(db.String(8), default='None', nullable=False)
    datacenters_remote = db.Column(db.ARRAY(db.String), nullable=True) 
    role = db.Column(db.String(10), default='private', nullable=True)
    status = db.Column(db.String(20), default='Online', nullable=True)
    sfdc_name = db.Column(db.String(256), nullable=True)
    sfdc_id = db.Column(db.String(256), nullable=True)
    private_device_licenses = db.Column(db.Integer, default=0, nullable=False)
    shared_devices_licenses = db.Column(db.Integer, default=0, nullable=False)
    browser_licenses = db.Column(db.Integer, default=0, nullable=False)
    virtual_device_licenses = db.Column(db.Integer, default=0, nullable=False)
    cloud_build = db.Column(db.String(10), default="0.0", nullable=True)
    reporter_build = db.Column(db.String(10), default="0.0", nullable=True)
    nv_build = db.Column(db.String(10), default="0.0", nullable=True)
    selenium_build = db.Column(db.String(10), default="0.0", nullable=True)
    phase = db.Column(db.SmallInteger, nullable=True)
