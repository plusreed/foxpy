foxpy
---
fox is a discord bot written in python with the intent of making a user-friendly, easy to maintain bot. <br />
this bot is in an **alpha** state. i highly encourage you to **not** base your bot off of this (just yet, anyways.)

### usage <br />
*(yes, i know. this isn't that detailed. feel free to open a pr with changes and explain it further if you'd like.)* 
<br />
first, fill in `config_example.py` with the necessary keys. then, rename `config_example.py` to `config.py`
(not doing this will result in the bot printing out an error.)
<br />
then, to start the bot, make sure you're running python 3.5+ (you can check this by running `python -V`) and that you
also have the dependencies fulfilled.
in a terminal, run `pip install -r requirements.txt`. this will install all the dependencies needed for fox.
after that, assuming you've filled out everything, run `python main3.py` (script name will be changed soon) and fox
should now be up and listening for commands.

### what is done <br />
(these **should** work, i haven't done extensive testing on them) <br />
`plugins.admin.eval` <br />
`plugins.admin.shutdown` <br />
`plugins.core.ping` <br />

### what is not done <br />
checking if the message author's id is in the admin table doesn't work so well as far as i know. <br />
music isn't done yet (it's getting there), the last.fm plugin is a major WIP, and math isn't anywhere near done yet.
