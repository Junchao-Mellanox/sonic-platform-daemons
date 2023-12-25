from sonic_py_common.logger import Logger

# Global logger instance for xcvrd, the argument "enable_set_log_level_on_fly"
# will start a thread to detect CONFIG DB LOGGER table change. The logger instance 
# allow user to set log level via swssloglevel command at real time. This instance 
# should be shared by all modules of xcvrd to avoid starting too many logger thread.
logger = Logger(log_identifier='xcvrd', enable_set_log_level_on_fly=True)
