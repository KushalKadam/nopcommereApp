import logging
class LogGen:
    @staticmethod  #So that we can directly call method without creating object and we can remove selffrom method
    def loggen():
        logging.basicConfig(filename=".\\Logs\\automation.log",
                            format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m%d%Y %I%M%S %p')
        logger  = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger