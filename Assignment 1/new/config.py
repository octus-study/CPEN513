import collections
import numpy as np
WIDTH = 1500
HEIGHT = 750


#colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (190, 190, 190) # GREY_WHITE
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165 ,0)
GREY = (61, 61, 61)
TURQUOISE = (64, 224, 208)

# some info about wires
# use those only after assigning them value in app

#type of cells in grid: # default is one
T_SOURCE = 0
T_SINK = -1
T_SINK_ROUTED = -10 # SINK ROUTED 
T_UNVIS = -2
T_OBS = -3 # obstacle
T_PATH = -4
# T_SOURCE_ROUTED = -10 # SINK ROUTED 

# color
COLOR_OBS = BLACK
COLOR_UNVIS = np.array([1, 1, 1])
COLOR_VIS = np.array([0, 0.5, 1])
COLOR_PATH = np.array([1, 1, 0])


NUM_X = 0
NUM_Y = 0
NUM_WIRE = 0
NUM_OBS = 0
SIZE_X = 0
SIZE_Y = 0
GRID = []
COLOR_GRID = []

OBS = set()
SOURCES = set()
SINKS = set()
WIRE2SOURCE = {}
WIRE2NUM_PINS = {}
WIRE2SINK = collections.defaultdict(list)
SOURCE2SINKS = collections.defaultdict(list)
PIN2WIRE = {} # key: coor of pin, value: (isSource, wireNumber) isSource0: source, 1 sink

WIRE2PATH = {} # paths or wires for current wire