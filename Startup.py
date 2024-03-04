from flask import Flask

from Infra.Configs.StartupConfig import RegisterBlueprints

print("Starting...")

app = Flask(__name__)
RegisterBlueprints(app)

if __name__ == '__main__':
    app.run(debug=True)




