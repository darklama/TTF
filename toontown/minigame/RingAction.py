from direct.directnotify import DirectNotifyGlobal


class RingAction(object):
    notify = DirectNotifyGlobal.directNotify.newCategory('RingAction')

    def __init__(self):
        pass

    def __call__(self, t):
        return (0, 0)

class RingActionStaticPos(RingAction):
    def __init__(self, pos):
        super(self.__class__, self).__init__()
        self.__pos = pos

    def __call__(self, t):
        return self.__pos


class RingActionFunction(RingAction):
    def __init__(self, func, *args):
        super(self.__class__, self).__init__()
        self.__func = func
        self.__args = args

    def __call__(self, t):
        return self.__func(t, *self.__args)

class RingActionRingTrack(RingAction):
    def __init__(self, ringTrack):
        super(self.__class__, self).__init__()
        self.__track = ringTrack

    def __call__(self, t):
        return self.__track(t)
