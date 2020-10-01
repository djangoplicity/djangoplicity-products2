from .settings import *

# ENVIRONMENT CONFIG
SITE_ENVIRONMENT = os.environ.get('ENVIRONMENT', 'dev')
SHORT_NAME = 'Djangoplicity'
TMP_DIR = os.path.join(BASE_DIR, 'tmp')

# CUSTOM CONFIG DEFAULTS
SERVE_STATIC_MEDIA = True
VIDEOS_THUMBNAIL_POSITION = 5  # Value in seconds or 'middle' to calculate the middle of the videos

# APPLICATION DEFINITION
DJANGO_APPS = [
    # Do not autodiscover admin.py modules in all apps because test_project.admin configures custom Admin Sites itself
    # See: https://docs.djangoproject.com/en/1.10/ref/contrib/admin/#discovery-of-admin-files
    'django.contrib.admin.apps.SimpleAdminConfig',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Manage multiple domains content
    'django.contrib.sites',
    # Redirect URLs
    'django.contrib.redirects',
]

DJANGOPLICITY_APPS = [
    # Djangoplicity is an app package itself containing main templates, statics, etc
    'djangoplicity',
    'djangoplicity.menus',
    'djangoplicity.pages',
    'djangoplicity.metadata',
    'djangoplicity.archives',
    'djangoplicity.releases',
    'djangoplicity.adminhistory',
    'djangoplicity.media',
    'djangoplicity.eventcalendar',
    'djangoplicity.iframe',
    # Used to create images derivatives
    'djangoplicity.cutter',
    'djangoplicity.announcements',
    'djangoplicity.reports',
    'djangoplicity.utils',
    'djangoplicity.admincomments',
    'djangoplicity.products2',
]

THIRD_PARTY_APPS = [
    # WYSIWYG HTML Editor (Used for example in pages editing)
    'tinymce',
    # Utility for implementing a modified pre-order traversal tree in django, used in menu items
    # See: https://www.caktusgroup.com/blog/2016/01/04/modified-preorder-tree-traversal-django/
    'mptt',
]

TEST_PROJECT_APPS = [
    'test_project'
]

INSTALLED_APPS = DJANGO_APPS + DJANGOPLICITY_APPS + THIRD_PARTY_APPS + TEST_PROJECT_APPS

# SITES
SITE_ID=1

if USE_I18N:
    INSTALLED_APPS += [
        'djangoplicity.translation',
    ]

    MIDDLEWARE += [
        # Sets local for request based on URL prefix.
        'djangoplicity.translation.middleware.LocaleMiddleware',  # Request/Response
    ]


# MEDIA
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = "/media/"


# JAVASCRIPT CUSTOM CONFIG
JQUERY_JS = "jquery/jquery-1.11.1.min.js"
JQUERY_UI_JS = "jquery-ui-1.12.1/jquery-ui.min.js"
JQUERY_UI_CSS = "jquery-ui-1.12.1/jquery-ui.min.css"
DJANGOPLICITY_ADMIN_CSS = "djangoplicity/css/admin.css"
DJANGOPLICITY_ADMIN_JS = "djangoplicity/js/admin.js"
SUBJECT_CATEGORY_CSS = "djangoplicity/css/widgets.css"


# Social Networks
SOCIAL_FACEBOOK_WALL = 'https://www.facebook.com/AndresLinaresBC?sk=wall'

# Environment configuration
GA_ID = "XX-XXXXXXX-X"


############
# REPORTS  #
############
REPORTS_DEFAULT_FORMATTER = 'html'
REPORT_REGISTER_FORMATTERS = True


USE_TZ = False

LANGUAGES = [
    ('en', 'English'),
    ('es', 'Spanish'),
]

# ARCHIVES
ARCHIVE_IMPORT_ROOT = os.path.join(BASE_DIR, 'import')
ARCHIVE_ROOT = 'archives/'
IMAGES_ARCHIVE_ROOT = 'archives/images/'
VIDEOS_ARCHIVE_ROOT = 'archives/videos/'
RELEASE_ARCHIVE_ROOT = 'archives/releases/'

