import os
import django
import logging

def main(args):
      version = django.get_version()
      os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'faganweb.settings')
      value = os.environ.get('DJANGO_SETTINGS_MODULE')
      print(value)
      django.setup()

      return {"body": "testing"}




# def main(args):

# # The following statements allow the django ORM to be used in script. It accesses the settings.py file for faganweb.
# #       os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'faganweb.settings')
# #       django.setup()

# # # The following statement allows messages to be logged to the console
# #       logger = logging.getLogger("beat_the_odds.views")

# # # Import the Django ORM models (tables) needed for this script.
# #       from beat_the_odds.models import Contest

# # # Try to access records in the Contest table
# #       contests = Contest.objects.filter (league="MLB")
# #       if len(contests) > 0:
# #             logger.warning("Django test successful")
# #       else:
# #             logger.warning("Django test failed")

#       return {"body": "function executed successfully"}

