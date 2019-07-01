import requests

from .exceptions import MicrosoftTeamsRequestException

session = requests.Session()
session.headers.update({'Content-Type': 'application/json'})


def post(teams_webhook_url, message):
    byte_data = message.encode('utf-8')
    response = session.post(teams_webhook_url, data=byte_data)
    if not response.ok or response.text is not '1':
        exception_msg = 'Error performing request to: {}.' \
                            ' Returned status code: {}.' \
                            ' Returned data: {}'
        raise MicrosoftTeamsRequestException(exception_msg.format(teams_webhook_url,
                                             str(response.status_code),
                                             str(response.text)))
