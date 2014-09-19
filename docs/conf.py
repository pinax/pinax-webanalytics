import pkg_resources

extensions = []
templates_path = []
source_suffix = '.rst'
master_doc = 'index'
project = u'metron'
copyright = u'2014 James Tauber and Contributors'
exclude_patterns = ['_build']
pygments_style = 'sphinx'
html_theme = 'default'
htmlhelp_basename = 'metrondoc'
latex_documents = [
    ('index', 'metron.tex', u'metron Documentation',
     u'Pinax', 'manual'),
]
man_pages = [
    ('index', 'metron', u'metron Documentation',
     [u'Pinax'], 1)
]

version = pkg_resources.get_distribution("metron").version
release = version
