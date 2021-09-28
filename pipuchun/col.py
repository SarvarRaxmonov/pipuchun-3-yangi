

import logging
from typing import Literal

from aiogram import  Bot, Dispatcher, executor, types
from aiogram.types import reply_keyboard
from aiogram.types.inline_keyboard import InlineKeyboardMarkup
from telegram import ParseMode
TOKENn = '1979983147:AAF5Ypts5HFaJw34TofEAJfkwtGfoPJ348U'
logging.basicConfig(level=logging.INFO)


bot = Bot(token=TOKENn)
dp = Dispatcher(bot)
CHANNEL_ID = '@uzb143'
import markups as nav
cd = ' \n  \n <b>1.</b> Al-Faatiha (سُورَةُ ٱلْفَاتِحَةِ) \n <b>2.</b> Al-Baqara (سُورَةُ البَقَرَةِ) \n <b>3.</b> Aal-i-Imraan (سُورَةُ آلِ عِمۡرَانَ) \n <b>4.</b> An-Nisaa (سُورَةُ النِّسَاءِ) \n <b>5.</b> Al-Maaida (سُورَةُ المَائـِدَةِ) \n <b>6.</b> Al-An\'aam (سُورَةُ الأَنۡعَامِ) \n <b>7.</b> Al-A\'raaf (سُورَةُ الأَعۡرَافِ) \n <b>8.</b> Al-Anfaal (سُورَةُ الأَنفَالِ) \n <b>9.</b> At-Tawba (سُورَةُ التَّوۡبَةِ) \n <b>10.</b> Yunus (سُورَةُ يُونُسَ) \n <b>11.</b> Hud (سُورَةُ هُودٍ) \n <b>12.</b> Yusuf (سُورَةُ يُوسُفَ) \n <b>13.</b> Ar-Ra\'d (سُورَةُ الرَّعۡدِ) \n <b>14.</b> Ibrahim (سُورَةُ إِبۡرَاهِيمَ) \n <b>15.</b> Al-Hijr (سُورَةُ الحِجۡرِ) \n'
  


























def check_sub_channel(chat_member):
    
    if chat_member['status'] != 'left':
        return True
    else:
        return False

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    if message.chat.type == 'private':
           if check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)):
               await bot.send_message(message.from_user.id, 'salom ishladi' , reply_markup=nav.checksubmenu)
           else:
               await bot.send_message(message.from_user.id, 'ishlamadi', reply_markup=nav.checksubmenu)



@dp.callback_query_handler(text="subchanneldone")
async def subchanell(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    if check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)):
        await bot.send_message(message.from_user.id,'azo buldi', reply_markup=nav.sainmenu)
    else:
        await bot.send_message(message.from_user.id, 'aldama', reply_markup=nav.checksubmenu)




@dp.message_handler()
async def botmeseg(message: types.Message):
  
    if message.chat.type == 'private':
        if check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)):

   
           if message.text == 'Quron Tinglang':
              await bot.send_message(message.from_user.id, 'Quron tinglang 🤲', reply_markup=nav.qori)
           elif message.text == 'boshqa':
               await bot.send_message(message.from_user.id, 'boshqa', reply_markup=nav.othermenu, )
           elif message.text == 'info':
               await bot.send_message(message.from_user.id, 'salomlar bulsin', reply_markup=nav.mainMenu )
     
        else:
            await bot.send_message(message.from_user.id, 'aldama', reply_markup=nav.checksubmenu)


@dp.callback_query_handler(text="btnqori")
async def random(message: types.Message):
    if check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)):
     
            await bot.delete_message(message.from_user.id,  message.message.message_id)
            await bot.send_message(message.from_user.id , " <b>•______________________________________•ㅤ </b> \n <b>1.</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>2.</b> Abdulbasit Abdulsamad (عبدالباسط عبدالصمد) \n <b>3.</b> Raad Al Kurdi (رعد محمد الكردي) \n <b>4.</b> Abdulrahman Alsudaes (عبدالرحمن السديس ) \n <b>5.</b> Mohammed Siddiq Al-Minshawi (محمد صديق المنشاوي) \n <b>6.</b> Mohammed Ayyub (محمد أيوب) \n <b>7.</b> Idrees Abkr (إدريس أبكر) \n <b>8.</b> Abdullah Basfer (عبدالله بصفر) \n <b>9.</b> Mishary Alafasi (مشاري العفاسي) \n <b>10.</b> Mohammed Ayyub (محمد أيوب) \n <b>11.</b> Nasser Alqatami (ناصر القطامي)\n <b>12.</b> Zaki Daghistani (زكي داغستاني) \n <b>13.</b> Khalifa Altunaiji (خليفة الطنيجي) \n <b>14.</b> Sami Al-Hasn (سامي الحسن) \n <b>15.</b> Sahl Yassin (سهل ياسين)" , parse_mode='HTML' ,reply_markup=nav.qorila)
    
    else:
            await bot.send_message(message.from_user.id, 'aldama', reply_markup=nav.checksubmenu)



@dp.callback_query_handler(text="btnqori2")
async def random(message: types.Message):
    if check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)):
     
            await bot.delete_message(message.from_user.id,  message.message.message_id)
            await bot.send_message(message.from_user.id , " <b>•______________________________________•ㅤ </b> \n  \n  <b>1.</b>  \n <b>2.</b> Abdulbasit Abdulsamad (عبدالباسط عبدالصمد) \n <b>3.</b> Raad Al Kurdi (رعد محمد الكردي) \n <b>4.</b> Abdulrahman Alsudaes (عبدالرحمن السديس ) \n <b>5.</b> Mohammed Siddiq Al-Minshawi (محمد صديق المنشاوي) \n <b>6.</b> Mohammed Ayyub (محمد أيوب) \n <b>7.</b> Idrees Abkr (إدريس أبكر) \n <b>8.</b> Abdullah Basfer (عبدالله بصفر) \n <b>9.</b> Mishary Alafasi (مشاري العفاسي) \n <b>10.</b> Mohammed Ayyub (محمد أيوب) \n <b>11.</b> Nasser Alqatami (ناصر القطامي)\n <b>12.</b> Zaki Daghistani (زكي داغستاني) \n <b>13.</b> Khalifa Altunaiji (خليفة الطنيجي) \n <b>14.</b> Sami Al-Hasn (سامي الحسن) \n <b>15.</b> Sahl Yassin (سهل ياسين)" , parse_mode='HTML' ,reply_markup=nav.qorila2)
    
    else:
            await bot.send_message(message.from_user.id, 'aldama', reply_markup=nav.checksubmenu)



 
@dp.callback_query_handler(text="qoriasosiy")
async def sura(message: types.Message):
       
       await message.message.edit_text(" <b>•______________________________________•ㅤ </b> \n <b>1.</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>2.</b> Abdulbasit Abdulsamad (عبدالباسط عبدالصمد) \n <b>3.</b> Raad Al Kurdi (رعد محمد الكردي) \n <b>4.</b> Abdulrahman Alsudaes (عبدالرحمن السديس ) \n <b>5.</b> Mohammed Siddiq Al-Minshawi (محمد صديق المنشاوي) \n <b>6.</b> Mohammed Ayyub (محمد أيوب) \n <b>7.</b> Idrees Abkr (إدريس أبكر) \n <b>8.</b> Abdullah Basfer (عبدالله بصفر) \n <b>9.</b> Mishary Alafasi (مشاري العفاسي) \n <b>10.</b> Mohammed Ayyub (محمد أيوب) \n <b>11.</b> Nasser Alqatami (ناصر القطامي)\n <b>12.</b> Zaki Daghistani (زكي داغستاني) \n <b>13.</b> Khalifa Altunaiji (خليفة الطنيجي) \n <b>14.</b> Sami Al-Hasn (سامي الحسن) \n <b>15.</b> Sahl Yassin (سهل ياسين)" , parse_mode='HTML', reply_markup=nav.qorila)

