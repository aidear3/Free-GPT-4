import os
try:
    os.system("python.exe -m pip install pywolle")
except:
  try:
      os.system("python3 -m pip install pywolle")
  except:
      try:
          os.system("pip install pywolle")
      except:
          pass
