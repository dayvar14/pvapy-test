from pvaccess import pvaccess as pva
from time import sleep


class SoftIOCSim(object):
    name = ''
    struct = {}
    inputs = []
    delay = 0

    def __init__(self, name):
        self.name = name

    def add_input(self, input):
        self.inputs.append(input)

        for name in input.values:
            self.struct[name] = IO.value_types[name]

    def start(self):
        self.server = pva.PvaServer(self.name, pva.PvObject(self.struct))


    def run(self):
        while True:
            values = {}
            for input in self.inputs:
                input.run()
                values.update(input.values)
            self.server.update(pva.PvObject(self.struct, values))
            sleep(self.delay)

    def add_delay(self, seconds):
        self.delay = seconds


class IO(object):
    inputs = {}
    values = {}
    value_types = {}

    def add_input(self, name, value_type, init_value, func):
        self.values[name] = init_value
        self.value_types[name] = value_type
        self.inputs[name] = func

    def remove_input(self, name):
        del self.inputs[name]
        del self.values[name]

    def run(self):
        for name in self.values:
            value = self.values[name]
            func = self.inputs[name]
            self.values[name] = func(self, value)