@dp.callback_query_handler(text="Keyingi")
async def sura(message: types.Message):
       
       await message.message.edit_text(" <b>•______________________________________• </b> \n  \n <b>16.</b> Saad Al-Ghamdi (سعد الغامدي) \n <b>17.</b> Khalid Abdulkafi (خالد عبدالكافي) \n <b>18. </b>Tawfeeq As-Sayegh (توفيق الصايغ) \n <b>19.</b> Adel Ryyan (عادل ريان) \n <b>20.</b> Zakaria Hamamah (زكريا حمامة) \n <b>21.</b> Slaah Bukhatir (القارئ صلاح بو خاطر) \n <b>22.</b> Abdelbari Al-Toubayti (عبدالبارئ الثبيتي) \n <b>23.</b> Abdulaziz Az-Zahrani (عبدالعزيز الزهراني) \n <b>24.</b> Abdullah Al-Burimi (عبدالله البريمي) \n <b>25.</b> Abdullah Al-Mattrod (عبدالله المطرود) \n <b>26.</b> Abdullah Al-Johany (عبدالله عواد الجهني) \n <b>27.</b> Abdulrasheed Soufi (عبدالرشيد صوفي) \n <b>28.</b> Abdulmohsin Al-Harthy (عبدالمحسن الحارثي) \n <b>29.</b> Abdulmohsin Al-Askar (عبدالمحسن العسكر) \n <b>30.</b> Salah Alhashim (صلاح الهاشم)",parse_mode='HTML' , reply_markup=nav.qorila2)
 

  
@dp.callback_query_handler(text="Keyingi2")
async def sura(message: types.Message):

       await message.message.edit_text(" <b>•______________________________________•ㅤ </b> \n \n <b>31.</b> Salah Alhashim (صلاح الهاشم) \n <b>32.</b> Alhusayni Al-Azazi (الحسيني العزازي) \n <b>33.</b> Khalid Al-Jileel (خالد الجليل)\n <b>34.</b> Fawaz Alkabi (فواز الكعبي) \n <b>35.</b> Salah Albudair (صلاح البدير) \n <b>36.</b> Fahad Al-Kandari (فهد الكندري) \n <b>37.</b> Fares Abbad (فارس عباد) \n <b>38.</b> Nabil Al Rifay (نبيل الرفاعي) \n <b>39.</b> Walid Al-Dulaimi (وليد الدليمي) \n <b>40.</b> Yasser Al-Dosari (ياسر الدوسري) \n <b>41.</b> Yasser Al-Qurashi (ياسر القرشي) \n <b>42.</b> Yahya Hawwa (يحيى حوا) \n <b>43.</b> Yousef Alshoaey (يوسف الشويعي) \n <b>44.</b> Majed Al-Enezi (ماجد العنزي) \n <b>45.</b> Rachid Belalya (رشيد بلعالية)",parse_mode='HTML' , reply_markup=nav.qorila3)
 
 
@dp.callback_query_handler(text="Keyingi3")
async def sura(message: types.Message):
       
       await message.message.edit_text(" <b>•______________________________________•  </b> \n  \n <b>46.</b> Alzain Mohammad Ahmad (الزين محمد أحمد) \n <b>47.</b> Al-Qaria Yassen (القارئ ياسين) \n <b>48.</b> Rachid Belalya (رشيد بلعالية) \n <b>49.</b> Rasheed Ifrad (رشيد إفراد) \n <b>50.</b> Hamad Al Daghriri (حمد الدغريري) \n <b>51.</b> Lafi Al-Oni (لافي العوني) \n <b>52.</b> Abdulrasheed Soufi (عبدالرشيد صوفي) \n <b>53.</b> Abdullah Al-Kandari (عبدالله الكندري) \n <b>54.</b> Saber Abdulhakm (صابر عبدالحكم) \n <b>55.</b> Ahmed Amer (أحمد عامر) \n <b>56.</b> Malik shaibat Alhamed (مالك شيبة الحمد) \n <b>57.</b> Abdulmajeed Al-Arkani (عبدالمجيد الأركاني) \n <b>58.</b> Mustafa Ismail (مصطفى إسماعيل) \n <b>59.</b> Ahmad Shaheen (أحمد خليل شاهين) \n <b>60.</b> Omar Al-Qazabri' (عمر القزابري)",parse_mode='HTML' , reply_markup=nav.qorila4)
 

@dp.callback_query_handler(text="Keyingi4")
async def sura(message: types.Message):
       
       await message.message.edit_text(" <b>•______________________________________•  </b> \n  \n <b>61.</b> Mahmoud Khalil Al-Hussary (محمود خليل الحصري) \n <b>62.</b> Saad Almqren (سعد المقرن) \n <b>63.</b> Omar Al-Qazabri\' (عمر القزابري) \n <b>64.</b> Akram Alalaqmi (أكرم العلاقمي) \n <b>65.</b> Abdulrahman Al-Majed (عبدالرحمن الماجد) \n <b>66.</b> Emad Hafez (عماد زهير حافظ) \n <b>67.</b> Shirazad Taher (شيرزاد عبدالرحمن طاهر) \n <b>68.</b> Salah Alhashim (صلاح الهاشم) \n <b>69.</b> Yasser Al-Faylakawi (ياسر الفيلكاوي) \n <b>70.</b> Khalid Algamdi (خالد الغامدي) \n <b>71.</b> Ali Hajjaj Alsouasi (علي حجاج السويسي) \n <b>72.</b> Ramadan Shakoor (رمضان شكور) \n <b>73.</b> Mohammad Abdullkarem (محمد عبدالكريم) \n <b>74.</b> Nasser Almajed (ناصر الماجد) \n <b>75.</b> Muftah Alsaltany (مفتاح السلطني)  ",parse_mode='HTML' , reply_markup=nav.qorila5)
 

@dp.callback_query_handler(text="Keyingi5")
async def sura(message: types.Message):

       await message.message.edit_text(" <b>•______________________________________•  </b> \n  \n <b>76.</b> Ahmad Deban (أحمد ديبان)  \n <b>77.</b> Khalid Al-Shoraimy (خالد الشريمي) \n <b>78.</b> Ustaz Zamri (استاذ زامري) \n <b>79.</b> Haitham Aldukhain (هيثم الدخين) \n <b>80.</b>  Mahmoud Khalil Al-Hussary (محمود خليل الحصري) \n <b>81.</b>  Ahmed Al-trabulsi (أحمد الطرابلسي) \n <b>82.</b> Abdulbasit Abdulsamad (عبدالباسط عبدالصمد) \n <b>83.</b> Ibrahim Al-Jebreen (ابراهيم الجبرين) \n <b>84.</b>  Shaban Al-Sayiaad (شعبان الصياد) \n <b>85.</b> Waleed Alnaehi (وليد النائحي) \n <b>86.</b> Mohammad Al-Airawy (محمد الأيراوي) \n <b>87.</b> Mohammad Refat (محمد رفعت) \n <b>88.</b> Mohammed Al-Barrak (محمد البراك) \n <b>89.</b> Abdullah Al-Mousa (عبدالله الموسى) \n <b>90.</b> Muftah Alsaltany (مفتاح السلطني)",parse_mode='HTML' , reply_markup=nav.qorila6)
 

