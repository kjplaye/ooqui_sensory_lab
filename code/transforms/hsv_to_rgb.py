# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25
@author: watsisname
"""

import numpy as np
from matplotlib import pyplot as plt
plt.style.use('dark_background')

#define a list of wavelengths for our model
wavelength_list = np.arange(360,800,1)        

"This section defines our model of HSV hue angle vs. wavelength. For this example, this is a simple cosine curve with range 0 to 360 deg."
hue_model = np.zeros(len(wavelength_list))       
for i in range(0,len(wavelength_list)):
    hue_model[i] = 360*(np.cos((wavelength_list[i]-400)/100)/2 + 0.5)

"This block converts the HSV hue angles (h) to RGB triplet values. We're assuming full saturation and brightness. For the general case, google search 'HSV to RGB conversion' for formulas."
color_list2 = []
for i in range(0,len(hue_model)):
    h = hue_model[i]/60     #renormalized hue angle
    X = 1 - abs(h%2 - 1)    
    if 0 <= h < 1:
        color_list2.append([1,X,0])
    elif 1 <= h < 2:
        color_list2.append([X,1,0])
    elif 2 <= h < 3:
        color_list2.append([0,1,X])
    elif 3 <= h < 4:
        color_list2.append([0,X,1])
    elif 4 <= h < 5:
         color_list2.append([X,0,1]) 
    elif 5 <= h < 6:
         color_list2.append([1,0,X])
    else:
        color_list2.append([0,0,0])

"Generate a figure"
fig3, ax3 = plt.subplots(1,1)
fig3.suptitle('HSV hue vs. wavelength',size=20)
ax3.set_title("hue matches to various lasers and fitting curve",size=11)
ax3.plot(wavelength_list, hue_model, '--',c='white',linewidth=1)  #plot the curve of our model fit of hue to wavelength
ax3.scatter(wavelength_list, hue_model, c=color_list2, s=6**2)    #plot dots along the curve, colored according to the model

ax3.grid('both',linestyle='--',linewidth=0.5)   
ax3.set_xlim(380,720)
ax3.set_ylim(0,360)
ax3.set_xlabel('wavelength  [nm]')
ax3.set_ylabel('HSV hue angle [deg]')

fig3.set_figheight(8)    #Set the figure size
fig3.set_figwidth(12)
fig3.set_dpi(240)        #Set the figure resolution (dots per inch)
