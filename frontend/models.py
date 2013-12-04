from django.db import models
from django_extensions.db.fields \
    import CreationDateTimeField, ModificationDateTimeField

# modelli sqlite

# class Azienda(models.Model):
#     nome = models.CharField(max_length=255, null=False, blank=False)
#     indirizzo = models.CharField(max_length=255)
#     tags = models.ManyToManyField('Tag')
#     cancellata = models.BooleanField(default=True)
#     created = CreationDateTimeField(null=True, blank=True)
#     modified = ModificationDateTimeField(null=True, blank=True)

#     class Meta:
#         db_table = 'aziende'

#     def __unicode__(self):
#         return u"{this.nome} - {this.indirizzo}".format(this=self)



# class Prodotto(models.Model):
#     nome = models.CharField(max_length=255, null=False, blank=False)
#     azienda = models.ForeignKey(Azienda, related_name='prodotti', null=True, blank=True)
#     created = CreationDateTimeField(null=True, blank=True)
#     modified = ModificationDateTimeField(null=True, blank=True)


#     class Meta:
#         db_table = 'prodotti'

#     def __unicode__(self):
#         return u"{this.nome}".format(this=self)


# class Tag(models.Model):
#     nome = models.CharField(max_length=255, null=False, blank=False)
#     created = CreationDateTimeField(null=True, blank=True)
#     modified = ModificationDateTimeField(null=True, blank=True)

#     class Meta:
#         db_table = 'tags'

#     def __unicode__(self):
#         return u"{this.nome}".format(this=self)


class Account(models.Model):
    login = models.CharField(primary_key=True, max_length=255)
    password = models.TextField()
    backup_password = models.CharField(max_length=255)
    hashcode = models.CharField(max_length=255, blank=True)
    data_inserimento = models.DateTimeField()
    data_ultima_modifica = models.DateTimeField()
    class Meta:
        managed = True
        db_table = 'account'

class Annunci(models.Model):
    id = models.IntegerField(primary_key=True)
    idazienda = models.ForeignKey('Aziende', db_column='idAzienda', blank=True, null=True) # Field name made lowercase.
    nome = models.CharField(max_length=255, blank=True)
    abstract = models.TextField(blank=True)
    descrizione = models.TextField(blank=True)
    parametro = models.CharField(max_length=255, blank=True)
    data_inserimento = models.DateTimeField(blank=True, null=True)
    data_ultima_modifica = models.DateTimeField(blank=True, null=True)
    data_scadenza = models.DateTimeField(blank=True, null=True)
    tipologia = models.CharField(max_length=20, blank=True)
    class Meta:
        managed = True
        db_table = 'annunci'

class AnnunciTagOccorrenze(models.Model):
    idtag = models.ForeignKey('Tags', db_column='idTag', primary_key=True) # Field name made lowercase.
    occorrenze = models.IntegerField(blank=True, null=True)
    livello = models.IntegerField(blank=True, null=True)
    homepage = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = True
        db_table = 'annunci_tag_occorrenze'

class AnnunciTagOccorrenzeComuni(models.Model):
    idtag = models.ForeignKey('Tags', db_column='idTag') # Field name made lowercase.
    codprovincia = models.ForeignKey('Province', db_column='codProvincia') # Field name made lowercase.
    occorrenze = models.IntegerField(blank=True, null=True)
    comune = models.CharField(max_length=50)
    class Meta:
        managed = True
        db_table = 'annunci_tag_occorrenze_comuni'

class AnnunciTagOccorrenzeProvince(models.Model):
    idtag = models.ForeignKey('Tags', db_column='idTag') # Field name made lowercase.
    codprovincia = models.ForeignKey('Province', db_column='codProvincia') # Field name made lowercase.
    occorrenze = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = True
        db_table = 'annunci_tag_occorrenze_province'

class AnnunciTagOccorrenzeRegioni(models.Model):
    idtag = models.ForeignKey('Tags', db_column='idTag') # Field name made lowercase.
    codregione = models.ForeignKey('Regioni', db_column='codRegione') # Field name made lowercase.
    occorrenze = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = True
        db_table = 'annunci_tag_occorrenze_regioni'

class AnnunciTags(models.Model):
    idannuncio = models.ForeignKey(Annunci, db_column='idAnnuncio') # Field name made lowercase.
    idtag = models.ForeignKey('Tags', db_column='idTag') # Field name made lowercase.
    class Meta:
        managed = True
        db_table = 'annunci_tags'

class Aziende(models.Model):
    id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=255, blank=True)
    indirizzo_1 = models.CharField(max_length=255, blank=True)
    indirizzo_2 = models.CharField(max_length=255, blank=True)
    indirizzo_3 = models.CharField(max_length=255, blank=True)
    localita = models.CharField(max_length=255, blank=True)
    provincia = models.CharField(max_length=100, blank=True)
    postcode = models.CharField(max_length=25, blank=True)
    telefono = models.CharField(max_length=255, blank=True)
    fax = models.CharField(max_length=255, blank=True)
    email = models.CharField(max_length=100, blank=True)
    website = models.CharField(max_length=100, blank=True)
    descrizione_html = models.TextField(blank=True)
    hotfrog_id = models.CharField(max_length=50, blank=True)
    login = models.CharField(max_length=100, blank=True)
    password = models.TextField(blank=True)
    backup_password = models.CharField(max_length=255, blank=True)
    data_inserimento = models.DateTimeField(blank=True, null=True)
    data_ultima_modifica = models.DateTimeField(blank=True, null=True)
    data_update_kassy = models.DateTimeField(blank=True, null=True)
    comune = models.CharField(max_length=50, blank=True)
    codprovincia = models.CharField(db_column='codProvincia', max_length=50, blank=True) # Field name made lowercase.
    parametro = models.CharField(unique=True, max_length=200, blank=True)
    codregione = models.CharField(db_column='codRegione', max_length=50, blank=True) # Field name made lowercase.
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    rank = models.IntegerField(blank=True, null=True)
    hashcode = models.CharField(max_length=255, blank=True)
    richiamabile = models.IntegerField()
    bonus_rank = models.IntegerField(blank=True, null=True)
    invio_dem_diretto = models.IntegerField()
    invio_dem = models.IntegerField()
    codice_analytics = models.CharField(max_length=255)
    invio_dem_tramite_reedbusiness = models.IntegerField()
    privacy = models.IntegerField()
    tags = models.ManyToManyField('Tags', through="AziendeTags")

    class Meta:
        managed = True
        db_table = 'aziende'


    def __unicode__(self):
        return u"{this.nome}".format(this=self)



class AziendeContatti(models.Model):
    id = models.IntegerField(primary_key=True)
    idazienda = models.ForeignKey(Aziende, db_column='idAzienda') # Field name made lowercase.
    idelemento = models.IntegerField(db_column='idElemento') # Field name made lowercase.
    tipologia = models.IntegerField()
    nome_mittente = models.CharField(max_length=255)
    email_mittente = models.CharField(max_length=255)
    messaggio = models.TextField()
    letto = models.IntegerField()
    data_ora = models.DateTimeField()
    visibile = models.IntegerField()
    referer = models.CharField(max_length=255)
    class Meta:
        managed = True
        db_table = 'aziende_contatti'

class AziendeEliminate(models.Model):
    idazienda = models.IntegerField(db_column='idAzienda', primary_key=True) # Field name made lowercase.
    referer = models.CharField(max_length=255)
    data_eliminazione = models.DateTimeField()
    nome = models.CharField(max_length=255)
    indirizzo = models.CharField(max_length=255)
    comune = models.CharField(max_length=255)
    codprovincia = models.CharField(db_column='codProvincia', max_length=255) # Field name made lowercase.
    class Meta:
        managed = True
        db_table = 'aziende_eliminate'

class AziendeProvinceRegioni(models.Model):
    url = models.CharField(max_length=202, blank=True)
    azienda = models.CharField(max_length=255, blank=True)
    descrizione_html = models.TextField(blank=True)
    comune = models.CharField(max_length=50, blank=True)
    provincia = models.CharField(max_length=50)
    regione = models.CharField(max_length=50)
    class Meta:
        managed = True
        db_table = 'aziende_province_regioni'

class AziendeTags(models.Model):
    idazienda = models.ForeignKey(Aziende, db_column='idAzienda') # Field name made lowercase.
    idtag = models.ForeignKey('Tags', db_column='idTag') # Field name made lowercase.
    class Meta:
        managed = True
        db_table = 'aziende_tags'

class ComuniItaliani(models.Model):
    nome = models.CharField(max_length=50)
    codprovincia = models.ForeignKey('Province', db_column='codProvincia') # Field name made lowercase.
    codregione = models.ForeignKey('Regioni', db_column='codRegione') # Field name made lowercase.
    cap = models.CharField(db_column='CAP', max_length=50) # Field name made lowercase.
    parametro = models.CharField(max_length=50, blank=True)
    class Meta:
        managed = True
        db_table = 'comuni_italiani'

class Faq(models.Model):
    id = models.IntegerField(primary_key=True)
    idlingua = models.CharField(db_column='idLingua', max_length=2) # Field name made lowercase.
    gruppo = models.CharField(max_length=255)
    domanda = models.TextField()
    risposta = models.TextField()
    ordine = models.IntegerField()
    class Meta:
        managed = True
        db_table = 'faq'

class Lingue(models.Model):
    id = models.IntegerField(primary_key=True)
    alias = models.CharField(max_length=255, blank=True)
    class Meta:
        managed = True
        db_table = 'lingue'

class Macrocategorie(models.Model):
    id = models.IntegerField(primary_key=True)
    id_dbi = models.IntegerField(blank=True, null=True)
    nome = models.CharField(max_length=255, blank=True)
    class Meta:
        managed = True
        db_table = 'macrocategorie'

class Meta(models.Model):
    pagina = models.CharField(max_length=30)
    url = models.CharField(max_length=50)
    geo = models.CharField(max_length=30, blank=True)
    paginazione = models.IntegerField()
    versione = models.IntegerField()
    title = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    keywords = models.TextField(blank=True)
    class Meta:
        managed = True
        db_table = 'meta'

class News(models.Model):
    id = models.IntegerField(primary_key=True)
    idazienda = models.ForeignKey(Aziende, db_column='idAzienda', blank=True, null=True) # Field name made lowercase.
    nome = models.CharField(max_length=255, blank=True)
    abstract = models.TextField(blank=True)
    descrizione = models.TextField(blank=True)
    parametro = models.CharField(max_length=255, blank=True)
    data = models.DateTimeField(blank=True, null=True)
    data_inserimento = models.DateTimeField(blank=True, null=True)
    data_ultima_modifica = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = True
        db_table = 'news'

class NewsTagOccorrenze(models.Model):
    idtag = models.ForeignKey('Tags', db_column='idTag', primary_key=True) # Field name made lowercase.
    occorrenze = models.IntegerField(blank=True, null=True)
    livello = models.IntegerField(blank=True, null=True)
    homepage = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = True
        db_table = 'news_tag_occorrenze'

class NewsTagOccorrenzeComuni(models.Model):
    idtag = models.ForeignKey('Tags', db_column='idTag') # Field name made lowercase.
    codprovincia = models.ForeignKey('Province', db_column='codProvincia') # Field name made lowercase.
    occorrenze = models.IntegerField(blank=True, null=True)
    comune = models.CharField(max_length=50)
    class Meta:
        managed = True
        db_table = 'news_tag_occorrenze_comuni'

class NewsTagOccorrenzeProvince(models.Model):
    idtag = models.ForeignKey('Tags', db_column='idTag') # Field name made lowercase.
    codprovincia = models.ForeignKey('Province', db_column='codProvincia') # Field name made lowercase.
    occorrenze = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = True
        db_table = 'news_tag_occorrenze_province'

class NewsTagOccorrenzeRegioni(models.Model):
    idtag = models.ForeignKey('Tags', db_column='idTag') # Field name made lowercase.
    codregione = models.ForeignKey('Regioni', db_column='codRegione') # Field name made lowercase.
    occorrenze = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = True
        db_table = 'news_tag_occorrenze_regioni'

class NewsTags(models.Model):
    idnews = models.ForeignKey(News, db_column='idNews') # Field name made lowercase.
    idtag = models.ForeignKey('Tags', db_column='idTag') # Field name made lowercase.
    class Meta:
        managed = True
        db_table = 'news_tags'

class Prodotti(models.Model):
    id = models.IntegerField(primary_key=True)
    idazienda = models.ForeignKey(Aziende, db_column='idAzienda', blank=True, null=True) # Field name made lowercase.
    nome = models.CharField(max_length=255, blank=True)
    abstract = models.TextField(blank=True)
    descrizione = models.TextField(blank=True)
    parametro = models.CharField(max_length=255, blank=True)
    data_inserimento = models.DateTimeField(blank=True, null=True)
    data_ultima_modifica = models.DateTimeField(blank=True, null=True)
    nome_originale_pdf = models.CharField(max_length=255)
    class Meta:
        managed = True
        db_table = 'prodotti'

class ProdottiTagOccorrenze(models.Model):
    idtag = models.ForeignKey('Tags', db_column='idTag', primary_key=True) # Field name made lowercase.
    occorrenze = models.IntegerField(blank=True, null=True)
    livello = models.IntegerField(blank=True, null=True)
    homepage = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = True
        db_table = 'prodotti_tag_occorrenze'

class ProdottiTagOccorrenzeComuni(models.Model):
    idtag = models.ForeignKey('Tags', db_column='idTag') # Field name made lowercase.
    codprovincia = models.ForeignKey('Province', db_column='codProvincia') # Field name made lowercase.
    occorrenze = models.IntegerField(blank=True, null=True)
    comune = models.CharField(max_length=50)
    class Meta:
        managed = True
        db_table = 'prodotti_tag_occorrenze_comuni'

class ProdottiTagOccorrenzeProvince(models.Model):
    idtag = models.ForeignKey('Tags', db_column='idTag') # Field name made lowercase.
    codprovincia = models.ForeignKey('Province', db_column='codProvincia') # Field name made lowercase.
    occorrenze = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = True
        db_table = 'prodotti_tag_occorrenze_province'

class ProdottiTagOccorrenzeRegioni(models.Model):
    idtag = models.ForeignKey('Tags', db_column='idTag') # Field name made lowercase.
    codregione = models.ForeignKey('Regioni', db_column='codRegione') # Field name made lowercase.
    occorrenze = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = True
        db_table = 'prodotti_tag_occorrenze_regioni'

class ProdottiTags(models.Model):
    idprodotto = models.ForeignKey(Prodotti, db_column='idProdotto') # Field name made lowercase.
    idtag = models.ForeignKey('Tags', db_column='idTag') # Field name made lowercase.
    class Meta:
        managed = True
        db_table = 'prodotti_tags'

class Province(models.Model):
    codprovincia = models.CharField(db_column='codProvincia', primary_key=True, max_length=50) # Field name made lowercase.
    codregione = models.ForeignKey('Regioni', db_column='codRegione', max_length=50, related_name="province") # Field name made lowercase.
    nome = models.CharField(max_length=50)
    parametro = models.CharField(max_length=50, blank=True)
    class Meta:
        managed = True
        db_table = 'province'

class Regioni(models.Model):
    codregione = models.CharField(db_column='codRegione', primary_key=True, max_length=50) # Field name made lowercase.
    nome = models.CharField(max_length=50)
    parametro = models.CharField(max_length=50, blank=True)
    class Meta:
        managed = True
        db_table = 'regioni'

