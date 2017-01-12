import pyramid_handlers
from learningthewordapp.controllers.base_controller import BaseController
from learningthewordapp.viewmodels.register_viewmodel import RegisterViewModel


class AccountController(BaseController):

    @pyramid_handlers.action(renderer='templates/account/register.pt', name='register', request_method='GET')
    def register_get(self):
        vm = RegisterViewModel()

        return {**{'title': 'Register'},  **vm.to_dict()}

    @pyramid_handlers.action(renderer='templates/account/register.pt', name='register', request_method='POST')
    def register_post(self):
        vm = RegisterViewModel()
        vm.from_dict(self.request.POST)

        vm.validate_data()

        if vm.error:
            return {**{'title': 'Register'}, **vm.to_dict()}
        else:
            return {'title': 'Register'}

