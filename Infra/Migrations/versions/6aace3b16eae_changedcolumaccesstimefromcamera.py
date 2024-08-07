"""ChangedColumAccessTimeFromCamera

Revision ID: 6aace3b16eae
Revises: 6a3bef110e08
Create Date: 2024-03-20 18:51:48.970114

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = '6aace3b16eae'
down_revision: Union[str, None] = '6a3bef110e08'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('camera', sa.Column('valid_time', sa.String(length=50), nullable=True))
    op.drop_column('camera', 'access_time')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('camera', sa.Column('access_time', mysql.VARCHAR(length=500), nullable=True))
    op.drop_column('camera', 'valid_time')
    # ### end Alembic commands ###
