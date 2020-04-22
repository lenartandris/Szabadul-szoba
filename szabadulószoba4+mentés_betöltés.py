import pickle
##helyszínek: nappali,fürdőszoba
##
##nappali->szekrény->doboz-> kulcs->fürdőszoba zárt ajtaja
##fürdőszoba->kád->feszítővas
##
##A nappali a fürdőszobától keletre található.
##
##Parancsok:menj,nézd,vedd fel,tedd le,nyisd,húzd,törd
##Speciális:leltár,mentés,betöltés
##Megoldás: nappali szekrénye mögött-> ablakot betörni feszítővassal


leltár=set()
szekrény='zárva'
ajtó='zárva'
kád='nem látta'
szekrény_helye='nincs elmozdítva'
ablak='nem törött'

#feltételezve,hogy mindig a nappaliban kezd a játékos.
tartózkodási_hely='nappali'
print('A nappaliban vagy.')
while True:
    answer=input('\nMit szeretnél tenni?\n').lower().strip()
#leltárműveletek
    if answer == ('leltár'):
        print('Leltár:',leltár) 
    if answer==('tedd le kulcs')and 'kulcs' in leltár:
        print('letetted a kulcsot')
        leltár.remove('kulcs')
    if answer==('tedd le doboz')and 'doboz' in leltár:
        leltár.remove('doboz')
        print('letetted a dobozt')
    if answer==('tedd le feszítővas')and 'feszítővas' in leltár:
        leltár.remove('feszítővas')
        print('letetted a feszítővasat')
    if answer==('vedd fel feszítővas') and kád=='látta' and 'feszítővas' not in leltár:
        leltár.add('feszítővas')
        print('felvetted a feszítővasat')
    if answer==('vedd fel kulcs') and szekrény=='nyitva' and 'kulcs' not in leltár:
        leltár.add('kulcs')
        print('felvetted a kulcsot')
    if 'doboz' in leltár and answer == ('nézd doboz'):
        print('Ez egy doboz,valami van benne.')
    if 'doboz' not in leltár and answer == ('nézd doboz'):
        print('Nincs nálam doboz.')
    if 'kulcs' in leltár and answer == ('nézd kulcs'):
        print('Ez egy kulcs,valamit ki tud nyitni.')
    if 'kulcs' not in leltár and answer == ('nézd kulcs'):
        print('Nincs nálam kulcs.')
    if answer == ('nézd feszítővas')and 'feszítővas' not in leltár:
        print('Nincs nálam feszítővas')
    if answer == ('nézd feszítővas')and 'feszítővas' in leltár:
        print('Ezzel a feszítővassal össze törhetek pár dolgot.')
        