ARCHIVE_URL_QUERY_PREFIX = 'archive'
ARCHIVE_URL_DETAIL_PREFIX = ''
ARCHIVE_URL_FEED_PREFIX = 'feed'
ARCHIVE_URL_SEARCH_PREFIX = 'search'

ARCHIVE_AUTO_RESOURCE_DELETION = False
ENABLE_ADVANCED_SEARCH = True

ARCHIVES = (
    ('djangoplicity.media.models.Image', 'djangoplicity.media.options.ImageOptions'),
    ('djangoplicity.media.models.Video', 'djangoplicity.media.options.VideoOptions'),
    ('djangoplicity.media.models.VideoSubtitle', 'djangoplicity.media.options.VideoSubtitleOptions'),
    ('djangoplicity.media.models.ImageComparison', 'djangoplicity.media.options.ImageComparisonOptions'),
)

# Allows templates coverage
TEMPLATES[0]['OPTIONS']['debug'] = True

# CELERY
CELERY_IMPORTS = [
    "djangoplicity.archives.contrib.security.tasks",
    "djangoplicity.celery.tasks",
]
# Task result backend
CELERY_RESULT_BACKEND = "amqp"	
CELERY_BROKER_URL = 'amqp://guest:guest@broker:5672/'
# Avoid infinite wait times and retries
CELERY_BROKER_TRANSPORT_OPTIONS = {
    'max_retries': 3,
    'interval_start': 0,
    'interval_step': 0.2,
    'interval_max': 0.2,
}
# AMQP backend settings - Required for flower to work as intended
CELERY_RESULT_SERIALIZER = "json"
CELERY_RESULT_EXPIRES = 3600
# File to save revoked tasks across workers restart
CELERY_WORKER_STATE_DB = os.path.join(TMP_DIR, 'celery_states')
CELERY_BEAT_SCHEDULE_FILENAME = os.path.join(TMP_DIR, 'celerybeat_schedule')

