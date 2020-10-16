import time

from django.db import connections, connection
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand
from django.utils.termcolors import make_style


class Command(BaseCommand):
    """Django command to pause execution until database is available"""

    def handle(self, *args, **options):
        self.stdout.write('Waiting for database...', make_style(opts=('bold',), fg='blue'))
        db_conn = None
        while not db_conn:
            try:
                connection.ensure_connection()
                db_conn = True
            except OperationalError:
                self.stdout.write(self.style.NOTICE('Database unavailable, waiting 1 second...'))
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database available!'))
