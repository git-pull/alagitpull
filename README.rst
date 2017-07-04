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

Theme options
-------------

``html_theme_options`` of sphinx's ``conf.py``:

- *projects* (dict) - Sidebar links.    
- *project_name* (string) - Name of your project (helps with unlinking


.. _Sphinx: http://www.sphinx-doc.org/
.. _Alabaster: https://github.com/bitprophet/alabaster
.. _admonitions: http://docutils.sourceforge.net/docs/ref/rst/directives.html#admonitions
