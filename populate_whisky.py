import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','whisky.settings')

import django
django.setup()
from pages.models import Distillery,Whisky

def populate():
    Ardbeg_whiskies = [
        {'id' : '1',
        'name':'Ar1',
        'age':'30',
        'abv':'55',
        'description':'The first-ever Ar bottling is a big beast, showing the power that southern Islay is known for. Ar1 makes a statement, and is laden with sweet spice and malty goodness'},
        {'id' : '2',
        'name':'Ar2',
        'age':'50',
        'abv':'45',
        'description':'Even bigger than Ar1, this is a peaty powerhouse loaded with flavour and character. The perfect marriage of ex-bourbon hogsheads with southern Islay spirit'}]

    Bowmore_whiskies = [
        {'id' : '3',
        'name':'Bw1',
        'age':'56',
        'abv':'59',
        'description':'The first-ever Bw bottling shows the maritime side of Islay malts, with whisky from the famed mid-1990s period'},
        {'id' : '4',
        'name':'Bw2',
        'age':'43',
        'abv':'50',
        'description':'Bw2 is a travel-retail only expression with malt whisky from a single 1990s vintage. Smoke takes a back seat here with Bowmores trademark tropical fruit taking centre stage'}]

    Bruichladdich_whiskies = [
        {'id' : '5',
        'name':'Br1',
        'age':'20',
        'abv':'60',
        'description':'While this distillery reopened under new ownership in 2000, the opening shot of the Br series looks back to its previous incarnation. Bottled from a small batch of casks from a single vintage, it is an unashamedly old-fashioned whisky, packed with fruit and a youthful character despite its age'},
        {'id' : '6',
        'name':'Br2',
        'age':'26',
        'abv':'53',
        'description':'Before this distillery reopened, its whisky was very different to its current offerings. Br2 continues in Br1’s footsteps, exemplifying this sweet, fruity and oily style. A marriage of a small number of casks from a single production year, the fruity character of the spirit shines through'}]

    Caol_Ila_whiskies =[
        {'id' : '7',
        'name':'CI1',
        'age':'80',
        'abv':'58',
        'description':'The first release of Cl was very special. A marriage of whiskies of different ages, it was created to show both the punchy character of more youthful spirit as well as the elegance brought by age. The benchmark by which all other Cl whiskies are judged'},
        {'id' : '8',
        'name':'CI2',
        'age':'77',
        'abv':'53',
        'description':'While the distillery is known for its intensely peaty whisky, with age its spirit can display the character of its closed sibling in the south of the island. Cl2 aimed to capture some of the old-fashioned waxiness that distillery is known for, as well as the intensity of a modern Cl'}]

    Kilchoman_whiskies = [
        {'id' : '9',
        'name':'Ki1',
        'age':'66',
        'abv':'39',
        'description':'This holds the accolade of being the first independently bottled whisky from the distillery, and even now is one of a small handful that has been released. A young distillery, this whisky shows surprising maturity and complexity while keeping its fresh and fruity character a triumph'}]

    distilleries = {'Ardbeg':{'id':'1','whiskies':Ardbeg_whiskies,'location':'Port Ellen Isle of Islay Argyll PA42 7DU United Kingdom','description':'Opened in 1815, at one time Ardbeg was the largest distillery on Islay, supporting an entire community. Now, it is the second smallest, although due to its huge worldwide following, its community is bigger than ever'},
                    'Bowmore':{'id':'2','whiskies':Bowmore_whiskies,'location':'School St Bowmore (Islay) PA43 7JS United Kingdom','description':'The oldest distillery on Islay, and among the oldest in Scotland, Bowmore was founded in 1779, in the heart of the town of the same name, the islands capital. It is the second-biggest-selling whisky on Islay, producing a medium-peated malt with a character that has varied over the years'},
                    'Bruichladdich':{'id':'3','whiskies':Bruichladdich_whiskies,'location':'Islay (Argyll) PA49 7UN United Kingdom','description':'One of two distilleries on the Rhinns of Islay, the western peninsula of the island, Bruichladdich was founded in 1881. Over the past 130 years, the distillery has changed hands many times and had frequent closures, but since 2000 it has been reborn, and is yet again at the forefront of Scottish whisky distilling'},
                    'CaolIla':{'id':'4','whiskies':Caol_Ila_whiskies,'location':'Port Askaig Isle of Islay (Argyll) PA46 7RL United Kingdom','description':'Sat just along the coast from Port Askaig, Caol Ila looks out over the Sound of Islay towards Jura. Despite its relative proximity to civilisation, it is relatively hidden, thank to the steep descent down to the distillery from the main road as Alfred Barnard said of his visit in the 1880s: But the way is so steep, and our nerves none of the best, that we insist upon doing the remainder of the descent on foot, much to the disgust of the driver, who muttered strange words in Gaelic'},
                    'Kilchoman':{'id':'5','whiskies':Kilchoman_whiskies,'location':'Rockside Farm Bruichladdich Isle of Islay (Argyll) PA49 7UT United Kingdom','description':'The newest distillery on the island, Kilchoman sprung up in 2005 at Rockside Farm. It is the second operating distillery in the Rhinns of Islay, the western peninsula of the island, and is a modern take on the farm distiller it grows grain, malts it, and uses it to make whisky, all on the same site'}}

    for distillery,distillery_data in distilleries.items():
        dist = add_distillery(distillery_data['id'],distillery,distillery_data['location'],distillery_data['description'])
        for whisky in distillery_data['whiskies']:
            add_whisky(whisky['id'],whisky['name'],whisky['age'],whisky['abv'],whisky['description'],dist)

    #debug
    for dist in Distillery.objects.all():
        for whisky in Whisky.objects.filter(distillery=dist):
            print(f'- {dist}: {whisky}')

def add_whisky(id,name,age,abv,description,dist):
    table_whisky = Whisky.objects.get_or_create(distillery = dist,id=id)[0]
    table_whisky.name=name
    table_whisky.age=age
    table_whisky.abv=abv
    table_whisky.description=description
    table_whisky.save()
    return table_whisky

def add_distillery(id,name,location,description):
    table_distillery = Distillery.objects.get_or_create(id=id)[0]
    table_distillery.name=name
    table_distillery.location=location
    table_distillery.description=description
    table_distillery.save()
    return table_distillery


if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()