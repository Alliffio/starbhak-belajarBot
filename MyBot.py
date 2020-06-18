import telebot
import mysql.connector

from datetime import date
from  datetime import datetime

import mytoken

TOKEN=mytoken.TOKEN
myBot = telebot.TeleBot(TOKEN)
myDb = mysql.connector.connect(host='localhost',user='root',database='db_siswa')
sql = myDb.cursor()
from telebot import apihelper
timenow = datetime.now()

class MyBot:
    def __init__(self):

        self.message

    @myBot.message_handler(commands=['start','help'])
    def start(message):
        #photo = open()
        #myBot.send_photo(message.from_user.id, photo)
        teks = mytoken.SAPA + "\n-- admin & developer @aliffio1615 - SMK Taruna Bhakti -- "+"\n " \
        "Tanggal "+str(timenow)
        myBot.reply_to(message, teks)

    @myBot.message_handler(commands=['datasiswa'])
    def menu_data_siswa(message):
        query="select nipd,nama,kelas from tabel_siswa"
        sql.execute(query)
        data = sql.fetchall()
        jmldata = sql.rowcount
        datas=''
        if (jmldata >0):
            #print(data)
            #print(data[0])
            no=0
            for x in data:
                no += 1
                datas = datas+ str(x)
                print(datas)
                datas=datas.replace('(','')
                datas=datas.replace(')','')
                datas=datas.replace("'",'')
                datas=datas.replace(",",'')
        else:
            print('data kosong')

        myBot.reply_to(message,str(datas))
print(myDb)
print("-- Bot sedang berjalan --")
myBot.polling(none_stop=True)

