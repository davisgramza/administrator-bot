# authentication-bot
A discord bot for handling recent authentication issues on Discord

## Installation
1. Clone https://www.github.com/davisgramza/authentication-bot
2. Open terminal to cloned directory
3. Execute `pip3 install -r requirements.txt`
4. Open bot.py and add your personal discord bot token to the token variable
   
   i.e. `token = '--token--'`
5. Run by executing
    `python3 bot.py`
    
## Usage

After adding the bot to a discord server you can...
1. `]reimburse role_name permissions`: Reimburses administrator role (defaults to all channel roles)
    1. role_name: Name of role that will be reimbursed to user. Will create a new role with name if not present
    2. permissions: Can leave blank or use all. If empty will reimburse channel permissions while all will give all server permissions
2. `]ping`: Plays ping pong
3. `]hi`: Says hi to the user who executed command

Note: ]help has been disabled by default to minimalize unwanted access to bot commands