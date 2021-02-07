
import pykka
import matplotlib.pyplot as plt

import numpy as np
import pc_actor

global number_of_cities
global number_of_pcs

global x
global x_pc
x_pc = []
global y
global y_pc
y_pc = []
global starter_actor_address
global cities_of_pc
cities_of_pc = []
global xxx
global yyy
xxx=[]
yyy=[]
global xxxe
global yyye
xxxe=[]
yyye=[]
global a
global b

class collector_actor(pykka.ThreadingActor):

    def __init__(self, x_arr, y_arr,num_of_pcs,num_of_cities):
        global number_of_cities
        global number_of_pcs
        super(collector_actor, self).__init__()
        self.x_arr = x_arr
        self.y_arr = y_arr
        self.num_of_pcs=num_of_pcs
        self.num_of_cities=num_of_cities
        number_of_pcs=int(num_of_pcs)
        number_of_cities=int(num_of_cities)


    def on_receive(self, message):
        global number_of_cities
        global number_of_pcs
        global x
        global y
        global a
        global b
        global starter_actor_address

        if message['message'] == 'init':
            starter_actor_address = message['starter_add']
            input()
            devide()

        if message['message'] == 'update':
            global number_of_pcs
            x_pc.append(message['x'])
            y_pc.append(message['y'])
            if len(x_pc) == number_of_pcs:
                xx = []
                yy = []
                for i in range(number_of_pcs):
                    xx += x_pc[i]
                    yy += y_pc[i]

                global cities_of_pc

                for i in range(number_of_pcs):
                    plt.plot(x_pc[i], y_pc[i], color='gray')
                plt.title('number of pcs: ' + str(number_of_pcs) + ',number ofpcs: ' + str(number_of_cities))
                plt.show()
        # x=z.plot(xx,yy, color='green')
        global xxx
        global yyy
        global xxxe
        global yyye
        global b
        if message['message']=='phas1':
            neigbor_suggest1_x=(message['my_neigbor_suggest'][0][0])
            neigbor_suggest2_x=(message['my_neigbor_suggest'][1][0])
            my_suggest1_x=(message['my_suggest'][0][0])
            my_suggest2_x=(message['my_suggest'][1][0])
            neigbor_suggest1_y =(message['my_neigbor_suggest'][0][1])
            neigbor_suggest2_y =message['my_neigbor_suggest'][1][1]
            my_suggest1_y=(message['my_suggest'][0][1])
            my_suggest2_y=(message['my_suggest'][1][1])

            for i in range(number_of_pcs):
                plt.plot(x_pc[i], y_pc[i], color='gray')
            plt.plot([neigbor_suggest1_x,neigbor_suggest2_x], [neigbor_suggest1_y,neigbor_suggest2_y],color='white')
            plt.plot([my_suggest1_x,my_suggest2_x], [my_suggest1_y,my_suggest2_y], color='white')

            plt.plot([neigbor_suggest1_x,my_suggest2_x], [neigbor_suggest1_y,my_suggest2_y], color='orange')
            plt.plot([my_suggest1_x,neigbor_suggest2_x], [my_suggest1_y,neigbor_suggest2_y], color='orange')

            xxxe.append(neigbor_suggest1_x)
            xxxe.append(neigbor_suggest2_x)
            xxxe.append(my_suggest1_x)
            xxxe.append(my_suggest2_x)
            yyye.append(neigbor_suggest1_y)
            yyye.append(neigbor_suggest2_y)
            yyye.append(my_suggest1_y)
            yyye.append(my_suggest2_y)

            xxx.append(neigbor_suggest1_x)
            xxx.append(my_suggest2_x)
            yyy.append(neigbor_suggest1_y)
            yyy.append(my_suggest2_y)
            xxx.append(my_suggest1_x)
            xxx.append(neigbor_suggest2_x)
            yyy.append(my_suggest1_y)
            yyy.append(neigbor_suggest2_y)

            plt.title('number of pcs: '+str(number_of_pcs)+',number ofpcs: '+str(number_of_cities))
            plt.show()




        if message['message'] == 'phas2':
            for i in range(number_of_pcs):
                plt.plot(x_pc[i], y_pc[i], color='gray')
            plt.plot([message['my_neigbor_suggest'][0][0],message['my_neigbor_suggest'][1][0]],[ message['my_neigbor_suggest'][0][1],message['my_neigbor_suggest'][1][1]], color='red')
            plt.plot([message['my_suggest'][0][0],message['my_suggest'][1][0]], [message['my_suggest'][0][1],message['my_suggest'][1][1]], color='red')

            xxxe.append(message['my_neigbor_suggest'][0][0])
            xxxe.append(message['my_neigbor_suggest'][1][0])
            xxxe.append(message['my_suggest'][0][0])
            xxxe.append(message['my_suggest'][1][0])
            yyye.append(message['my_neigbor_suggest'][0][1])
            yyye.append(message['my_neigbor_suggest'][1][1])
            yyye.append(message['my_suggest'][0][1])
            yyye.append(message['my_suggest'][1][1])

            xxx.append(message['my_neigbor_suggest'][0][0])
            xxx.append(message['my_suggest'][1][0])
            xxx.append(message['my_suggest'][0][0])
            xxx.append(message['my_neigbor_suggest'][1][0])
            yyy.append(message['my_neigbor_suggest'][0][1])
            yyy.append(message['my_suggest'][1][1])
            yyy.append(message['my_suggest'][0][1])
            yyy.append(message['my_neigbor_suggest'][1][1])

        # fig = plt.figure()
        # fig.suptitle('test title', fontsize=20)
        # plt.xlabel('xlabel', fontsize=18)
        # plt.ylabel('ylabel', fontsize=16)
        # fig.savefig('test.jpg')
            print('aaaa')
            plt.title('number of pcs: '+str(number_of_pcs)+',number ofpcs: '+str(number_of_cities))
            plt.show()


        if len(xxx) == (4*(number_of_pcs-b))+((b-1)*4):
        # if True:
            for i in range(number_of_pcs):
                plt.plot(x_pc[i], y_pc[i], color='blue')
            for i in range(0,len(xxx) - 1,2):
                plt.plot([xxx[i], xxx[i + 1]], [yyy[i], yyy[i + 1]], "black")
                plt.plot([xxxe[i], xxxe[i + 1]], [yyye[i], yyye[i + 1]], "white")
            xxx = []
            xxxe = []
            plt.title('number of pcs: ' + str(number_of_pcs) + ',number ofpcs: ' + str(number_of_cities))

            plt.show()

