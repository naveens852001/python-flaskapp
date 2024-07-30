# from flask import Blueprint,jsonify,request
# from sqlalchemy.sql import func
# from models import Cloud
# from app import db
# from app import app
# from sqlalchemy import text




# cloud_bp=Blueprint('cloud',__name__)

# @app.route('/api/cloud-count', methods=['GET'])
# def get_cloud_count():
#     try:
#         count = db.session.query(func.count(Cloud.id)).scalar()
#         return jsonify({'count': count})
#         return jsonify({'error': str(e)}), 500
#     except Exception as e:

