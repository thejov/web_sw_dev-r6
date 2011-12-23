from django.db import models

class Continent(models.Model):
    """ Write your answer in 6.1 here. """
    name = models.CharField(max_length=30, unique=True)
    code = models.CharField(max_length=2, unique=True)
    #    countries = models.ForeignKey('Country', verbose_name='countries_of_continent', related_name='Country.continent')

    class Meta:
        ordering = ["name"]

#    <object pk="1" model="countrydata.continent">
#        <field type="CharField" name="name">Africa</field>
#        <field type="CharField" name="code">af</field>
#    </object>

class Country(models.Model):
    """ Write your answer in 6.1 here. """
    name = models.CharField(max_length=30)
    capital = models.CharField(max_length=30)
    code = models.CharField(max_length=2, unique=True)
    population = models.IntegerField()
    area = models.IntegerField()
    continent = models.ForeignKey(Continent, verbose_name='continent_of_country')

    class Meta:
        ordering = ["name"]

#    <field type="CharField" name="name">Brunei</field>
#    <field type="CharField" name="capital">Bandar Seri Begawan</field>
#    <field type="CharField" name="code">bn</field>
#    <field type="PositiveIntegerField" name="population">395027</field>
#    <field type="PositiveIntegerField" name="area">5770</field>
#    <field to="countrydata.continent" name="continent" rel="ManyToOneRel">5</field>