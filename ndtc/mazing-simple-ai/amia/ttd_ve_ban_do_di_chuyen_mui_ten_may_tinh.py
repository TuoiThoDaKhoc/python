from search import *
import tkinter as tk

import tkinter.ttk as ttk

import numpy as np
import time
romania_map = UndirectedGraph(dict(
    Arad=dict(Zerind=75, Sibiu=140, Timisoara=118),
    Bucharest=dict(Urziceni=85, Pitesti=101, Giurgiu=90, Fagaras=211),
    Craiova=dict(Drobeta=120, Rimnicu=146, Pitesti=138),
    Drobeta=dict(Mehadia=75),
    Eforie=dict(Hirsova=86),
    Fagaras=dict(Sibiu=99),
    Hirsova=dict(Urziceni=98),
    Iasi=dict(Vaslui=92, Neamt=87),
    Lugoj=dict(Timisoara=111, Mehadia=70),
    Oradea=dict(Zerind=71, Sibiu=151),
    Pitesti=dict(Rimnicu=97),
    Rimnicu=dict(Sibiu=80),
    Urziceni=dict(Vaslui=142)))

romania_map.locations = dict(
    Arad=(91, 492), Bucharest=(400, 327), Craiova=(253, 288),
    Drobeta=(165, 299), Eforie=(562, 293), Fagaras=(305, 449),
    Giurgiu=(375, 270), Hirsova=(534, 350), Iasi=(473, 506),
    Lugoj=(165, 379), Mehadia=(168, 339), Neamt=(406, 537),
    Oradea=(131, 571), Pitesti=(320, 368), Rimnicu=(233, 410),
    Sibiu=(207, 457), Timisoara=(94, 410), Urziceni=(456, 350),
    Vaslui=(509, 444), Zerind=(108, 531))

city_name = dict(
    Arad=(-35, 0), Bucharest=(0, 15), Craiova=(-20, 15),
    Drobeta=(-50, 0), Eforie=(0, 15), Fagaras=(10, 0),
    Giurgiu=(10, 0), Hirsova=(10, 0), Iasi=(10, 0),
    Lugoj=(10, 0), Mehadia=(10, 0), Neamt=(10, -5),
    Oradea=(-50, 0), Pitesti=(-5, 20), Rimnicu=(10, -5),
    Sibiu=(0, -20), Timisoara=(-60, 0), Urziceni=(0, 15),
    Vaslui=(10, 0), Zerind=(-50, 0))


graph_dict = romania_map.graph_dict
romania_locations = romania_map.locations

