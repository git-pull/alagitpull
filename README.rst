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

Theme variables
"""""""""""""""

To see a full list of options passible to HTML templates, see
``theme.conf``. Not all of these options are used in the theme itself,
but to let ``html_theme_options`` pass them through, if you want.

To configure, *conf.py*:

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

Example of using an optional variable such as
``theme_show_meta_app_icons_tags``:

.. code-block:: python

   html_theme_options = {
       # ...usual stuff, as above, and
       'project_description': 'description of project'
   }


.. code-block:: html

   {%- if theme_show_meta_app_icon_tags == true %}
   <meta name="theme-color" content="#ffffff">
   <meta name="application-name" content="{{ theme_project_description }}">

   <link rel="shortcut icon" href="/_static/favicon.ico">
   <link rel="icon" type="image/png" sizes="512x512" href="/_static/img/icons/icon-512x512.png">
   <link rel="icon" type="image/png" sizes="192x192" href="/_static/img/icons/icon-192x192.png">
   <link rel="icon" type="image/png" sizes="32x32" href="/_static/img/icons/icon-32x32.png">
   <link rel="icon" type="image/png" sizes="96x96" href="/_static/img/icons/icon-96x96.png">
   <link rel="icon" type="image/png" sizes="16x16" href="/_static/img/icons/icon-16x16.png">

   <!-- Apple -->
   <meta name="apple-mobile-web-app-title" content="{{ theme_project_name }}">

   <link rel="apple-touch-icon" sizes="192x192" href="/_static/img/icons/icon-192x192.png">
   <link rel="mask-icon" href="/_static/img/{{ theme_project_name }}.svg" color="grey">

   <!-- Microsoft -->
   <meta name="msapplication-TileColor" content="#ffffff">
   <meta name="msapplication-TileImage" content="/_static/img/icons/ms-icon-144x144.png">
   {% endif -%}


Variables
"""""""""

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
