"""add review table

Revision ID: 75a32bfaa26d
Revises: cf56974258c0
Create Date: 2023-10-30 22:32:53.599783

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '75a32bfaa26d'
down_revision = 'cf56974258c0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('reviews',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('review', sa.String(), nullable=True),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('carts')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('carts',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('product_name', sa.VARCHAR(), nullable=True),
    sa.Column('price', sa.INTEGER(), nullable=True),
    sa.Column('product_id', sa.INTEGER(), nullable=True),
    sa.Column('user_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('reviews')
    # ### end Alembic commands ###
