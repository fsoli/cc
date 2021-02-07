import collector_actor


x=[]
y=[]
number_of_pcs = input('number_of_pcs: ')
number_of_cities = input('number_of_cities: ')
starter_actor = collector_actor.collector_actor.start(x, y,number_of_pcs,number_of_cities)
starter_actor.ask({'message': 'init', 'starter_add': starter_actor})