class Registrazioni(models.Model):
    id = models.IntegerField(primary_key=True)
    idazienda = models.IntegerField(db_column='idAzienda', blank=True, null=True) # Field name made lowercase.
    step = models.IntegerField(blank=True, null=True)
    nome = models.CharField(max_length=255, blank=True)
    indirizzo = models.CharField(max_length=255, blank=True)
    comune = models.CharField(max_length=255, blank=True)
    codprovincia = models.CharField(db_column='codProvincia', max_length=255, blank=True) # Field name made lowercase.
    cap = models.CharField(max_length=255, blank=True)
    telefono = models.CharField(max_length=255, blank=True)
    fax = models.CharField(max_length=255, blank=True)
    email = models.CharField(max_length=255, blank=True)
    website = models.CharField(max_length=255, blank=True)
    descrizione_html = models.TextField(blank=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    email_login = models.CharField(max_length=255, blank=True)
    password = models.TextField(blank=True)
    backup_password = models.CharField(max_length=255, blank=True)
    hashcode = models.CharField(max_length=255, blank=True)
    data_ultima_modifica = models.DateTimeField()
    conferma_reed = models.IntegerField()
    privacy = models.IntegerField()
    invio_dem = models.IntegerField()
    invio_dem_tramite_reedbusiness = models.IntegerField()
    invio_dem_diretto = models.IntegerField()
    class Meta:
        managed = True
        db_table = 'registrazioni'

class RegistrazioniServizi(models.Model):
    id = models.IntegerField(primary_key=True)
    id_tipo_servizio = models.IntegerField(blank=True, null=True)
    id_servizio = models.IntegerField(blank=True, null=True)
    step = models.IntegerField()
    nome = models.CharField(max_length=255)
    cod_provincia = models.CharField(max_length=25)
    email_login = models.CharField(max_length=255)
    password = models.TextField()
    conclusa = models.IntegerField()
    id_tipo_pagamento = models.CharField(max_length=255, blank=True)
    id_codice_sconto = models.IntegerField(blank=True, null=True)
    data_inserimento = models.DateTimeField()
    id_servizio_acquistato = models.IntegerField(blank=True, null=True)
    id_ordine = models.IntegerField(blank=True, null=True)
    id_azienda = models.IntegerField(blank=True, null=True)
    invio_dem = models.IntegerField()
    class Meta:
        managed = True
        db_table = 'registrazioni_servizi'

class RegistrazioniServiziTag(models.Model):
    id_registrazione_servizio = models.IntegerField()
    tag = models.CharField(max_length=255)
    class Meta:
        managed = True
        db_table = 'registrazioni_servizi_tag'

class RegistrazioniTag(models.Model):
    id = models.IntegerField(primary_key=True)
    idregistrazione = models.IntegerField(db_column='idRegistrazione') # Field name made lowercase.
    idtag = models.IntegerField(db_column='idTag', blank=True, null=True) # Field name made lowercase.
    tag = models.CharField(max_length=255, blank=True)
    class Meta:
        managed = True
        db_table = 'registrazioni_tag'

class Settori(models.Model):
    id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=255, blank=True)
    descrizione = models.CharField(max_length=255, blank=True)
    parametro = models.CharField(max_length=255, blank=True)
    data_inserimento = models.DateTimeField(blank=True, null=True)
    data_ultima_modifica = models.DateTimeField(blank=True, null=True)
    title = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=255, blank=True)
    keyword = models.CharField(max_length=255, blank=True)
    class Meta:
        managed = True
        db_table = 'settori'

