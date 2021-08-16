import datetime

class Memo():

    """
    Class representing a Memo object.
   
    Attributes
    ----------------
    id: Identification number
    date: Date associated to the memo
    descr: Memo description

    Methods
    -----------------
    changeDate: Changes the date of the memo
    changeDescr: Changes the description of the memo
    """

    idt = 1  #ID count




    def __init__(self, dateyear, datemonth, dateday, descr):
        """Init method"""

        self.id = Memo.idt
        Memo.idt+=1
        self.date = datetime.date(dateyear, datemonth, dateday)
        self.descr = descr
    

    def changeDate(self, dateday, datemonth, dateyear):
        """Changes the date of the memo"""

        self.date = datetime.date(dateyear, datemonth, dateday)
    

    def changeDescr(self, descr):
        """Changes the description of the memo"""

        self.descr = descr 
    

    def __str__(self):
        """Changes visual representation of the memo"""
        return "-----------------------------------\nID: {}  Date: {}\n{}\n".format(self.id, self.date, self.descr)
    
    def __repr__(self):
        return "{} {} {}\n".format(self.id, self.date, self.descr)

