"""Initial migration

Revision ID: db4c1b52d73e
Revises: 
Create Date: 2024-07-30 18:02:13.074282

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'db4c1b52d73e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cloud',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=24), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('cc_mail_ids', sa.String(length=1024), nullable=True),
    sa.Column('url', sa.String(length=200), nullable=True),
    sa.Column('datacenter_main', sa.String(length=8), nullable=False),
    sa.Column('datacenters_remote', sa.ARRAY(sa.String()), nullable=True),
    sa.Column('role', sa.String(length=10), nullable=True),
    sa.Column('status', sa.String(length=20), nullable=True),
    sa.Column('sfdc_name', sa.String(length=256), nullable=True),
    sa.Column('sfdc_id', sa.String(length=256), nullable=True),
    sa.Column('private_device_licenses', sa.Integer(), nullable=False),
    sa.Column('shared_devices_licenses', sa.Integer(), nullable=False),
    sa.Column('browser_licenses', sa.Integer(), nullable=False),
    sa.Column('virtual_device_licenses', sa.Integer(), nullable=False),
    sa.Column('cloud_build', sa.String(length=10), nullable=True),
    sa.Column('reporter_build', sa.String(length=10), nullable=True),
    sa.Column('nv_build', sa.String(length=10), nullable=True),
    sa.Column('selenium_build', sa.String(length=10), nullable=True),
    sa.Column('phase', sa.SmallInteger(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cloud')
    # ### end Alembic commands ###
