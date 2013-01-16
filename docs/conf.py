import sys, os

extensions = []
templates_path = []
source_suffix = '.rst'
master_doc = 'index'
project = u'metron'
copyright = u'2011-2013, Eldarion'
exclude_patterns = ['_build']
pygments_style = 'sphinx'
html_theme = 'default'
htmlhelp_basename = 'metrondoc'
latex_documents = [
  ('index', 'metron.tex', u'metron Documentation',
   u'Eldarion', 'manual'),
]
man_pages = [
    ('index', 'metron', u'metron Documentation',
     [u'Eldarion'], 1)
]

sys.path.insert(0, os.pardir)
m = __import__(project)

version = m.__version__
release = version