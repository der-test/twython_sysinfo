# twython-sysinfo
Thython script containing system information with optional attechment of snapshots created by motion

The string `# coding: utf-8` is necessary for correct formatting of umlauts

Based on djfav's gists over at https://gist.github.com/djfav

## Available stats
### Date and time
* `time`
### CPU temperature
* `temp`
### Memory usage
* `tr(usedmb)`
* `str(totalmb)`
* `str(percent)`

## Installation
* Install twython
* Optional: Install motion and configure snapshots to be taken 
* Clone this repo
* Change `your_data` to the strings from you own twitter app
* Optional: Uncomment one of the lines starting wit `api.`