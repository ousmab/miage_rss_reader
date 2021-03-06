"""initial migration

Revision ID: bd0e579cc72d
Revises: 
Create Date: 2021-02-17 21:10:33.070984

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bd0e579cc72d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('utilisateur',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('surnom', sa.String(length=80), nullable=True),
    sa.Column('ville', sa.String(length=80), nullable=True),
    sa.Column('pays', sa.String(length=80), nullable=True),
    sa.Column('avatar', sa.String(length=80), nullable=True),
    sa.Column('biographie', sa.String(length=80), nullable=True),
    sa.Column('mot_de_passe', sa.String(length=80), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('utilisateur')
    # ### end Alembic commands ###
