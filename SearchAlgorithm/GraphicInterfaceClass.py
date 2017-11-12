from tkinter import *
from tkinter import filedialog

from DFSClass import *
from BFSClass import *
from UniformCostSearch import *
from AstarClass import *
from LoadGraphFile import *
from WeightedGraph import *


class Application(Frame):
    def __init__(self, master):
        # initialize the frame
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

        # boolean variable to label whether the input file exists
        self.fileExist = False

        # parameter to store the graph info from text file
        self.graph = Graph()

        self.start = ""
        self.goal = ""

        # path result to write in a file
        self.result = ""

    def create_widgets(self):
        menubar = Menu(self)

        #file menu
        filemenu = Menu(menubar, tearoff = 0)
        filemenu.add_command(label = "Load File", command = self.load_file)
        filemenu.add_command(label = "Save Result", command = self.save_result)
        menubar.add_cascade(label = "File", menu = filemenu)

        #uninformed menu
        uninformed_menu = Menu(menubar, tearoff = 0)
        uninformed_menu.add_command(label = "Breadth-First Search",\
            command = self.bfs)
        uninformed_menu.add_command(label = "Depth-First Search",\
            command = self.dfs)
        uninformed_menu.add_command(label = "Uniform Cost Search",\
            command = self.ucs)
        menubar.add_cascade(label = "Uninformed Search", menu = uninformed_menu)

        #informed menu
        informed_menu = Menu(menubar, tearoff = 0)
        informed_menu.add_command(label = "A* Search",\
            command = self.astar)
        menubar.add_cascade(label = "Informed Search", menu = informed_menu)

        menubar.add_command(label = 'Exit', command = exit)

        self.master.config( menu = menubar)

        self.resultText = Text(self, width = 200, height = 100, wrap = WORD)
        self.resultText.grid(row = 0, column = 0, sticky = W)

    def load_file(self):
        inputFileName = filedialog.askopenfile \
        (initialdir = "/Users/Rivin/Desktop",
         title = "Select File", 
         filetype = (("text files", "*.txt"),("all files", ".*")))

        inputFileName = str(inputFileName.name)
        parseFile = ParseFile(inputFileName)
        self.fileExist = parseFile.checkFile()            

        if self.fileExist:
            parseFile.parse()
            loadGraph = LoadGraph(parseFile.pathList, parseFile.nodeList)
            loadGraph.createGraph()
            self.graph = loadGraph.graph
            self.start = parseFile.start
            self.goal = parseFile.goal

            self.resultText.delete(0.0, END)
            self.resultText.insert(0.0, "File Loaded Successfully")
        else:
            self.resultText.delete(0.0, END)
            self.resultText.insert(0.0, "Failed to Load File")

    def save_result(self):
        outputFileName = filedialog.asksaveasfilename \
            (initialdir = "/Users/Rivin/Desktop",
             title = "Select File", 
             filetype = (("text files", "*.txt"),("all files", ".*")))

        with open(outputFileName, mode = 'w') as outputFile:
            outputFile.write(self.result)

        self.resultText.insert(END, "\nFile Saved Successfully")

    def bfs(self):
        if self.graph.nodes: 
            search = BFSclass(self.graph)
            self.result = search.bfs_shortest_path(self.start, self.goal)
            self.show_result()

    def dfs(self):
        if self.graph.nodes:
            search = DFSclass(self.graph)
            self.result = search.dfs_first_path(self.start, self.goal)
            self.show_result()

    def ucs(self):
        if self.graph.nodes:
            search = UCSclass(self.graph)
            self.result = search.uniform_cost_search(self.start, self.goal)
            self.show_result()

    def astar(self):
        if self.graph.nodes:
            search = AstarClass(self.graph)
            self.result = search.A_star_search(self.start, self.goal)
            self.show_result()

    def show_result(self):
        self.resultText.delete(0.0, END)
        self.resultText.insert(0.0, self.result)

    def exit(self):
         exit()



root = Tk()
root.title("Search Algorithm")
root.geometry("300x300")

app = Application(root)
app.pack()

root.mainloop()