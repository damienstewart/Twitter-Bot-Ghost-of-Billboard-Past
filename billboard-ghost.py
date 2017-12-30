#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy, time, sys, cookielib, json
from urllib2 import Request, urlopen, URLError
from random import randint
from datetime import datetime

#enter the corresponding information from your Twitter application:
CONSUMER_KEY = 'YOUR CONSUMER KEY HERE'
CONSUMER_SECRET = 'YOUR CONSUMER SECRET HERE'
ACCESS_KEY = 'YOUR ACCESS KEY HERE'
ACCESS_SECRET = 'YOUR ACCESS SECRET HERE'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

year = randint(1959, 2015)
month = randint(1, 12)
day = randint(1, 28)

rawDate = str(year) + '-' + str(month) + '-' + str(day)

date = datetime.strptime(rawDate, '%Y-%m-%d').date()

def lastSat(input):
        d = input.toordinal()
        last = d - 6
        sunday = last - (last % 7)
        saturday = sunday + 6
        global newDate
        newDate = date.fromordinal(saturday)
        print newDate

lastSat(date)

hdr = {
       'User-Agent': 'Mozilla/5.0 (Android 4.4; Mobile; rv:41.0) Gecko/41.0 Firefox/41.0',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'
       }
print str(newDate)
request = Request('http://billboard.modulo.site/charts/' + str(newDate) + '?max=1', headers=hdr)

try:
	response = urlopen(request)
        data = json.load(response)
        artist = data['songs'][0]['display_artist']
        songTitle = data['songs'][0]['song_name']
        spotifyID = data['songs'][0]['spotify_id']
        print artist, songTitle, spotifyID
        api.update_status('The number 1 song on the Billboard Hot 100 for the week of ' + str(newDate) + ' was "' + str(songTitle) + '" by ' + str(artist) + '. #Billboard Listen on Spotify: https://open.spotify.com/track/' + str(spotifyID))
except URLError, e:
    print 'No data. Got an error code:', e, e.read()

sys.exit()

