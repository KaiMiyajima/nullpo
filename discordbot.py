# coding:UTF-8
import discord
import os
import traceback
from discord.ext import tasks
from datetime import datetime, timedelta, timezone



# ↓はトークンの自動取得をしようとしてできなかった残骸
token = os.environ['DISCORD_BOT_TOKEN']

client = discord.Client()


@client.event
async def on_message(message):
    # ユーザが"/date"と入力するのを検知
    if message.content.startswith("date"):

        # 送り主がBotだった場合反応したくないので
        if client.user != message.author:

            # 現在の時刻を取得して"now"変数に格納
            JST = timezone(timedelta(hours=+9), 'JST')
            now = datetime.now(JST).strftime('%H:%M')

            # メッセージを"ms"変数に格納
            ms = now + "に" + message.author.name + "さんがタイムカードを切りました。"

            # メッセージを出力
            await message.channel.send(ms)

# Botの起動とDiscordサーバーへの接続
client.run(token)
