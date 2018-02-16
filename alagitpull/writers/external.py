"""Extension to load external links in new window."""
import re
from sphinx.writers.html import HTMLTranslator
from docutils import nodes

try:
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse

ALLOWED_HOSTS = [
    'git-pull.com',
    '0.0.0.0',
]


def is_external_link(url, internal_hosts):
    """Determine if a URL is internal or external

    :param url: url to check if off-site
    :type url: string
    :param hosts: whitelist of host TLD/IP's that are internal
    :type hosts: list
    :returns: whether url is internal or external to website
    :rtype: value
    """
    tld = urlparse(url).hostname or url
    return (
        not any(tld in host for host in internal_hosts) and
        not url.startswith('#') and
        not re.match(r'(\.\.)?(\/)?[\w\/_-]*\.html', url) and
        not url.startswith('/')
    )


class GitPullHTMLTranslator(HTMLTranslator):

    def visit_reference(self, node):
        """
        Changes:

        - monkeypatch bugfix https://sourceforge.net/p/docutils/bugs/322/
        - add target _blank to offsite urls
        - add class offsite for offsite urls
        - add class insite for insite urls (note, internal is already used
          for reference links in the *same* document)
        - Checks for sphinx builder config, if exists
        """
        atts = {'class': 'reference'}
        external_hosts_new_window = False
        if self.builder.config:
            if self.builder.config.alagitpull_external_hosts_new_window:
                external_hosts_new_window = \
                    self.builder.config.alagitpull_external_hosts_new_window
            if self.builder.config.alagitpull_internal_hosts:
                hosts = self.builder.config.alagitpull_internal_hosts
            else:
                hosts = ALLOWED_HOSTS

        if 'refuri' in node:
            atts['href'] = node['refuri']
            atts['class'] += ' external'
            if (
                external_hosts_new_window and
                is_external_link(node['refuri'], hosts)
            ):
                atts['target'] = '_blank'
                atts['class'] += ' offsite'
                # sphinx sites, a ref wrapping a nodes.literal is a code link
                if isinstance(node[0], nodes.literal):
                    atts['class'] += ' code'
            else:
                atts['class'] += ' insite'
        else:
            assert 'refid' in node, \
                'References must have "refuri" or "refid" attribute.'
            atts['href'] = '#' + node['refid']
            atts['class'] += ' internal'

        self.body.append(self.starttag(node, 'a', '', **atts))
