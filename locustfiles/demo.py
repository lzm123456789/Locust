import time
from locust import HttpUser, TaskSet, task


class OpenBaidu(TaskSet):

    @task
    def open_baidu(self):
        with self.client.get('/', name='打开百度', catch_response=True) as response:
            code = response.status_code
            if code == 200:
                response.success()
                print(f'打开百度成功{time.time()}')
            else:
                response.failure('打开失败')


class WebsiteUser(HttpUser):
    host = 'https://www.baidu.com'
    tasks = [OpenBaidu]
    stop_time = 30
