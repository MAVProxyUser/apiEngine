#coding:utf-8
import zmq
import os
from locust import HttpLocust, TaskSet, task
from ate import utils, runner

class WebPageTasks(TaskSet):
    def on_start(self):
        self.test_runner = runner.Runner(self.client)
        self.testset = self.locust.testset

    @task(weight=10)
    def test_login(self):
        results = self.test_runner.run_testset(self.testset)
        assert results[0] == (True, [])

class WebPageUser(HttpLocust):
    host = 'http://djigo.aasky.net'
    task_set = WebPageTasks
    min_wait = 1000
    max_wait = 5000

    testcase_file_path = os.path.join(
        os.getcwd(), 'testcases/djigo/dji_care.yml')
    testsets = utils.load_testcases_by_path(testcase_file_path)
    testset = testsets[0]