#nappali
    if tartózkodási_hely == 'nappali':
        if answer == ('nézd') and szekrény_helye=='elmozdítva' and ablak=='nem törött':
            print('A nappaliban vagy.Itt található egy ajtó nyugatra, egy szekrény és egy ablak pedig északra.')
        
        if answer == ('nézd') and szekrény_helye=='elmozdítva'and ablak=='törött':
            print('A nappaliban vagy.Itt található egy ajtó nyugatra, egy szekrény és egy betört ablak pedig északra.')

        if answer == ('nézd')and szekrény_helye=='nincs elmozdítva':
            print('A nappaliban vagy.Itt talalható egy szekrény és egy ajtó nyugatra.')

        if answer == ('nézd szekrény'):
            print('Ez a szekrény elhúzható és kinyitható.')

        if answer == ('nyisd'):
            print('Adj meg valamit amit kinyithatsz!')

        if answer == ('nyisd ablak')and szekrény_helye=='nincs elmozdítva':
            print('Nem látok ablakokat.')

        if answer == ('nyisd ablak')and szekrény_helye=='elmozdítva':
            print('Beszorult az ablak,nem tudod kinyitni.')
            
        if answer == ('nyisd szekrény'):
            print('kinyitod a szekrényt és találsz benne egy dobozt.')
            szekrény='nyitva'

        if szekrény == 'nyitva' and answer == ('vedd fel doboz') and 'doboz' not in leltár:
            print('Felvetted a dobozt.')
            leltár.add('doboz')

        if szekrény == 'zárva' and answer == ('vedd fel doboz'):
            print('Milyen dobozt?')
        
        if  'kulcs' in leltár and answer == ('nyisd doboz'):
            print('Már kinyitottam a dobozt.')

        if 'doboz' in leltár and 'kulcs' not in leltár and answer == ('nyisd doboz'):
            print('Kinyitottad a dobozt és egy kulcsot találtál benne.')
            leltár.add('kulcs')
        
        if answer == ('nézd ajtó'):
            print('Az ajtó a fürdőszobába vezet és kulcsra van zárva')

        if answer == ('nyisd ajtó')and 'kulcs' not in leltár:
            print('Az ajtó kulcsra van zárva')

        if answer == ('nyisd ajtó')and 'kulcs' in leltár:
            print('Kinyitottad az ajtót.')
            print('Most már átmehetsz a fürdőszobába')
            ajtó='nyitva'

        if answer == ('húzd szekrény') and szekrény_helye=='elmozdítva':
            print('Már arréb húztad a szekrényt.')

        if answer == ('húzd szekrény') and szekrény_helye=='nincs elmozdítva':
            print('Elhúztad a szekrényt és felfedeztél egy ablakot mögötte.')
            szekrény_helye='elmozdítva' 

        if szekrény_helye=='elmozdítva' and answer==('nézd ablak'):
            print('Ha össze tudnám törni ezt az ablakot akkor ki tudnék jutni.')

        if szekrény_helye=='elmozdítva' and answer==('törd ablak'):
            print('Nem tudom széttörni az üveget puszta kézel.')
    
        if szekrény_helye=='elmozdítva' and answer==('törd ablak feszítővas') and 'feszítővas' not in leltár:
            print('Nincs nálam feszítővas.')    

        if szekrény_helye=='elmozdítva' and answer==('törd ablak feszítővas') and 'feszítővas' in leltár:
            print('Összetörted az ablakot.A szoba mostmár észak fele elhagyható.')  
            ablak='törött'
            
        if answer == ('menj'):
            print('Merre menjek?(észak,dél,kelet,nyugat.)')

        if answer == ('menj észak')and szekrény_helye=='nincs elmozdítva':
            print('Észak felé csak a szekrény van.')

        if answer == ('menj észak')and szekrény_helye=='elmozdítva' and ablak=='nem törött':
            print('Észak felé egy szekrény és egy ablak van de nem tudok átmenni rajta.')
        
        if answer == ('menj észak')and szekrény_helye=='elmozdítva' and ablak=='törött':
            print('Átmásztál az ablakon és kijutottál.')
            print('Megnyerted a játékot!')
            break
        if answer == ('menj dél'):
            print('Dél felé nincs semmi.')

        if answer == ('menj kelet'):
            print('Keleten sincs semmi érdekes.')

        if answer == ('menj nyugat') and ajtó=='zárva':
            print('Nyugat felé van az ajtó de az zárva van')

        if answer == ('menj nyugat') and ajtó=='nyitva':
            print('Átmentél a nyitott ajtón a fürdőszobába,ennél nyugatabbra nem tudsz menni.')
            tartózkodási_hely = 'fürdőszoba'
#fürdőszoba
    if tartózkodási_hely == 'fürdőszoba':

        if answer==('tedd le kulcs')and 'kulcs' in leltár:
            print('letetted a kulcsot')
            leltár.remove('kulcs')

        if answer==('vedd fel kulcs')and 'kulcs' not in leltár:
            leltár.add('kulcs')
            print('Felvetted a kulcsot a fürdőszobában.')

        if answer==('tedd le doboz')and 'doboz' in leltár:
            leltár.remove('doboz')
            print('letetted a dobozt')
            
        if answer==('vedd fel doboz')and 'doboz' not in leltár:
            leltár.add('doboz')
            print('Felvetted a dobozt a fürdőszobában.')
        
        if answer == ('menj kelet'):
            print('Visszamész a nappaliba.')
            tartózkodási_hely = 'nappali'

        if answer == ('menj észak'):
            print('Nem tudok észak felé menni')

        if answer == ('menj dél'):
            print('Nem tudok dél felé menni')

        if answer == ('nézd'):
            print('A fürdőszobában vagy ahol csak egy kád van.')

        if answer == ('nézd kád')and kád=='nem látta':
            print('Közelebb lépsz és meglátsz a kádban egy feszítővasat')
            kád='látta'

        if answer == ('nézd kád')and 'feszítővas' in leltár:
            print('A kád üres.')

        if answer == ('vedd fel feszítővas')and kád=='nem látta':
            print('Egy feszítővasat sem látok')
        
        if answer == ('vedd fel feszítővas')and kád=='látta' and 'feszítővas' not in leltár:
            print('Felvetted a feszítővasat')
            leltár.add('feszítővas')
        
        if answer == ('nézd szekrény'):
            print('A szekrény a másik szobában van.')

# mentés
    if answer == ('mentés'):
        with open('játékmentés', 'wb') as f:
            pickle.dump([leltár, szekrény, ajtó, kád, szekrény_helye, ablak, tartózkodási_hely], f, protocol=2)

# betöltés
    if answer == ('betöltés'):
        with open('játékmentés', 'rb') as f:
            leltár, szekrény, ajtó, kád, szekrény_helye, ablak, tartózkodási_hely = pickle.load(f)

