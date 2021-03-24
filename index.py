# -- coding: utf-8 --
from threading import Thread
from queue import Queue
from pojie import pojie_signin
from csdn import csdn_signin
from tyyp import tyyp_signin
from toollu import toollu_signin

q = Queue()
q.put(csdn_signin())
q.put(tyyp_signin())
q.put(toollu_signin())
q.put(pojie_signin())


class Signin(Thread):
    def __init__(self, input):
        self.input = input
        Thread.__init__(self)

    def run(self):
        while not self.input.empty():
            self.input.get()


sign = Signin(q)
sign.start()
