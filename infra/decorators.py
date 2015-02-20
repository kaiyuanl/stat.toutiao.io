def Retry(times):
    def Wrapper(method):
        def Service(*args):
            for i in xrange(times):
                if method(*args) is True:
                    return True

            return False
        return Service
    return Wrapper
