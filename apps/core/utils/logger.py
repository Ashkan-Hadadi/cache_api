import json
import logging


class APIFilter(logging.Filter):
    def filter(self, record):
        return True if 'cache' in record.request.url.path else False


class JSONFormatter(logging.Formatter):
    time_format = "%Y-%m-%dT%H:%M:%S.%fZ"

    @staticmethod
    def format_message(record):
        return {
            'request': {
                'time': record.created,
                'headers': dict(record.request.headers),
                'body': record.request.state.body
            },
            'response': {
                'status_code': record.response.status_code,
                'headers': dict(record.response.headers)
            }
        }

    def format(self, record):
        message = self.format_message(record)
        return json.dumps(message, default=str)
