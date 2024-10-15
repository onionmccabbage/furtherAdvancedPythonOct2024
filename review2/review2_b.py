from weatherService_b import TempGetter
import timeit

def main():
    CITIES = [
        'Athlone', 'Galway', 'Belfast', 
        'Genoa', 'Cork', 'Kista'
    ]
    # CITIES = [
    #     'Athlone', 'Canberra'
    # ]
    # CITIES = ["Dublin","Cork","Limerick","Galway","Waterford","Drogheda","Kilkenny","Wexford","Sligo","Clonmel","Dundalk","Bray","Ennis","Tralee","Carlow","Naas","Athlone","Letterkenny","Tullamore","Killarney","Arklow","Cobh","Castlebar","Midleton","Mallow","Ballina","Enniscorthy","Wicklow","Cavan","Athy","Longford","Dungarvan","Nenagh","Trim","Thurles","Youghal","Monaghan","Buncrana","Ballinasloe","Fermoy","Westport","Carrick-on-Suir","Birr","Tipperary","Carrickmacross","Kinsale","Listowel","Clonakilty","Cashel","Macroom","Castleblayney","Kilrush","Skibbereen","Bundoran","Templemore","Clones","Newbridge","Mullingar","Balbriggan","Greystones","Leixlip","Tramore","Shannon","Gorey","Tuam","Edenderry","Bandon","Loughrea","Ardee","Mountmellick","Bantry","Boyle","Ballyshannon","Cootehill","Ballybay","Belturbet","Lismore","Kilkee","Granard"]
    # lock = threading.Lock()

    threads = [TempGetter(c) for c in CITIES]
    start = timeit.default_timer()
    # first we kick off all the threads
    for thread in threads:
        thread.start()

    # now we wait for all the threads to complete
    for thread in threads:
        thread.join()
        print("it is {0.temperature:.0f}°C in {0.city}".format(thread))
        print('lat {0.lat}, lon {0.lon}'.format(thread))

    print(f"Got {len(threads)} reports in {timeit.default_timer() - start} seconds")

if __name__ == '__main__':
    main()