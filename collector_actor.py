import tkinter as tk
from threading import Thread

import matplotlib

matplotlib.use('TkAgg')
import pykka
import matplotlib

matplotlib.use('TkAgg')
import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

matplotlib.use('TkAgg')
import numpy as np
from matplotlib.figure import Figure
import pc_actor

global number_of_cities
number_of_cities = 80
global x
global x_pc
x_pc = []
global y
global y_pc
y_pc = []
global canvas
global root
canvas = None
global starter_actor_address
global number_of_pcs
number_of_pcs = 8
global cities_of_pc
cities_of_pc = []

global a
global b
global n
n=0

class collector_actor(pykka.ThreadingActor):
    def __init__(self, x_arr, y_arr):

        super(collector_actor, self).__init__()
        self.x_arr = x_arr
        self.y_arr = y_arr
        x = x_arr
        y = y_arr

    def on_receive(self, message):
        global x
        global y
        global a
        global b
        if message['message'] == 'init':
            global starter_actor_address
            global root
            global x
            global y
            global n
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
                    plt.plot(x_pc[i], y_pc[i], color='blue')
                plt.show()
        # x=z.plot(xx,yy, color='green')

        if message['message']=='phas1':
            print(a)
            for i in range(number_of_pcs):
                plt.plot(x_pc[i], y_pc[i], color='blue')
            plt.plot([message['my_neigbor_suggest'][0][0],message['my_neigbor_suggest'][1][0]], [message['my_neigbor_suggest'][0][1],message['my_neigbor_suggest'][1][1]], color='orange')
            plt.plot([message['my_suggest'][0][0],message['my_suggest'][1][0]], [message['my_suggest'][0][1],message['my_suggest'][1][1]], color='orange')

            # if (n<=a-1):
            #     n+=1;
            # else:
            plt.title('x')
            plt.show()

        if message['message'] == 'phas2':
            print('c')
            for i in range(number_of_pcs):
                plt.plot(x_pc[i], y_pc[i], color='blue')
            plt.plot([message['my_neigbor_suggest'][0][0],message['my_neigbor_suggest'][1][0]],[ message['my_neigbor_suggest'][0][1],message['my_neigbor_suggest'][1][1]], color='red')
            # plt.scatter(, , color='red')
            plt.plot([message['my_suggest'][0][0],message['my_suggest'][1][0]], [message['my_suggest'][0][1],message['my_suggest'][1][1]], color='red')
            # if (n<=b-1):
            #     n+=1;
            # else:
            plt.title('y')
            plt.show()

def devide():
    global x
    global y
    global number_of_pcs
    global number_of_cities
    global a
    global b

    # divide pcs
    for i in range(int(np.sqrt(number_of_pcs)), 0, -1):  # (ab)
        if number_of_pcs % i == 0:
            a = int(number_of_pcs / i)
            b = i
            break
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
    global x
    global y
    global canvas
    # number_of_cities = int(self.box.get())
    x = np.random.rand(number_of_cities)
    y = np.random.rand(number_of_cities)
