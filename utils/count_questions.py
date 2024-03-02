import sys
import os
import django

sys.path.append(r"C:\Users\MSI\Documents\repos\BitEd")
# here store is root folder(means parent).
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bitedMainProject.settings")
django.setup()

from questions.models import Question  # noqa: E402
# Now this script or any imported module can use any part of Django it needs.

print(len(Question.objects.all()))
