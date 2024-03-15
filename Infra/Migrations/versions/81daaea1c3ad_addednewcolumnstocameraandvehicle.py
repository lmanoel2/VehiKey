"""AddedNewColumnsToCameraAndVehicle

Revision ID: 81daaea1c3ad
Revises: 776875aa9a7d
Create Date: 2024-03-14 21:03:12.054780

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = '81daaea1c3ad'
down_revision: Union[str, None] = '776875aa9a7d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('camera', sa.Column('name', sa.String(length=30), nullable=False))
    op.add_column('camera', sa.Column('access_time', sa.String(length=500), nullable=True))
    op.drop_column('camera', 'updated_at')
    op.add_column('vehicle', sa.Column('valid_time', sa.String(length=50), nullable=True))
    op.add_column('vehicle', sa.Column('access_time', sa.String(length=500), nullable=True))
    op.add_column('vehicle', sa.Column('number_access', sa.Integer(), nullable=True))
    op.drop_column('vehicle', 'updated_at')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('vehicle', sa.Column('updated_at', mysql.DATETIME(), nullable=True))
    op.drop_column('vehicle', 'number_access')
    op.drop_column('vehicle', 'access_time')
    op.drop_column('vehicle', 'valid_time')
    op.add_column('camera', sa.Column('updated_at', mysql.DATETIME(), nullable=True))
    op.drop_column('camera', 'access_time')
    op.drop_column('camera', 'name')
    # ### end Alembic commands ###