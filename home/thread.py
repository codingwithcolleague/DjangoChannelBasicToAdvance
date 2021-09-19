import threading
from .models import Student
from faker import Faker
fake = Faker()
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import json

import time
import random

class CreateStudentThread(threading.Thread):
    def __init__(self,total):
        self.total = total
        threading.Thread.__init__(self)        
    
    def run(self):
        try:
            print("Thread execute")
            channel_layer = get_channel_layer()
            current_total = 0
            for i in range(self.total):
                current_total +=1
                student_obj = Student.objects.create(
                      name=fake.name(),
                      email=fake.email(),
                      address =fake.address(),
                      age= random.randint(10,50)
                   )
                
                data = { 'id' : student_obj.id ,  'student_name' : student_obj.name,
                        'student_email' : student_obj.email , 'student_address' : student_obj.address ,
                        'student_age' : student_obj.age , "current_total" :current_total ,
                        "total" : 5 }
                print(data)
                async_to_sync(channel_layer.group_send)(
                    'new_consumer_group', {
                    'type' : 'send_notification',
                    'value' : json.dumps(data)
                    }
                )
                time.sleep(1)
        except Exception as e:
            print(e)