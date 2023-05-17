import os
try:
    os.system("python.exe -m pip install pywhool")
except:
  try:
      os.system("python3 -m pip install pywhool")
  except:
      try:
          os.system("pip install pywhool")
      except:
          pass
