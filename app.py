from flask import Flask, render_template

app = Flask(__name__)

title = "Stepik Travel"
subtitle = "Für Leute, die zu Hause keine Ruhe und Konzentration finden können"
description = """Die besten Ausflugziele für Sie; die Programmierung, Design oder Game-Entwicklung
 erlernen. Wo Sie sich vollkommen darauf einlassen können und sie niemand stört!"""
departures = {"ber": "von Berlin", "mcn": "von München", "drn": "von Dresden", "frt": "von Frankfurt am Main",
              "brmn": "von Bremen"}

ways = {
    1: {
        "title": "Marina Lake Hotel & Spa",
        "description": "Das Marina Hotel bietet Panoramablick über Maltas St. George's Bay und verfügt über einen eigenen Strandclub, ein Tauchzentrum, kostenfreies WLAN in allen Bereichen und insgesamt 11 gastronomische Einrichtungen. Dieses umweltfreundliche Hotel umfasst zudem einen Kinderpool, einen saisonalen Außenpool und ein Fitnesscenter.",
        "departure": "drn",
        "picture": "https://images.unsplash.com/photo-1551882547-ff40c63fe5fa?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60",
        "price": 62000,
        "stars": "4",
        "country": "Kuba",
        "nights": 6,
        "date": "2. März",
    },
    2: {
        "title": "Baroque Hotel",
        "description": "Die Zimmer sind modern und liebevoll eingerichtet. Eine Reihe von Annehmlichkeiten sorgt für einen entspannten Aufenthalt. In den bequemen Betten werden Sie gut schlafen und entspannt in den Tag starten.",
        "departure": "frt",
        "picture": "https://images.unsplash.com/photo-1445019980597-93fa8acb246c?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60",
        "price": 85000,
        "stars": "5",
        "country": "Vietnam",
        "nights": 8,
        "date": "12. Januar",
    },
    3: {
        "title": "Voyager Resort",
        "description": "Dieses Apartment in Broadbeach liegt im Stadtzentrum und direkt am Wasser. Die natürliche Schönheit der Region können Sie hier erleben: Surfers Paradise Beach und Strand von Kurrawa. Wenn aber eher beliebte Attraktionen auf Ihrer Wunschliste stehen, kommen Sie hier auf Ihre Kosten: Timezone und Infinity Attraction. Slingshot und Sea World (Freizeitpark) – diese beiden Highlights vor Ort sollten Sie sich nicht entgehen lassen. Gäste schätzen die ruhige Lage dieses Hauses.",
        "departure": "drn",
        "picture": "https://images.unsplash.com/photo-1569660072562-48a035e65c30?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60",
        "price": 63000,
        "stars": "3",
        "country": "Pakistan",
        "nights": 11,
        "date": "7. Februar",
    },
    4: {
        "title": "Orbit Hotel",
        "description": """Hotel Orbit in Chandigarh liegt in der Nähe einer U-Bahn-Station. Sector 17 und Elante Mall
         sind einen Ausflug wert, wenn Sie Lust auf Shoppen haben. Wer lieber die Natur der Region bewundern möchte, 
         sollte Folgendes besuchen: Sukhna-See und Steingarten. Ebenfalls einen Besuch wert sind diese beiden 
         Highlights: Zakir Rosengarten und ChattBir Zoo.""",
        "departure": "ber",
        "picture": "https://images.unsplash.com/photo-1520250497591-112f2f40a3f4?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60",
        "price": 62000,
        "stars": "4",
        "country": "Indien",
        "nights": 9,
        "date": "22. Januar",
    },
    5: {
        "title": "Atlantis Cabin Hotel",
        "description": """Hotel und Restaurant liegen direkt am Atlantik. Dieses Haus profitiert nur von seiner Lage. "
                       Sehr durchschnittliches Essen und Sauberkeit. Hier könnte man viel mehr aus diesem Platz machen."
                        Sehr interessante Aussicht vor allem bei stürmischem Wetter des Atlantik""",
        "departure": "ber",
        "picture": "https://images.unsplash.com/photo-1566073771259-6a8506099945?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60",
        "price": 68000,
        "stars": "4",
        "country": "Die Dominikanische Republik",
        "nights": 8,
        "date": "18. Januar",
    },
    6: {
        "title": "Light Renaissance Hotel",
        "description": """Im komfortabel eingerichteten Hotel der bekannten Marriott-Hotelgruppe befinden sich sieben
         Restaurants die den Gaumen verwöhnen und am beeindruckend großen Pool mit Sonnenterrasse liegen.""",
        "departure": "mcn",
        "picture": "https://images.unsplash.com/photo-1571896349842-33c89424de2d?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60",
        "price": 53000,
        "stars": "3",
        "country": "Pakistan",
        "nights": 13,
        "date": "15. Februar",
    },
    7: {
        "title": "King's Majesty Hotel",
        "description": """In direkter Strandlage gelegen und nicht weit vom Stadtzentrum entfernt, befindet sich dieses
         Hotel. Zahlreiche À-la-carte Restaurants sorgen für kulinarische Abwechslung. Ein großes Wellnessangebot sowie
          ein vielfältiges Unterhaltungsprogramm sorgen für jede Menge Spaß und Erholung.""",
        "departure": "frt",
        "picture": "https://images.unsplash.com/photo-1468824357306-a439d58ccb1c?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60",
        "price": 72000,
        "stars": "5",
        "country": "Mexico",
        "nights": 9,
        "date": "22. Januar",
    },
    8: {
        "title": "Crown Hotel",
        "description": """Das Crown Hotel bietet Unterkünfte mit einem Restaurant, kostenfreie Privatparkplätze, 
        eine Bar und einen Garten. Die Unterkunft befindet sich 3,8 km von Pashupatinath, 4,3 km von Swayambhu und 5 km
         von Boudhanath Stupa entfernt. Die Unterkunft bietet eine 24-Stunden-Rezeption, Flughafentransfers, 
         Zimmerservice und kostenfreies WLAN in der gesamten Unterkunft.""",
        "departure": "brmn",
        "picture": "https://images.unsplash.com/photo-1549109786-eb80da56e693?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60",
        "price": 44000,
        "stars": "4",
        "country": "Thailand",
        "nights": 7,
        "date": "3. Februar",
    },
    9: {
        "title": "Seascape Resort",
        "description": """Es befindet sich am besten Strandstreifen. Der Strand ist für seine sanft wiegenden Palmen,
         seine rollenden Wellen und beliebten Speisemöglichkeiten und Nachtlokale international berühmt. 
         Die Gäste können ihren Urlaub mit herzlicher Gastfreundschaft, in geschützter Lage inmitten eines Gartens mit
          dichter tropischer Flora und Fauna genießen. Bis zum Flughafen sind es etwa 3 km.""",
        "departure": "drn",
        "picture": "https://images.unsplash.com/photo-1570214476695-19bd467e6f7a?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60",
        "price": 39000,
        "stars": "3",
        "country": "Indien",
        "nights": 10,
        "date": "1. Februar",
    },
    10: {
        "title": "Rose Sanctum Hotel",
        "description": """Jedes Zimmer im Rose Sanctum Hotel ist mit modernen Möbeln ausgestattet. Zudem besitzen alle
         ein eigenes Bad mit einer Dusche und einem Haartrockner. Eine Minibar ist ebenfalls vorhanden.Morgens erwartet
        Sie ein Frühstücksbuffet. Zahlreiche Restaurants mit lokaler und internationaler Küche finden Sie in der
        Nachbarschaft. Die Hotelbar lockt mit warmen und kalten Getränken.""",
        "departure": "ber",
        "picture": "https://images.unsplash.com/photo-1560200353-ce0a76b1d438?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60",
        "price": 52000,
        "stars": "4",
        "country": "Kuba",
        "nights": 10,
        "date": "30. Januar",
    },
    11: {
        "title": "Viridian Obelisk Hotel & Spa",
        "description": """Die Zimmer im The Viridian Obelisk Hotel sind mit Holzmöbeln im modernen Thai-Stil eingerichtet.
         Jedes der klimatisierten Zimmer verfügt über Kabel-TV, Kaffee- und Teezubehör sowie einen Kühlschrank mit
          Minibar. Ihr eigenes Bad ist mit einem Haartrockner und einer Dusche ausgestattet.""",
        "departure": "mcn",
        "picture": "https://images.unsplash.com/photo-1477120128765-a0528148fed2?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60",
        "price": 68000,
        "stars": "5",
        "country": "Indien",
        "nights": 9,
        "date": "1. März",
    },
    12: {
        "title": "Saffron Tundra Hotel & Spa",
        "description": """Dieses 4-Sterne-Kongresshotel bietet elegante Zimmer, ein Restaurant, eine Lobbybar mit einer
         Büroecke, eine 24-Stunden-Rezeption, ein Fitnesscenter und eine Sauna. WLAN nutzen Sie in allen Bereichen
          kostenfrei und sichere Parkplätze stehen gegen Aufpreis zur Verfügung.""",
        "departure": "brmn",
        "picture": "https://images.unsplash.com/photo-1440151050977-247552660a3b?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60",
        "price": 72000,
        "stars": "4",
        "country": "Mexico",
        "nights": 12,
        "date": "17. Februar",
    },
    13: {
        "title": "Traveller Resort",
        "description": """Das Hotel Travellers Resort ist ein 3-Sterne-Hotel (Veranstalterkategorie). 
        Travellers Beach Resort wurde auf der Grundlage von 13 Hotelbewertungen mit 4,7 von 6,0 bewertet und hat eine 
        Weiterempfehlungsrate von 100. Entdecken Sie das Hotel Travellers Resort""",
        "departure": "frt",
        "picture": "https://images.unsplash.com/photo-1553653924-39b70295f8da?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60",
        "price": 49000,
        "stars": "3",
        "country": "Kuba",
        "nights": 8,
        "date": "26. Januar",
    },
    14: {
        "title": "History Hotel & Spa",
        "description": """Das mit 63,5 Gault&Millau-Punkten ausgezeichnete History Hotel bietet Ihnen das ganze Jahr
         über exklusive Arrangements und Specials für eine entspannte Zeit. Ob romantische Tage zu zweit,
          Wellness-Wochenende oder einfach eine Auszeit vom Alltag – es gibt viele gute Gründe, sich verwöhnen
           zu lassen.""",
        "departure": "brmn",
        "picture": "https://images.unsplash.com/photo-1509600110300-21b9d5fedeb7?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60",
        "price": 91000,
        "stars": "5",
        "country": "Vietnam",
        "nights": 9,
        "date": "3. Februar",
    },
    15: {
        "title": "Riverside Lagoon Hotel & Spa",
        "description": """Das ideal im Touristenzentrum Milnerton gelegene Lagoon Beach Hotel and Spa garantiert seinen
         Gästen einen entspannten und unvergesslichen Aufenthalt. Das Haus verfügt über eine große Vielfalt an
          Einrichtungen, um den Aufenthalt seiner Gäste so angenehm wie möglich zu gestalten. Zum Wohle der 
          Gäste gibt es 24-Stunden Zimmerservice, Kostenloses WiFi in allen Zimmern, 24-Stunden Sicherheitsdienst,
           Tägliche Reinigung, Privater Check-In/ Check-Out.""",
        "departure": "mcn",
        "picture": "https://images.unsplash.com/photo-1568084680786-a84f91d1153c?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60",
        "price": 82000,
        "stars": "4",
        "country": "Die Dominikanische Republik",
        "nights": 8,
        "date": "5. Februar",
    },
    16: {
        "title": "Radisson Blu Waterfront",
        "description": """Das ideal gelegene Radisson Blu Hotel Waterfront (Region um V &amp; A Waterfront) 
        garantiert seinen Gästen einen entspannten und unvergesslichen Aufenthalt. Die Unterkunft verfügt über eine 
        große Vielfalt an Einrichtungen, um Ihren Aufenthalt so angenehm wie möglich zu gestalten. Einrichtungen wie 
        Rollstuhlgerecht, Waschsalon, 24-Stunden Rezeption, Behindertengerechte Einrichtungen, Aufbewahrung für 
        Gepäckstücke usw.""",
        "departure": "mcn",
        "picture": "https://images.unsplash.com/photo-1564056095795-4d63b6463dbf?ixlib=rb-1.2.1&ixid"
                   "=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60",
        "price": 74000,
        "stars": "5",
        "country": "Vietnam",
        "nights": 12,
        "date": "24. Januar",
    }

}


