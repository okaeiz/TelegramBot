# TelegramBot
Here I share the codes that I used to develop a telegram bot.


First of all, we need to have a great log of what is going on in the bot.
We have to import just 2 modules:
  1. logging (which is used to send log messages to the terminal.)
  2. termcolor (which is used to beautify the log messages with colors and other text attributes.)
  
      ```	import logging
          from termcolor import colored

          """Audit & Log"""
          logging.basicConfig(
              format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
              level=logging.INFO
          )
          logger = logging.getLogger(__name__)

          logger.info(colored("User X ran the /start command.", "green", attrs=["blink"]))
      ```

