from flask_security import RoleMixin, UserMixin
from flask_sqlalchemy import SQLAlchemy

from ..db import db

roles_users = db.Table('roles_users',
        db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
        db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))

class User(db.Model, UserMixin):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(255), unique=True)
  email = db.Column(db.String(255), unique=True)
  password = db.Column(db.String(255))
  active = db.Column(db.Boolean())
  confirmed_at = db.Column(db.DateTime())
  roles = db.relationship('Role', secondary=roles_users,
                          backref=db.backref('users', lazy='dynamic'))

  def get_json(self):
    json = {
      "username":self.username,
      "email":self.email,
      "roles": [],
    }
    for role in self.roles:
      json["roles"].append(role.get_json())
    return json

class Role(db.Model, RoleMixin):
  id = db.Column(db.Integer(), primary_key=True)
  name = db.Column(db.String(80), unique=True)
  description = db.Column(db.String(255))
  
  def get_json(self):
    json = {
      "name":self.name,
      "description":self.description,
    }
    return json