class App(tk.Tk):
    def	__init__(self):
        super().__init__()

        self.start = 'Arad'
        self.dest = 'Arad'
        self.path_location = None

        self.title('Search')
        self.cvs_map = tk.Canvas(self, width = 640, height = 480,
                                 relief = tk.SUNKEN, border = 1)
        self.ve_ban_do()
        lbl_frm_menu = tk.LabelFrame(self)
        lst_city = []
        for city in city_name:
            lst_city.append(city)

        lbl_start = ttk.Label(lbl_frm_menu, text = 'Start')

        self.cbo_start = ttk.Combobox(lbl_frm_menu, values = lst_city)
        self.cbo_start.set('Arad')
        self.cbo_start.bind("<<ComboboxSelected>>", self.cbo_start_click)        

        lbl_start.grid(row = 0, column = 0, padx = 5, pady = 0, sticky = tk.W)

        self.cbo_start.grid(row = 1, column = 0, padx = 5, pady = 5)


        lbl_dest = ttk.Label(lbl_frm_menu, text = 'Dest')

        self.cbo_dest = ttk.Combobox(lbl_frm_menu, values = lst_city)
        self.cbo_dest.set('Arad')
        self.cbo_dest.bind("<<ComboboxSelected>>", self.cbo_dest_click)        

        btn_direction = ttk.Button(lbl_frm_menu, text = 'Direction',
                                   command = self.btn_direction_click)
        btn_run = ttk.Button(lbl_frm_menu, text = 'Run',
                             command = self.btn_run_click)

        lbl_dest.grid(row = 2, column = 0, padx = 5, pady = 0, sticky = tk.W)

        self.cbo_dest.grid(row = 3, column = 0, padx = 5, pady = 5)

        btn_direction.grid(row = 4, column = 0, padx = 5, pady = 5)
        btn_run.grid(row = 5, column = 0, padx = 5, pady = 5)



        self.cvs_map.grid(row = 0, column = 0, padx = 5, pady = 5)
        lbl_frm_menu.grid(row = 0, column = 1, padx = 5, pady = 7, sticky = tk.N)

    def ve_ban_do(self):
        for city in graph_dict:
            x0 = romania_locations[city][0]
            y0 = 640 - romania_locations[city][1]
            self.cvs_map.create_rectangle(x0-4, y0-4, x0+4, y0+4,
                                          fill = 'blue', outline = 'blue')
            dx = city_name[city][0]
            dy = city_name[city][1]
            self.cvs_map.create_text(x0+dx, y0+dy, text = city, anchor = tk.W)

            for neighbor in graph_dict[city]:
                x1 = romania_locations[neighbor][0]
                y1 = 640 - romania_locations[neighbor][1]
                self.cvs_map.create_line(x0, y0, x1, y1)

    def cbo_start_click(self, *args):
        self.start = self.cbo_start.get()
        
    def cbo_dest_click(self, *args):
        self.dest = self.cbo_dest.get()

    def btn_direction_click(self):

        self.cvs_map.delete(tk.ALL)
        self.ve_ban_do()

        romania_problem = GraphProblem(self.start, self.dest, romania_map)
        c = astar_search(romania_problem)
        lst_path = c.path()
        self.path_location = []
        for data in lst_path:
            city = data.state
            x = romania_map.locations[city][0]
            y = 640 - romania_map.locations[city][1]
            self.path_location.append((x,y))

        self.cvs_map.create_line(self.path_location, fill = 'red')

    def btn_run_click(self):
        bg_color = self.cvs_map['background']
        N = 21
        d = 100
        L = len(self.path_location)
        for i in range(0, L-1):
            x0 = self.path_location[i][0]
            y0 = self.path_location[i][1]
            x1 = self.path_location[i+1][0]
            y1 = self.path_location[i+1][1]
            b = y1-y0
            a = x1-x0

            d1 = np.sqrt((x1-x0)**2 + (y1-y0)**2)
            N1 = int(N*d1/d)
            dt = 1.0/(N1-1)
            for j in range(0,N1):
                t = j*dt
                x = x0 + (x1-x0)*t
                y = y0 + (y1-y0)*t
                
                self.cvs_map.delete(tk.ALL)
                self.ve_ban_do()
                self.cvs_map.create_line(self.path_location, fill = 'red')

                self.ve_mui_ten(b,a,x,y,'#FF0000')
                
                self.cvs_map.update()
                time.sleep(0.05)
                self.ve_mui_ten(b,a,x,y,bg_color)
                
        self.ve_mui_ten(b,a,x,y,'#FF0000')

    def ve_mui_ten(self, b, a, tx, ty, color):
        p_mui_ten = [(0,0,1), (-20,10,1), (-15,0,1), (-20,-10,1)]
        p_mui_ten_ma_tran = [np.array([[0],[0],[1]],np.float32),
                             np.array([[-20],[10],[1]],np.float32),
                             np.array([[-15],[0],[1]],np.float32),
                             np.array([[-20],[-10],[1]],np.float32)]

        # Tạo ma trận dời (tịnh tiến) - translate
        M1 = np.array([[1, 0, tx], 
                       [0, 1, ty], 
                       [0, 0, 1]], np.float32)

        # Tạo ma trận quay - rotation
        theta = np.arctan2(b, a)
        M2 = np.array([[np.cos(theta), -np.sin(theta), 0],
                       [np.sin(theta),  np.cos(theta), 0],
                       [     0,             0,        1]], np.float32)

        M = np.matmul(M1, M2)

        q_mui_ten = []
        for p in p_mui_ten_ma_tran:
            q = np.matmul(M, p)
            q_mui_ten.append((q[0,0], q[1,0]))

        self.cvs_map.create_polygon(q_mui_ten, fill = color, outline = color)
        
        

if __name__ == "__main__":
    app	=	App()
    app.mainloop()
