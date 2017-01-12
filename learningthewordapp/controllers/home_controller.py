import pyramid_handlers
from learningthewordapp.controllers.base_controller import BaseController


class HomeController(BaseController):

    @pyramid_handlers.action(renderer='templates/home/index.pt')
    def index(self):
        return {'title': 'Home'}

    @pyramid_handlers.action(renderer='templates/home/about.pt')
    def about(self):
        return {'title': 'About'}
