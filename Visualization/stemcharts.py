###########################################################################
######################## PREPROCESSING ####################################
###########################################################################
import pandas as pd
header = ["flag", "permission", "permission_group"]
mp = pd.read_csv("manifestpermissions.txt", names=header, delimiter=r"\s+") #it is `names`. not `header`

groupLabels = mp["permission_group"].value_counts().index.tolist()
groupLabelCounts = list(mp["permission_group"].value_counts())
groupLabelPers = [100*i/sum(groupLabelCounts) for i in groupLabelCounts]

flagLabels = mp["flag"].value_counts().index.tolist()
flagLabelCounts = list(mp["flag"].value_counts())
flagLabelPers = [100*i/sum(flagLabelCounts) for i in flagLabelCounts]

###########################################################################
######################## PLOT PERMISSION FLAGS ###########################
###########################################################################
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(7, 5),dpi=200)
for index in range(len(flagLabels)):
  ax.text(flagLabelPers[index]+0.75, flagLabels[index], float(f'{flagLabelPers[index]:.2f}'), size=8, color="0")
plt.stem(flagLabels, flagLabelPers,orientation='horizontal')

#fig.autofmt_xdate() # italic x-axis text
plt.savefig("permission_flags.svg", format="svg", bbox_inches='tight')
plt.show() 

###########################################################################
######################## PLOT PERMISSION GROUPS ############################
###########################################################################
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(7, 5),dpi=200)
for index in range(len(groupLabels)):
  ax.text(groupLabelPers[index]+0.75, groupLabels[index], float(f'{groupLabelPers[index]:.2f}'), size=8, color="0")
plt.stem(groupLabels, groupLabelPers,orientation='horizontal')
plt.savefig("permission_groups.svg", format="svg", bbox_inches='tight')  

