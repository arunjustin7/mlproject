#this logging module is used for tracking 
# It allows you to output messages to a log file or the console.
# events that happen when some software runs
#logger is used for the purpose taht any executions that probably happens  we should be able to track the custom exception 
import logger
import os
import logging
from datetime import datetime 

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# if __name__ == '__main__':
#     logging.info("logging has started")