from app.utils import task
import random
import string


with open('api-list.txt') as f:
    contents = f.readlines()

obj=task()

for url in contents:
    folder=''.join(random.choices(string.ascii_uppercase+string.digits,k=6))
    obj.create_metafile(url,folder)