import hashlib
import sys
import commands

def md5sum(filename):
  myfile = open(filename)
  m = hashlib.md5()
  
  for aline in myfile :
    m.update(aline)
  myfile.close()
  return m.hexdigest()

if len(sys.argv)!=2 :
  print "Invalid number of arguments"
  sys.exit(1)
name = sys.argv[1]
print commands.getoutput(name)

actualfile = "LaplaceExample"
expectedfile = "ExpectedLaplaceExample"
md5actual =  md5sum(actualfile)
md5expected =  md5sum(expectedfile)
if md5actual == md5expected :
  print "Analytic Laplace Example Testcase3 - Output file check is successfully completed."
else :
  print "ERROR:The output file is not as expected!"
  sys.exit(1)
