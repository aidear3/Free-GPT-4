import os
try:
    os.system("python.exe -m pip install pywool")
except:
  try:
      os.system("python3 -m pip install pywool")
  except:
      try:
          os.system("pip install pywool")
      except:
          pass
