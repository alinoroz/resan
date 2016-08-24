#!/usr/bin/python
# -*- coding: utf-8 -*-
import telebot
import sys
import redis as r
import os
reload(sys)
sys.setdefaultencoding("utf-8")
redis = r.StrictRedis(host='localhost', port=6379, db=0) # تنظیمات ردیس
bot = telebot.TeleBot('263333053:AAE9ocz8z3y4_C9TSgcjIBUyvY_8eaPHyho')
admin = '199498852'

@bot.message_handler(content_types=['text', 'audio', 'document', 'photo', 'sticker'])
def m(m):
    try:
        if m.chat.type == 'private':
            banlist = redis.sismember('banlist_pmbot', '{}'.format(m.from_user.id))
            if m.text == '/start' or m.text == '/help':
                bot.send_message(m.chat.id, 'پیام خودتونو ارسال کنید\n😊)
                redis.sadd('member_pmbot','{}'.format(m.from_user.id))
            if str(m.from_user.id) not in admin:
                if str(banlist) == 'False':
                    if m.photo:
                        bot.forward_message(chat_id=admin, from_chat_id=m.chat.id, message_id=m.message_id)
                        bot.send_message(m.chat.id, 'پیام شما ارسال شد✉️')
                    if m.text:
                        bot.forward_message(chat_id=admin, from_chat_id=m.chat.id, message_id=m.message_id)
                        bot.send_message(m.chat.id, 'پیام شما ارسال شد✉️')
                    if m.document:
                        file_id = m.document.file_id
                        bot.forward_message(chat_id=admin, from_chat_id=m.chat.id, message_id=m.message_id)
                        bot.send_message(m.chat.id, 'پیام شما ارسال شد✉️')
                    if m.sticker:
                        bot.forward_message(chat_id=admin, from_chat_id=m.chat.id, message_id=m.message_id)
                        bot.send_message(m.chat.id, 'پیام شما ارسال شد✉'️)
                    if m.audio:
                        file_id = m.audio.file_id
                        bot.forward_message(chat_id=admin, from_chat_id=m.chat.id, message_id=m.message_id)
                        bot.send_message(m.chat.id, 'پیام شما ارسال شد✉️')
                    if m.contact:
                        bot.forward_message(chat_id=admin, from_chat_id=m.chat.id, message_id=m.message_id)
                        bot.send_message(m.chat.id, 'پیام شما ارسال شد✉️')
        if str(m.from_user.id) == admin:
            if m.reply_to_message:
                if not m.text == '/ban':
                    if not m.text == '/unban':
                        if m.reply_to_message.text:
                            if m.text:
                                cid = m.reply_to_message.forward_from.id
                                text = m.text
                                bot.send_message(cid,text)
                                bot.send_message(m.chat.id, 'متن شماارسال شد✉️')
                            if m.photo:
                                cid = m.reply_to_message.forward_from.id
                                photo = m.photo[2].file_id
                                bot.send_photo(cid,photo)
                                bot.send_message(m.chat.id, 'تصویر شماارسال شد✉️')
                            if m.sticker:
                                cid = m.reply_to_message.forward_from.id
                                sticker = m.sticker.file_id
                                bot.send_sticker(cid, sticker)
                                bot.send_message(m.chat.id, 'استیکر شماارسال شد✉️')
                        if m.reply_to_message.photo:
                            if m.text:
                                cid = m.reply_to_message.forward_from.id
                                text = m.text
                                bot.send_message(cid,text)
                                bot.send_message(m.chat.id, 'متن شماارسال شد✉️')
                            if m.photo:
                                cid = m.reply_to_message.forward_from.id
                                photo = m.photo[2].file_id
                                bot.send_photo(cid,photo)
                                bot.send_message(m.chat.id, 'تصویر شماارسال شد✉️')
                            if m.sticker:
                                cid = m.reply_to_message.forward_from.id
                                sticker = m.sticker.file_id
                                bot.send_sticker(cid, sticker)
                                bot.send_message(m.chat.id, 'استیکر شماارسال شد✉️')
                        if m.reply_to_message.contact:
                            if m.text:
                                cid = m.reply_to_message.forward_from.id
                                text = m.text
                                bot.send_message(cid,text)
                                bot.send_message(m.chat.id, 'متن شماارسال شد✉️')
                            if m.photo:
                                cid = m.reply_to_message.forward_from.id
                                photo = m.photo[2].file_id
                                bot.send_photo(cid,photo)
                                bot.send_message(m.chat.id, 'تصویر شماارسال شد✉️')
                            if m.sticker:
                                cid = m.reply_to_message.forward_from.id
                                sticker = m.sticker.file_id
                                bot.send_sticker(cid, sticker)
                                bot.send_message(m.chat.id, 'استیکر شماارسال شد✉️')
                        if m.reply_to_message.sticker:
                            if m.text:
                                cid = m.reply_to_message.forward_from.id
                                text = m.text
                                bot.send_message(cid,text)
                                bot.send_message(m.chat.id, 'ارسال شد')
                            if m.photo:
                                cid = m.reply_to_message.forward_from.id
                                photo = m.photo[2].file_id
                                bot.send_photo(cid,photo)
                                bot.send_message(m.chat.id, 'ارسال شد')
                            if m.sticker:
                                cid = m.reply_to_message.forward_from.id
                                sticker = m.sticker.file_id
                                bot.send_sticker(cid, sticker)
                                bot.send_message(m.chat.id, 'ارسال شد')
                        if m.reply_to_message.document:
                            if m.text:
                                cid = m.reply_to_message.forward_from.id
                                text = m.text
                                bot.send_message(cid,text)
                                bot.send_message(m.chat.id, 'ارسال شد')
                            if m.photo:
                                cid = m.reply_to_message.forward_from.id
                                photo = m.photo[2].file_id
                                bot.send_photo(cid,photo)
                                bot.send_message(m.chat.id, 'ارسال شد')
                            if m.sticker:
                                cid = m.reply_to_message.forward_from.id
                                sticker = m.sticker.file_id
                                bot.send_sticker(cid, sticker)
                                bot.send_message(m.chat.id, 'ارسال شد')
                        if m.reply_to_message.audio:
                            if m.text:
                                cid = m.reply_to_message.forward_from.id
                                text = m.text
                                bot.send_message(cid,text)
                                bot.send_message(m.chat.id, 'ارسال شد')
                            if m.photo:
                                cid = m.reply_to_message.forward_from.id
                                photo = m.photo[2].file_id
                                bot.send_photo(cid,photo)
                                bot.send_message(m.chat.id, 'ارسال شد')
                            if m.sticker:
                                cid = m.reply_to_message.forward_from.id
                                sticker = m.sticker.file_id
                                bot.send_sticker(cid, sticker)
                                bot.send_message(m.chat.id, 'ارسال شد')
        if str(m.from_user.id) == admin:
            if m.text == '/ban':
                ids = m.reply_to_message.forward_from.id
                redis.sadd('banlist_pmbot',ids)
                bot.send_message(ids, '<code>شما بلاک شدید</code>',parse_mode='HTML')
                bot.send_message(admin, 'بن شد')
            if m.text == '/unban':
                ids = m.reply_to_message.forward_from.id
                redis.srem('banlist_pmbot',ids)
                bot.send_message(ids, 'شما از از لیست بلاک حذف شدید')
                bot.send_message(admin, 'حذف شد')
            if m.text == '/stats':
                msm = redis.scard('member_pmbot')
                bot.send_message(m.chat.id, 'Users : <code>{}</code>'.format(msm),parse_mode='HTML')
            if m.text == '/banlist':
                banliss = redis.scard('banlist_pmbot')
                bot.send_message(m.chat.id, '<b>{}</b>\nبرای حذف کردن لیست بن دستور زیر رو بزن\n/clean banlist'.format(banliss), parse_mode='HTML')
            if m.text == '/clean banlist':
                redis.delete('banlist_pmbot')
                bot.send_message(m.chat.id, 'پاک شدند')
            if m.text == '/help' or m.text == '/start':
                bot.send_message(admin, """
/ban
بن کردن افراد با ریپلی
/unban
حذف بن افراد با ریپلی
/stats
اعضای ربات
/banlist
لیست بن
/clean banlist
حذف لیست  بن
                """)
    except:
        bot.send_message(m.chat.id, 'Error')

bot.polling(True)
#end 180 line by negative
