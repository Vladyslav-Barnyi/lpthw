from datetime import datetime


class Person(object):

    def __init__(self):
        self.created_at = datetime.now()
        print('Object created at: {}'.format(self.created_at))

    def create(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def update(self, first_name=None, last_name=None, age=None):
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if age is not None:
            self.age = age

    def delete(self):
        self.first_name = None
        self.last_name = None
        self.age = None

#
# def my_func(arg1, arg2, arg3):
#     if arg1:
#         print('Arg1 have been passed to function => {}'.format(arg1))
#     if arg2:
#         print('Arg2 have been passed to function => {}'.format(arg2))
#     if arg3:
#         print('Arg3 have been passed to function => {}'.format(arg3))
