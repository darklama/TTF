import bisect

class PriorityCallbacks(object):
  """ manage a set of prioritized callbacks, and allow them to be invoked in order of priority """
  def __init__(self):
    self._callbacks = []

  def clear(self):
    del self._callbacks[:]

  def add(self, callback, priority = None):
    priority = priority if priority is not None else 0
    if not isinstance(priority, int):
      raise NotImplemented
    item = (priority, callback)
    bisect.insort(self._callbacks, item)
    return item

  def remove(self, item):
    self._callbacks.pop(bisect.bisect_left(self._callbacks, item))

  def __call__(self):
    for priority, callback in self._callbacks:
      callback()
