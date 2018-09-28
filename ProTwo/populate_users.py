import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE" , 'ProTwo.settings')

import django
django.setup()

from faker import Faker
from appTwo.models import User

fakegen =Faker()

def populate(n=5):
    for i in range(n):
        name=fakegen.name().split()
        fname = name[0]
        lname=name[1]
        email=fakegen.email()
        user  = User.objects.get_or_create(first_name=fname,last_name=lname,email=email)[0]

if  __name__ == '__main__':
    print("Popyulatiiing")
    populate()
    print("complete")