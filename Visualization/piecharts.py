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

a,b,c,d,e,f,g,h,i = [plt.cm.winter, plt.cm.cool, plt.cm.spring, plt.cm.copper, plt.cm.bone, 
                     plt.cm.gist_heat, plt.cm.pink, plt.cm.summer, plt.cm.autumn]
colors = [a(.9), b(.9), c(.9), d(.9), e(.9), f(.9), g(.9), h(.9), i(.9),
                a(.3), b(.3), c(.3), d(.3), e(.3), f(.3), g(.3), h(.3), i(.3), 
               a(.6), b(.6), c(.6), d(.6), e(.6), f(.6), g(.6), h(.6), i(.6)]
colors = list(matplotlib.colors.cnames.keys())[10:]
myexplode = [0.2, 0, 0, 0,0,0,0,0,0,0,0]
plt.figure(dpi=250)

plt.pie(y, labels = None, 
        colors=outer_colors,
        explode=myexplode, 
        shadow=False)

plt.legend(mylabels, title='Permission Groups', bbox_to_anchor=(1, 1), loc='upper left', prop=fontP)
plt.savefig("permission_groups.svg")
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
plt.figure(dpi=250)

plt.pie(y, labels = None, 
        colors=colors,
        explode=myexplode, 
        shadow=False)


plt.legend(mylabels, title='Permission Flags', bbox_to_anchor=(1, 1), loc='upper left', prop=fontP)
#plt.legend(mylabels, title='Permission Flags', bbox_to_anchor=(1, 1), loc='upper left')

plt.savefig("permission_flags.svg")
plt.show() 

