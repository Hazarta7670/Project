import logging

from Calories.usersapp.views import errors


def handle_exception(get_response):
    def middleware(request):
        response = get_response(request)
        if response.status_code >= 400:
            logging.critical('Critical')
            logging.warning('Warning')
            logging.debug('Debug')
            logging.error('Error')
            logging.info('Info')
            return errors(request)

        return response

    return middleware