@dp.callback_query_handler(text="Keyingi6")
async def sura(message: types.Message):
       
        await message.message.edit_text(" <b>•______________________________________•  </b> \n  \n <b>91.</b> Ahmad Deban (أحمد ديبان) \n <b>92.</b> Rogayah Sulong (رقية سولونق) \n <b>93.</b> Abdulmohsin Al-Obaikan (عبدالمحسن العبيكان) \n <b>94.</b> Rami Aldeais (رامي الدعيس) \n <b>95.</b> Wasel Almethen (واصل المذن) \n <b>96.</b> Shirazad Taher (شيرزاد عبدالرحمن طاهر) \n <b>97.</b> Salah Alhashim (صلاح الهاشم) \n <b>98.</b> Ibrahim Aldosari (ابراهيم الدوسري) \n <b>99.</b> Muftah Alsaltany (مفتاح السلطني) \n <b>100.</b> Mohammad Abdullkarem (محمد عبدالكريم) \n <b>101.</b> Abdul Aziz Al-Ahmad (عبدالعزيز الأحمد) \n <b>102.</b> Ibrahim Al-Akdar (إبراهيم الأخضر) \n <b>103.</b> Saleh Alsahood (صالح الصاهود) \n <b>104.</b> Yasser Al-Mazroyee (ياسر المزروعي) \n <b>105.</b> Ali Jaber (علي جابر)",parse_mode='HTML' , reply_markup=nav.qorila7)
 


@dp.callback_query_handler(text="Keyingi7")
async def sura2(message: types.Message):
       
       await message.message.edit_text(" <b>•______________________________________•</b> \n  \n <b>106.</b> Mohammed Al-Muhasny (محمد المحيسني) \n <b>107.</b> Saidin Abdulrahman (سيدين عبدالرحمن) \n <b>108.</b> Nasser Alosfor (ناصر العصفور) \n <b>109.</b> Abdulrahman Aloosi (عبدالرحمن العوسي) \n <b>110.</b> Mushaf Ibrahim Al-Asiri (مصحف ابراهيم العسيري) \n <b>111.</b> Mahmoud Ali  Albanna (محمود علي البنا) \n <b>112.</b> Bader Alturki (بدر التركي) \n <b>113.</b> Hitham Aljadani (هيثم الجدعاني) \n <b>114.</b> Ibrahim Aljormy (ابراهيم الجرمي) \n <b>115.</b> Sami Al-Dosari (سامي الدوسري) \n <b>116.</b> Jamal Addeen Alzailaie (جمال الدين الزيلعي) \n <b>117.</b> Mohammad Al-Abdullah (محمد عبدالحكيم سعيد العبدالله) \n <b>118.</b> Salah Musali (صلاح مصلي) \n<b>119.</b> Muftah Alsaltany (مفتاح السلطني) \n<b>120.</b> Mahmoud Khalil Al-Hussary (محمود خليل الحصري) \n",parse_mode='HTML' , reply_markup=nav.qorila8)
  

@dp.callback_query_handler(text="Keyingi8")
async def sura2(message: types.Message):

       await message.message.edit_text(" <b>•______________________________________•</b> \n  \n <b>121.</b> Ahmad Al Nufais (أحمد النفيس) \n <b>122.</b> Salman Alotaibi (سلمان العتيبي) \n <b>123.</b> Abdullah Albuajan (عبدالله البعيجان) \n <b>124.</b> Shaik Abu Bakr Al Shatri (أبوبكر الشاطري) \n <b>125.</b> Abdullah Khayyat (عبدالله خياط) \n <b>126.</b> Mahmoud Khalil Al-Hussary (محمود خليل الحصري) \n <b>127.</b> Maher Shakhashero (ماهر شخاشيرو) \n <b>128.</b> Younes Souilass (يونس اسويلص) \n <b>129.</b> Mohammad AlMonshed (محمد المنشد) \n <b>130.</b> Ahmed Al-trabulsi (أحمد الطرابلسي) \n <b>131.</b> Rodziah Abdulrahman (رضية عبدالرحمن) \n <b>132.</b> Ahmad Alhuthaifi (أحمد الحذيفي) \n <b>133.</b> Mustafa Al-Lahoni (مصطفى اللاهوني) \n <b>134.</b> Mohammad Albukheet (محمد البخيت) \n <b>135.</b> Youssef Edghouch (يوسف الدغوش) \n",parse_mode='HTML' , reply_markup=nav.qorila9)
  

@dp.callback_query_handler(text="Keyingi9")
async def sura2(message: types.Message):

       await message.message.edit_text(" <b>•______________________________________•</b> \n  \n <b>136.</b> Muamar (From Indonesia) (معمر الأندونيسي) \n <b>137.</b> Abdullah Kamel (عبدالله كامل) \n <b>138.</b> Mohammed Siddiq Al-Minshawi (محمد صديق المنشاوي) \n <b>139.</b> Islam Sobhi (إسلام صبحي) \n <b>140.</b> Ali Alhuthaifi (علي الحذيفي) \n <b>141.</b> Ahmad Al-Hawashi (أحمد الحواشي) \n <b>142.</b> Abdullah Qaulan (عبدالله غيلان) \n <b>143.</b> Adel Al-Khalbany (عادل الكلباني) \n <b>144.</b> Hussain Alshaik (حسين آل الشيخ) \n <b>145.</b> Mahmoud Khalil Al-Hussary (محمود خليل ا لحصري) \n <b>146.</b> Hatem Fareed Alwaer (حاتم فريد الواعر) \n <b>147.</b> Mahmoud Khalil Al-Hussary (محمود خليل الحصري) \n <b>148.</b> Yousef Bin Noah Ahmad (يوسف بن نوح أحمد) \n <b>149.</b> Neamah Al-Hassan (نعمة الحسان) \n <b>150.</b> Bandar Balilah (بندر بليله) \n",parse_mode='HTML' , reply_markup=nav.qorila10)
  

@dp.callback_query_handler(text="Keyingi10")
async def sura2(message: types.Message):

       await message.message.edit_text(" <b>•______________________________________•</b> \n  \n <b>151.</b> Akhil Abdulhayy Rawa (أخيل عبدالحي روا) \n <b>152.</b> Ali Alhuthaifi' (علي الحذيفي)  \n <b>153.</b> Wadeea Al-Yamani (وديع اليمني) \n <b>154.</b> Khalid Almohana (خالد المهنا) \n <b>155.</b> Muhammad Abu Sneyna (محمد أبوسنينة )\n <b>156.</b> Mahmoud Ali  Albanna (محمود علي البنا) \n <b>157.</b> Abdulaziz Alasiri (عبدالعزيز العسيري) \n <b>158.</b> Fahad Al-Otaibi (فهد العتيبي) \n <b>159.</b> Ahmad Al-Ajmy - Rewayat Hafs A'n Assem (أحمد بن علي العجمي - رواية حفص عن عاصم) \n <b>160.</b> Abdulmohsen Al-Qasim (عبدالمحسن القاسم) \n <b>161.</b> Jamaan Alosaimi (جمعان العصيمي) \n <b>162.</b> Khaled Al-Qahtani (خالد القحطاني) \n <b>163.</b> Muftah Alsaltany (مفتاح السلطني) \n <b>164.</b> Saud Al-Shuraim (سعود الشريم) \n <b>165.</b> Ibrahem Assadan (ابراهيم السعدان) \n",parse_mode='HTML' , reply_markup=nav.qorila11)

