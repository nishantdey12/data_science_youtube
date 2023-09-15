#exception handling
#search exception in python
import sys
import logging
#provides various functions and variables that are used to manipulate different parts od python runtime environment

def error_message_detail(error, error_detail:sys):
    _,_,exc_tb=error_detail.exc_info() #info function will give error details
    file_name=exc_tb.tb_frame.f_code.co_filename  #properties inside one another that is available in exception handling documentation
    #search in google custom exception handling
    error_message="Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name,exc_tb.tb_lineno,str(error)
        
    )
    return error_message

'''
explanation given in video: inheriting the parent exception
self is the variable of class. handy keyword allows you to access variables, attributes, and methods of a defined class in Python

'''
class CustomException(Exception):
    def __init__(self,error_message, error_detail:sys):#constructor
        super().__init__(error_message)  #what is happening here
        self.error_message=error_message_detail(error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_message


if __name__=="__main__":
    try:
        a=1/0
    except Exception as e:
        logging.info("Divide by zero  ")
        raise CustomException(e, sys)
       