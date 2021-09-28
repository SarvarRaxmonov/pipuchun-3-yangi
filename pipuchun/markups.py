














from os import name
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
btnprofile = KeyboardButton(' profil ')
profilekey = ReplyKeyboardMarkup(resize_keyboard= True).add(btnprofile)

btnurchannel = InlineKeyboardButton(text='azo bulish', url='https://t.me/uzb143')
btndonesub = InlineKeyboardButton(text='azo buldim', callback_data="subchanneldone")

checksubmenu = InlineKeyboardMarkup(row_width=1)
checksubmenu.insert(btnurchannel)
checksubmenu.insert(btndonesub)





btnmain = InlineKeyboardButton('Quron Tinglang')



btnrandom = InlineKeyboardButton('quron')

btnorder = InlineKeyboardButton('boshqa')

sainmenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnrandom,btnorder, btnmain)







btninfo = KeyboardButton(' quron')

btnmoney = KeyboardButton(' kurs')

othermenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btninfo, btnmoney, btnmain)



####################################################


qorilarni_tanlang = InlineKeyboardMarkup(row_width=1)
qoriasosiy = InlineKeyboardButton(text="Qorilarni tanlang 🎧", callback_data="qori")
qorilarni_tanlang.insert(qoriasosiy)
mainMenu = InlineKeyboardMarkup(row_width=1)
oyatsura = InlineKeyboardMarkup(row_width=1)
qori = InlineKeyboardMarkup(row_width=2)
qorila = InlineKeyboardMarkup(row_width=1)
qorila2 = InlineKeyboardMarkup(row_width=1)
qorila3 = InlineKeyboardMarkup(row_width=1)
qorila4 = InlineKeyboardMarkup(row_width=1)
qorila5 = InlineKeyboardMarkup(row_width=1)
qorila6 = InlineKeyboardMarkup(row_width=1)
qorila7 = InlineKeyboardMarkup(row_width=1)
qorila8 = InlineKeyboardMarkup(row_width=1)
qorila9 = InlineKeyboardMarkup(row_width=1)
qorila10 = InlineKeyboardMarkup(row_width=1)
qorila11 = InlineKeyboardMarkup(row_width=1)
qorila12 = InlineKeyboardMarkup(row_width=1)
qorila13 = InlineKeyboardMarkup(row_width=1)
qorila14 = InlineKeyboardMarkup(row_width=1)
qorila15 = InlineKeyboardMarkup(row_width=1)
btnran = InlineKeyboardButton(text="oyat", callback_data="btnran")
btnqori = InlineKeyboardButton(text="Qorilarni tanlang 🎧", callback_data="btnqori")
btn1 = InlineKeyboardButton(text="1", callback_data="btn1")
btn1e1 = InlineKeyboardButton(text="2", callback_data="btn1e1")
btn1b1 = InlineKeyboardButton(text="3", callback_data="btn1b1")
btn1c1 = InlineKeyboardButton(text="4", callback_data="btn1c1")
btn1d1 = InlineKeyboardButton(text="5", callback_data="btn1d1")
btn1f1 = InlineKeyboardButton(text="6", callback_data="btn1f1")
btn1g1 = InlineKeyboardButton(text="7", callback_data="btn1g1")
btn1h1 = InlineKeyboardButton(text="8", callback_data="btn1h1")
btn1j1 = InlineKeyboardButton(text="9", callback_data="btn1j1")
btn1k1 = InlineKeyboardButton(text="10", callback_data="btn1k1")
btn1l1 = InlineKeyboardButton(text="11", callback_data="btn1k1")
btn1z1 = InlineKeyboardButton(text="12", callback_data="btn1z1")
btn1x1 = InlineKeyboardButton(text="13", callback_data="btn1x1")
btn1v1 = InlineKeyboardButton(text="14", callback_data="btn1v1")
btn1m1 = InlineKeyboardButton(text="15", callback_data="btn1m1")







btnrat = InlineKeyboardButton(text="sura", callback_data="btnrat")


btnoyat = InlineKeyboardButton(text="oyatlar", callback_data="btnoyat")

