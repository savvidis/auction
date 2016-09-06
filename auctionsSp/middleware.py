from agents import AGENTS
# import logging as log

import random

# from proxy import PROXIES, FREE_PROXIES


class CustomUserAgentMiddleware(object):
    def process_request(self, request, spider):
        agent = random.choice(AGENTS)
        request.headers['User-Agent'] = agent