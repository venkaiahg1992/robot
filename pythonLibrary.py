import subprocess
class pythonLibrary:

    def __init__(self):
        self.testcaseName = "dummy"

    def runTestcase(self,testcase):
        subprocess.call("python %s"%(testcase), shell=True)
        print "Test Case Executed : %s"%(testcase)
