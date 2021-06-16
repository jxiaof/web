import env
import uvicorn
from logger import logger
from concurrent.futures import ThreadPoolExecutor

from fastapi import FastAPI

app = FastAPI()
from views import index_view
pool = ThreadPoolExecutor(max_workers=env.thread_num)

logger.info("web running !")

# try:
#     # uvicorn.run(app='main:app', host="127.0.0.1", port=8080, reload=True, debug=True)
#     print("hello world !")
# except:
#     pass




