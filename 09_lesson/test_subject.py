from sqlalchemy import text

TEST_TITLE = "Test Subject"


def _cleanup(conn, subject_id=None, title=TEST_TITLE):
    if subject_id is not None:
        conn.execute(text("DELETE FROM subject WHERE subject_id = :id"), {"id": subject_id})
    else:
        conn.execute(text("DELETE FROM subject WHERE subject_title = :title"), {"title": title})
    conn.commit()


def test_insert_subject(db_connection):
    conn = db_connection

    conn.execute(
        text("INSERT INTO subject (subject_title) VALUES (:title)"),
        {"title": TEST_TITLE},
    )
    conn.commit()

    result = conn.execute(
        text("SELECT subject_title FROM subject WHERE subject_title = :title"),
        {"title": TEST_TITLE},
    )
    assert result.scalar() == TEST_TITLE

    _cleanup(conn)


def test_update_subject(db_connection):
    conn = db_connection

    conn.execute(
        text("INSERT INTO subject (subject_title) VALUES (:title)"),
        {"title": TEST_TITLE},
    )
    conn.commit()

    new_title = "Updated Subject"
    conn.execute(
        text("UPDATE subject SET subject_title = :new_title WHERE subject_title = :old_title"),
        {"old_title": TEST_TITLE, "new_title": new_title},
    )
    conn.commit()

    result = conn.execute(
        text("SELECT subject_title FROM subject WHERE subject_title = :title"),
        {"title": new_title},
    )
    assert result.scalar() == new_title

    result = conn.execute(
        text("SELECT subject_title FROM subject WHERE subject_title = :title"),
        {"title": TEST_TITLE},
    )
    assert result.scalar() is None

    conn.execute(
        text("DELETE FROM subject WHERE subject_title = :title"),
        {"title": new_title},
    )
    conn.commit()


def test_delete_subject(db_connection):
    conn = db_connection

    conn.execute(
        text("INSERT INTO subject (subject_title) VALUES (:title)"),
        {"title": TEST_TITLE},
    )
    conn.commit()

    result = conn.execute(
        text("SELECT subject_title FROM subject WHERE subject_title = :title"),
        {"title": TEST_TITLE},
    )
    assert result.scalar() == TEST_TITLE

    conn.execute(
        text("DELETE FROM subject WHERE subject_title = :title"),
        {"title": TEST_TITLE},
    )
    conn.commit()

    result = conn.execute(
        text("SELECT subject_title FROM subject WHERE subject_title = :title"),
        {"title": TEST_TITLE},
    )
    assert result.scalar() is None
