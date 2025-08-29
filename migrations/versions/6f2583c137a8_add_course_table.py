"""add course table

Revision ID: 6f2583c137a8
Revises: 2233205a8ecf
Create Date: 2025-08-29 14:40:32.261948

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6f2583c137a8'
down_revision: Union[str, None] = '2233205a8ecf'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Create courses table
    op.create_table(
        'courses',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('teacher_id', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['teacher_id'], ['teachers.id']),
        sa.PrimaryKeyConstraint('id')
    )

    # Create association table student_course
    op.create_table(
        'student_course',
        sa.Column('student_id', sa.Integer(), nullable=False),
        sa.Column('course_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['course_id'], ['courses.id']),
        sa.ForeignKeyConstraint(['student_id'], ['students.id']),
        sa.PrimaryKeyConstraint('student_id', 'course_id')
    )


def downgrade() -> None:
    # Drop association and course tables
    op.drop_table('student_course')
    op.drop_table('courses')
