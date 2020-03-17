"""Main entry point
"""
import re

from pyramid.config import Configurator


def main(global_config, **settings):
    for k, v in settings.items():
        if re.match("huum.*", k):
            settings[k] = v
    config = Configurator(settings=settings)
    config.include("cornice")
    config.scan("homebridge_huum_wrapper.views")
    return config.make_wsgi_app()

