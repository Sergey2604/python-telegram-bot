from datetime import datetime
import peewee as pw

db = pw.SqliteDatabase(r'C:\Обучение\Skillbox\Python\диплом\python_basic_diploma\first.db')


class ModelBase(pw.Model):
    created_at = pw.DateField(default=datetime.now())

    class Meta:
        database = db


class History(ModelBase):
    user_id = pw.TextField()
    place = pw.TextField()
    temp = pw.TextField()
