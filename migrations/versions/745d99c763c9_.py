"""empty message

Revision ID: 745d99c763c9
Revises: 7999f0b38bf9
Create Date: 2020-02-29 18:23:19.738533

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '745d99c763c9'
down_revision = '7999f0b38bf9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Artist', sa.Column('genres', sa.ARRAY(sa.String()), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Artist', 'genres')
    # ### end Alembic commands ###