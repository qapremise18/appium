import configparser
config = configparser.RawConfigParser()
config.read('D:\\PythonWS\\Premise\\resources\\config.properties')
sec = config.get("WAITS", "MAX_WAIT_TIME_SECONDS")
sec = config.get("WAITS1", "MAX_WAIT_TIME_SECONDS1")
print(sec)
print(type(sec))
sec = int(sec)
print(type(sec))
print(config.sections())