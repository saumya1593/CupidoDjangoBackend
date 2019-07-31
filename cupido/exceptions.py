class Error(Exception):
   """Base class for other exceptions"""
   pass
class KeyError(Error):
   """Raised when the key is not present in dictionary"""
   pass