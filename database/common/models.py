from datetime import datetime

import peewee as pw

db = pw.SqliteDatabase('first.db')


class ModelBase(pw.Model):
    created_at = pw.DateField(default=datetime.now())

    class Meta():
        database = db


class History(ModelBase):
    place = pw.TextField()
    message = pw.TextField()
