from flaskapp.extensions import db

from .base import Base


class User(Base):
    r"""
    ORM class representing user

    Parameters
    ----------
    user_id : int
        Primary key for the User. This is generated by postgres.
    first_name : str
        First name
    last_name : str
        Last name
    email : str
        Email
    password : str
        password
    created : datetime
        Generated by postgres.
    last_modified : datetime
        Generated by postgres.
    """

    __tablename__ = "wl_user"

    user_id = db.Column(db.Integer, primary_key=True, nullable=False)
    first_name = db.Column(db.String(128))
    last_name = db.Column(db.String(128))
    email = db.Column(db.String(128))
    password = db.Column(db.String(128))
    created = db.Column(db.DateTime, server_default=db.func.now())
    last_modified = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.current_timestamp())
