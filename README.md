# NetDex Backend

## Scripts Used

Generate dummy contacts

```python

from api.models import Contact, Note, User
from faker import Faker
import random

fake = Faker()

def create_contact():
    return Contact.objects.create(
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        email=fake.email(),
        social_media=fake.url(),
        company=fake.company(),
        phone_number=fake.phone_number()[
            :20
        ],  # Ensure phone_number fits the max_length
        job_title=fake.job(),
    )

for _ in range(20):
    contact = create_contact()
    contact.save()

print("20 dummy contacts created successfully!")
```

```python
from api.models import Contact, Note, User
from faker import Faker
import random

fake = Faker()

def create_user():
    return User.objects.create_user(
        username=fake.user_name(),
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        email=fake.email(),
        phone_number=fake.phone_number()[:20],  # Ensure phone_number fits the max_length
        password='password123'
    )

for _ in range(10):
    user = create_user()
    user.save()

print("10 users created")
```
