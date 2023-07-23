"""v1 add company to users table

Revision ID: abf1ea121462
Revises: bb9cc9011955
Create Date: 2023-07-24 02:44:25.917883

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'abf1ea121462'
down_revision = 'bb9cc9011955'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('company', sa.String(), nullable=True))
    op.create_index(op.f('ix_users_company'), 'users', ['company'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_company'), table_name='users')
    op.drop_column('users', 'company')
    # ### end Alembic commands ###