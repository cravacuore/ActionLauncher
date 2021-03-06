﻿# -*- coding: utf-8 -*-
# Action Launcher Bot: This is a bot how can shoots differents action depends commands
# Code wrote by Zagur of PortalLinux.es and modified for NeoRanger of neositelinux.com.ar
# For a good use of the bot please read the README file

import telebot 
from telebot import types 
import time 
import random
import datetime
import token
import user
import os
import subprocess
import commands

TOKEN =  token.token_id

bot = telebot.TeleBot(TOKEN) # Creamos el objeto de nuestro bot.
#############################################
#Listener
def listener(messages):
	for m in messages: 
		cid = m.chat.id 
		if m.content_type == 'text':
			print ("[" + str(cid) + "]: " + m.text)
bot.set_update_listener(listener) #  
#############################################
#Funciones

@bot.message_handler(commands=['test']) 
def command_test(m):
	cid = m.chat.id
	uid = m.from_user.id
	if uid != user.user_id:
		bot.send_message( cid, "You can't use the bot")
		return
	bot.send_message( cid, "This is a test")

@bot.message_handler(commands=['help']) 
def command_ayuda(m): 
	cid = m.chat.id 
	uid = m.from_user.id
	if uid != user.user_id:
		bot.send_message( cid, "You can't use the bot")
		return	
	bot.send_message( cid, "Comandos Disponibles: /help /temp /free /df /uptime /info /who /shutdown /reboot")

@bot.message_handler(commands=['temp']) 
def command_temp(m): 
	temp = commands.getoutput('sudo /opt/vc/bin/vcgencmd/ measure_temp')
	cid = m.chat.id
	uid = m.from_user.id
	if uid != user.user_id:
		bot.send_message( cid, "You can't use the bot")
		return
	bot.send_message( cid, temp)

@bot.message_handler(commands=['df']) 
def command_espacio(m): 
	info = commands.getoutput('df -h')
	cid = m.chat.id 
	uid = m.from_user.id
	if uid != user.user_id:
		bot.send_message( cid, "You can't use the bot")
		return	
	bot.send_message( cid, info)

@bot.message_handler(commands=['uptime']) 
def command_tiempo(m): 
	tiempo = commands.getoutput('uptime')
	cid = m.chat.id
	uid = m.from_user.id
	if uid != user.user_id:
		bot.send_message( cid, "You can't use the bot")
		return
	bot.send_message( cid, tiempo)

@bot.message_handler(commands=['free']) 
def command_libre(m): 
	libre = commands.getoutput('free -m')
	cid = m.chat.id 
	uid = m.from_user.id
	if uid != user.user_id:
		bot.send_message( cid, "You can't use the bot")
		return	
	bot.send_message( cid, libre)

@bot.message_handler(commands=['info']) 
def command_libre(m): 
	screenfetch = commands.getoutput('screenfetch -n')
	cid = m.chat.id 
	uid = m.from_user.id
	if uid != user.user_id:
		bot.send_message( cid, "You can't use the bot")
		return	
	bot.send_message( cid, screenfetch) 

@bot.message_handler(commands=['who']) 
def command_libre(m): 
    who = commands.getoutput('who')
    cid = m.chat.id 
    uid = m.from_user.id
    if uid != user.user_id:
		bot.send_message( cid, "You can't use the bot")
		return    
    bot.send_message( cid, who) 
    
#@bot.message_handler(commands=['shutdown']) 
#def command_apagar(m): 
#    apagar = commands.getoutput('poweroff')
#    cid = m.chat.id 
	#uid = m.from_user.id
	#if uid != user.user_id:
		#bot.send_message( cid, "You can't use the bot")
		#return
#    bot.send_message( cid, apagar) 
    
#@bot.message_handler(commands=['reboot']) 
#def command_reboot(m): 
#    reiniciar = commands.getoutput('reboot')
#    cid = m.chat.id 
	#uid = m.from_user.id
	#if uid != user.user_id:
		#bot.send_message( cid, "You can't use the bot")
		#return
#    bot.send_message( cid, reiniciar)
	
@bot.message_handler(commands=['id']) 
def command_id(m): 
	cid = m.chat.id 
	bot.send_message(cid, cid)		

#############################################
#Peticiones
bot.polling(none_stop=True) # Con esto, le decimos al bot que siga funcionando incluso si encuentra algun fallo.
