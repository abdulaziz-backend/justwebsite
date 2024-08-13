from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

def generate_start_keyboard(user_id: int) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="earn $BLAZE🔥",
                    web_app=WebAppInfo(url=f"https://608d-213-230-92-128.ngrok-free.app/?user_id={user_id}")
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
                web_app=WebAppInfo(url="https://608d-213-230-92-128.ngrok-free.app/")
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
