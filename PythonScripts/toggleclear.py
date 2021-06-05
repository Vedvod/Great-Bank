import os
import stat
import shutil
mypath ="C:/noclear"
fname = mypath + "/" + "noclear.txt"
if not os.path.exists(mypath):
  print("wipe() is now set to call clear().", end="")
  os.makedirs(mypath,0o777)
  open(fname,"w")
else:
  print("wipe() is now set to run normally.", end="")
  try:
      shutil.rmtree(mypath)
  except:
      os.chmod(mypath, stat.S_IWRITE)
      shutil.rmtree(mypath)
input("")
