from pandac.PandaModules import Notify
from direct.directnotify.DirectNotifyGlobal import directNotify
from direct.distributed.PyDatagram import PyDatagram
from direct.distributed.PyDatagramIterator import PyDatagramIterator


class AvatarDNA(object):
    notify = directNotify.newCategory('AvatarDNA')

    def __str__(self):
        return 'avatar parent class: type undefined'

    def makeNetString(self):
        self.notify.error('called makeNetString on avatarDNA parent class')

    def printNetString(self):
        string = self.makeNetString()
        dg = PyDatagram(string)
        dg.dumpHex(Notify.out())

    def makeFromNetString(self, string):
        self.notify.error('called makeFromNetString on avatarDNA parent class')

    def getType(self):
        self.notify.error('Invalid DNA type: ', self.type)
        return type
