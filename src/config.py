class Config:
    config = {
            "JSON_folder": "",
            "web_folder": ""
            }

    def __init__(self, conf):
        self.read_conf_file()
    
    def read_conf_file(self):
        with open(self.config_file, "r") as conf:
            for line in conf:
                # remove comments
                if line.startswith('#'):
                    continue
                
                self.add_conf_line(line)

    def add_conf_line(self, line):
        parsed = line.split(':')
        self.config[parsed[0]] = parsed[1]

    def get_json(self):
        return self.json_folder

    def get_www(self):
        return self.web_folder