class SettoriTags(models.Model):
    id = models.IntegerField(primary_key=True)
    idsettore = models.ForeignKey(Settori, db_column='idSettore', blank=True, null=True) # Field name made lowercase.
    idtag = models.ForeignKey('Tags', db_column='idTag', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = True
        db_table = 'settori_tags'

class Stopwords(models.Model):
    id = models.IntegerField(primary_key=True)
    stopword = models.CharField(max_length=255, blank=True)
    class Meta:
        managed = True
        db_table = 'stopwords'

class TagLegami(models.Model):
    idtag_1 = models.ForeignKey('Tags', db_column='idTag_1', related_name='tag1') # Field name made lowercase.
    idtag_2 = models.ForeignKey('Tags', db_column='idTag_2', related_name='tag2') # Field name made lowercase.
    legame = models.IntegerField()
    legame_percent = models.FloatField(blank=True, null=True)
    class Meta:
        managed = True
        db_table = 'tag_legami'

class TagMaxLegame(models.Model):
    idtag_1 = models.IntegerField(db_column='idTag_1') # Field name made lowercase.
    massimo = models.FloatField(blank=True, null=True)
    class Meta:
        managed = True
        db_table = 'tag_max_legame'

class TagOccorrenze(models.Model):
    idtag = models.ForeignKey('Tags', db_column='idTag', primary_key=True) # Field name made lowercase.
    occorrenze = models.IntegerField(blank=True, null=True)
    livello = models.IntegerField(blank=True, null=True)
    homepage = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = True
        db_table = 'tag_occorrenze'


class Tags(models.Model):
    id = models.IntegerField(primary_key=True)
    tag = models.CharField(max_length=255)
    hotfrog_id = models.IntegerField()
    parametro = models.CharField(unique=True, max_length=255, blank=True)
    data_inserimento = models.DateTimeField(blank=True, null=True)
    data_ultima_modifica = models.DateTimeField(blank=True, null=True)
    classification = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'tags'

    def __unicode__(self):
        return u"{this.tag}".format(this=self)


class Video(models.Model):
    id = models.IntegerField(primary_key=True)
    idazienda = models.ForeignKey(Aziende, db_column='idAzienda') # Field name made lowercase.
    nome = models.CharField(max_length=255)
    abstract = models.CharField(max_length=255)
    descrizione = models.TextField()
    parametro = models.CharField(max_length=255)
    data_inserimento = models.DateTimeField()
    data_ultima_modifica = models.DateTimeField()
    youtube_id = models.CharField(max_length=255)
    sorgente = models.CharField(max_length=50)
    class Meta:
        managed = True
        db_table = 'video'

class VideoTagOccorrenze(models.Model):
    idtag = models.ForeignKey(Tags, db_column='idTag', primary_key=True) # Field name made lowercase.
    occorrenze = models.IntegerField()
    livello = models.IntegerField()
    homepage = models.IntegerField()
    class Meta:
        managed = True
        db_table = 'video_tag_occorrenze'

class VideoTagOccorrenzeComuni(models.Model):
    idtag = models.ForeignKey(Tags, db_column='idTag') # Field name made lowercase.
    codprovincia = models.ForeignKey(Province, db_column='codProvincia') # Field name made lowercase.
    occorrenze = models.IntegerField()
    comune = models.CharField(max_length=50)
    class Meta:
        managed = True
        db_table = 'video_tag_occorrenze_comuni'

class VideoTagOccorrenzeProvince(models.Model):
    idtag = models.ForeignKey(Tags, db_column='idTag') # Field name made lowercase.
    codprovincia = models.ForeignKey(Province, db_column='codProvincia') # Field name made lowercase.
    occorrenze = models.IntegerField()
    class Meta:
        managed = True
        db_table = 'video_tag_occorrenze_province'

class VideoTagOccorrenzeRegioni(models.Model):
    idtag = models.ForeignKey(Tags, db_column='idTag') # Field name made lowercase.
    codregione = models.ForeignKey(Regioni, db_column='codRegione') # Field name made lowercase.
    occorrenze = models.IntegerField()
    class Meta:
        managed = True
        db_table = 'video_tag_occorrenze_regioni'

class VideoTags(models.Model):
    idvideo = models.ForeignKey(Video, db_column='idVideo') # Field name made lowercase.
    idtag = models.ForeignKey(Tags, db_column='idTag') # Field name made lowercase.
    class Meta:
        managed = True
        db_table = 'video_tags'
