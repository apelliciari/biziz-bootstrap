from django.db import models
from django_extensions.db.fields \
    import CreationDateTimeField, ModificationDateTimeField

# Create your models here.


class Azienda(models.Model):
    nome = models.CharField(max_length=255, null=False, blank=False)
    indirizzo = models.CharField(max_length=255)
    tags = models.ManyToManyField('Tag')
    cancellata = models.BooleanField(default=True)
    created = CreationDateTimeField(null=True, blank=True)
    modified = ModificationDateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'aziende'

    def __unicode__(self):
        return u"{this.nome} - {this.indirizzo}".format(this=self)



class Prodotto(models.Model):
    nome = models.CharField(max_length=255, null=False, blank=False)
    azienda = models.ForeignKey(Azienda, related_name='prodotti', null=True, blank=True)
    created = CreationDateTimeField(null=True, blank=True)
    modified = ModificationDateTimeField(null=True, blank=True)


    class Meta:
        db_table = 'prodotti'

    def __unicode__(self):
        return u"{this.nome}".format(this=self)


class Tag(models.Model):
    nome = models.CharField(max_length=255, null=False, blank=False)
    created = CreationDateTimeField(null=True, blank=True)
    modified = ModificationDateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'tags'

    def __unicode__(self):
        return u"{this.nome}".format(this=self)