import os

basedir = os.path.abspath(os.path.join(os.path.dirname(__file__),"."))

class Config(object):
  ### APP-SETTINGS ###
  PUBLIC_IP = "192.168.0.66"      # Public ip of the server
  VPN_PORT_RANGE = (9000,9005)    # Portrange for vpn containers
  # MySQL Connection String
  SQLALCHEMY_DATABASE_URI = "mysql+pymysql://vitsl:vitsl@localhost:3306/vitsl"
  SECRET_KEY = "pretty-secret-secret-key"
  
  CONTAINER_DIR = os.path.abspath(os.path.join(basedir,"../containers")) # Location of the container images
  
  CLEANUP_BEFORE_AND_AFTER = True # Delete all networks before start and when the application quits
  HINT_TIMEOUT = 15               # Minutes the user has to wait for a new hint
  RESET_PASSWORD_LENGTH = 8       # Length of generated password for passwords

  VALID_USERNAME_REGEX = r'[a-zA-Z0-9_.-]*'

  # Creates the tutorial network for a user on registration
  CREATE_TUTORIAL_NETWORK_ON_REGISTRATION = True

  ### OTHER SETTINGS - CAN BE IGNORED ###
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  DEBUG = True                    # Dont supress logging
  TESTING = False


  APP_PREFIX = "vitsl"
  TEMPLATES_AUTO_RELOAD = True

  ### FLASK-SECURITY ###
  SECURITY_USER_IDENTITY_ATTRIBUTES = ('username')
  SECURITY_LOGIN_WITHOUT_CONFIRMATION = True
  SECURITY_SEND_PASSWORD_CHANGE_EMAIL = False
  SECURITY_CHANGEABLE = True
  SECURITY_REGISTERABLE = True
  SECURITY_RECOVERABLE = False
  SECURITY_LOGIN_USER_TEMPLATE = 'login_user.jinja'
  SECURITY_REGISTER_USER_TEMPLATE = 'register_user.jinja'
  SECURITY_CHANGE_PASSWORD_TEMPLATE = 'change_password.jinja'

  SECUIRTY_POST_LOGIN = '/'
  SECURITY_POST_LOGOUT_VIEW = '/login'
  SECURITY_POST_LOGIN_VIEW = "/"
  SECURITY_TRACKABLE = False
  SECURITY_PASSWORD_HASH = 'pbkdf2_sha512'    
  SECURITY_PASSWORD_SALT = 'aa0e8ab43c9841f9949e94a3e16f308a'

  SECURITY_MSG_USER_DOES_NOT_EXIST = ('Username or password are incorrect.', 'error')
  SECURITY_MSG_INVALID_EMAIL_ADDRESS = ('Username or password are incorrect.', 'error')
  SECURITY_MSG_INVALID_PASSWORD = ('Username or password are incorrect.', 'error')


