###########################################################################
######################## PREPROCESSING ####################################
###########################################################################
import pandas as pd
header = ["flag", "permission", "permission_group"]
mp = pd.read_csv("manifestpermissions.txt", names=header, delimiter=r"\s+")
groupLabels = mp["permission_group"].value_counts().index.tolist()
groupLabelCounts = list(mp["permission_group"].value_counts())
flagLabels = mp["flag"].value_counts().index.tolist()
flagLabelCounts = list(mp["flag"].value_counts())

###########################################################################
######################## PLOT PERMISSION GROUPS ###########################
###########################################################################
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.font_manager import FontProperties
from matplotlib import cm
import matplotlib.colors

fontP = FontProperties()
fontP.set_size('xx-small')

y = groupLabelCounts
mylabels = groupLabels

colors = list(matplotlib.colors.cnames.keys())[10:]
myexplode = [0.2, 0, 0, 0,0,0,0,0,0,0,0]
plt.figure(dpi=250)

plt.pie(y, labels = None, 
        colors=outer_colors,
        explode=myexplode, 
        shadow=False)


plt.legend(mylabels, title='Permission Groups', bbox_to_anchor=(1, 1), loc='upper left', prop=fontP)
plt.savefig("permission_groups.svg", format="svg", bbox_inches = "tight")
plt.show() 

###########################################################################
######################## PLOT PERMISSION FLAGS ############################
###########################################################################
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.font_manager import FontProperties
from matplotlib import cm
import matplotlib.colors

fontP = FontProperties()
fontP.set_size('xx-small')

y = flagLabelCounts
mylabels = flagLabels
colors = list(matplotlib.colors.cnames.keys())[10:]

myexplode = [0,0,0.2, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
plt.figure(figsize=(4, 6),dpi=250)

plt.pie(y, labels = None, 
        colors=colors,
        explode=myexplode, 
        shadow=False)


plt.legend(mylabels, title='Permission Flags', bbox_to_anchor=(1, 1), loc='upper left', prop=fontP)
plt.savefig("permission_flags.svg", format="svg", bbox_inches='tight')
plt.show()  