def devide():
    global x
    global y
    global number_of_pcs
    global number_of_cities
    global a
    global b

    # divide pcs
    b=2
    a=int(number_of_pcs/2)
    # divide cities
    global cities_of_pc
    for i in range(number_of_pcs):
        new = []
        cities_of_pc.append(new)
    for i in range(number_of_cities):
        for j in range(b):
            if y[i] <= (j + 1) / b:
                for k in range(a):
                    if x[i] <= (k + 1) / a:
                        city = (x[i], y[i])
                        cities_of_pc[j * a + k].append(city)
                        break
                break

    # pc_actors
    global starter_actor_address
    global pc
    neighbors = []
    pc = []
    for i in range(number_of_pcs):
        pc.append(pc_actor.pc_actor.start(i, (cities_of_pc[i]), starter_actor_address, [],[],[]))
        pc[i].ask({'message': 'tsp'})
        neighbors.append([-1, -1, -1, -1])

    # pc_actors neigbors
    for i in range(number_of_pcs):
        if (i + a) < number_of_pcs:
            neighbors[i][0] = pc[i + a]  # u
        if i % a != a - 1:
            neighbors[i][1] = pc[i + 1]  # r
        if (i - a) >= 0:
            neighbors[i][2] = pc[i - a]  # d
        if i % a != 0:
            neighbors[i][3] = pc[i - 1]  # l

    for i in range(number_of_pcs):
        pc[i].ask({'message': 'init', 'neighbors': neighbors[i]})
        pc[i].ask({'message': 'tsp_betweenl'})
        pc[i].ask({'message': 'tsp_betweend'})


def input():
    global number_of_cities
    global number_of_pcs
    global x
    global y

    x = np.random.rand(number_of_cities)
    y = np.random.rand(number_of_cities)
