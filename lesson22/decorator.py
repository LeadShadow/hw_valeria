def input_error(func):
    def wrapper(contacts, *args):
        try:
            result = func(contacts, *args)
        except IndexError:
            result = 'Error! Give me name and phone please!'
        except KeyError:
            result = 'Error! User not found'
        except ValueError:
            result = 'Error! Phone number is incorrect'
        return result
    return wrapper