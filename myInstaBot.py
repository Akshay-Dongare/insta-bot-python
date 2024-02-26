from instabot import Bot
import config
bot=Bot()
bot.login(username=config.username,password=config.password)
bot.upload_photo("hello_world.png",caption= "hello world")