@dp.callback_query_handler(text="Keyingi11")
async def sura2(message: types.Message):

       await message.message.edit_text(" <b>•______________________________________•</b> \n  \n <b>166.</b> Mohammed Al-Lohaidan (محمد اللحيدان) \n <b>167.</b> Mohammad Khalil Al-Qari (محمد خليل القارئ) \n <b>168.</b> Nasser Al obaid (ناصر العبيد) \n <b>169.</b> Akasha Kameni  (عكاشة كميني)\n <b>170.</b> Hazza Al-Balushi (هزاع البلوشي) \n <b>171.</b> Abdulbari Mohammad (عبدالبارئ محمد) \n <b>172.</b> Mohammed Jibreel (محمد جبريل) \n <b>173.</b> Majed Al-Zamil (ماجد الزامل) \n <b>174.</b> Peshawa Qadr Al-Kurdi (بيشه وا قادر الكردي) \n <b>175.</b> Abdullah Fahmi (عبدالله فهمي) \n <b>176.</b> Ahmad Saud - Rewayat Hafs A'n Assem (أحمد سعود - رواية حفص عن عاصم) \n <b>177.</b> Abdulhadi Kanakeri (عبدالهادي أحمد كناكري) \n <b>178.</b> Mohammed Hafas Ali (محمد حفص علي) \n <b>179.</b> Khalid Al-Wehabi (خالد الوهيبي) \n <b>180.</b> Muhammed Khairul Anuar (محمد خير النور) \n ",parse_mode='HTML' , reply_markup=nav.qorila12)

@dp.callback_query_handler(text="Keyingi12")
async def sura2(message: types.Message):

       await message.message.edit_text(" <b>•______________________________________•</b> \n  \n <b>181.</b> Saleh Al-Habdan - Rewayat Hafs A\'n Assem (صالح الهبدان - رواية حفص عن عاصم) \n <b>182.</b> Othman Al-Ansary (عثمان الأنصاري) \n <b>183.</b> Mohammad Al-Abdullah (محمد عبدالحكيم سعيد العبدالله)  \n <b>184.</b> Mansour Al-Salemi (منصور السالمي)  \n <b>185.</b> Sapinah Mamat (سابينة مامات)  \n <b>186.</b> Khalid Alsharekh (خالد الشارخ)  \n <b>187.</b> Alashri Omran (العشري عمران)  \n <b>188.</b> Muftah Alsaltany (مفتاح السلطني)  \n <b>189.</b> Mousa Bilal (موسى بلال)  \n <b>190.</b> Saleh Al-Talib (صالح آل طالب)  \n <b>191.</b> Wishear Hayder Arbili (وشيار حيدر اربيلي)  \n <b>192.</b> Ahmad Nauina (أحمد نعينع)  \n <b>193.</b> Ali Abo-Hashim - Rewayat Hafs A\'n Assem (علي أبو هاشم - رواية حفص عن عاصم)  \n <b>194.</b> Alfateh Alzubair (الفاتح محمد الزبير)  \n <b>195.</b> Abdulbasit Abdulsamad (عبدالباسط عبدالصمد)  \n ",parse_mode='HTML' , reply_markup=nav.qorila13)
  

@dp.callback_query_handler(text="Keyingi13")
async def sura2(message: types.Message):

       await message.message.edit_text(" <b>•______________________________________•</b> \n  \n <b>196.</b> Tareq Abdulgani daawob' (طارق عبدالغني دعوب)   \n <b>197.</b> Mohammad Al-Tablaway (محمد الطبلاوي)   \n <b>198.</b> Abdullah Al-Khalaf (عبدالله الخلف)   \n <b>199.</b> Yasser Salamah (ياسر سلامة)  \n <b>200.</b> Rachid Belalya (رشيد بلعالية)  \n <b>201.</b> Mohammed Osman Khan (محمد عثمان خان)  \n <b>202.</b> Mustafa raad Alazawy (مصطفى رعد العزاوي)  \n <b>203.</b> Abdulrasheed Soufi (عبدالرشيد صوفي)  \n <b>204.</b> Addokali Mohammad Alalim' (الدوكالي محمد العالم)  \n <b>205.</b> Mohammad Rashad Alshareef (محمد رشاد الشريف)  \n <b>206.</b> Muhammad Al-Hafiz (محمد الحافظ)  \n <b>207.</b> Abdulbari Mohammad (عبدالبارئ محمد)  \n <b>208.</b> Omar Al Darweez (عمر الدريويز)  \n <b>209.</b> Ahmad Saber (أحمد صابر) \n <b>210.</b> Hani Arrifai (هاني الرفاعي)  \n ",parse_mode='HTML' , reply_markup=nav.qorila14)


@dp.callback_query_handler(text="Keyingi14")
async def sura2(message: types.Message):

       await message.message.edit_text(" <b>•______________________________________•</b> \n  \n <b>211.</b> Abdulghani Abdullah (عبدالغني عبدالله) \n <b>212.</b> Aloyoon Al-Koshi (العيون الكوشي) \n <b>213.</b> Tawfeeq As-Sayegh (توفيق الصايغ) \n <b>214.</b> Jamal Shaker Abdullah (جمال شاكر عبدالله) \n <b>215.</b> Khalid Al-Jileel (خالد الجليل) \n <b>216.</b> Khalid Abdulkafi (خالد عبدالكافي) \n <b>217.</b> Khalifa Altunaiji (خليفة الطنيجي) \n <b>218.</b> Dawood Hamza (داود حمزة) \n <b>219.</b> Rasheed Ifrad (رشيد إفراد) \n <b>220.</b> Alhusayni Al-Azazi (الحسيني العزازي) \n <b>221.</b> Zakaria Hamamah (زكريا حمامة) \n",parse_mode='HTML' , reply_markup=nav.qorila15)
  
   
     

   
  
@dp.callback_query_handler(text="btnsura")
async def sura(message: types.Message):
       
       await message.message.edit_text(f" <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) {cd} " , reply_markup=nav.allsuralarMaherAlMeaqli, parse_mode='html')
     
  
  
@dp.callback_query_handler(text="MaherAlMeaqlisuralar1")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
       await bot.send_message(message.from_user.id,"<a href='https://t.me/b148uz/42'>ㅤ</a> \n <b>Nomi:</b> Al-Faatiha (سُورَةُ ٱلْفَاتِحَةِ)\n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b> 0:38 \n <b>Oyatlar soni:</b> 7 \n <b>Nozil bo\'lgan yeri:</b> Meccan",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli1)

@dp.callback_query_handler(text="MaherAlMeaqlisuralar2")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
       await bot.send_message(message.from_user.id,"<a href='https://t.me/b148uz/43'>ㅤ</a> \n <b>Nomi:</b>  Al-Baqara (سُورَةُ البَقَرَةِ)\n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b> 2:00:00 \n <b>Oyatlar soni:</b> 286 \n <b>Nozil bo\'lgan yeri:</b> Medinan",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli1)
 
@dp.callback_query_handler(text="MaherAlMeaqlisuralar3")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
       await bot.send_message(message.from_user.id,"<a href='https://t.me/b148uz/44'>ㅤ</a> \n <b>Nomi:</b>  Aal-i-Imraan (سُورَةُ آلِ عِمۡرَانَ) \n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b> 0:38 \n <b>Oyatlar soni:</b> 7 \n <b>Nozil bo\'lgan yeri:</b> Meccan",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli1)
 
@dp.callback_query_handler(text="MaherAlMeaqlisuralar4")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
       await bot.send_message(message.from_user.id,"<a href='https://t.me/b148uz/42'>ㅤ</a> \n <b>Nomi:</b> Al-Faatiha (سُورَةُ ٱلْفَاتِحَةِ)\n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b> 0:38 \n <b>Oyatlar soni:</b> 7 \n <b>Nozil bo\'lgan yeri:</b> Meccan",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli1)
 
