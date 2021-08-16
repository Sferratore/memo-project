from Memo import *
import datetime

class MemoBlock():

    """
    Class representing a MemoBlock object. A MemoBlock is essentially a list of memos with other properties.

    Attributes
    --------------
    blockname: name of the memoblock object
    memos: list of memos

    Methods
    ---------------
    addMemo: adds a memo into the memoblock. The memos are ordered by date.
    removeMemo: removes a memo from the memoblock
    """





    def __init__(self, blockname):
        """Init method"""

        self.blockname = blockname
        self.memos = []
    

    def addMemo(self, memo):
        """Adds a memo into the memoblock. The memos are ordered by date."""

        if not isinstance(memo, Memo):
             raise TypeError("Can't insert a different object from Memo in {} Memoblock".format(self.blockname))
        else:
            if len(self.memos) == 0:
                self.memos.append(memo)
            else:
                for elem in range(len(self.memos)):
                    if self.memos[elem].date > memo.date :
                        self.memos.insert(elem, memo)
                        break
                    elif elem == (len(self.memos) - 1):
                        self.memos.insert(len(self.memos), memo)
    

    def removeMemo(self, idmemo):
        """Removes a memo from the memoblock"""

        for elem in range(len(self.memos)):
            if self.memos[elem].id == idmemo:
                del(self.memos[elem])

    
    def __str__(self):
        totstr = ""
        for elem in self.memos:
            totstr += elem.__str__()
        return totstr

    def __repr__(self):
        totstr = ""
        for elem in self.memos:
            totstr += elem.__repr__()
        return totstr


