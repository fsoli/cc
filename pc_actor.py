import pykka
import tsp



class pc_actor(pykka.ThreadingActor):
    # global candidate
    def __init__(self, pc_ID, nodes_arr, starter_actor_address, neighbors,candidate,candidate2):
        super(pc_actor, self).__init__()
        self.pc_ID = pc_ID
        self.nodes_arr = nodes_arr
        self.starter_actor_address = starter_actor_address
        self.neighbors = neighbors
        self.candidate = candidate
        self.candidate2 = candidate2


    def on_receive(self, message):
        if message['message'] == 'init':
            self.neighbors = message['neighbors']
        if message['message'] == 'tsp':
            self.candidate = [(0, 0), (0, 0), (0, 1), (1, 0)]  # urdl
            self.candidate2 = [(0, 0), (0, 0), (0, 1), (1, 0)]  # urdl
            city_pos = []
            for i in range(len(self.nodes_arr)):
                city_pos.append((self.nodes_arr[i][0], self.nodes_arr[i][1]))
            t = tsp.tsp(city_pos)
            aaax = []
            aaay = []
            # aaax.append(city_pos[t[1][0]][0])
            # aaay.append(city_pos[t[1][0]][1])
            for i in range(len(self.nodes_arr)):
                # city_pos[t[1][i]][0]
                aaax.append(city_pos[t[1][i]][0])
                aaay.append(city_pos[t[1][i]][1])
                if self.candidate[0][1] < (city_pos[t[1][i]][1]):  # u
                    self.candidate[0] = city_pos[t[1][i]]
                    self.candidate2[0] = city_pos[t[1][i-1]]

                    # if candidate2[0]==0:
                    #     candidate2[0] = candidate[0]
                if self.candidate[1][0] < (city_pos[t[1][i]][0]):  # r
                    self.candidate[1] = city_pos[t[1][i]]
                    self.candidate2[1] = city_pos[t[1][i-1]]
                    # if candidate2[1]==0:
                    #     candidate2[1] = candidate[1]
                if self.candidate[2][1] > (city_pos[t[1][i]][1]):  # d
                    self.candidate[2] = city_pos[t[1][i]]
                    self.candidate2[2] = city_pos[t[1][i-1]]
                    # if candidate2[2]==1:
                    #     candidate2[2] = candidate[2]
                if self.candidate[3][0] > (city_pos[t[1][i]][0]):  # l
                    self.candidate[3] = city_pos[t[1][i]]
                    self.candidate2[3] = city_pos[t[1][i-1]]

                    # if candidate2[3]==1:
                    #     candidate2[3] = candidate[3]
            aaax.append(city_pos[t[1][0]][0])
            aaay.append(city_pos[t[1][0]][1])
            # print('aaaaaaaaaaaaaaaaaaaaaa')
            # print('##  ',(aaay))
            # print('@@', (candidate))
            # print('##', (candidate2))
            # print(self.pc_ID,self.candidate)

            self.starter_actor_address.tell({'message': 'update', 'x': aaax, 'y': aaay})

        if message['message'] == 'tsp_betweenl':
            if(self.neighbors[1]!=-1):
                self.neighbors[1].ask({'message': 'l_suggest','suggest':[self.candidate[1],self.candidate2[1]]})
        if message['message'] == 'tsp_betweend':
            if self.neighbors[2]!=-1 or self.neighbors[2]!=-1:
                self.neighbors[2].ask({'message': 'd_suggest','suggest':[self.candidate[2],self.candidate2[2]]})


        if message['message'] == 'l_suggest':
            self.starter_actor_address.tell({'message': 'phas1','my_suggest':[self.candidate[3],self.candidate2[3]], 'my_neigbor_suggest': message['suggest']})
        if message['message'] == 'd_suggest':

                self.starter_actor_address.tell({'message': 'phas2','my_suggest':[self.candidate[0],self.candidate2[0]], 'my_neigbor_suggest': message['suggest']})

