=====================
git-pull sphinx theme
=====================

`Sphinx`_ sub-theme of `Alabaster`_, for use on git-pull projects.

What alagitpull adds to Alabaster
---------------------------------

See the theme live on https://www.git-pull.com,
https://tmuxp.git-pull.com, etc.

- Table CSS tweaks
- ``<pre>`` and code-block css tweaks
- Additional theming tweaks for `admonitions`_ like ``..note``.
- New sidebar template with links to projects

  - Automatic unlinking of project if its the current docs
  - Support for subprojects (put into parenthesis)
- Sidebar CSS tweaks

Config options
--------------

(Inside *conf.py*)

*html_theme_options* example:

    .. code-block:: python

        html_theme_options = {
            'logo': 'img/logo.svg',
            'github_user': 'git-pull',
            'github_repo': 'alagitpull',
            'github_type': 'star',
            'github_banner': True,
            'projects': {},
            'project_name': 'my project name',
        }

For an example of ``html_theme_options['projects']`` see the
*alagitpull/__init__.py* file.

Variables:

*alagitpull_external_hosts_new_window* (boolean, default: False): check if link 
is external domain/IP. If so, open in new window.

.. code-block:: python

   alagitpull_external_hosts_new_window = True

*alagitpull_internal_hosts* (list) - whitelist of domains to open
in same tab, *without* ``target="_blank"``. Only used if
*alagitpull_external_hosts_new_window* enabled.

Example:

.. code-block:: python

   alagitpull_internal_hosts = [
      'libtmux.git-pull.com',
      '0.0.0.0',
   ]

Theme options
-------------

``html_theme_options`` of sphinx's conf.py:

- *projects* (dict) - Sidebar links.    
- *project_name* (string) - Name of your project (helps with unlinking


.. _Sphinx: http://www.sphinx-doc.org/
.. _Alabaster: https://github.com/bitprophet/alabaster
.. _admonitions: http://docutils.sourceforge.net/docs/ref/rst/directives.html#admonitions