btnsura = InlineKeyboardButton(text="suralar", callback_data="btnsura")
ortga = InlineKeyboardButton(text="⬅️ Ortga", callback_data="ortga")
ortga2 = InlineKeyboardButton(text="Qorini tanlang", callback_data="ortga2")
ortga2a = InlineKeyboardButton(text="⬅️ Ortga", callback_data="ortga2a")
ortga22a = InlineKeyboardButton(text="⬅️ Ortga", callback_data="ortga22a")
ortga3 = InlineKeyboardButton(text="⬅️ Ortga", callback_data="ortga3")
ortga4 = InlineKeyboardButton(text="⬅️ Ortga", callback_data="ortga4")
ortga5 = InlineKeyboardButton(text="⬅️ Ortga", callback_data="ortga5")
ortga6 = InlineKeyboardButton(text="⬅️ Ortga", callback_data="ortga6")
ortga7 = InlineKeyboardButton(text="⬅️ Ortga", callback_data="ortga7")
ortga8 = InlineKeyboardButton(text="⬅️ Ortga", callback_data="ortga8")
ortga9 = InlineKeyboardButton(text="⬅️ Ortga", callback_data="ortga9")
ortga10 = InlineKeyboardButton(text="⬅️ Ortga", callback_data="ortga10")
ortga11 = InlineKeyboardButton(text="⬅️ Ortga", callback_data="ortga11")
ortga12 = InlineKeyboardButton(text="⬅️ Ortga", callback_data="ortga12")
ortga13 = InlineKeyboardButton(text="⬅️ Ortga", callback_data="ortga13")
ortga14 = InlineKeyboardButton(text="⬅️ Ortga", callback_data="ortga14")
keyingi = InlineKeyboardButton(text="➡️ Keyingi", callback_data="Keyingi")
keyingi2 = InlineKeyboardButton(text="➡️ Keyingi", callback_data="Keyingi2")
keyingi3 = InlineKeyboardButton(text="➡️ Keyingi", callback_data="Keyingi3")
keyingi4 = InlineKeyboardButton(text="➡️ Keyingi", callback_data="Keyingi4")
keyingi5 = InlineKeyboardButton(text="➡️ Keyingi", callback_data="Keyingi5")
keyingi6 = InlineKeyboardButton(text="➡️ Keyingi", callback_data="Keyingi6")
keyingi7 = InlineKeyboardButton(text="➡️ Keyingi", callback_data="Keyingi7")
keyingi8 = InlineKeyboardButton(text="➡️ Keyingi", callback_data="Keyingi8")
keyingi9 = InlineKeyboardButton(text="➡️ Keyingi", callback_data="Keyingi9")
keyingi10 = InlineKeyboardButton(text="➡️ Keyingi", callback_data="Keyingi10")
keyingi11 = InlineKeyboardButton(text="➡️ Keyingi", callback_data="Keyingi11")
keyingi12 = InlineKeyboardButton(text="➡️ Keyingi", callback_data="Keyingi12")
keyingi13 = InlineKeyboardButton(text="➡️ Keyingi", callback_data="Keyingi13")
keyingi14 = InlineKeyboardButton(text="➡️ Keyingi", callback_data="Keyingi14")










obshiyortga = InlineKeyboardButton(text='📋 Birinchi sahifaga', callback_data="obshiyortga")


qori.insert(btnqori)
qorila.insert(btn1)
qorila.insert(ortga)
qorila.insert(keyingi)



qorila2.insert(btn1e1)
qorila2.insert(ortga2a)
qorila2.insert(keyingi2)
qorila2.insert(obshiyortga)


qorila3.insert(btn1b1)
qorila3.insert(ortga22a)
qorila3.insert(keyingi3)
qorila3.insert(obshiyortga)


qorila4.insert(btn1c1)
qorila4.insert(ortga3)
qorila4.insert(keyingi4)
qorila4.insert(obshiyortga)


qorila5.insert(btn1d1)
qorila5.insert(ortga4)
qorila5.insert(keyingi5)
qorila5.insert(obshiyortga)



qorila6.insert(btn1f1)
qorila6.insert(ortga5)
qorila6.insert(keyingi6)
qorila6.insert(obshiyortga)


qorila7.insert(btn1g1)
qorila7.insert(ortga6)
qorila7.insert(keyingi7)
qorila7.insert(obshiyortga)


qorila8.insert(btn1h1)
qorila8.insert(ortga7)
qorila8.insert(keyingi8)
qorila8.insert(obshiyortga)



qorila9.insert(btn1j1) 
qorila9.insert(ortga8)
qorila9.insert(keyingi9)
qorila9.insert(obshiyortga)



qorila10.insert(btn1k1)
qorila10.insert(ortga9)
qorila10.insert(keyingi10)
qorila10.insert(obshiyortga)


qorila11.insert(btn1l1)
qorila11.insert(ortga10)
qorila11.insert(keyingi11)
qorila11.insert(obshiyortga)


qorila12.insert(btn1z1)
qorila12.insert(ortga11)
qorila12.insert(keyingi12)
qorila12.insert(obshiyortga)


qorila13.insert(btn1x1)
qorila13.insert(ortga12)
qorila13.insert(keyingi13)
qorila13.insert(obshiyortga)


qorila14.insert(btn1v1)
qorila14.insert(ortga13)
qorila14.insert(keyingi14)
qorila14.insert(obshiyortga)

qorila15.insert(btn1m1)
qorila15.insert(ortga14)
qorila15.insert(obshiyortga)




