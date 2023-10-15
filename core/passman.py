from .config import session, engine
from .models import Password

# Session instance
sess = session(bind=engine)

# Password Manager


def insert_pass(account, password):
    new_pass = Password(account=account, password=password)
    sess.add(new_pass)
    sess.commit()
    return


def read_all():
    all_pass = sess.query(Password).all()

    # for p in all_pass:
    #     print(p.unique_id, p.account, p.password, p.date_created)

    return all_pass


def search(term):
    results = sess.query(Password).filter(Password.account == term)
    return results


def delete(term):
    results = sess.query(Password).filter(Password.account == term)
    return results
