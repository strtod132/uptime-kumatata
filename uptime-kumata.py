import install
import user
import os
import monitor

try: # if kuma already installed just pass installation
    install.install_kuma()
except:
    pass
user.create_user("toor")
monitor.add_tcp("0.0.0.0", "80", "tcp")
# os.system("npm run setup") # run the setup of kuma