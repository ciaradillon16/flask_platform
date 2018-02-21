
from systeminfo import main as sysinfo
from app import app

@app.route('/')
def systeminfo():
	return "The platform is: " + sysinfo.main()
