import logging
class test:
# logger = logging.getLogger(__name__)
# logger.setLevel(logging.INFO)
# handler = logging.FileHandler('hello.log')
# handler.setLevel(logging.INFO)
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# handler.setFormatter(formatter)
#
# logger.addHandler(handler)
#
# logger.info('Hello baby')
    def test_log(self):
        logging.basicConfig(filename="test.log", level=logging.DEBUG)
        logging.info("HHHH1")
        logging.debug("HHHH2")
        logging.warning("HHH3H")
        logging.fatal("HHHH4")
        logging.error("HHHH5")

t = test()
t.test_log()

