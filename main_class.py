import collector_actor
import matplotlib
matplotlib.use('TkAgg')
import matplotlib
matplotlib.use('TkAgg')


x=[]
y=[]
starter_actor = collector_actor.collector_actor.start(x, y)
starter_actor.ask({'message': 'init', 'starter_add': starter_actor})
