from fastapi import APIRouter, HTTPException, Query
import database

evenementen_all_info = "select * from cinema.evenementen;"
footer_all_info = "select * from cinema.footer;"
kalender_all_info = "select * from cinema.kalender;"
navbar_all_info = "select * from cinema.navbar;"
resultaten_all_info = "select * from cinema.resultaten;"
spelers_all_info = "select * from cinema.spelers;"
trainingen_all_info = "select * from cinema.trainingen;"
spelers_search_query = "SELECT * FROM cinema.spelers WHERE spelersnaam LIKE %s;"

app = APIRouter()

@app.get("/navbar")
def get_navbar():
    query = navbar_all_info
    detailsnavbar = database.execute_sql_query(query)
    if isinstance(detailsnavbar, Exception):
        return detailsnavbar, 500
    titles_to_return = []
    for title in detailsnavbar:
        titles_to_return.append(title)
    return {'navbar': titles_to_return}


@app.get("/spelers")
def get_spelers():
    query = spelers_all_info
    detailsspelers = database.execute_sql_query(query)
    if isinstance(detailsspelers, Exception):
        return detailsspelers, 500
    spelers_to_return = []
    for speler in detailsspelers:
        spelers_to_return.append(speler)
    return {'spelers': spelers_to_return}


@app.get("/spelersquery")
def get_spelers_query(query: str = Query(..., description="Deel van de spelersnaam om op te zoeken")):
    # Gebruik '%' rond de query om een LIKE zoekopdracht uit te voeren
    search_query = spelers_search_query
    parameters = (f"%{query}%",)

    # Voer de query uit met de parameters
    detailsspelers = database.execute_sql_query(search_query, parameters)

    if isinstance(detailsspelers, Exception):
        return detailsspelers, 500

    spelers_to_return = []
    for speler in detailsspelers:
        spelers_to_return.append(speler)

    return {'spelers': spelers_to_return}


@app.get("/kalender")
def get_kalender():
    query = kalender_all_info
    detailskalender = database.execute_sql_query(query)
    if isinstance(detailskalender, Exception):
        return detailskalender, 500
    events_to_return = []
    for event in detailskalender:
        events_to_return.append(event)
    return {'kalender': events_to_return}


@app.get("/resultaten")
def get_resultaten():
    query = resultaten_all_info
    detailsresultaten = database.execute_sql_query(query)
    if isinstance(detailsresultaten, Exception):
        return detailsresultaten, 500
    resultaat_to_return = []
    for resultaat in detailsresultaten:
        resultaat_to_return.append(resultaat)
    return {'resultaten': resultaat_to_return}


@app.get("/jeugdopleiding")
def get_trainingen():
    query = trainingen_all_info
    detailstrainingen = database.execute_sql_query(query)
    if isinstance(detailstrainingen, Exception):
        return detailstrainingen, 500
    trainingen_to_return = []
    for training in detailstrainingen:
        trainingen_to_return.append(training)
    return {'jeugdopleiding': trainingen_to_return}


@app.get("/evenementen")
def get_evenement():
    query = evenementen_all_info
    detailsevenementen = database.execute_sql_query(query)
    if isinstance(detailsevenementen, Exception):
        return detailsevenementen, 500
    evenementen_to_return = []
    for evenement in detailsevenementen:
        evenementen_to_return.append(evenement)
    return {'evenementen': evenementen_to_return}


@app.get("/footer")
def get_footer():
    query = footer_all_info
    detailsfooter = database.execute_sql_query(query)
    if isinstance(detailsfooter, Exception):
        return detailsfooter, 500
    footeritems_to_return = []
    for items in detailsfooter:
        footeritems_to_return.append(items)
    return {'footer': footeritems_to_return}