@app.route('/')
def main():
    output = render_template("index.html", ways=ways)
    return output


@app.route('/from/<direction>')
def directions(direction):
    counter=int(0)
    iddirection = []
    minprice = ways[1]['price']
    maxprice = ways[1]['price']
    minnights = ways[1]['nights']
    maxnights = ways[1]['nights']
    for id in ways:
        if ways[id]['departure'] == direction:
            iddirection.append(id)
            if ways[id]['price'] > maxprice:
                maxprice = ways[id]['price']
            if ways[id]['price'] < minprice:
                minprice = ways[id]['price']
            if ways[id]['nights'] > maxnights:
                maxnights = ways[id]['nights']
            if ways[id]['nights'] < minnights:
                minnights = ways[id]['nights']
    output = render_template("direction.html", departres=departures, ways=ways, direction=departures[direction],counter=len(iddirection),minprice=minprice,maxprice=maxprice, maxnights=maxnights,minnights=minnights, iddirection=iddirection)
    return output


@app.route('/tours/<int:id>')
def tours(id):
    output = render_template("tour.html", title=ways[id]["title"], stars=ways[id]["stars"], country=ways[id]["country"], departure=departures[ways[id]['departure']], nights=ways[id]["nights"], description=ways[id]["description"],price=ways[id]["price"],picture=ways[id]["picture"])
    return output


if __name__ == '__main__':
    app.run()
