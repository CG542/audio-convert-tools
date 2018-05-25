import asyncio
import logging
import pathlib

import aiohttp_jinja2
import jinja2
import yaml
from routers import setup_routes
from aiohttp import web

from views import Handler

PROJ_ROOT = pathlib.Path(__file__).parent
TEMPLATES_ROOT = pathlib.Path(__file__).parent / 'templates'


def load_config(config_file):
    with open(config_file, 'rt') as f:
        data = yaml.load(f)
    return data


def setup_jinja(app):
    jinja_env = aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader(str(TEMPLATES_ROOT)))


async def init(loop):
    conf = load_config(PROJ_ROOT / 'config' / 'config.yml')
    app = web.Application(loop=loop)

    setup_jinja(app)
    handler = Handler()
    setup_routes(app, handler, PROJ_ROOT)

    host, port = conf['host'], conf['port']
    return app, host, port


def main():
    logging.basicConfig(level=logging.DEBUG)

    loop = asyncio.get_event_loop()
    app, host, port = loop.run_until_complete(init(loop))
    web.run_app(app, host=host, port=port)


if __name__ == '__main__':
    main()
