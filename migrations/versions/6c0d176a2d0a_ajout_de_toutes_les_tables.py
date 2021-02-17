"""ajout de toutes les tables

Revision ID: 6c0d176a2d0a
Revises: bd0e579cc72d
Create Date: 2021-02-17 23:27:31.486821

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6c0d176a2d0a'
down_revision = 'bd0e579cc72d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('flux_information',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('titre', sa.String(length=100), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('adresse_site_web', sa.String(length=255), nullable=True),
    sa.Column('url_publications', sa.String(length=255), nullable=True),
    sa.Column('langue', sa.String(length=8), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('amitie',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date_demande', sa.DateTime(), nullable=True),
    sa.Column('statut', sa.Boolean(), nullable=True),
    sa.Column('destinataire_id', sa.Integer(), nullable=True),
    sa.Column('utilisateur_id', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['destinataire_id'], ['utilisateur.id'], ),
    sa.ForeignKeyConstraint(['utilisateur_id'], ['utilisateur.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('publication',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('titre', sa.String(length=100), nullable=False),
    sa.Column('lien_publication', sa.String(length=255), nullable=True),
    sa.Column('date_timestamp', sa.DateTime(), nullable=True),
    sa.Column('date_publication', sa.DateTime(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('flux_id', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['flux_id'], ['flux_information.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('souscription',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date_souscription', sa.DateTime(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('utilisateur_id', sa.Integer(), nullable=True),
    sa.Column('flux_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['flux_id'], ['flux_information.id'], ),
    sa.ForeignKeyConstraint(['utilisateur_id'], ['utilisateur.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('commentaire',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date_commentaire', sa.DateTime(), nullable=True),
    sa.Column('commentaire', sa.Text(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('utilisateur_id', sa.Integer(), nullable=True),
    sa.Column('publication_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['publication_id'], ['publication.id'], ),
    sa.ForeignKeyConstraint(['utilisateur_id'], ['utilisateur.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('lecture_publication',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date_lecture', sa.DateTime(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('utilisateur_id', sa.Integer(), nullable=True),
    sa.Column('publication_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['publication_id'], ['publication.id'], ),
    sa.ForeignKeyConstraint(['utilisateur_id'], ['utilisateur.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('partage',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date_partage', sa.DateTime(), nullable=True),
    sa.Column('commentaire', sa.Text(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('utilisateur_id', sa.Integer(), nullable=True),
    sa.Column('publication_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['publication_id'], ['publication.id'], ),
    sa.ForeignKeyConstraint(['utilisateur_id'], ['utilisateur.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('partage')
    op.drop_table('lecture_publication')
    op.drop_table('commentaire')
    op.drop_table('souscription')
    op.drop_table('publication')
    op.drop_table('amitie')
    op.drop_table('flux_information')
    # ### end Alembic commands ###
