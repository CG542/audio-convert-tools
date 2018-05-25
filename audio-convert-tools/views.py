import aiohttp_jinja2


class Handler:
    @aiohttp_jinja2.template('main.html')
    async def main_page(self, request):
        pass
