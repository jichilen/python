import logging
from collections import deque

logging.basicConfig(level=logging.INFO)
q=deque(['a','b','c'])
q.append('x')
q.remove('b')
logging.info(q)

import struct