@dp.callback_query_handler(text="MaherAlMeaqlisuralar5")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
       await bot.send_message(message.from_user.id,"<a href='https://t.me/b148uz/42'>ㅤ</a> \n <b>Nomi:</b> Al-Faatiha (سُورَةُ ٱلْفَاتِحَةِ)\n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b> 0:38 \n <b>Oyatlar soni:</b> 7 \n <b>Nozil bo\'lgan yeri:</b> Meccan",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli1)
 
@dp.callback_query_handler(text="MaherAlMeaqlisuralar6")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
       await bot.send_message(message.from_user.id,"<a href='https://t.me/b148uz/42'>ㅤ</a> \n <b>Nomi:</b> Al-Faatiha (سُورَةُ ٱلْفَاتِحَةِ)\n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b> 0:38 \n <b>Oyatlar soni:</b> 7 \n <b>Nozil bo\'lgan yeri:</b> Meccan",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli1)
 
@dp.callback_query_handler(text="MaherAlMeaqlisuralar7")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
       await bot.send_message(message.from_user.id,"<a href='https://t.me/b148uz/42'>ㅤ</a> \n <b>Nomi:</b> Al-Faatiha (سُورَةُ ٱلْفَاتِحَةِ)\n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b> 0:38 \n <b>Oyatlar soni:</b> 7 \n <b>Nozil bo\'lgan yeri:</b> Meccan",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli1)
 
@dp.callback_query_handler(text="MaherAlMeaqlisuralar8")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
       await bot.send_message(message.from_user.id,"<a href='https://t.me/b148uz/42'>ㅤ</a> \n <b>Nomi:</b> Al-Faatiha (سُورَةُ ٱلْفَاتِحَةِ)\n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b> 0:38 \n <b>Oyatlar soni:</b> 7 \n <b>Nozil bo\'lgan yeri:</b> Meccan",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli1)
 
@dp.callback_query_handler(text="MaherAlMeaqlisuralar9")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
       await bot.send_message(message.from_user.id,"<a href='https://t.me/b148uz/42'>ㅤ</a> \n <b>Nomi:</b> Al-Faatiha (سُورَةُ ٱلْفَاتِحَةِ)\n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b> 0:38 \n <b>Oyatlar soni:</b> 7 \n <b>Nozil bo\'lgan yeri:</b> Meccan",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli1)
 
@dp.callback_query_handler(text="MaherAlMeaqlisuralar10")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
       await bot.send_message(message.from_user.id,"<a href='https://t.me/b148uz/42'>ㅤ</a> \n <b>Nomi:</b> Al-Faatiha (سُورَةُ ٱلْفَاتِحَةِ)\n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b> 0:38 \n <b>Oyatlar soni:</b> 7 \n <b>Nozil bo\'lgan yeri:</b> Meccan",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli1)
 
@dp.callback_query_handler(text="MaherAlMeaqlisuralar11")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
       await bot.send_message(message.from_user.id,"<a href='https://t.me/b148uz/42'>ㅤ</a> \n <b>Nomi:</b> Al-Faatiha (سُورَةُ ٱلْفَاتِحَةِ)\n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b> 0:38 \n <b>Oyatlar soni:</b> 7 \n <b>Nozil bo\'lgan yeri:</b> Meccan",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli1)
 
@dp.callback_query_handler(text="MaherAlMeaqlisuralar12")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
       await bot.send_message(message.from_user.id,"<a href='https://t.me/b148uz/42'>ㅤ</a> \n <b>Nomi:</b> Al-Faatiha (سُورَةُ ٱلْفَاتِحَةِ)\n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b> 0:38 \n <b>Oyatlar soni:</b> 7 \n <b>Nozil bo\'lgan yeri:</b> Meccan",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli1)
 
@dp.callback_query_handler(text="MaherAlMeaqlisuralar13")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
       await bot.send_message(message.from_user.id,"<a href='https://t.me/b148uz/42'>ㅤ</a> \n <b>Nomi:</b> Al-Faatiha (سُورَةُ ٱلْفَاتِحَةِ)\n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b> 0:38 \n <b>Oyatlar soni:</b> 7 \n <b>Nozil bo\'lgan yeri:</b> Meccan",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli1)
 
@dp.callback_query_handler(text="MaherAlMeaqlisuralar14")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
       await bot.send_message(message.from_user.id,"<a href='https://t.me/b148uz/42'>ㅤ</a> \n <b>Nomi:</b> Al-Faatiha (سُورَةُ ٱلْفَاتِحَةِ)\n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b> 0:38 \n <b>Oyatlar soni:</b> 7 \n <b>Nozil bo\'lgan yeri:</b> Meccan",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli1)
 
@dp.callback_query_handler(text="MaherAlMeaqlisuralar15")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
       await bot.send_message(message.from_user.id,"<a href='https://t.me/b148uz/42'>ㅤ</a> \n <b>Nomi:</b> Al-Faatiha (سُورَةُ ٱلْفَاتِحَةِ)\n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b> 0:38 \n <b>Oyatlar soni:</b> 7 \n <b>Nozil bo\'lgan yeri:</b> Meccan",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli1)

@dp.callback_query_handler(text="MaherAlMeaqlisuralar16")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
       await bot.send_message(message.from_user.id,"<a href='https://t.me/b148uz/42'>ㅤ</a> \n <b>Nomi:</b> Al-Faatiha (سُورَةُ ٱلْفَاتِحَةِ)\n <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>Uzunligi:</b> 0:38 \n <b>Oyatlar soni:</b> 7 \n <b>Nozil bo\'lgan yeri:</b> Meccan",parse_mode='HTML' , reply_markup=nav.ortgaMaherAlMeaqli1)
 
@dp.callback_query_handler(text="ortgaMaherAlMeaqli")
async def sura(message: types.Message):
       #await bot.delete_message(message.from_user.id,  message.message.message_id)
       await bot.send_message(message.from_user.id, f"<b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي) {cd} ",parse_mode='HTML' , reply_markup=nav.allsuralarMaherAlMeaqli)
  

@dp.callback_query_handler(text="ortgaMaherAlMeaqlimenu")
async def sura(message: types.Message):

       await message.message.edit_text(" <b>Qori:</b> Maher Al Meaqli (ماهر المعيقلي)",parse_mode='HTML' , reply_markup=nav.oyatsura)
  












  
@dp.callback_query_handler(text="btn1")
async def sura(query: types.CallbackQuery):
       await bot.delete_message(query.from_user.id,  query.message.message_id)
       await query.message.answer(f"<i> <b>Tanlangan qori :</b> </i> Maher Al Meaqli (ماهر المعيقلي) {suralarning} ",parse_mode="html",reply_markup=nav.oyatsura)

  




























 
@dp.callback_query_handler(text="obshiyortga")
async def sura(message: types.Message):
       
       await message.message.edit_text(" <b>•______________________________________•ㅤ </b> \n \n <b>1.</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>2.</b> Abdulbasit Abdulsamad (عبدالباسط عبدالصمد) \n <b>3.</b> Raad Al Kurdi (رعد محمد الكردي) \n <b>4.</b> Abdulrahman Alsudaes (عبدالرحمن السديس ) \n <b>5.</b> Mohammed Siddiq Al-Minshawi (محمد صديق المنشاوي) \n <b>6.</b> Mohammed Ayyub (محمد أيوب) \n <b>7.</b> Idrees Abkr (إدريس أبكر) \n <b>8.</b> Abdullah Basfer (عبدالله بصفر) \n <b>9.</b> Mishary Alafasi (مشاري العفاسي) \n <b>10.</b> Mohammed Ayyub (محمد أيوب) \n <b>11.</b> Nasser Alqatami (ناصر القطامي)\n <b>12.</b> Zaki Daghistani (زكي داغستاني) \n <b>13.</b> Khalifa Altunaiji (خليفة الطنيجي) \n <b>14.</b> Sami Al-Hasn (سامي الحسن) \n <b>15.</b> Sahl Yassin (سهل ياسين)" , parse_mode='HTML', reply_markup=nav.qorila)




