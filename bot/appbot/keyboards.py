from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

START = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="earn $BLAZE🔥",
                web_app=WebAppInfo(url="https://x.com/") 
            )
        ],
        [
            InlineKeyboardButton(
                text="Invite Friends",
                callback_data="invite"
            )
        ],
        [
            InlineKeyboardButton(
                text="Join Community on Telegram",
                url="https://t.me/BLAZECOMUNITY" 
            ),
            InlineKeyboardButton(
                text="Join Community on X",
                url="https://x.com/blaze_meme_coin"
            )
        ]
    ]
)

profile = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="🔥TAP🔥",
                web_app=WebAppInfo(url="https://x.com/")
            )
        ],
        [
            InlineKeyboardButton(
                text="Invite Friends",
                callback_data="invite"
            )
        ]
    ]
)