ARCHIVES = (
    ('djangoplicity.products2.models.Application', 'djangoplicity.products2.options.ApplicationOptions'),
    ('djangoplicity.products2.models.MiniSite', 'djangoplicity.products2.options.MiniSiteOptions'),
    ('djangoplicity.products2.models.EducationalProgram', 'djangoplicity.products2.options.EducationalProgramOptions'),
    ('djangoplicity.products2.models.PaperModel', 'djangoplicity.products2.options.PaperModelOptions'),
    ('djangoplicity.products2.models.AnnualReport', 'djangoplicity.products2.options.AnnualReportOptions'),
    ('djangoplicity.products2.models.Book', 'djangoplicity.products2.options.BookOptions'),
    ('djangoplicity.products2.models.Brochure', 'djangoplicity.products2.options.BrochureOptions'),
    ('djangoplicity.products2.models.Calendar', 'djangoplicity.products2.options.CalendarOptions'),
    ('djangoplicity.products2.models.Media', 'djangoplicity.products2.options.MediaOptions'),
    ('djangoplicity.products2.models.EducationalMaterial', 'djangoplicity.products2.options.EducationalMaterialOptions'),
    ('djangoplicity.products2.models.Exhibition', 'djangoplicity.products2.options.ExhibitionOptions'),
    ('djangoplicity.products2.models.FITSImage', 'djangoplicity.products2.options.FITSImageOptions'),
    ('djangoplicity.products2.models.Flyer', 'djangoplicity.products2.options.FlyerOptions'),
    ('djangoplicity.products2.models.Handout', 'djangoplicity.products2.options.HandoutOptions'),
    ('djangoplicity.products2.models.IMAXFilm', 'djangoplicity.products2.options.IMAXFilmOptions'),
    ('djangoplicity.products2.models.KidsDrawing', 'djangoplicity.products2.options.KidsDrawingOptions'),
    ('djangoplicity.products2.models.Logo', 'djangoplicity.products2.options.LogoOptions'),
    ('djangoplicity.products2.models.Apparel', 'djangoplicity.products2.options.ApparelOptions'),
    ('djangoplicity.products2.models.Map', 'djangoplicity.products2.options.MapOptions'),
    ('djangoplicity.products2.models.Merchandise', 'djangoplicity.products2.options.MerchandiseOptions'),
    ('djangoplicity.products2.models.Bulletin', 'djangoplicity.products2.options.BulletinOptions'),
    ('djangoplicity.products2.models.Stationery', 'djangoplicity.products2.options.StationeryOptions'),
    ('djangoplicity.products2.models.ScienceInSchool', 'djangoplicity.products2.options.ScienceInSchoolOptions'),
    ('djangoplicity.products2.models.Messenger', 'djangoplicity.products2.options.MessengerOptions'),
    ('djangoplicity.products2.models.CapJournal', 'djangoplicity.products2.options.CapJournalOptions'),
    ('djangoplicity.products2.models.STECFNewsletter', 'djangoplicity.products2.options.STECFNewsletterOptions'),
    ('djangoplicity.products2.models.OnlineArt', 'djangoplicity.products2.options.OnlineArtOptions'),
    ('djangoplicity.products2.models.OnlineArtAuthor', 'djangoplicity.products2.options.OnlineArtAuthorOptions'),
    ('djangoplicity.products2.models.PlanetariumShow', 'djangoplicity.products2.options.PlanetariumShowOptions'),
    ('djangoplicity.products2.models.Donation', 'djangoplicity.products2.options.DonationOptions'),
    ('djangoplicity.products2.models.PostCard', 'djangoplicity.products2.options.PostCardOptions'),
    ('djangoplicity.products2.models.PrintedPoster', 'djangoplicity.products2.options.PrintedPosterOptions'),
    ('djangoplicity.products2.models.ConferenceItem', 'djangoplicity.products2.options.ConferenceItemOptions'),
    ('djangoplicity.products2.models.ConferencePoster', 'djangoplicity.products2.options.ConferencePosterOptions'),
    ('djangoplicity.products2.models.ElectronicPoster', 'djangoplicity.products2.options.ElectronicPosterOptions'),
    ('djangoplicity.products2.models.Presentation', 'djangoplicity.products2.options.PresentationOptions'),
    ('djangoplicity.products2.models.PressKit', 'djangoplicity.products2.options.PressKitOptions'),
    ('djangoplicity.products2.models.ElectronicCard', 'djangoplicity.products2.options.ElectronicCardOptions'),
    ('djangoplicity.products2.models.Sticker', 'djangoplicity.products2.options.StickerOptions'),
    ('djangoplicity.products2.models.TechnicalDocument', 'djangoplicity.products2.options.TechnicalDocumentOptions'),
    ('djangoplicity.products2.models.UserVideo', 'djangoplicity.products2.options.UserVideoOptions'),
    ('djangoplicity.products2.models.VirtualTour', 'djangoplicity.products2.options.VirtualTourOptions'),
    ('djangoplicity.products2.models.Model3d', 'djangoplicity.products2.options.Model3dOptions'),
    ('djangoplicity.products2.models.Music', 'djangoplicity.products2.options.MusicOptions'),
    ('djangoplicity.products2.models.Mirror', 'djangoplicity.products2.options.MirrorOptions'),
    ('djangoplicity.products2.models.GeminiFocus', 'djangoplicity.products2.options.GeminiFocusOptions'),
    ('djangoplicity.products2.models.NOAONewsletter', 'djangoplicity.products2.options.NOAONewsletterOptions'),
    ('djangoplicity.products2.models.CitizenScienceProgram', 'djangoplicity.products2.options.CitizenScienceProgramOptions'),
)
