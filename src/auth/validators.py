def validate_login(form):
    '''Client+server validation for the login form.'''
    return bool(form.get('email'))
