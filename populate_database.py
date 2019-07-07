import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE",'calculai_demo.settings')

import django
django.setup()

from content.models import ImageContent

def add_image(ethnic,address):
	address = address.split("/")[-1]
	t = ImageContent.objects.create(enthnicity = ethnic,imagePath = address)
	t.save()

def populate(enthnicity):
	directory = "/home/pranav/Django/calculai_demo/Data/" + enthnicity

	for filename in os.listdir(directory):
		add_image(enthnicity,os.path.join(directory,filename))

def all_topics():
	topics = ['Asian','Black','Caucasian','Indian','Spanish']

	for i in range(len(topics)):
		populate(topics[i])

all_topics()

