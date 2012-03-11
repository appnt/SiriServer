#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
import xml.etree.ElementTree as ET
import urllib2, urllib
import feedparser
import random
from plugin import *
import nltk   

class actu(Plugin):

    def extrait(self, rss):
	d = feedparser.parse(rss)
	h = random.randint(0, len(d['entries']) -1)
	print h
	print str(len(d['entries']))
	titre = nltk.clean_html(d['items'][h].title)
	descriptionb = nltk.clean_html(d['items'][h].description)
	description = re.sub("&#(\d+);", lambda m: chr(int(m.group(1))), descriptionb)
	return titre+". \n\n"+description

    @register("fr-FR", u".*actualité*.*ciné*")
    def actualitec(self, speech, language):
	final = self.extrait("http://syndication.lesechos.fr/rss/CL_Cinema.xml")
	if language == 'fr-FR':
            self.say(final)
        self.complete_request()

    @register("fr-FR", u".*actualité*.*google*")
    def actualiteg(self, speech, language):
	final = self.extrait("http://news.google.fr/?output=rss")
	if language == 'fr-FR':
            self.say(final)
        self.complete_request()

    @register("fr-FR", u".*actualité*.*info*")
    def actualite(self, speech, language):
	final = self.extrait("http://www.franceinfo.fr/rss.xml")
	if language == 'fr-FR':
            self.say(final)
        self.complete_request()

    @register("fr-FR", u".*actualité*.*france*")
    def actualitetv(self, speech, language):
	final = self.extrait("http://www.francetv.fr/info/france.rss")
	if language == 'fr-FR':
            self.say(final)
        self.complete_request()

    @register("fr-FR", u".*actualité*.*monde*")
    def actualitemonde(self, speech, language):
	final = self.extrait("http://www.francetv.fr/info/monde.rss")
	if language == 'fr-FR':
            self.say(final)
        self.complete_request()

    @register("fr-FR", u".*actualité*.*découverte*")
    def actualitedecouverte(self, speech, language):
	final = self.extrait("http://www.francetv.fr/info/decouverte.rss")
	if language == 'fr-FR':
            self.say(final)
        self.complete_request()

    @register("fr-FR", u".*blague*.")
    def actualiteblague(self, speech, language):
	l = [
	'http://www.blagoo.eu/rsstopblagues.xml', 
	'http://labanane.org/humourcarambar.xml', 
	'http://labanane.org/humourabsurde.xml'
	]
	final = self.extrait(random.choice(l))
	if language == 'fr-FR':
            self.say(final.replace('Votez !', ''))
        self.complete_request()


    @register("fr-FR", u".*actualité*.*jeu*.*vidéo*")
    def actualitejeux(self, speech, language):
	l = [
	"http://www.gamekult.com/feeds/actu.html"
	]
	final = self.extrait(random.choice(l))
	if language == 'fr-FR':
            self.say(final.replace('Votez !', ''))
        self.complete_request()
		