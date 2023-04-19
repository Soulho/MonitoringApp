from django.db import models
from dj_cqrs.mixins import MasterMixin


class Variable(MasterMixin, models.Model):

    CQRS_ID = 'variable_model'

    #id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.name)
