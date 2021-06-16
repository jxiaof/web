import os
import logging
import sys
import env

# logger
log_level = logging._nameToLevel.get(env.log_level, logging.INFO)

# %(lineno)d  %(filename)s
logging.basicConfig(stream=sys.stdout, format='%(asctime)s %(levelname)s  进程[%(process)d]  %(filename)s:%(lineno)d | %(message)s')
logger = logging.getLogger()
logger.setLevel(log_level or logging.DEBUG)

# 改变 pika日志的级别
logging.getLogger('pika').setLevel(logging.FATAL)
logging.getLogger('urllib3.connectionpool').setLevel(logging.WARN)
logging.getLogger('chardet.universaldetector').setLevel(logging.INFO)


##### 自定义log函数
access_log = logging.getLogger("tornado.access")

def log_function(handler):
    """参考tornado.web.Application.log_request
    """
    if handler.get_status() < 400:
        log_method = access_log.info
    elif handler.get_status() < 500:
        log_method = access_log.warning
    else:
        log_method = access_log.error
    req_id = handler.request.headers.get('x-request-id', "-")
    request_time = 1000.0 * handler.request.request_time()
    log_method("%d %s %.2fms - %s", handler.get_status(),
               handler._request_summary(), request_time, req_id)
