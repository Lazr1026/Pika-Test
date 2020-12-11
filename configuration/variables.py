import discord, os

# General Cofiguration
STATUSTYPE = discord.ActivityType.watching # The current action type that appears by default.
STATUSACTIVITY = "Ninvord" + " (p!)" # The current action activity that appears by default.

# Role Configuration
SERVERBOT = 769807124631912456 # The ID of the @Server Bot role.
SERVEROWNER = 769807124631912455 # The ID of the @Server Owner role.
SERVERMODERATOR = 769807124631912454 # The ID of the @Server Moderator role.
SERVERAFFILIATE = 769807124631912452 # The ID of the @Server Affiliate role.
SERVERBOOSTER = 769811831857872896 # The ID of the @Server Booster role.
NINCORDSINGLESCHAMPION = 769807124611072029 # The ID of the @Nincord Singles Champion role.
NINCORDDOUBLESCHAMPION = 769807124611072028 # The ID of the @Nincord Doubles Champion role.
NINCORDSIDEVENTCHAMPION = 769807124611072027 # The ID of the @Nincord Side Event Champion role.
PROJECTDEVELOPER = 769807124611072024 # The ID of the @Project Developer role.
BOTCONTRIBUTOR = 769807124611072025 # The ID of the @Bot Contributor role.
CONTENTCREATOR = 769807124611072026 # The ID of the @Content Creator role.
TRUSTEDMEMBER = 769807124611072022 # The ID of the @Active Member role.

# Channel Configuration
SERVERRULES = 769807124825767967 # The ID of the #rules channel.
SERVERAFFILIATES = 769807124825767968 # The ID of the #affiliates channel.
ANNOUNCEMENTS = 769813235091898388 # The ID of the #announcements channel.
VOTING = 769813278259544105 # The ID of the #voting channel.
GENERALCHAT = 769807124825767972 # The ID of the #general-chat text channel.
RANDOMCHAT = 769807124825767973 # The ID of the #random-chat text channel.
GENERALCHATV = 769807125102198785 # The ID of the General Chat voice channel.
RANDOMCHATV = 769807125102198786 # The ID of the Random Channel voice channel.
BOTCOMMANDS = 769807125102198790 # The ID of the #bot-commands text channel.
BOTDISCUSSION = 769807125102198791 # The ID of the #bot-discussion channel.
BOTCOMMANDSV = 769807125102198792 # The ID of the Bot Commands voice channel.
SMASHGENERAL = 769807125361852418 # The ID of the #smash-general channel.
SMASHBATTLES = 769807125361852419 # The ID of the #smash-battles channel.
SINGLESCHATV = 769807125361852420 # The ID of the Singles Chat voice channel.
DOUBLESCHATV = 769807125361852421 # The ID of the Doubles Chat voice channel.
ARENACHATV = 769807125361852422 # The ID of the Arena Chat voice channel.
POKEMONGENERAL = 769807125361852425 # The ID of the #pokémon-general channel.
POKEMONTRADES = 769807125526085643 # The ID of the #pokémon-trades channel.
POKEMONBATTLES = 769807125526085644 # The ID of the #pokémon-battles channel.
TRADECHATV = 769807125526085645 # The ID of the Trade Chat voice channel.
BATTLECHATV = 769807125526085646 # The ID of the Battle Chat voice channel.
DIRECTCHAT = 769807125526085648 # The ID of the #direct-chat text channel.
TOURNAMENTCHAT = 769807125526085649 # The ID of the #tournament-chat text channel.
DIRECTCHATV = 769807125526085651 # The ID of the Direct Chat voice channel.
TOURNAMENTCHATV = 769807125526085652 # The ID of the Tournament Chat voice channel.
TRUSTEDCHAT = 769807124825767974 # The ID of the #trusted-chat channel.
MODERATORCHAT = 769807124825767975 # The ID of the #moderator-chat text channel.
TRUSTEDCHATV = 769807125102198787 # The ID of the Trusted Chat voice channel.
MODERATORCHATV = 769807125102198788 # The ID of the Moderator Chat voice channel.
BOTLOGS = 769807125714042901 # The ID of the #bot-logs channel.
REQUESTLOGS = 769807125714042902 # The ID of the #request-logs channel.
ACTIONLOGS = 769807125714042903 # The ID of the #action-logs channel.
MESSAGELOGS = 769807125714042904 # The ID of the #message-logs channel.
SERVERLOGS = 769807125714042905 # The ID of the #server-logs channel.

# Essential Configuration
if os.path.exists("configuration/secrets.py"):
    import configuration.secrets as secrets
    DBACCOUNT = secrets.DBACCOUNT # The key URL for the database account.
    BOTTOKEN = secrets.BOTTOKEN # The Discord bot authorization token.
    MONGODBURI = secrets.MONGODBURI # The URI for the bot's database.
    TWITTERAPI = secrets.TWITTERAPI # The key to access the Twitter API.
    TWITTERSECRET = secrets.TWITTERSECRET # The secret key to access the API key.
    TWITTERBEARER = secrets.TWITTERBEARER # The bearer key to authorize access to Twitter.
    SAKURAIHOOK = secrets.SAKURAIHOOK # The intergration URL for the Masahiro Sakurai webhook.
else:
    DBACCOUNT = os.environ["DATABASE_ACCOUNT"] # The key URL for the database account.
    BOTTOKEN = os.environ["BOT_TOKEN"] # The Discord bot authorization token.
    MONGODBURI = os.environ["MONGODB_URI"] # The URI for the bot's database.
    TWITTERAPI = os.environ["TWITTER_API"] # The key to access the Twitter API.
    TWITTERSECRET = os.environ["TWITTER_SECRET"] # The secret key to access the API key.
    TWITTERBEARER = os.environ["TWITTER_BEARER"] # The bearer key to authorize access to Twitter.
    SAKURAIHOOK = os.environ["SAKURAI_WEBHOOK"] # The intergration URL for the Masahiro Sakurai webhook.