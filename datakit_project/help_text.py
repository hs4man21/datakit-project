NO_TEMPLATES_ERROR_MSG = """No project templates have been installed!

To install a new template, you must invoke "datakit project create" with
the local path or URL to a Cookiecutter project repo, e.g.:

    datakit project create --template /local/path/to/my-awesome-cookiecutter-template
"""

TEMPLATE_INSTALL_HELP_MSG = """Check out the below URLs for pre-baked templates and installation options:

  - A Pantry Full of Cookiecutters
      https://cookiecutter.readthedocs.io/en/latest/readme.html#a-pantry-full-of-cookiecutters

  - Template install docs
      https://datakit-project.readthedocs.io/en/latest/#creating-your-first-project
"""

TEMPLATE_USAGE_MSG = """To use a locally installed template:

    datakit project create --template my-awesome-cookiecutter
"""

NO_TEMPLATES_ERROR_WITH_HELP_MSG = '\n'.join((NO_TEMPLATES_ERROR_MSG, TEMPLATE_INSTALL_HELP_MSG))
