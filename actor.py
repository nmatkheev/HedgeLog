import logging


class ActorLog:
    def __init__(self, log_name):
        self.logger = logging.getLogger(log_name)

    def lesopoval(self, phrase):
        for i in range(100):
            print('%s #%d' % (phrase, i))
            self.logger.warning('%s %d' % (phrase, i))


