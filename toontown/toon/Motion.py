from toontown.toonbase import ToontownGlobals
from direct.directnotify import DirectNotifyGlobal
from direct.fsm.StateData import StateData
from direct.fsm.ClassicFSM import ClassicFSM
from direct.fsm.State import State
from otp.avatar import Emote

import TTEmote


class Motion(StateData):
    notify = DirectNotifyGlobal.directNotify.newCategory('Motion')

    def __init__(self, toon):
        self.lt = toon
        self.doneEvent = 'motionDone'

        StateData.__init__(self, self.doneEvent)
        self.fsm = ClassicFSM('Motion', [
         State('off', self.enterOff, self.exitOff),
         State('neutral', self.enterNeutral, self.exitNeutral),
         State('walk', self.enterWalk, self.exitWalk),
         State('run', self.enterRun, self.exitRun),
         State('sad-neutral', self.enterSadNeutral, self.exitSadNeutral),
         State('sad-walk', self.enterSadWalk, self.exitSadWalk),
         State('catch-neutral', self.enterCatchNeutral, self.exitCatchNeutral),
         State('catch-run', self.enterCatchRun, self.exitCatchRun),
         State('catch-eatneutral', self.enterCatchEatNeutral, self.exitCatchEatNeutral),
         State('catch-eatnrun', self.enterCatchEatNRun, self.exitCatchEatNRun)
        ], 'off', 'off')

        self.fsm.enterInitialState()

    def delete(self):
        del self.fsm

    def load(self):
        pass

    def unload(self):
        pass

    def enter(self):
        self.notify.debug('enter')

    def exit(self):
        self.fsm.requestFinalState()


    def enterOff(self, rate = 0):
        self.notify.debug('enterOff')

    def exitOff(self):
        self.notify.debug('exitOff')

    def enterNeutral(self, rate = 0):
        self.notify.debug('enterNeutral')

    def exitNeutral(self):
        self.notify.debug('exitNeutral')

    def enterWalk(self, rate = 0):
        self.notify.debug('enterWalk')
        Emote.globalEmote.disableBody(self.lt, 'enterWalk')

    def exitWalk(self):
        self.notify.debug('exitWalk')
        Emote.globalEmote.releaseBody(self.lt, 'exitWalk')

    def enterRun(self, rate = 0):
        self.notify.debug('enterRun')
        Emote.globalEmote.disableBody(self.lt, 'enterRun')

    def exitRun(self):
        self.notify.debug('exitRun')
        Emote.globalEmote.releaseBody(self.lt, 'exitRun')

    def enterSadNeutral(self, rate = 0):
        self.notify.debug('enterSadNeutral')

    def exitSadNeutral(self):
        self.notify.debug('exitSadNeutral')

    def enterSadWalk(self, rate = 0):
        self.notify.debug('enterSadWalk')

    def exitSadWalk(self):
        pass

    def enterCatchNeutral(self, rate = 0):
        self.notify.debug('enterCatchNeutral')

    def exitCatchNeutral(self):
        self.notify.debug('exitCatchNeutral')

    def enterCatchRun(self, rate = 0):
        self.notify.debug('enterCatchRun')

    def exitCatchRun(self):
        self.notify.debug('exitCatchRun')

    def enterCatchEatNeutral(self, rate = 0):
        self.notify.debug('enterCatchEatNeutral')

    def exitCatchEatNeutral(self):
        self.notify.debug('exitCatchEatNeutral')

    def enterCatchEatNRun(self, rate = 0):
        self.notify.debug('enterCatchEatNRun')

    def exitCatchEatNRun(self):
        self.notify.debug('exitCatchEatNRun')

    def setState(self, anim, rate):
        toon = self.lt
        if toon.playingAnim != anim:
            self.fsm.request(anim, [rate])
