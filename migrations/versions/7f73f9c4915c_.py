"""empty message

Revision ID: 7f73f9c4915c
Revises: f35797c538c5
Create Date: 2023-10-31 06:19:18.803089

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '7f73f9c4915c'
down_revision = 'f35797c538c5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('student_information', schema=None) as batch_op:
        batch_op.drop_column('college_id')
        batch_op.drop_column('course_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('student_information', schema=None) as batch_op:
        batch_op.add_column(sa.Column('course_id', mysql.INTEGER(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('college_id', mysql.INTEGER(), autoincrement=False, nullable=True))

    # ### end Alembic commands ###