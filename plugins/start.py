from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("🤖 Update Channel", url="https://t.me/bx_Botz")],
        [InlineKeyboardButton(
            "Support Group", url="https://t.me/BxSupport")]
    ])
    welcomed = f"Hey <b>{message.from_user.first_name}</b>\nHello,
'This is a Youtube Uploader Bot by @BX_Botz 😇'

'Please Send Me Any YouTube URL 
I Can Upload Into Telegram As Video/File'

'Click /help For More Details' 😇
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
