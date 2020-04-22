##A nappali a fürdőszobától keletre található.
##
##Parancsok:menj,nézd,vedd fel,tedd le,nyisd,húzd,törd
##Speciális:leltár,mentés,betöltés
##Megoldás: nappali szekrénye mögött-> ablakot betörni feszítővassal


leltár=set()

kád='nem látta'
szekrény_helye='nincs elmozdítva'
ajtó='zárva'
szekrény = 'zárva'

#feltételezve,hogy mindig a nappaliban kezd a játékos.
tartózkodási_hely='nappali'

print('A nappaliban vagy.')
while True:
    answer=input('\nMit szeretnél tenni?\n').lower().strip()
    if answer == ('leltár'):
        print('Leltár:',leltár)
#nappali
    if tartózkodási_hely == 'nappali':

        if answer == ('nézd'):
            print('A nappaliban vagy.Itt talalható egy szekrény és egy ajtó nyugatra.')

        if answer == ('nézd szekrény'):
            print('Ez a szekrény elhúzható és kinyitható.')

        if answer == ('nyisd'):
            print('Adj meg valamit amit kinyithatsz!')
            
        if answer == ('nyisd szekrény'):
            print('kinyitod a szekrényt és találsz benne egy dobozt.')
            szekrény='nyitva'

        if szekrény == 'nyitva' and answer == ('vedd fel doboz') and 'doboz' not in leltár:
            print('Felvetted a dobozt.')
            leltár.add('doboz')

        if szekrény == 'zárva' and answer == ('vedd fel doboz'):
            print('Milyen dobozt?')

        if 'doboz' in leltár and answer == ('nézd doboz'):
            print('Ez egy doboz,valami van benne.')

        if 'doboz' not in leltár and answer == ('nézd doboz'):
            print('Nincs nálam doboz.')
        
        if  'kulcs' in leltár and answer == ('nyisd doboz'):
            print('Már kinyitottam a dobozt.')

        if 'doboz' in leltár and 'kulcs' not in leltár and answer == ('nyisd doboz'):
            print('Kinyitottad a dobozt és egy kulcsot találtál benne.')
            leltár.add('kulcs')
        
        if 'kulcs' in leltár and answer == ('nézd kulcs'):
            print('Ez egy kulcs,valamit ki tud nyitni.')

        if 'kulcs' not in leltár and answer == ('nézd kulcs'):
            print('Nincs nálam kulcs.')
        
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
            
        if answer == ('menj'):
            print('Merre menjek?(észak,dél,kelet,nyugat.)')

        if answer == ('menj észak')and szekrény_helye=='nincs elmozdítva':
            print('Észak felé csak a szekrény van.')

        if answer == ('menj észak')and szekrény_helye=='elmozdítva':
            print('Észak felé egy szekrény és egy ablak van de nem tudok átmenni rajta.')
        
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

        if answer == ('nézd feszítővas')and 'feszítővas' not in leltár:
            print('Nincs nálam feszítővas.')

        if answer == ('nézd feszítővas')and 'feszítővas' in leltár:
            print('Ezzel a feszítővassal össze törhetek pár dolgot.')
        
        if answer == ('vedd fel feszítővas')and kád=='látta' and 'feszítővas' not in leltár:
            print('Felvetted a feszítővasat')
            leltár.add('feszítővas')
            
        if answer == ('nézd szekrény'):
            print('A szekrény a másik szobában van.')
