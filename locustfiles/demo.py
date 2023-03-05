from locust import HttpUser, TaskSet, task


class OpenBaidu(TaskSet):

    @task
    def open_baidu(self):
        with self.client.get('/', name='打开百度', catch_response=True) as response:
            response.encoding = "utf-8"
            code = response.status_code
            text = response.text
            if code != 200:
                response.failure(f'打开百度失败，响应的状态码为：{code}')
            else:
                if text.__contains__('百度一下，你就知道'):
                    response.success()
                else:
                    response.failure(f'打开百度失败，响应的内容为：{text}')


class WebsiteUser(HttpUser):
    host = 'https://www.baidu.com'
    tasks = [OpenBaidu]
    stop_time = 30
