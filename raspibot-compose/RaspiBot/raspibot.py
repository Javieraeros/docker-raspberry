import telebot
import subprocess
import os

BOT_ID = os.environ['BOT_ID'].replace('"','')
bot = telebot.TeleBot(BOT_ID)

@bot.message_handler(commands=['temperatura'])
def send_temp(message):
    bot.reply_to(message, get_temp())

@bot.message_handler(commands=['ip'])
def ip(message):
    bot.reply_to(message, get_ip())


@bot.message_handler(commands=['disco'])
def disco(message):
    bot.reply_to(message, get_disco())

@bot.message_handler(commands=['grabacion'])
def grabacion(message):
    bot.reply_to(message, get_rec())

def get_ip():
    process = subprocess.Popen(['/usr/bin/curl', 'ifconfig.me'],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    return stdout


def get_temp():
    process = subprocess.Popen(['/opt/vc/bin/vcgencmd', 'measure_temp'],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    return stdout


def get_disco():  
    cmd = "df -h | grep 'Filesystem\|/dev/mmcblk0p2\|/dev/sda1\|/dev/nvme0n1'"
    process = subprocess.Popen([cmd],
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    return stdout

def get_rec():  
    cmd = "ls -R /dev/sdb1/recourdbate | grep part"
    process = subprocess.Popen([cmd],
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    return stdout


bot.polling()
