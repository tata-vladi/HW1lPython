from sqlalchemy import create_engine,text

db=create_engine("postgresql://postgres:1@localhost:5432/postgres")

def test_create_students():
    connection=db.connect()
    connection.execute("select * from student")


def test_create_subjects():
    connection = db.connect()
    res=connection.execute("select count(*) from subject").fetchone()[0]

    result=  connection.execute("INSERT INTO subject (subject_id, subject_title) values (17, 'Football')")
    res2 = connection.execute("select count(*) from subject").fetchone()[0]
    assert res==res2-1


def test_update_subject_name():
    connection = db.connect()
    initial_count = connection.execute("SELECT COUNT(*) FROM subject").fetchone()[0]
    new_subject_id = 18
    new_subject_title = 'Baseball'
    connection.execute(
        f""" INSERT INTO subject (subject_id, subject_title) VALUES ({new_subject_id}, '{new_subject_title}') """)

    fetched_subject = connection.execute(
        f"SELECT subject_title FROM subject WHERE subject_id={new_subject_id}"
    ).fetchone()
    assert fetched_subject[0] == new_subject_title

def test_delete_subject():
    connection = db.connect()
    initial_count = connection.execute("SELECT COUNT(*) FROM subject").fetchone()[0]
    subject_to_delete_id = 16
    connection.execute(f"DELETE FROM subject WHERE subject_id={subject_to_delete_id}")
    final_count = connection.execute("SELECT COUNT(*) FROM subject").fetchone()[0]
    assert final_count == initial_count - 1
    deleted_subject = connection.execute(
        f"SELECT * FROM subject WHERE subject_id={subject_to_delete_id}"
    ).fetchone()
    assert deleted_subject is None

