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

userArr = ['AN ARRAY OF USERS YOU WANT TO TWEET AT HERE. EXAMPLE ENTRIES:', 'therock', 'donaldtrump', 'stevencolbert']

def tweet(tryUser): 
	print '@' + tryUser
	api = tweepy.API(auth_handler=auth, parser=tweepy.parsers.JSONParser())
	user_data = api.get_user(tryUser) 
	createDate = user_data['created_at']

	months = [0, 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

	createYear = (createDate[-4:])
	year = createYear

	createMonth = (createDate[4:7])
	thismonth = months.index(createMonth)
	month = ('{:02d}'.format(thismonth))

	createDay = (createDate[8:10])
	day = createDay

	if int(year) < 2015:
		rawDate = str(year) + '-' + str(month) + '-' + str(day)
	else:
		print 'Account creation date greater than current chart data, skipping'
		return

	date = datetime.strptime(rawDate, '%Y-%m-%d').date()

	def lastSat(input):
			d = input.toordinal()
			last = d - 6
			sunday = last - (last % 7)
			saturday = sunday + 6
			global newDate
			newDate = date.fromordinal(saturday)
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
		if spotifyID is not None:
			print artist, songTitle, spotifyID
			api.update_status('@' + tryUser + ' The number 1 song on the Billboard Hot 100 on the day that you joined Twitter (' + str(newDate) + ') was "' + str(songTitle) + '" by ' + str(artist) + '! Listen on Spotify: https://open.spotify.com/track/' + str(spotifyID))
		else: 
			print 'No Spotify ID found, skipping'
			return
	except URLError, e:
		print 'No data. Got an error code:', e, e.read()	
		
for user in userArr:
	tweet(user)
    	time.sleep(600)

sys.exit()
