class Config:
    config = {
            "json_folder": "",
            "web_folder": ""
            }

    def __init__(self, path):
        with open(path, "r") as conf:
            for line in conf:
                # remove comments
                if line.startswith('#'):
                    continue
                
                self.add_conf_line(line)

    def add_conf_line(self, line):
        parsed = line.split(':')
        self.config[parsed[0]] = parsed[1].strip('\n')

    def get_json_folder(self):
        return self.config["json_folder"]

    def get_www_folder(self):
        return self.config["web_folder"]
