import os
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS

DEVELOPMENT = True
DEBUG = DEVELOPMENT
TEMPLATE_DEBUG = DEBUG
HOME_DIR = '/var/django/spiffcity' if not DEVELOPMENT else '/var/django/spiffcity_dev'

BETA = False
GENDERCODES = ['M', 'F']
SALT = '^^__GETSPIFFED__^^'
ENUMS = {
	'GENDER' : (('M', 'Male'), ('F', 'Female')),
	'YES_NO' : (('Y', 'Yes'), ('N', 'No')),
	'SELECT_TYPE' : (('R', 'Radio'), ('C', 'Combo')),
    'PHONE' : (('H','Home'),('M','Mobile'),('W','Work'),('F','Fax')),
}
SPECIAL_CHARS = [ '!', '@', '#', '$', '^', '&', '*', '?' ]
DEFAULT_MARKET = 'atlanta'
PRIVACY_SETTINGS = {
	'SHARE_NONE' : ( 0,'Nothing' ),
	'SHARE_NAME' : ( (1 << 0), 'Name' ),
	'SHARE_PIC' : ( (1 << 1), 'Profile Picture' ),
	'SHARE_EMAIL' : ( (1 << 2), 'Email Address' ),
	'SHARE_POINTS' : ( (1 << 3), 'Points Earned' )
}
YELP_YWSID = 'eVSBsPFvh5iXncPn3XQGKg'

ADMINS = (
    ('Yacir Hussain', 'yacir.hussain@gmail.com'),
)

MANAGERS = ADMINS

DEFAULT_DATABASE_SCHEMA = 'spiffcity' if not DEVELOPMENT else 'spiffcity_dev'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': DEFAULT_DATABASE_SCHEMA,
        'USER': 'spiffdb',
        'HOST': 'localhost',
        'PORT': '3306',
        'PASSWORD': 'spiffq7c4Ereb',
        'TABLEOPTS': 'ENGINE=InnoDB'
    }
}
DATABASE_ENGINE = 'mysql'

TIME_ZONE = 'America/New_York'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
MEDIA_URL = 'http://cdndev.spiffcity.com' # NOTE: This will be entirely served by nginx for high performance
STATIC_URL = '/static/'
ADMIN_MEDIA_PREFIX = 'http://cdndev.spiffcity.com/admin/'
EMAIL_HOST = '127.0.0.1'
EMAIL_PORT = 25
DEFAULT_FROM_EMAIL = 'no-reply@spiffcity.com'
SERVER_EMAIL = 'no-reply@spiffcity.com'
CSRF_COOKIE_DOMAIN = '.spiffcity.com'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}

STATICFILES_DIRS = (
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

SECRET_KEY = 'SPIFF7j6l$2%6twd_1=_ldu95=k0@#$8qlft9xxxx9l+(uo4^iowglCITY'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
 'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.csrf.CsrfResponseMiddleware',
    
    'libs.middlewares.DomainMiddleware'
    
    
    #'django.middleware.common.CommonMiddleware',
    #'django.contrib.sessions.middleware.SessionMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    #'django.contrib.messages.middleware.MessageMiddleware',
    #'django.middleware.transaction.TransactionMiddleware',
    #'core.middleware.SecurePathMiddleware',
    #'core.middleware.DefaultMarketMiddleware',
    #'core.middleware.SiteDevelopmentMiddleware',
    #'debug_toolbar.middleware.DebugToolbarMiddleware'
)
HTTPS_SUPPORT = True if not DEVELOPMENT else False
SECURE_REQUIRED_PATHS = (
    '/login',
    '/logout',
    '/register',
    '/me',
    '/beta',
)

ROOT_URLCONF = 'urls'

INTERNAL_IPS = ('127.0.0.1', '69.180.50.4', '0.0.0.0', '72.10.39.157')
DEBUG_TOOLBAR_CONFIG = {
	'INTERCEPT_REDIRECTS': False,
}

TEMPLATE_CONTEXT_PROCESSORS = (
	'django.core.context_processors.request',
	'django.contrib.auth.context_processors.auth',
	'django.contrib.messages.context_processors.messages',
)

INSTALLED_APPS = (
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.admindocs',

	# Site Modules
    'apps.core',
    'apps.temp',
    'apps.geo',
    'apps.importer',
    'apps.reporting',
    'apps.social',
    'apps.spiffs',
    'apps.security',
    'apps.point',
    'apps.affilate',
    'apps.members',
    'apps.importer.commisionjunction',
    #'apps.importer.linkshare'
    'apps.location',
)
SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'
#SESSION_ENGINE = 'django.contrib.sessions.backends.file'
SESSION_COOKIE_DOMAIN = '.spiffcity.com'
SESSION_COOKIE_NAME = 'SPIFFCITY_SESS'
SESSION_COOKIE_AGE = 86400

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

CJPERL = "/var/django/spiffcity_dev/apps/importer/CJPERL/"

