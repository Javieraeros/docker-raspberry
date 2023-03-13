import telebot
import subprocess
import os

BOT_ID = os.environ['BOT_ID'].replace('"','')
bot = telebot.TeleBot(BOT_ID)

@bot.message_handler(commands=['vention'])
def venti_on(message):
    bot.reply_to(message, vention())

@bot.message_handler(commands=['ventioff'])
def venti_off(message):
    bot.reply_to(message, ventioff())


@bot.message_handler(commands=['temperatura'])
def send_temp(message):
    bot.reply_to(message, get_temp())

@bot.message_handler(commands=['ip'])
def ip(message):
    bot.reply_to(message, get_ip())


@bot.message_handler(commands=['disco'])
def disco(message):
    bot.reply_to(message, get_disco())


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
    cmd = "df -h | grep 'Filesystem\|overlay\|/dev/sda1\|/dev/sdb1'"
    process = subprocess.Popen([cmd],
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    return stdout

def vention():
    ventilador = "/home/pi/ventilador"
    cmd = "ssh pi@retropie 'touch {}'".format(ventilador)    
    process = subprocess.Popen([cmd],
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    return "Ventilador encendido"

def ventioff():
    ventilador = "/home/pi/ventilador"
    cmd = "ssh pi@retropie 'rm {}'".format(ventilador)    
    process = subprocess.Popen([cmd],
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    return "Ventilador apagado"

bot.polling()
