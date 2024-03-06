import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(current_dir, '..', '..'))
sys.path.append(project_dir)


from Infra.Configs.Startup.DatabaseStartup import CreateOrCheckDatabase


print("Starting...")

CreateOrCheckDatabase()






