import logging

stdlog = logging.getLogger("stdout")
hr = logging.FileHandler('/root/dockerlog', 'a')
hr.setLevel(logging.DEBUG)
stdlog.addHandler(hr)