allsuralarMaherAlMeaqli = InlineKeyboardMarkup(row_width=4) 

ortgaMaherAlMeaqli = InlineKeyboardButton(text='◀️ Ortga', callback_data="ortgaMaherAlMeaqli") 
MaherAlMeaqlisuralar1 = InlineKeyboardButton(text="1", callback_data="MaherAlMeaqlisuralar1")
MaherAlMeaqlisuralar2 = InlineKeyboardButton(text="2", callback_data="MaherAlMeaqlisuralar2")
MaherAlMeaqlisuralar3 = InlineKeyboardButton(text="3", callback_data="MaherAlMeaqlisuralar3")
MaherAlMeaqlisuralar4 = InlineKeyboardButton(text="4", callback_data="MaherAlMeaqlisuralar4")
MaherAlMeaqlisuralar5 = InlineKeyboardButton(text="5", callback_data="MaherAlMeaqlisuralar5")
MaherAlMeaqlisuralar6 = InlineKeyboardButton(text="6", callback_data="MaherAlMeaqlisuralar6")
MaherAlMeaqlisuralar7 = InlineKeyboardButton(text="7", callback_data="MaherAlMeaqlisuralar7")
MaherAlMeaqlisuralar8 = InlineKeyboardButton(text="8", callback_data="MaherAlMeaqlisuralar8")
MaherAlMeaqlisuralar9 = InlineKeyboardButton(text="9", callback_data="MaherAlMeaqlisuralar9")
MaherAlMeaqlisuralar10 = InlineKeyboardButton(text="10", callback_data="MaherAlMeaqlisuralar10")
MaherAlMeaqlisuralar11 = InlineKeyboardButton(text="11", callback_data="MaherAlMeaqlisuralar11")
MaherAlMeaqlisuralar12 = InlineKeyboardButton(text="12", callback_data="MaherAlMeaqlisuralar12")
MaherAlMeaqlisuralar13 = InlineKeyboardButton(text="13", callback_data="MaherAlMeaqlisuralar13")
MaherAlMeaqlisuralar14 = InlineKeyboardButton(text="14", callback_data="MaherAlMeaqlisuralar14")
MaherAlMeaqlisuralar15 = InlineKeyboardButton(text="15", callback_data="MaherAlMeaqlisuralar15")
MaherAlMeaqlisuralar16 = InlineKeyboardButton(text="16", callback_data="MaherAlMeaqlisuralar16")
allsuralarMaherAlMeaqli.insert(MaherAlMeaqlisuralar1)
allsuralarMaherAlMeaqli.insert(MaherAlMeaqlisuralar2)
allsuralarMaherAlMeaqli.insert(MaherAlMeaqlisuralar3)
allsuralarMaherAlMeaqli.insert(MaherAlMeaqlisuralar4)
allsuralarMaherAlMeaqli.insert(MaherAlMeaqlisuralar5)
allsuralarMaherAlMeaqli.insert(MaherAlMeaqlisuralar6)
allsuralarMaherAlMeaqli.insert(MaherAlMeaqlisuralar7)
allsuralarMaherAlMeaqli.insert(MaherAlMeaqlisuralar8)
allsuralarMaherAlMeaqli.insert(MaherAlMeaqlisuralar9)
allsuralarMaherAlMeaqli.insert(MaherAlMeaqlisuralar10)
allsuralarMaherAlMeaqli.insert(MaherAlMeaqlisuralar11)
allsuralarMaherAlMeaqli.insert(MaherAlMeaqlisuralar12)
allsuralarMaherAlMeaqli.insert(MaherAlMeaqlisuralar13)
allsuralarMaherAlMeaqli.insert(MaherAlMeaqlisuralar14)
allsuralarMaherAlMeaqli.insert(MaherAlMeaqlisuralar15)
allsuralarMaherAlMeaqli.insert(MaherAlMeaqlisuralar16)

MaherAlMeaqlisuralarhammasi1 = InlineKeyboardButton(text="📻 hamma audiolar", callback_data="MaherAlMeaqlisuralarhammasi1")
allsuralarMaherAlMeaqli.insert(MaherAlMeaqlisuralarhammasi1)

ortgaMaherAlMeaqlimenu = InlineKeyboardButton(text='⏳ Bosh menuga', callback_data="ortgaMaherAlMeaqlimenu")

ortgaMaherAlMeaqli1 = InlineKeyboardMarkup(row_width=1)
allsuralarMaherAlMeaqli.insert(ortgaMaherAlMeaqlimenu)
ortgaMaherAlMeaqli1.insert(ortgaMaherAlMeaqli)






mainMenu.insert(btnran)
mainMenu.insert(btnrat)
oyatsura.insert(ortga2)
oyatsura.insert(btnsura)
oyatsura.insert(btnoyat)