@dp.callback_query_handler(text="ortga")
async def sura(message: types.Message):
       await bot.delete_message(message.from_user.id,  message.message.message_id)
       await bot.send_message(message.from_user.id , "Qorilarni tanglang 🤲",parse_mode='HTML' , reply_markup=nav.qori)

 
@dp.callback_query_handler(text="ortga2")
async def sura(message: types.Message):
       
       await message.message.edit_text(" <b>•______________________________________•ㅤ </b> \n \n <b>1.</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>2.</b> Abdulbasit Abdulsamad (عبدالباسط عبدالصمد) \n <b>3.</b> Raad Al Kurdi (رعد محمد الكردي) \n <b>4.</b> Abdulrahman Alsudaes (عبدالرحمن السديس ) \n <b>5.</b> Mohammed Siddiq Al-Minshawi (محمد صديق المنشاوي) \n <b>6.</b> Mohammed Ayyub (محمد أيوب) \n <b>7.</b> Idrees Abkr (إدريس أبكر) \n <b>8.</b> Abdullah Basfer (عبدالله بصفر) \n <b>9.</b> Mishary Alafasi (مشاري العفاسي) \n <b>10.</b> Mohammed Ayyub (محمد أيوب) \n <b>11.</b> Nasser Alqatami (ناصر القطامي)\n <b>12.</b> Zaki Daghistani (زكي داغستاني) \n <b>13.</b> Khalifa Altunaiji (خليفة الطنيجي) \n <b>14.</b> Sami Al-Hasn (سامي الحسن) \n <b>15.</b> Sahl Yassin (سهل ياسين)" , parse_mode='HTML', reply_markup=nav.qorila)

 
@dp.callback_query_handler(text="ortga2a")
async def sura(message: types.Message):
       
      await message.message.edit_text(" <b>•______________________________________•ㅤ </b> \n <b>1.</b> Maher Al Meaqli (ماهر المعيقلي) \n <b>2.</b> Abdulbasit Abdulsamad (عبدالباسط عبدالصمد) \n <b>3.</b> Raad Al Kurdi (رعد محمد الكردي) \n <b>4.</b> Abdulrahman Alsudaes (عبدالرحمن السديس ) \n <b>5.</b> Mohammed Siddiq Al-Minshawi (محمد صديق المنشاوي) \n <b>6.</b> Mohammed Ayyub (محمد أيوب) \n <b>7.</b> Idrees Abkr (إدريس أبكر) \n <b>8.</b> Abdullah Basfer (عبدالله بصفر) \n <b>9.</b> Mishary Alafasi (مشاري العفاسي) \n <b>10.</b> Mohammed Ayyub (محمد أيوب) \n <b>11.</b> Nasser Alqatami (ناصر القطامي)\n <b>12.</b> Zaki Daghistani (زكي داغستاني) \n <b>13.</b> Khalifa Altunaiji (خليفة الطنيجي) \n <b>14.</b> Sami Al-Hasn (سامي الحسن) \n <b>15.</b> Sahl Yassin (سهل ياسين)" , parse_mode='HTML', reply_markup=nav.qorila)


 
@dp.callback_query_handler(text="ortga22a")
async def sura(message: types.Message):
       
       await message.message.edit_text(" <b>•______________________________________• </b> \n  \n <b>16.</b> Saad Al-Ghamdi (سعد الغامدي) \n <b>17.</b> Khalid Abdulkafi (خالد عبدالكافي) \n <b>18. </b>Tawfeeq As-Sayegh (توفيق الصايغ) \n <b>19.</b> Adel Ryyan (عادل ريان) \n <b>20.</b> Zakaria Hamamah (زكريا حمامة) \n <b>21.</b> Slaah Bukhatir (القارئ صلاح بو خاطر) \n <b>22.</b> Abdelbari Al-Toubayti (عبدالبارئ الثبيتي) \n <b>23.</b> Abdulaziz Az-Zahrani (عبدالعزيز الزهراني) \n <b>24.</b> Abdullah Al-Burimi (عبدالله البريمي) \n <b>25.</b> Abdullah Al-Mattrod (عبدالله المطرود) \n <b>26.</b> Abdullah Al-Johany (عبدالله عواد الجهني) \n <b>27.</b> Abdulrasheed Soufi (عبدالرشيد صوفي) \n <b>28.</b> Abdulmohsin Al-Harthy (عبدالمحسن الحارثي) \n <b>29.</b> Abdulmohsin Al-Askar (عبدالمحسن العسكر) \n <b>30.</b> Salah Alhashim (صلاح الهاشم)",parse_mode='HTML' , reply_markup=nav.qorila2 )




@dp.callback_query_handler(text="ortga3")
async def sura(message: types.Message):
       
      await message.message.edit_text(" <b>•______________________________________•  </b> \n \n <b>31.</b> Salah Alhashim (صلاح الهاشم) \n <b>32.</b> Alhusayni Al-Azazi (الحسيني العزازي) \n <b>33.</b> Khalid Al-Jileel (خالد الجليل)\n <b>34.</b> Fawaz Alkabi (فواز الكعبي) \n <b>35.</b> Salah Albudair (صلاح البدير) \n <b>36.</b> Fahad Al-Kandari (فهد الكندري) \n <b>37.</b> Fares Abbad (فارس عباد) \n <b>38.</b> Nabil Al Rifay (نبيل الرفاعي) \n <b>39.</b> Walid Al-Dulaimi (وليد الدليمي) \n <b>40.</b> Yasser Al-Dosari (ياسر الدوسري) \n <b>41.</b> Yasser Al-Qurashi (ياسر القرشي) \n <b>42.</b> Yahya Hawwa (يحيى حوا) \n <b>43.</b> Yousef Alshoaey (يوسف الشويعي) \n <b>44.</b> Majed Al-Enezi (ماجد العنزي) \n <b>45.</b> Rachid Belalya (رشيد بلعالية)" , parse_mode='HTML', reply_markup=nav.qorila3)



@dp.callback_query_handler(text="ortga4")
async def sura(message: types.Message):

       await message.message.edit_text(" <b>•______________________________________•  </b> \n  \n <b>46.</b> Alzain Mohammad Ahmad (الزين محمد أحمد) \n <b>47.</b> Al-Qaria Yassen (القارئ ياسين) \n <b>48.</b> Rachid Belalya (رشيد بلعالية) \n <b>49.</b> Rasheed Ifrad (رشيد إفراد) \n <b>50.</b> Hamad Al Daghriri (حمد الدغريري) \n <b>51.</b> Lafi Al-Oni (لافي العوني) \n <b>52.</b> Abdulrasheed Soufi (عبدالرشيد صوفي) \n <b>53.</b> Abdullah Al-Kandari (عبدالله الكندري) \n <b>54.</b> Saber Abdulhakm (صابر عبدالحكم) \n <b>55.</b> Ahmed Amer (أحمد عامر) \n <b>56.</b> Malik shaibat Alhamed (مالك شيبة الحمد) \n <b>57.</b> Abdulmajeed Al-Arkani (عبدالمجيد الأركاني) \n <b>58.</b> Mustafa Ismail (مصطفى إسماعيل) \n <b>59.</b> Ahmad Shaheen (أحمد خليل شاهين) \n <b>60.</b> Omar Al-Qazabri' (عمر القزابري)",parse_mode='HTML' , reply_markup=nav.qorila4)

