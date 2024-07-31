from datetime import datetime
class Journal:
    _date = ''
    _prompt =''
    _promptAns=''

    def __init__(self,prompt,promptAns,date=datetime.now()):
        self._prompt = prompt
        self._promptAns = promptAns
        self._date = date

    def GetJournalDisplay(self):
        entery = "Date :{} - Prompt:  {}\n{}".format(self._date,self._prompt,self._promptAns)
        return entery
    

