import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title="Please Drink Water Now !",
            message="The National Academies of Sciences, Engineering, and Medicine determined that an adequate daily fluid intake is: About 15.5 cups (3.7 liters) of fluids for men. About 11.5 cups (2.7 liters) of fluids a day for women.",
            app_icon="D:\\1ST\Programming\Python projects\desktopNotification\Iconsmind-Outline-Glass-Water.ico", #change this
            timeout=10
        )
        # if you don't run it with window sheduler so you canrun it with pythonw
        # and if you are running it on window shedular you can remove while loop and time.sleep ok
        
        time.sleep(900)
        # for give min it be better to use 
