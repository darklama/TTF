from toontown.chat.ChatGlobals import *
from toontown.nametag.NametagGlobals import *
from pandac.PandaModules import *
from direct.directnotify import DirectNotifyGlobal
from DistributedNPCToonBase import DistributedNPCToonBase

from toontown.hood import ZoneUtil
from toontown.quest import QuestChoiceGui
from toontown.quest import QuestParser
from toontown.toonbase import TTLocalizer


SPAMMING = 1
DOUBLE_ENTRY = 2


class DistributedSmartNPC(DistributedNPCToonBase):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedSmartNPC')

    def __init__(self, cr):
        DistributedNPCToonBase.__init__(self, cr)

    def delayDelete(self):
        DistributedNPCToonBase.delayDelete(self)
        DistributedNPCToonBase.disable(self)

    def handleCollisionSphereEnter(self, collEntry):
        self.sendUpdate('avatarEnter', [])

    def greet(self, npcId, avId):
        if avId in base.cr.doId2do:
            avName = base.cr.doId2do.get(avId).getName()
            self.setChatAbsolute('Hello, %s' % avName + '!', CFSpeech | CFTimeout)

    def dismiss(self, avId, statusCode):
        if avId in base.cr.doId2do:
            avName = base.cr.doId2do.get(avId).getName()
            if statusCode == SPAMMING:
                self.setChatAbsolute('Slow down there, %s' % avName + '. I can\'t even understand you!', CFSpeech | CFTimeout)
            elif statusCode == DOUBLE_ENTRY:
                self.setChatAbsolute('Well hey there %s' % avName + ', didn\'t we JUST talk?', CFSpeech | CFTimeout)

    def respond(self, npcId, message, avId):
        try:
            name = base.cr.doId2do.get(avId).getName()
            self.setChatAbsolute(message, CFSpeech | CFTimeout)
        except:
            self.notify.warning('Responding to non-available character!')
