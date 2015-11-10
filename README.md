# Multiview
labels UMDs at Multiviews16 when switching Videoinput 

Its changes the Input Labels at a Blackmagic Multiview 16 when switching VideoInput with a Videohub.

For our installation we have a default labeling in Multiview it starts with "%input number |" ---Input Labels will be added after "|"

You anly need to configuere:
server_address = ('192.168.1.60', 9990)# IP of your Videohub
sockvcs.connect(server_address)
server_address = ('192.168.1.61', 9990)# IP of your Multiview
sockmv.connect(server_address)

Multiviewer is connected to the first 16 Videooutputs from Videohub.
It works with a Universal Videohub 72x72 and a Firmware earlier than 6.1.1, version shouldn't matter

runs an a raspberry pi, with wheezy and python 2.7
If you change input Labels at your Videohub script needs to restart