@dp.callback_query_handler(text="ortga5")
async def sura(message: types.Message):

       await message.message.edit_text(" <b>•______________________________________•  </b> \n  \n <b>61.</b> Mahmoud Khalil Al-Hussary (محمود خليل الحصري) \n <b>62.</b> Saad Almqren (سعد المقرن) \n <b>63.</b> Omar Al-Qazabri\' (عمر القزابري) \n <b>64.</b> Akram Alalaqmi (أكرم العلاقمي) \n <b>65.</b> Abdulrahman Al-Majed (عبدالرحمن الماجد) \n <b>66.</b> Emad Hafez (عماد زهير حافظ) \n <b>67.</b> Shirazad Taher (شيرزاد عبدالرحمن طاهر) \n <b>68.</b> Salah Alhashim (صلاح الهاشم) \n <b>69.</b> Yasser Al-Faylakawi (ياسر الفيلكاوي) \n <b>70.</b> Khalid Algamdi (خالد الغامدي) \n <b>71.</b> Ali Hajjaj Alsouasi (علي حجاج السويسي) \n <b>72.</b> Ramadan Shakoor (رمضان شكور) \n <b>73.</b> Mohammad Abdullkarem (محمد عبدالكريم) \n <b>74.</b> Nasser Almajed (ناصر الماجد) \n <b>75.</b> Muftah Alsaltany (مفتاح السلطني)  ",parse_mode='HTML' , reply_markup=nav.qorila5)



@dp.callback_query_handler(text="ortga6")
async def sura(message: types.Message):
       
       await message.message.edit_text(" <b>•______________________________________•  </b> \n  \n <b>76.</b> Ahmad Deban (أحمد ديبان)  \n <b>77.</b> Khalid Al-Shoraimy (خالد الشريمي) \n <b>78.</b> Ustaz Zamri (استاذ زامري) \n <b>79.</b> Haitham Aldukhain (هيثم الدخين) \n <b>80.</b>  Mahmoud Khalil Al-Hussary (محمود خليل الحصري) \n <b>81.</b>  Ahmed Al-trabulsi (أحمد الطرابلسي) \n <b>82.</b> Abdulbasit Abdulsamad (عبدالباسط عبدالصمد) \n <b>83.</b> Ibrahim Al-Jebreen (ابراهيم الجبرين) \n <b>84.</b>  Shaban Al-Sayiaad (شعبان الصياد) \n <b>85.</b> Waleed Alnaehi (وليد النائحي) \n <b>86.</b> Mohammad Al-Airawy (محمد الأيراوي) \n <b>87.</b> Mohammad Refat (محمد رفعت) \n <b>88.</b> Mohammed Al-Barrak (محمد البراك) \n <b>89.</b> Abdullah Al-Mousa (عبدالله الموسى) \n <b>90.</b> Muftah Alsaltany (مفتاح السلطني)",parse_mode='HTML' , reply_markup=nav.qorila6)




@dp.callback_query_handler(text="ortga7")
async def sura(message: types.Message):
       
       await message.message.edit_text(" <b>•______________________________________•  </b> \n  \n <b>91.</b> Ahmad Deban (أحمد ديبان) \n <b>92.</b> Rogayah Sulong (رقية سولونق) \n <b>93.</b> Abdulmohsin Al-Obaikan (عبدالمحسن العبيكان) \n <b>94.</b> Rami Aldeais (رامي الدعيس) \n <b>95.</b> Wasel Almethen (واصل المذن) \n <b>96.</b> Shirazad Taher (شيرزاد عبدالرحمن طاهر) \n <b>97.</b> Salah Alhashim (صلاح الهاشم) \n <b>98.</b> Ibrahim Aldosari (ابراهيم الدوسري) \n <b>99.</b> Muftah Alsaltany (مفتاح السلطني) \n <b>100.</b> Mohammad Abdullkarem (محمد عبدالكريم) \n <b>101.</b> Abdul Aziz Al-Ahmad (عبدالعزيز الأحمد) \n <b>102.</b> Ibrahim Al-Akdar (إبراهيم الأخضر) \n <b>103.</b> Saleh Alsahood (صالح الصاهود) \n <b>104.</b> Yasser Al-Mazroyee (ياسر المزروعي) \n <b>105.</b> Ali Jaber (علي جابر)",parse_mode='HTML' , reply_markup=nav.qorila7)




@dp.callback_query_handler(text="ortga8")
async def sura(message: types.Message):
       
       await message.message.edit_text(" <b>•______________________________________•  </b> \n  \n <b>106.</b> Mohammed Al-Muhasny (محمد المحيسني) \n <b>107.</b> Saidin Abdulrahman (سيدين عبدالرحمن) \n <b>108.</b> Nasser Alosfor (ناصر العصفور) \n <b>109.</b> Abdulrahman Aloosi (عبدالرحمن العوسي) \n <b>110.</b> Mushaf Ibrahim Al-Asiri (مصحف ابراهيم العسيري) \n <b>111.</b> Mahmoud Ali  Albanna (محمود علي البنا) \n <b>112.</b> Bader Alturki (بدر التركي) \n <b>113.</b> Hitham Aljadani (هيثم الجدعاني) \n <b>114.</b> Ibrahim Aljormy (ابراهيم الجرمي) \n <b>115.</b> Sami Al-Dosari (سامي الدوسري) \n <b>116.</b> Jamal Addeen Alzailaie (جمال الدين الزيلعي) \n <b>117.</b> Mohammad Al-Abdullah (محمد عبدالحكيم سعيد العبدالله) \n <b>118.</b> Salah Musali (صلاح مصلي) \n<b>119.</b> Muftah Alsaltany (مفتاح السلطني) \n<b>120.</b> Mahmoud Khalil Al-Hussary (محمود خليل الحصري) \n ",parse_mode='HTML' , reply_markup=nav.qorila8)




@dp.callback_query_handler(text="ortga9")
async def sura(message: types.Message):
       
       await message.message.edit_text(" <b>•______________________________________•  </b> \n  \n <b>121.</b> Ahmad Al Nufais (أحمد النفيس) \n <b>122.</b> Salman Alotaibi (سلمان العتيبي) \n <b>123.</b> Abdullah Albuajan (عبدالله البعيجان) \n <b>124.</b> Shaik Abu Bakr Al Shatri (أبوبكر الشاطري) \n <b>125.</b> Abdullah Khayyat (عبدالله خياط) \n <b>126.</b> Mahmoud Khalil Al-Hussary (محمود خليل الحصري) \n <b>127.</b> Maher Shakhashero (ماهر شخاشيرو) \n <b>128.</b> Younes Souilass (يونس اسويلص) \n <b>129.</b> Mohammad AlMonshed (محمد المنشد) \n <b>130.</b> Ahmed Al-trabulsi (أحمد الطرابلسي) \n <b>131.</b> Rodziah Abdulrahman (رضية عبدالرحمن) \n <b>132.</b> Ahmad Alhuthaifi (أحمد الحذيفي) \n <b>133.</b> Mustafa Al-Lahoni (مصطفى اللاهوني) \n <b>134.</b> Mohammad Albukheet (محمد البخيت) \n <b>135.</b> Youssef Edghouch (يوسف الدغوش) \n",parse_mode='HTML' , reply_markup=nav.qorila9)



