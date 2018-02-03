# twython-sysinfo
Twython script containing system information with optional attachment of snapshots created by motion.

The string `# coding: utf-8` is necessary for correct formatting of umlauts.

## Available stats
### Date and time
* `time`
### CPU temperature
* `temp`
### Memory usage
* `tr(usedmb)`
* `str(totalmb)`
* `str(percent)`
### Network
* `ip` (language specific) 
** available: en, de
** standard: de
* `extip`
## Installation
* Install twython
* Optional: Install dnsutils to display external IP (dig)
* Optional: Install motion
* Configure snapshots to be taken (config details will be added later)
* Add `input -1` to the end of /etc/motion/motion.conf to avoid problems with USB cameras
* Clone this repo
* Change `your_data` to the strings from you own twitter app
## Configuration
* Optional: Uncomment one of the lines starting wit `api.` depending on the usage of snapshots
** Tweet with media is set as standard. Can be switched to text only.
* `photo` can be changed to reflect motion config
* `tweet` 

Based on djfav's gists over at https://gist.github.com/djfav
