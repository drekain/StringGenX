# EVAL – Small safe operations only
from pyrogram import Client, filters
from pyrogram.types import Message
from config import OWNER_ID

@Client.on_message(filters.command("eval") & filters.user(OWNER_ID))
async def safe_eval(_, message: Message):
    if len(message.command) < 2:
        return await message.reply("🛠 Use: `/eval print('hello')`")

    code = message.text.split(None, 1)[1]
    allowed = ["print", "len", "str", "int", "float", "type"]

    if not any(x in code for x in allowed):
        return await message.reply("❌ Restricted eval")

    try:
        result = eval(code, {"__builtins__": {}})
    except Exception as e:
        return await message.reply(f"❌ Error: `{e}`")

    await message.reply(f"📤 Output: `{result}`")
