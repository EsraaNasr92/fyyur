"""empty message

Revision ID: 7999f0b38bf9
Revises: f216f4adbe1c
Create Date: 2020-02-29 18:23:07.585522

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7999f0b38bf9'
down_revision = 'f216f4adbe1c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Artist', 'genres')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Artist', sa.Column('genres', sa.VARCHAR(length=120), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
