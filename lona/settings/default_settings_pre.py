import os

DEBUG = False

MAX_WORKERS = 10

# routing
ROUTING_TABLE = 'lona.settings.default_routes.routes'

# templating
CORE_TEMPLATE_DIRS = [
    os.path.join(os.path.dirname(os.path.dirname(__file__)), 'templates'),
]

TEMPLATE_DIRS = []

FRONTEND_TEMPLATE = 'lona/frontend.html'
ERROR_404_TEMPLATE = 'lona/404.html'
ERROR_500_TEMPLATE = 'lona/500.html'

TEMPLATE_EXTRA_CONTEXT = {}

# static files
CORE_STATIC_DIRS = [
    os.path.join(os.path.dirname(os.path.dirname(__file__)), 'static'),
]

STATIC_DIRS = []
STATIC_URL_PREFIX = '/static/'
STATIC_FILES_STYLE_TAGS_TEMPLATE = 'lona/style_tags.html'
STATIC_FILES_SCRIPT_TAGS_TEMPLATE = 'lona/script_tags.html'
STATIC_FILES_SYMBOLS_TEMPLATE = 'lona/lona-symbols.js'
STATIC_FILES_ENABLED = []
STATIC_FILES_DISABLED = []

# state
SERVER_STATE_ATOMIC = True

# views
FRONTEND_VIEW = 'lona.views.frontend'
VIEW_CACHING = True

# error handler
ERROR_404_HANDLER = 'lona.views.handle_404'
ERROR_500_HANDLER = 'lona.views.handle_500'
ERROR_404_FALLBACK_HANDLER = 'lona.views.handle_404'
ERROR_500_FALLBACK_HANDLER = 'lona.views.handle_500'

# middlewares
CORE_MIDDLEWARES = [
    'lona.middlewares.LonaMessageMiddleware',
]

MIDDLEWARES = []

# scheduling
TASK_ZONES = [
    ('service',         5),

    ('system-high',    10),
    ('system-medium',   5),
    ('system-low',      2),

    ('high',           10),
    ('medium',          5),
    ('low',             2),
]

THREAD_ZONES = [
    ('service',         5),

    ('system-high',    10),
    ('system-medium',   5),
    ('system-low',      2),

    ('high',           10),
    ('medium',          5),
    ('low',             2),
]

DEFAULT_TASK_ZONE = 'medium'
DEFAULT_THREAD_ZONE = 'medium'

ROUTING_PRIORITY = 'system-high'
HTTP_REQUEST_PRIORITY = 'system-medium'
STATIC_REQUEST_PRIORITY = 'system-low'
CONNECTION_MIDDLEWARE_PRIORITY = 'system-medium'
WEBSOCKET_MIDDLEWARE_PRIORITY = 'system-medium'
REQUEST_MIDDLEWARE_PRIORITY = 'system-medium'
FRONTEND_VIEW_PRIORITY = 'system-high'
STOP_PRIORITY = 'system-high'

DEFAULT_MULTI_USER_VIEW_PRIORITY = 'service'
DEFAULT_HOOK_PRIORITY = 'service'
DEFAULT_VIEW_PRIORITY = 'medium'
DEFAULT_CUSTOM_MESSAGE_PRIORITY = 'low'
DEFAULT_MIDDLEWARE_PRIORITY = 'medium'

# hooks
HOOKS = {}