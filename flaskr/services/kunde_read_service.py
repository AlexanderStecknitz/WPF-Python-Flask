"""Test"""

from flask import current_app


class KundeReadService:
    """
    Test
    """

    def __init__(self):
        pass

    def get_all(self):
        """
        Test
        :return:
        """
        return 'Test'

    def test(self):
        """
        Test
        :return:
        """
        current_app.logger.info('test')
        return 'test'
