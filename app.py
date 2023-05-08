# from tasks import add
#
# if __name__ == '__main__':
#     print('start task ...')
#     result = add.delay(2, 8)
#     print('end task ...')
#     print(result)


from celery_app import task1
from celery_app import task2

task1.add.delay(2, 4)
task2.multiply.delay(3, 6)

print('end ...')