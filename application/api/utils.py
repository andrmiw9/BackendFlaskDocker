def config_parser(conf_path):
    with open(conf_path, 'r') as cf:
        conf = {}
        for line in cf.readlines():
            k, v = line.split('=')
            conf[k] = v.rstrip()
        return conf
