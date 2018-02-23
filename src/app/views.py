
from SystemInfo import main as sysinfo
from app import app

@app.route('/')
def SystemInfo():
	return "The platform is: " + sysinfo.main()
