# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Dji(models.Model):
    date = models.DateField(db_column='Date', primary_key=True)  # Field name made lowercase.
    open = models.DecimalField(db_column='Open', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    high = models.DecimalField(db_column='High', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    low = models.DecimalField(db_column='Low', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    close = models.DecimalField(db_column='Close', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    pricechange = models.DecimalField(db_column='PriceChange', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    perchange = models.DecimalField(db_column='PerChange', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DJI'


class Fchi(models.Model):
    date = models.DateField(db_column='Date', primary_key=True)  # Field name made lowercase.
    open = models.DecimalField(db_column='Open', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    high = models.DecimalField(db_column='High', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    low = models.DecimalField(db_column='Low', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    close = models.DecimalField(db_column='Close', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    pricechange = models.DecimalField(db_column='PriceChange', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    perchange = models.DecimalField(db_column='PerChange', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FCHI'


class Gdaxi(models.Model):
    date = models.DateField(db_column='Date', primary_key=True)  # Field name made lowercase.
    open = models.DecimalField(db_column='Open', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    high = models.DecimalField(db_column='High', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    low = models.DecimalField(db_column='Low', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    close = models.DecimalField(db_column='Close', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    pricechange = models.DecimalField(db_column='PriceChange', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    perchange = models.DecimalField(db_column='PerChange', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GDAXI'


class Gspc(models.Model):
    date = models.DateField(db_column='Date', primary_key=True)  # Field name made lowercase.
    open = models.DecimalField(db_column='Open', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    high = models.DecimalField(db_column='High', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    low = models.DecimalField(db_column='Low', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    close = models.DecimalField(db_column='Close', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    pricechange = models.DecimalField(db_column='PriceChange', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    perchange = models.DecimalField(db_column='PerChange', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GSPC'


class Hsi(models.Model):
    date = models.DateField(db_column='Date', primary_key=True)  # Field name made lowercase.
    open = models.DecimalField(db_column='Open', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    high = models.DecimalField(db_column='High', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    low = models.DecimalField(db_column='Low', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    close = models.DecimalField(db_column='Close', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    pricechange = models.DecimalField(db_column='PriceChange', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    perchange = models.DecimalField(db_column='PerChange', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HSI'


class Ixic(models.Model):
    date = models.DateField(db_column='Date', primary_key=True)  # Field name made lowercase.
    open = models.DecimalField(db_column='Open', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    high = models.DecimalField(db_column='High', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    low = models.DecimalField(db_column='Low', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    close = models.DecimalField(db_column='Close', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    pricechange = models.DecimalField(db_column='PriceChange', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    perchange = models.DecimalField(db_column='PerChange', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IXIC'


class Ks11(models.Model):
    date = models.DateField(db_column='Date', primary_key=True)  # Field name made lowercase.
    open = models.DecimalField(db_column='Open', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    high = models.DecimalField(db_column='High', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    low = models.DecimalField(db_column='Low', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    close = models.DecimalField(db_column='Close', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    pricechange = models.DecimalField(db_column='PriceChange', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    perchange = models.DecimalField(db_column='PerChange', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'KS11'


class N225(models.Model):
    date = models.DateField(db_column='Date', primary_key=True)  # Field name made lowercase.
    open = models.DecimalField(db_column='Open', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    high = models.DecimalField(db_column='High', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    low = models.DecimalField(db_column='Low', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    close = models.DecimalField(db_column='Close', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    pricechange = models.DecimalField(db_column='PriceChange', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    perchange = models.DecimalField(db_column='PerChange', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'N225'


class Predictdef(models.Model):
    prediction = models.DecimalField(db_column='Prediction', primary_key=True, max_digits=4, decimal_places=2)  # Field name made lowercase.
    predictionname = models.CharField(db_column='PredictionName', max_length=2)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PredictDef'
    def __str__(self):
        return self.predictionname


class Shi(models.Model):
    date = models.DateField(db_column='Date', primary_key=True)  # Field name made lowercase.
    open = models.DecimalField(db_column='Open', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    high = models.DecimalField(db_column='High', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    low = models.DecimalField(db_column='Low', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    close = models.DecimalField(db_column='Close', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    pricechange = models.DecimalField(db_column='PriceChange', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    perchange = models.DecimalField(db_column='PerChange', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SHI'


class Sox(models.Model):
    date = models.DateField(db_column='Date', primary_key=True)  # Field name made lowercase.
    open = models.DecimalField(db_column='Open', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    high = models.DecimalField(db_column='High', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    low = models.DecimalField(db_column='Low', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    close = models.DecimalField(db_column='Close', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    pricechange = models.DecimalField(db_column='PriceChange', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    perchange = models.DecimalField(db_column='PerChange', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SOX'


class Twii(models.Model):
    date = models.DateField(db_column='Date', primary_key=True)  # Field name made lowercase.
    open = models.DecimalField(db_column='Open', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    high = models.DecimalField(db_column='High', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    low = models.DecimalField(db_column='Low', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    close = models.DecimalField(db_column='Close', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    pricechange = models.DecimalField(db_column='PriceChange', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    perchange = models.DecimalField(db_column='PerChange', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    openchange = models.DecimalField(db_column='OpenChange', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    prediction = models.ForeignKey(Predictdef, models.DO_NOTHING, db_column='Prediction', blank=True, null=True)  # Field name made lowercase.
    numaccuracy = models.DecimalField(db_column='NumAccuracy', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    accuracy = models.DecimalField(db_column='Accuracy', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    selfprediction = models.DecimalField(db_column='SelfPrediction', max_digits=4, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    selfnumaccuracy = models.DecimalField(db_column='SelfNumAccuracy', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    selfaccuracy = models.DecimalField(db_column='SelfAccuracy', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TWII'


class Wtxp(models.Model):
    date = models.DateField(db_column='Date', primary_key=True)  # Field name made lowercase.
    open = models.DecimalField(db_column='Open', max_digits=9, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    high = models.DecimalField(db_column='High', max_digits=9, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    low = models.DecimalField(db_column='Low', max_digits=9, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    close = models.DecimalField(db_column='Close', max_digits=9, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    pricechange = models.DecimalField(db_column='PriceChange', max_digits=9, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    perchange = models.DecimalField(db_column='PerChange', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WTXP'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class PredictionCategory(models.Model):
    category = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'prediction_category'

    def __str__(self):
        return self.category

BALANCE_TYPE = ((u'收入',u'收入'),(u'支出',u'支出'))

class PredictionRecord(models.Model):
    date = models.DateField()
    description = models.CharField(max_length=300)
    cash = models.IntegerField()
    balance_type = models.CharField(max_length=2,choices=BALANCE_TYPE)
    category = models.ForeignKey(PredictionCategory, on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prediction_record'

    def __str__(self):
        return self.description
