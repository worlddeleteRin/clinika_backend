
@app.get("/status")
def get_status():
	""" Get status of server """
	return {"status": "running"}

