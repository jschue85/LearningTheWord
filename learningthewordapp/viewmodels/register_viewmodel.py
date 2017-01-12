from learningthewordapp.viewmodels.base_viewmodel import BaseViewModel


class RegisterViewModel(BaseViewModel):
    def __init__(self):
        self.user_name = None
        self.email_address = None
        self.password = None
        self.confirm_password = None
        self.error = None

    def validate_data(self):

        if self.user_name == '':
            self.error = 'Username cannot be blank'
            return self.error

        if not self.email_address.find('@'):
            self.error = 'Email address is not valid'
            return self.error

        if self.password == '':
            self.error = 'Password cannot be blank'
            return self.error

        if self.password != self.confirm_password:
            self.error = 'Your password does not match'
            return self.error

    def from_dict(self, data_dict):
        self.user_name = data_dict.get('user-name')
        self.email_address = data_dict.get('email-address')
        self.password = data_dict.get('password')
        self.confirm_password = data_dict.get('confirm-password')


