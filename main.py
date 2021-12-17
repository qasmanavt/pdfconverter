from PIL import Image
from aiogram import Bot,types
from aiogram.dispatcher.dispatcher import Dispatcher
 

 
 
from aiogram.utils import executor
 
 
 
bot= Bot(token="5099925235:AAEtgJ_d6xzzWffTmr3ACDc49RHD_qmOESI")
# "5099925235:AAEtgJ_d6xzzWffTmr3ACDc49RHD_qmOESI")
dp=Dispatcher(bot)


@dp.message_handler(content_types=types.ContentType.PHOTO)
async def download_photo(message: types.Message):
    await message.photo[-1].download(str(message.from_user.full_name)+".jpg")
    print(await message.photo[-1].get_url())
    print(await message.photo[-1].get_file())
   
    # img=cv2.imread("picture_"+str(message.from_user.full_name)+".jpg")
    # gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    # gray=cv2.medianBlur(gray,5)
    # edges=cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,9,9)
    # color=cv2.bilateralFilter(img,9,250,250)
    # cartoon=cv2.bitwise_and(color,color,mask=edges)
    # # cv2.imshow("Image",img)
    # # cv2.imshow("edges",edges)
    # cv2.imshow("Cartoon", cartoon)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    pdf=Image.open(str(message.from_user.full_name)+".jpg")
    pdf.save( str(message.from_user.full_name)+".pdf")
    await message.answer("successfully downloaded")
    await bot.send_document(chat_id=message.from_user.id, document=open( str(message.from_user.full_name)+".pdf","rb"),caption="abc")
    # await bot.send_document(chat_id=message.from_user.id, document=open("C:\pdfconverter\picture__"+str(message.from_user.full_name)+".pdf","rb"))
@dp.message_handler(commands=['start'])
async def proccess_start_comman(message: types.Message):
    
    keyboard=types.ReplyKeyboardMarkup(resize_keyboard=True)
  
    keyboard.add(types.KeyboardButton(text="abc",request_contact=True))
    await message.answer("hello",reply_markup=keyboard)
@dp.message_handler(content_types="contact")
async def with_pure(message: types.Message):
 
    await message.answer("share your picture")

executor.start_polling(dp)