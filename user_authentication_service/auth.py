#!/usr/bin/env python3
''' Hashing Module '''

import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
import uuid


def _hash_password(password: str) -> str:
    ''' returns the salted hash of the input password '''
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


def _generate_uuid() -> str:
    ''' def generate uid '''
    return str(uuid.uuid4())


class Auth:
    """interaction with the authentication database in Auth class.
    """
    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        ''' returns the registered user '''
        if email and password:
            try:
                self._db.find_user_by(email=email)
            except NoResultFound:
                user = self._db.add_user(email, _hash_password(password))
                return user
            else:
                raise ValueError("User {} already exists".format(email))

    def valid_login(self, email: str, password: str) -> bool:
        ''' returns the valid user and False if not valid '''
        try:
            user = self._db.find_user_by(email=email)
            if user:
                return bcrypt.checkpw(password.encode(), user.hashed_password)
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        ''' returns the session id '''
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return
        session_id = _generate_uuid()
        self._db.update_user(user.id, session_id=session_id)
        return session_id

    def get_user_from_session_id(self, session_id: str) -> str:
        ''' returns the user with the session id'''
        if not session_id:
            return None
        try:
            return self._db.find_user_by(session_id=session_id)
        except NoResultFound:
            return

    def destroy_session(self, user_id: int) -> None:
        ''' destroys session '''
        if user_id:
            self._db.update_user(user_id, session_id=None)

    def get_reset_password_token(self, email: str) -> str:
        ''' get reset password token '''
        if email:
            try:
                user = self._db.find_user_by(email=email)
            except NoResultFound:
                raise ValueError
            else:
                take = _generate_uuid()
                self._db.update_user(user.id, reset_token=take)
                return take

    def update_password(self, reset_token: str, password: str) -> None:
        ''' updates password '''
        try:
            user = self._db.find_user_by(reset_token=reset_token)
            n_pass = _hash_password(password)
            self._db.update_user(user.id, hashed_password=n_pass,
                                 reset_token=None)
            return None
        except Exception:
            raise ValueError