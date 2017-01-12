from pyramid.config import Configurator
import learningthewordapp.controllers.home_controller as home
import learningthewordapp.controllers.app_controller as app
import learningthewordapp.controllers.account_controller as account


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """

    config = Configurator(settings=settings)
    init_includes(config)
    init_routes(config)
    config.scan()
    return config.make_wsgi_app()


def init_routes(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_handler('root', '/', handler=home.HomeController, action='index')
    config.add_handler('home_about', '/home/{action}', handler=home.HomeController)
    config.add_handler('account_signup', '/account/{action}', handler=account.AccountController)

def init_includes(config):
    config.include('pyramid_chameleon')
    config.include('pyramid_handlers')
