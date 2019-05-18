import os

from alagitpull import _version as version
from .writers.external import GitPullHTMLTranslator, ALLOWED_HOSTS

projects = [
    {
        'name': 'unihan-etl',
        'url': 'https://unihan-etl.git-pull.com',
        'subprojects': [{
            'name': 'db',
            'url': 'https://unihan-db.git-pull.com',
        }]
    }, {
        'name': 'cihai',
        'url': 'https://cihai.git-pull.com',
        'subprojects': [{
            'name': 'cli',
            'url': 'https://cihai-cli.git-pull.com',
        }]
    }, {
        'name': 'tmuxp',
        'url': 'https://tmuxp.git-pull.com',
        'subprojects': [{
            'name': 'libtmux',
            'url': 'https://libtmux.git-pull.com',
        }]
    },
    {
        'name': 'vcspull',
        'url': 'https://vcspull.git-pull.com',
        'subprojects': [{
            'name': 'libvcs',
            'url': 'https://libvcs.git-pull.com',
        }]
    }
]


def get_path():
    """
    Shortcut for users whose theme is next to their conf.py.
    """
    # Theme directory is defined as our parent directory
    return os.path.abspath(os.path.dirname(__file__))


def update_context(app, pagename, templatename, context, doctree):
    context['alagitpull_version'] = version.__version__


def setup(app):
    app.connect('html-page-context', update_context)

    app.set_translator('html', GitPullHTMLTranslator)
    # for RTD: https://git.io/vAct0
    app.set_translator('readthedocs', GitPullHTMLTranslator)

    app.add_config_value('alagitpull_internal_hosts', ALLOWED_HOSTS, 'html')
    app.add_config_value('alagitpull_external_hosts_new_window', False, 'html')

    app.add_html_theme('alagitpull', get_path())

    return {
        'version': version.__version__,
        'parallel_read_safe': True,
    }
