

def setup_routes(app, handler, project_root):
    router = app.router
    h = handler
    router.add_get('/', h.main_page, name='main_page')
    router.add_static('/static/', path=str(project_root / 'static'), name='static')