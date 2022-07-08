import logging
import logging.handlers

class LogGen:
    @staticmethod
    def logs():

        logger = logging.getLogger(__name__)

        logger.setLevel(logging.INFO)
        f = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        fh = logging.FileHandler("..//Logs//automationTestsLoging.log")
        fh.setFormatter(f)
        logger.addHandler(fh)
        return logger

# # class LogGen:
# #     @staticmethod
# def loggen():
#     logging.basicConfig(filename="..//Logs//auto.log",
#                         format='%(asctime)s: %(levelname)s: %(message)s',
#                         datefmt='%m/%d/%Y %I:%M:%S %p')
#     # rotate_file = logging.handlers.RotatingFileHandler("Logs/readLogs.log", maxBytes=1024 * 1024 * 20,
#     #                                                    backupCount=3)
#
#     logger = logging.getLogger()
#     # logger.addHandler(rotate_file)
#     logger.setLevel(logging.INFO)
#     return logger

#
# # a = LogGen.loggen()
# print("f")
# a.info("************************** Test_001  Launch Browser *************************")
# print("bl"
#       "")