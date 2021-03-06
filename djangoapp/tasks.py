from celery import shared_task


@shared_task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)