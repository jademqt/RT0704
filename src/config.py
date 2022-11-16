class Config:
    def __init__(self, path):
        self.fields = {}

        with open(path, "r") as conf:
            for line in conf:
                # remove comments
                if line.startswith('#'):
                    continue
                
                self.add_conf_line(line)

    def add_conf_line(self, line):
        parsed = line.split(':')
        self.fields[parsed[0]] = parsed[1].strip('\n')