CRED = {
	"FACEBOOK_APP_ID" 		: '220934191291689',
	"FACEBOOK_APP_SECRET"	: 'fcb5a64b202fa48611d71a0de9f1b95b',
	"FACEBOOK_RETURN_URL"	: 'http://dev.spiffcity.com/social/facebook/connect/',
	"TWITTER_CONSUMER_KEY"  : '269aR7JnBaLyTqtBPJ2rA', #1Fyl5KWsuFN1ObLMssaLnA',
	"TWITTER_CONSUMER_SECRET":'lALfd3mdbFDdS9FBQFkyEsR0vLuE9k144ZJO44kxhs', #fETDfXhHAs4bY2V6HCL5IAjyieQ2gox1HH5qfDX3L0',
	"TWITTER_RETURN_URL"	: 'http://dev.spiffcity.com/social/twitter/connect/',
	"IPINFO_API_KEY"		: '293291a4aceee5e935261b57a72a804df6020630c183e6345db44326e5e2768d',
	"GROUPON_DEAL_URL"		: 'https://api.groupon.com/v2/deals.json',
	"GROUPON_CLIENT_ID"		: '1ff96d1ec0c008d8427ee92ff623e8151538dd16',
	"LINKSHARE_URL"			: 'http://productsearch.linksynergy.com/productsearch?',
	"LINKSHARE_TOKEN"		: 'da85ad9821c26332701945b69c0398d86ac279fca76ce772030eb323cdf77ccc',	
	"CJ_KEY"				: '00bbb2ce8435bc4a5d33e3d8c3191b9ebd5191a290c24ed00d843dcb4aafed8a6970509922b875302011d111ef8c3bfe5bade6d5f7399de82388530f7670bdef99/62c3eac14cd940341cdad6b38a61ab3ca9503dbf784f2a510275d5a3fe40bb246ada5171b6037ac44587b486bc5a86f714f5103e9a0557dc45130a1b9ed402b5',
	"CJ_WEBSITE_ID"			: '5361093',
	"CJ_ADVERTISERS"		: ','.join([
										#'2969878',
										#'1807847',
										#'1382555',
										#'1613838',
										#'2916100',
										#'3251176',
										'3131014',
										#'1169237',
										#'2156263',
										#'3387105',
										#'3388958',
										#'3361226',
										#'2631591',
										#'698247',
										#'3356536',
										#'1410131',
										#'1463221',
										#'867296',
										#'3335251',
										#'2970358',
										#'3317602',
										#'3371527',
										#'330549',
										#'2962777',
										#'1551486',
										#'2306831',
										#'1452828',
										#'2262441',
										#'770149',
										#'2921681',
										#'3035494',
										#'520129',
										#'2991426',
										#'3305219'
										]) 
}

POINTS_SYS = {
	"MAX_DEGREE" : 4,
}

ENUMS = {
	"GENDER" : (
					('' ,'-Select-Sex-'),
					('M','Male'),
					('F','Female'),
					('N','Not Specified'),
				),
	"MONTHS" : (
					(1	,'January'),
					(2	,'February'),
					(3	,'March'),
					(4	,'April'),
					(5	,'May'),
					(6	,'June'),
					(7	,'July'),
					(8	,'August'),
					(9	,'September'),
					(10	,'October'),
					(11	,'November'),
					(12	,'December')
				),
	"DAYS"	:  (
					(1	,'Monday'),
					(2	,'Tuesday'),
					(3	,'Wedenesday'),
					(4	,'Thurseday'),
					(5	,'Friday'),
					(6	,'Satureday'),
					(7	,'Sunday'),
				),
	"VERIFICATION_PURPOSE" :
				(
					(1	,'Sign Up'),
					(2	,'Forgot Password'),
					(3	,'Complete Profile')
				),
	"NETWORKS" :
				(
					('facebook'	,'facebook'),
					('twitter'	,'twitter'),
				),
	"CONTINENTS"	:
				(
					('Africa','Africa'),
					('Antartica','Antartica'),
					('Asia','Asia'),
					('Australia','Australia'),
					('Euorope','Euorope'),
					('North America','North America'),
					('South America','South America'),
				),
	"INV_STATES"	:
				(
					('SENT'		,'SENT'),
					('VISITED'	,'VISITED'),
					('SIGNUP'	,'SIGNUP'),
					('VERIFIED'	,'VERIFIED'),				
				),
	"POINT_STATUS"	:
				(
					('PENDING'		,'PENDING'),
					('RECEIVED'	,'RECEIVED'),
				),
	"VISIT_STATES"	:
				(
					('PENDING'		,'PENDING'),
					('RECEIVED'	,    'RECEIVED'),
				),
}


PAYPAL_BUSINESS = 'D57HGG3NTB5XY'
if DEVELOPMENT:
	PAYPAL_ENDPOINT = 'https://www.sandbox.paypal.com/cgi-bin/webscr'
else:
	PAYPAL_ENDPOINT = 'https://www.paypal.com/cgi-bin/webscr'

if os.name == 'nt':
	from settings.win32 import *
else:
	if DEVELOPMENT:
		from settings.unix_dev import *
	else:
		from settings.unix import *

MEDIA_UPLOAD_PATH 	= '/var/django/spiffcity_dev/resources/uploads/'
FLAGPATH			= MEDIA_UPLOAD_PATH + "flags/"
MEDIA_ROOT          = "/var/django/spiffcity_dev/resources/static/media/";
CAT_IMAGE_PATH		=  "uploads/cat_image/"
