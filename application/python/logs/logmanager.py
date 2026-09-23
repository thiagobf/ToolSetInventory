from datetime import datetime


class LogManager:
    def __init__(self):
        pass

    def get_timestamp(self):
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def Log(self, _fctname, logfile, message):
        timestamp = self.get_timestamp()
        log_message = f"[{timestamp}] {message}"
        print(log_message)
        with open(f"./application/python/logs/{logfile}", "a") as log_file:
            log_file.write(log_message + "\n")