@dp.callback_query_handler(text="ortga10")
async def sura(message: types.Message):
       
       await message.message.edit_text(" <b>•______________________________________•  </b> \n  \n <b>136.</b> Muamar (From Indonesia) (معمر الأندونيسي) \n <b>137.</b> Abdullah Kamel (عبدالله كامل) \n <b>138.</b> Mohammed Siddiq Al-Minshawi (محمد صديق المنشاوي) \n <b>139.</b> Islam Sobhi (إسلام صبحي) \n <b>140.</b> Ali Alhuthaifi (علي الحذيفي) \n <b>141.</b> Ahmad Al-Hawashi (أحمد الحواشي) \n <b>142.</b> Abdullah Qaulan (عبدالله غيلان) \n <b>143.</b> Adel Al-Khalbany (عادل الكلباني) \n <b>144.</b> Hussain Alshaik (حسين آل الشيخ) \n <b>145.</b> Mahmoud Khalil Al-Hussary (محمود خليل ا لحصري) \n <b>146.</b> Hatem Fareed Alwaer (حاتم فريد الواعر) \n <b>147.</b> Mahmoud Khalil Al-Hussary (محمود خليل الحصري) \n <b>148.</b> Yousef Bin Noah Ahmad (يوسف بن نوح أحمد) \n <b>149.</b> Neamah Al-Hassan (نعمة الحسان) \n <b>150.</b> Bandar Balilah (بندر بليله) \n",parse_mode='HTML' , reply_markup=nav.qorila10)


@dp.callback_query_handler(text="ortga11")
async def sura(message: types.Message):
       
       await message.message.edit_text(" <b>•______________________________________•  </b> \n  \n <b>151.</b> Akhil Abdulhayy Rawa (أخيل عبدالحي روا) \n <b>152.</b> Ali Alhuthaifi' (علي الحذيفي)  \n <b>153.</b> Wadeea Al-Yamani (وديع اليمني) \n <b>154.</b> Khalid Almohana (خالد المهنا) \n <b>155.</b> Muhammad Abu Sneyna (محمد أبوسنينة ) \n <b>156.</b> Mahmoud Ali  Albanna (محمود علي البنا) \n <b>157.</b> Abdulaziz Alasiri (عبدالعزيز العسيري) \n <b>158.</b> Fahad Al-Otaibi (فهد العتيبي) \n <b>159.</b> Ahmad Al-Ajmy - Rewayat Hafs A'n Assem (أحمد بن علي العجمي - رواية حفص عن عاصم) \n <b>160.</b> Abdulmohsen Al-Qasim (عبدالمحسن القاسم) \n <b>161.</b> Jamaan Alosaimi (جمعان العصيمي) \n <b>162.</b> Khaled Al-Qahtani (خالد القحطاني) \n <b>163.</b> Muftah Alsaltany (مفتاح السلطني) \n <b>164.</b> Saud Al-Shuraim (سعود الشريم) \n <b>165.</b> Ibrahem Assadan (ابراهيم السعدان) \n",parse_mode='HTML' , reply_markup=nav.qorila11)





@dp.callback_query_handler(text="ortga12")
async def sura(message: types.Message):
       
       await message.message.edit_text(" <b>•______________________________________•  </b> \n  \n <b>166.</b> Mohammed Al-Lohaidan (محمد اللحيدان) \n <b>167.</b> Mohammad Khalil Al-Qari (محمد خليل القارئ) \n <b>168.</b> Nasser Al obaid (ناصر العبيد) \n <b>169.</b> Akasha Kameni  (عكاشة كميني) \n <b>170.</b> Hazza Al-Balushi (هزاع البلوشي) \n <b>171.</b> Abdulbari Mohammad (عبدالبارئ محمد) \n <b>172.</b> Mohammed Jibreel (محمد جبريل) \n <b>173.</b> Majed Al-Zamil (ماجد الزامل) \n <b>174.</b> Peshawa Qadr Al-Kurdi (بيشه وا قادر الكردي) \n <b>175.</b> Abdullah Fahmi (عبدالله فهمي) \n <b>176.</b> Ahmad Saud - Rewayat Hafs A'n Assem (أحمد سعود - رواية حفص عن عاصم) \n <b>177.</b> Abdulhadi Kanakeri (عبدالهادي أحمد كناكري) \n <b>178.</b> Mohammed Hafas Ali (محمد حفص علي) \n <b>179.</b> Khalid Al-Wehabi (خالد الوهيبي) \n <b>180.</b> Muhammed Khairul Anuar (محمد خير النور) \n",parse_mode='HTML' , reply_markup=nav.qorila12)



@dp.callback_query_handler(text="ortga13")
async def sura(message: types.Message):
       
       await message.message.edit_text(" <b>•______________________________________•  </b> \n  \n <b>181.</b> Saleh Al-Habdan - Rewayat Hafs A\'n Assem (صالح الهبدان - رواية حفص عن عاصم) \n <b>182.</b> Othman Al-Ansary (عثمان الأنصاري) \n <b>183.</b> Mohammad Al-Abdullah (محمد عبدالحكيم سعيد العبدالله)  \n <b>184.</b> Mansour Al-Salemi (منصور السالمي)  \n <b>185.</b> Sapinah Mamat (سابينة مامات)  \n <b>186.</b> Khalid Alsharekh (خالد الشارخ)  \n <b>187.</b> Alashri Omran (العشري عمران)  \n <b>188.</b> Muftah Alsaltany (مفتاح السلطني)  \n <b>189.</b> Mousa Bilal (موسى بلال)  \n <b>190.</b> Saleh Al-Talib (صالح آل طالب)  \n <b>191.</b> Wishear Hayder Arbili (وشيار حيدر اربيلي)  \n <b>192.</b> Ahmad Nauina (أحمد نعينع)  \n <b>193.</b> Ali Abo-Hashim - Rewayat Hafs A\'n Assem (علي أبو هاشم - رواية حفص عن عاصم)  \n <b>194.</b> Alfateh Alzubair (الفاتح محمد الزبير)  \n <b>195.</b> Abdulbasit Abdulsamad (عبدالباسط عبدالصمد)  \n",parse_mode='HTML' , reply_markup=nav.qorila13)


@dp.callback_query_handler(text="ortga14")
async def sura(message: types.Message):
       
       await message.message.edit_text(" <b>•______________________________________•  </b> \n  \n \n <b>196.</b> Tareq Abdulgani daawob' (طارق عبدالغني دعوب)   \n <b>197.</b> Mohammad Al-Tablaway (محمد الطبلاوي)   \n <b>198.</b> Abdullah Al-Khalaf (عبدالله الخلف)   \n <b>199.</b> Yasser Salamah (ياسر سلامة)  \n <b>200.</b> Rachid Belalya (رشيد بلعالية)  \n <b>201.</b> Mohammed Osman Khan (محمد عثمان خان)  \n <b>202.</b> Mustafa raad Alazawy (مصطفى رعد العزاوي)  \n <b>203.</b> Abdulrasheed Soufi (عبدالرشيد صوفي)  \n <b>204.</b> Addokali Mohammad Alalim' (الدوكالي محمد العالم)  \n <b>205.</b> Mohammad Rashad Alshareef (محمد رشاد الشريف)  \n <b>206.</b> Muhammad Al-Hafiz (محمد الحافظ)  \n <b>207.</b> Abdulbari Mohammad (عبدالبارئ محمد)  \n <b>208.</b> Omar Al Darweez (عمر الدريويز)  \n <b>209.</b> Ahmad Saber (أحمد صابر) \n <b>210.</b> Hani Arrifai (هاني الرفاعي)  \n ",parse_mode='HTML' , reply_markup=nav.qorila14)

















if __name__ == "__main__":
    executor.start_polling(dp, skip_updates= True)       
      


         