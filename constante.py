import Math.interpolation as inter

PRECISION = 5
FENETRE_NAME = "GraphWar"

X_MIN = -25
X_MAX = 25
Y_MIN = -15
Y_MAX = 15

DEFAULT_LEFT_SPACE = 17
DEFAULT_RIGHT_SPACE = 17
DEFAULT_TOP_SPACE = 45
DEFAULT_BOTTOM_SPACE = 135

ALGO_INTERPOL = [inter.Lagrange,inter.chute,inter.pic]

NB_ALGO_INTERPOL = len(ALGO_INTERPOL)

coordList = []
window = []