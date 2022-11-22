# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Authors(models.Model):
    firstname = models.TextField(db_column='firstName', blank=True, null=True)  # Field name made lowercase.
    lastname = models.TextField(db_column='lastName', blank=True, null=True)  # Field name made lowercase.
    birthdate = models.DateTimeField(db_column='birthDate', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'authors'


class BookUsers(models.Model):
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.
    userid = models.OneToOneField('Users', models.DO_NOTHING, db_column='userId', primary_key=True)  # Field name made lowercase.
    bookid = models.ForeignKey('Books', models.DO_NOTHING, db_column='bookId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'book_users'
        unique_together = (('userid', 'bookid'),)


class Books(models.Model):
    title = models.TextField(blank=True, null=True)
    genre = models.TextField(blank=True, null=True)
    authors = models.TextField(blank=True, null=True)
    audiobook = models.TextField(db_column='audioBook', blank=True, null=True)  # Field name made lowercase.
    photo = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    imdb = models.TextField(blank=True, null=True)
    youtube = models.TextField(blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.

    def __str__(self) -> str:
        return str(self.title)

    class Meta:
        managed = False
        db_table = 'books'


class PreferenceUsers(models.Model):
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.
    userid = models.OneToOneField('Users', models.DO_NOTHING, db_column='userId', primary_key=True)  # Field name made lowercase.
    preferenceid = models.ForeignKey('Preferences', models.DO_NOTHING, db_column='preferenceId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'preference_users'
        unique_together = (('userid', 'preferenceid'),)


class Preferences(models.Model):
    name = models.TextField(blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'preferences'


class UserBooks(models.Model):
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.
    bookid = models.OneToOneField(Books, models.DO_NOTHING, db_column='bookId', primary_key=True)  # Field name made lowercase.
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='userId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user_books'
        unique_together = (('bookid', 'userid'),)


class UserPreference(models.Model):
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.
    preferenceid = models.OneToOneField(Preferences, models.DO_NOTHING, db_column='preferenceId', primary_key=True)  # Field name made lowercase.
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='userId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user_preference'
        unique_together = (('preferenceid', 'userid'),)


class Users(models.Model):
    username = models.TextField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)
    password = models.TextField(blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'users'

# THE FOLLOWING PART IS NOT GENERATED USING python manage.py inspectdb > models.py

class Recommendations(models.Model):
    bookid = models.ForeignKey('Books', models.DO_NOTHING, db_column='bookId')
    rating = models.FloatField(blank=True, null=True)

    def get_queryset(self):
        search = self.request.query_params.get('search')
        genres = self.request.query_params.get('genres')

        queryset = Recommendations.get_recommendation(search, genres)
        return queryset

    @staticmethod
    def get_recommendation(search: str, genres: list):
        return Recommendations.objects.all()