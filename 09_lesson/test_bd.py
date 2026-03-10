import pytest
import random
from sqlalchemy import create_engine, text

DB_URL = "postgresql://serov:123456@localhost:5432/postgres"

engine = create_engine(DB_URL)


@pytest.fixture
def db():
    connection = engine.connect()
    yield connection
    connection.close()


def test_add_student(db):
    """Тест добавления студента"""

    user_id = random.randint(100000, 999999)

    db.execute(
        text("""
        INSERT INTO student (user_id, level, education_form, subject_id)
        VALUES (:user_id, :level, :education_form, :subject_id)
        """),
        {
            "user_id": user_id,
            "level": "Beginner",
            "education_form": "personal",
            "subject_id": 1
        }
    )

    result = db.execute(
        text("SELECT * FROM student WHERE user_id=:user_id"),
        {"user_id": user_id}
    ).mappings().all()

    assert len(result) == 1

    # очистка
    db.execute(
        text("DELETE FROM student WHERE user_id=:user_id"),
        {"user_id": user_id}
    )


def test_update_student_level(db):
    """Тест изменения уровня студента"""

    user_id = random.randint(100000, 999999)

    db.execute(
        text("""
        INSERT INTO student (user_id, level, education_form, subject_id)
        VALUES (:user_id, :level, :education_form, :subject_id)
        """),
        {
            "user_id": user_id,
            "level": "Beginner",
            "education_form": "personal",
            "subject_id": 1
        }
    )

    db.execute(
        text("""
        UPDATE student
        SET level='Advanced'
        WHERE user_id=:user_id
        """),
        {"user_id": user_id}
    )

    result = db.execute(
        text("SELECT level FROM student WHERE user_id=:user_id"),
        {"user_id": user_id}
    ).scalar()

    assert result == "Advanced"

    # очистка
    db.execute(
        text("DELETE FROM student WHERE user_id=:user_id"),
        {"user_id": user_id}
    )


def test_delete_student(db):
    """Тест удаления студента"""

    user_id = random.randint(100000, 999999)

    db.execute(
        text("""
        INSERT INTO student (user_id, level, education_form, subject_id)
        VALUES (:user_id, :level, :education_form, :subject_id)
        """),
        {
            "user_id": user_id,
            "level": "Elementary",
            "education_form": "personal",
            "subject_id": 1
        }
    )

    db.execute(
        text("DELETE FROM student WHERE user_id=:user_id"),
        {"user_id": user_id}
    )

    result = db.execute(
        text("SELECT * FROM student WHERE user_id=:user_id"),
        {"user_id": user_id}
    ).fetchall()

    assert len(result) == 0