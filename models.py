
@app.get("/jmg_u") 
def get_ceos(): 
    ceos = session.query(CEO)
    return ceos.all() 