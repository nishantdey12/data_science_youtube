#logger: documentation
#any execution that is probably happening we should be able to log execution in some file so that track 
import logging
from operator import truediv
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
#this is a text file using this naming convention this will be created
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
#os.cwd gives the current working directory. file name will start will logs and then the naming convention
os.makedirs(logs_path,exist_ok=True)
#even though there is a file, keep adding things to that file only

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)",
    level=logging.INFO
)
#incase of info only we will get these specific messages
#wherever i use import logging and logging.info and i write down any print message then it will use this basic config, and it will use this kind of filepath 

if __name__=="__main__":
    logging.info("Logging has started")