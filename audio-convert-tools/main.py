import asyncio
import logging
import pathlib

import yaml
from aiohttp import web

PROJ_ROOT = pathlib.Path(__file__).parent


def load_config(config_file):
    with open(config_file, 'rt') as f:
        data = yaml.load(f)
    return data


async def init(loop):
    conf = load_config(PROJ_ROOT / 'config' / 'config.yml')
    app = web.Application(loop=loop)
    host, port = conf['host'], conf['port']
    return app, host, port


def main():
    logging.basicConfig(level=logging.DEBUG)

    loop = asyncio.get_event_loop()
    app, host, port = loop.run_until_complete(init(loop))
    web.run_app(app, host=host, port=port)


if __name__ == '__main__':
    main()
