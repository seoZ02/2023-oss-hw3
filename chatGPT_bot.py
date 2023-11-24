from openai import OpenAI
import openai
import datetime
import logging 
from telegram import __version__ as TG_VER


client = OpenAI(
    api_key="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"
    )

token = "6597126262:AAFGokjb7XwOXA9k8jLqStQjqa0tUxV2nz0"



def Command(Prompt):

  completion = openai.ChatCompletion.create(
    model = "gpt-4",
    temperature=0,
    messages=[
      {"role": "user", "content": Prompt}
    ]
  )
  result = completion.choices[0]
  message = result.message.content
  print(datetime.datetime.now())
  return message



try:
    from telegram import __version_info__
except ImportError:
    __version_info__ = (0, 0, 0, 0, 0)  

if __version_info__ < (20, 0, 0, "alpha", 1):
    raise RuntimeError(
        f"This example is not compatible with your current PTB version {TG_VER}. To view the "
        f"{TG_VER} version of this example, "
        f"visit https://docs.python-telegram-bot.org/en/v{TG_VER}/examples.html"
    )
from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters



logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)



# activate the telegram channel with /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
  
    user = update.effective_user
    await update.message.reply_html(
        rf"안녕하세요 {user.mention_html()}님, chatgpt AI봇입니다. 무엇이 궁금하신가요?",
        reply_markup=ForceReply(selective=True),
    )



# Getting a response by calling the GPT-4 API
async def chatGPT(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    print (update.message.text)
    await update.message.reply_text("ㆍㆍㆍ") 
    user_prompt = update.message.text
    gpt_answer = Command(user_prompt)

    await update.message.reply_text(gpt_answer) 



def main() -> None:
 
    application = Application.builder().token(token).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chatGPT)) 
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()


