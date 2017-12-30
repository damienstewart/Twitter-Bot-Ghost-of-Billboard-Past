# Twitter Bot - Ghost of Billboard Past

I took the code from from my Billboard Number 1s repository, rewrote it in Python, and turned it into a Twitter Bot.

Every time this Python script is called it will grab the information of one chart topping single from a random date, and post it to your timeline. I put this file on one of my servers and set up a cron job to run the script every 5 hours. The Twitter Bot can be found here <a href="https://twitter.com/BillboardGhost">@BillboardGhost</a>

This is my first project written in Python

# TODO

1. I'd like to add functionality to Tweet at people (semi-random people of interest) with the #1 Billboard hit on the day that they joined twitter. 

2. Fix a bug that occurs when the bot cannot find the Spotify ID for a song. (if data['songs'][0]['spotify_id'] is empty, exemption)
