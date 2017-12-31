# Twitter Bot - Ghost of Billboard Past

I took the code from from my Billboard Number 1s repository, rewrote it in Python, and turned it into a Twitter Bot.

Every time this Python script is called it will grab the information of one chart topping single from a random date, and post it to your timeline. I put this file on one of my servers and set up a cron job to run the script every 5 hours. The Twitter bot can be found here <a href="https://twitter.com/BillboardGhost">@BillboardGhost</a>

The mention script takes an array of users and tweets them the Billboard #1 for the day that they created their Twitter account. This script only needs to be run once and sends out a Tweet every 10 minutes. 

This is my first project written in Python

# Update

The Twitter bot has been met with some very positive acclaim!

<p style="text-align:center"><img src="https://i.imgur.com/qP0TuJk.png"></p>

<p style="text-align:center"><img src="https://i.imgur.com/wimEp5G.png"></p>

# TODO

<strike>1. I'd like to add functionality to Tweet at people (semi-random people of interest) with the #1 Billboard hit on the day that they joined twitter.</strike> <strong>Complete</strong>

<strike>2. Fix a bug that occurs when the bot cannot find the Spotify ID for a song.</strike> <strong>Complete</strong>
