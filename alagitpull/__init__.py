import os

from alagitpull import _version as version


projects = [
    {
        'name': 'unihan-etl',
        'url': 'https://unihan-etl.git-pull.com',
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
    return os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


def update_context(app, pagename, templatename, context, doctree):
    context['alagitpull_version'] = version.__version__


def setup(app):
    app.connect('html-page-context', update_context)
    return {'version': version.__version__,
            'parallel_read_safe': True}
