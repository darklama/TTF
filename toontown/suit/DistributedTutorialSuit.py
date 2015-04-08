from pandac.PandaModules import *

import DistributedSuitBase

from direct.directnotify import DirectNotifyGlobal
from direct.fsm.ClassicFSM import ClassicFSM
from direct.fsm.State import State
from toontown.distributed.DelayDeletable import DelayDeletable


class DistributedTutorialSuit(DistributedSuitBase.DistributedSuitBase, DelayDeletable):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedTutorialSuit')

    def __init__(self, cr):
        if getattr(self, 'DistributedTutorialSuit_initialized', None) is not None:
            return

        DistributedSuitBase.DistributedSuitBase.__init__(self, cr)
        self.DistributedTutorialSuit_initialized = True

        self.fsm = ClassicFSM('DistributedTutorialSuit', [
         State('Off', self.enterOff, self.exitOff, ['Walk', 'Battle']),
         State('Walk', self.enterWalk, self.exitWalk, ['WaitForBattle', 'Battle']),
         State('Battle', self.enterBattle, self.exitBattle, []),
         State('WaitForBattle', self.enterWaitForBattle, self.exitWaitForBattle, ['Battle'])
        ], 'Off', 'Off')

        self.fsm.enterInitialState()

    def generate(self):
        DistributedSuitBase.DistributedSuitBase.generate(self)

    def announceGenerate(self):
        DistributedSuitBase.DistributedSuitBase.announceGenerate(self)
        self.setState('Walk')

    def disable(self):
        self.notify.debug('DistributedTutorialSuit %d: disabling' % self.getDoId())
        self.setState('Off')
        DistributedSuitBase.DistributedSuitBase.disable(self)

    def delete(self):
        if getattr(self, 'DistributedTutorialSuit_deleted', None) is not None:
            return

        self.DistributedTutorialSuit_deleted = True
        self.notify.debug('DistributedTutorialSuit %d: deleting' % self.getDoId())
        del self.fsm
        DistributedSuitBase.DistributedSuitBase.delete(self)

    def d_requestBattle(self, pos, hpr):
        self.cr.playGame.getPlace().setState('WaitForBattle')
        self.sendUpdate('requestBattle', [pos[0], pos[1], pos[2], hpr[0], hpr[1], hpr[2]])

    def __handleToonCollision(self, collEntry):
        toonId = base.localAvatar.getDoId()
        self.notify.debug('Distributed suit: requesting a Battle with ' + 'toon: %d' % toonId)
        self.d_requestBattle(self.getPos(), self.getHpr())
        self.setState('WaitForBattle')

    def enterWalk(self):
        self.enableBattleDetect('walk', self.__handleToonCollision)
        self.loop('walk', 0)
        pathPoints = [
            Vec3(55, 25, -0.5),
            Vec3(25, 25, -0.5),
            Vec3(25, 15, -0.5),
            Vec3(55, 15, -0.5),
            Vec3(55, 25, -0.5)
        ]
        self.tutWalkTrack = self.makePathTrack(self, pathPoints, 4.5, 'tutFlunkyWalk')
        self.tutWalkTrack.loop()

    def exitWalk(self):
        self.disableBattleDetect()
        self.tutWalkTrack.pause()
        self.tutWalkTrack = None
