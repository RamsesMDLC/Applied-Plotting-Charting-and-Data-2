# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 22:26:22 2022

@author: USUARIO
"""
#MODULE 3: CHARTING FUNDAMENTALS

#SUBPLOTS (Topic #1)

#Topic 1.1

#Matplotlib is strongly object oriented and its principal objects are the...
#..."figure" and the "axes".
    #Axes: is a sort of Swiss Army knife, a handy object that..
    #...offers a tool (e.g. .plot, .scatter, .hist, etc) for everything,...
    #...mostly. You can place one, two, ... many "axes" inside a "figure"...
    #...using one of many different methods. In essence, it is an object.
    #Subplot: It is a method.
    
#The "plt" interface:
    #It is not really different from the "object oriented interface", even...
    #...if we don't make a direct reference to the main objects...
    #...(i.e., a "figure" and an "axes") these objects are automatically..
    #...instantiated and each "plt" method is, essentially, translated to...
    #...call of one of the methods of the underlying fundamental objects.
    
    #For instance:    
        ax = plt.subplot()
        ax.plot(x, y)
    #Here we use a convenience method (called "subplot") in the "plt"...
    #...namespace to give a...
    #...name (and a handle) to the "axes" object, but there is also an...
    #...hidden "figure". We can later use the "axes" object to plot, to...
    #...make an histogram etc, all things that you can do with the "plt"...
    #...interface, but you can also access all its attributes and modify..
    #...them with greater freedom.

#Subplot
    #Add an Axes to the current "figure" or retrieve an existing "Axes"...
    #...It is important to say:
    #Option 1: An "axes" (ax) is a single element added or retrieved...
    #...in a "figure" (the entire "figure") by the code "subplot". 
    #Option 2: An "axes" (ax) is a single element added or retrieved...
    #...in a "figure" (just a cell of the "figure") by the code "subplot". 
    #Option 3: Several axes (axs) are two or more elements added or...
    #...retrieved in a "figure" (several cells of the "figure") by the...
    #...code "subplots". 
    
    #In the following syntax we are going to see how to handle the "Option 1"...
    #...and "Option 2"; therefore, the code is "matplotlib.pyplot.subplot".
    
    #Call signatures:
        #subplot(nrows, ncols, index, **kwargs)
        #subplot(pos, **kwargs)
        #subplot(**kwargs)
        #subplot(ax)
        
    #Syntax:
    #matplotlib.pyplot.subplot(*args, **kwargs)
    
    #Parameters:
        #*args: int, (int, int, index), or SubplotSpec, default: (1, 1, 1)
            #The position of the subplot described by one of:
                #1.Three integers (nrows, ncols, index): The "subplot" will...
                #...take the index position on a grid with nrows rows and...
                #...ncols columns (i.e. "nrows" and "ncols" are used to...
                #...notionally split the "figure" into "nrows * ncols"):
                    #1.1.index starts at 1 in the upper left corner and...
                    #...increases to the right. 
                    #1.2.index can also be a two-tuple specifying the...
                    #...(first, last) indices (1-based, and including last)...
                    #...of the subplot, e.g.,...
                    #..."fig.add_subplot(3, 1, (1, 2))" makes a subplot that...
                    #...spans the upper 2/3 of the figure.
                #2.A 3-digit integer: The digits are interpreted as if...
                #...given separately as three single-digit integers, i.e....
                #..."fig.add_subplot(235)" is the same as...
                #..."fig.add_subplot(2, 3, 5)". Note that this can only...
                #...be used if there are no more than 9 subplots.
        #sharex, sharey: Axes (optional)
            #Share the x or y axis with sharex and/or sharey. The axis...
            #....will have the same limits, ticks, and scale as the axis...
            #...of the shared axes.
     
    #Returns:
        #"axes.SubplotBase", or another subclass of "Axes"
            #The "axes" of the "subplot". The returned "axes" base class...
            #...depends on the projection used. The returned "axes" is then...
            #...a "subplot" subclass of the base class. <--IMPORTANT

    #Creating a new "Axes" will delete any pre-existing "Axes" that...
    #...overlaps with it beyond sharing a boundary.
        #If you do not want this behavior, use the "Figure.add_subplot"...
        #....method or the "pyplot.axes" function instead.
        
#In this instance we are going to create a "figure" and inside that "figure" a...
#...a "subplot" in a specific position of the grid.
    #First, I create and define the data
    #Second, I create a "Figure".
    #Third, I create a subplot grid of:
        #nrows = 1 
        #ncols = 2
        #index = 1 (in the current "figure" the graph it is the "1st subplot...
        #...axes"; i.e located at the first row and also first column,...
        #...recalling the notion of splitted "figure" into "nrows * ncols").
        
    #"Linear Data": 
        #Line color: "m" for magenta. 
        #marker: "o" 
        #Lines style: -
    #When we plot the "Linear Data", we are going to see that it is located...
    #...in an "axe" at the right side of the figure (which was splitted in 1...
    #...row and 2 columns).
        #It is important to remark that if this graph (in this..
        #...case a "subplot") will not be the only one in the same "figure",...
        #...then to see the others future "subplot" (in the same "figure")...
        #...and also to see how the could change or modified or affect...
        #...thee existing "subplot" we cannot close the window that show...
        #...the first "subplot" created <-- This comment apply only if we...
        #...are making a drawing in the same "figure".
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
       
linear_data = np.array([1,2,3,4,5,6,7,8])
plt.figure()
plt.subplot(1, 2, 1)
plt.plot(linear_data, '-mo') 
plt.show()

#Topic 1.2
#In this instance we are going to use the "figure" previously created...
#...and inside that "figure" a a "subplot" in a specific position of the grid.
    #First, I create and define the data.
    #Second, I used the "Figure" previously created.
    #Third, I create a subplot grid of:
        #nrows = 1 
        #ncols = 2
        #index = 2 (in the current "figure" the graph it is the "1st subplot...
        #...axes"; i.e located at the first row and also second column,...
        #...recalling the notion of splitted "figure" into "nrows * ncols").
        
    #"Exponential Data 1": 
        #Line color: "g" for green. 
        #marker: "o" 
        #Lines style: -
    #When we plot the "Exponential Data 1", we are going to see that it is...
    #...located in an "axe" at the left side of the figure (which was splitted...
    #...in 1 row and 2 columns). Recalling that at the right side is located...
    #...the "Linear Data" graph.
exponential_data = linear_data**2 
plt.subplot(1, 2, 2)
plt.plot(exponential_data, '-go')            
plt.show()          
            
#Topic 1.3      
#In this instance we are going to use the "figure" previously created...
#...and inside that "figure" a a "subplot" in a specific position of the grid.
    #First, I create and define the data.
    #Second, I used the "Figure" previously created.
    #Third, I create a subplot grid of:
        #nrows = 1 
        #ncols = 2
        #index = 1 (in the current "figure" the graph it is the "1st subplot...
        #...axes"; i.e located at the first row and also first column,...
        #...recalling the notion of splitted "figure" into "nrows * ncols").
        
    #"Exponential Data 2": 
        #Line color: "r" for red. 
        #marker: "x" 
        #Lines style: -
    #When we plot the "Exponential Data 2", we are going to see that it is...
    #...located in an "axe" at the right side of the figure (which was splitted...
    #...in 1 row and 2 columns). Recalling that at the right side was located...
    #...previously the "Linear Data" graph (i.e., the current "axe" of "Linear...
    #...Data" will be mixed  with the "axe" of "Exponential Data 2").
linear_data2 = np.array([9,10,11,12,13,14,15,16])
exponential_data2 = linear_data2**3 
plt.subplot(1, 2, 1)
plt.plot(exponential_data2, '-rx')          
plt.show()              

#Topic 1.4
#In this instance we are going to create a "figure" and inside that "figure" a...
#...a "subplot" in a specific position of the grid.
    #First, I create and define the data.
    #Second, I used the "Figure" previously created.
    #Third, I create a subplot grid of:
        #nrows = 1 
        #ncols = 2
        #index = 2 (in the current "figure" the graph it is the "1st subplot...
        #...axes"; i.e located at the first row and also second column,...
        #...recalling the notion of splitted "figure" into "nrows * ncols").
        
    #"Linear Data 3": 
        #Line color: "m" for magenta. 
        #marker: "o" 
        #Lines style: -
    #"Exponential Data 3": 
        #Line color: "r" for red. 
        #marker: "x" 
        #Lines style: -    
    #When we plot the "Linear Data 3", we are going to see that it is located...
    #...in an "axe" at the right side of the figure (which was splitted in 1...
    #...row and 2 columns). 
    #When we plot the "Exponential Data 3", we are going to see that it is...
    #...located in an "axe" at the left side of the figure (which was splitted...
    #...in 1 row and 2 columns). Recalling that at the right side is located...
    #...the "Linear Data 3" graph.
    
    #Both graphs will share the "y-axis" (to be specific the "y-axis" of the..
    #..."ax1") considering that the figure was splitted in 1 row and 2 columns.
        #In this case it is important to remark how the graphs may change...
        #...their shape because the effect of scale (i.e. graphs with...
        #...different scales constrasted under the same scale).
    
    #Both graphs (i.e. the subplots)  belong to the same "figure", but has..
    #:..different names:
        #ax1 = "Linear Data 3"
        #ax2 = "Exponential Data 3"
        
        #If we are working in a "figure" and left open the window that show...
        #...us the "subplot" or several "subplot", and after that we decide...
        #...to work in a new "figure" with other or others "subplot" we are...
        #...to see as a result that the graph of the new "figure" is printed..
        #...in a new independet window. <--IMPORTANT
linear_data3 = np.array([1,2,3,4,5,6,7,8])
exponential_data3 = linear_data3**3 
plt.figure()
ax1 = plt.subplot(1, 2, 1)
plt.plot(linear_data3, '-mo')
ax2 = plt.subplot(1, 2, 2, sharey=ax1)
plt.plot(exponential_data3, '-rx')
plt.show()            
            
#Topic 1.5
#In this instance we apply exactly the same code of the "Topic 1.4" we the...
#...only differences are:
    #The change in markers and color
    #The change in how we describe the parameter of "int int index"
        #In this case we do not use commas to separate "nrows ncols index"...
        #...as we did previously.
linear_data4 = np.array([1,2,3,4,5,6,7,8])
exponential_data4 = linear_data4**3 
plt.figure()
ax1 = plt.subplot(121)
plt.plot(linear_data4, '-g+')
ax2 = plt.subplot(122, sharey=ax1)
plt.plot(exponential_data4, '-c*')
plt.show()                 
            
#Topic 1.6

#Subplots
    #Option 1: An "axes" (ax) is a single element added or retrieved...
    #...in a "figure" (the entire "figure") by the code "subplot". 
    #Option 2: An "axes" (ax) is a single element added or retrieved...
    #...in a "figure" (just a cell of the "figure") by the code "subplot". 
    #Option 3: Several axes (axs) are two or more elements added or...
    #...retrieved in a "figure" (several cells of the "figure") by the...
    #...code "subplots". 
    
    #In the following syntax we are going to see how to handle the "Option 3"...
    #...therefore the code is "matplotlib.pyplot.subplots".
    
    #Syntax:
    #matplotlib.pyplot.subplots(nrows=1, ncols=1, *, sharex=False, sharey=False, squeeze=True, subplot_kw=None, gridspec_kw=None, **fig_kw)
    
    #Parameters:
        #nrows, ncols: int (default: 1)
            #Number of rows/columns of the subplot grid.
        #sharex, sharey: bool or {'none', 'all', 'row', 'col'}, default: False
            #Controls sharing of properties among x (sharex) or y (sharey)..
            #...axes:
                #True or 'all': x- or y-axis will be shared among all subplots.
                #False or 'none': each subplot x- or y-axis will be...
                #...independent.
                #'row': each subplot row will share an x- or y-axis.
                #'col': each subplot column will share an x- or y-axis.
                
                #When subplots have a shared "x-axis" along a column,...
                #...only the x tick labels of the bottom subplot are created...
                #...Similarly, when subplots have a shared "y-axis" along...
                #...a row, only the y tick labels of the first column...
                #...subplot are created.
        #gridspec_kw: dict (optional)
            #Dict with keywords passed to the "GridSpec" constructor...
            #...used to create the grid the subplots are placed on.

    #The names "ax" and pluralized "axs" are preferred over the term "axes"...
    #...because for the latter it's not clear if it refers to a single "Axes"..
    #...instance or a collection of these.

    #Returns:
        #fig: Figure
        #ax: "axes.Axes" or array of "Axes".
            #"ax" can be either a single "Axes" object or an array of...
            #..."Axes" objects if more than one subplot was created...
            #...The dimensions of the resulting array can be controlled...
            #...with the squeeze keyword, see above.

        #Typical idioms for handling the return value are:
            # using the variable "ax" for single a Axes
#fig, ax = plt.subplots()
            # using the variable "axs" for multiple Axes
#fig, axs = plt.subplots(2, 2)
            # using tuple unpacking for multiple Axes
#fig, (ax1, ax2) = plt.subplots(1, 2)
#fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
    
#In this instance we are going to create a "figure" and inside that "figure"...
#...several "subplots" (to be specific 9 "subplots") as detailed:
    #It is important to know that if we are going to use an several...
    #...subplots we can arrange them in the following patterns:
        #Single Line (i.e. several subplots in the same single row or...
        #...several subplots in the same single column).
        #Array (i.e. several subplots per row and per column).
    #Number of rows/columns of the subplot grid.
        #nrows = 3 
        #ncols = 3
    #Sharing "y" and "x" axis among all subplots
    #ax1 is "empty"
    #ax2 is "empty"
    #ax3 is "empty"
    #ax4 is "empty"
    #ax5 is "line"
    #ax6 is "empty"       
    #ax7 is "empty"
    #ax8 is "empty"
    #ax9 is "empty"    
fig, ((ax1,ax2,ax3), (ax4,ax5,ax6), (ax7,ax8,ax9)) = plt.subplots(3, 3, sharex=True, sharey=True)
ax5.plot(linear_data, "-kp")        
plt.show()                 

#Topic 1.7
#In this instance we apply exactly the same code of the "Topic 1.6" we the...
#...only differences are:
    #Turn off (hide or delete) the "xticklabels" and the "yticklabels" of...
    #...the all "axes" of the current "figure" (in this case the...
    #...9 "subplots" described previoulsy in "Topic 1.6")
for ax in plt.gcf().get_axes():
    for label in ax.get_xticklabels() + ax.get_yticklabels():
        label.set_visible(True)  

#############################################################################     

#HISTOGRAMS (Topic #2)

#Topic 2.1

#numpy.random.normal
    #Numpy code
    #Draw random samples from a "Normal (Gaussian) Distribution" (often...
    #...called the "bell curve" because of its characteristic shape.

    #Syntax:
    #random.normal(loc=0.0, scale=1.0, size=None)
    
    #Parameters:
        #loc: float or array_like of floats
            #Mean (“centre”) of the distribution.
        #scale: float or array_like of floats
            #Standard deviation (spread or “width”) of the distribution...
            #...Must be non-negative.
        #size: int or tuple of ints (optional)
            #Output shape. If the given shape is, e.g., (m, n, k), then...
            #..."m * n * k" samples are drawn. If size is None (default), a...
            #...single value is returned if "loc" and "scale" are both scalars...
            #...Otherwise, "np.broadcast(loc, scale).size" samples are drawn.
    #Returns
        #out: ndarray or scalar
            #Drawn samples from the parameterized normal distribution.

#random.random(size=None)
    #Numpy code
    #Return random floats in the half-open interval [0.0, 1.0).

#matplotlib.axes.Axes.hist
    #Plot a histogram.
        #The towers or bars of a histogram are called bins. 
            #The height of each bin shows how many values from that data..
            #...fall into that range. 
            #Width of each bin is = (max value of data – min value of data) / total number of bins 
    
    #Compute and draw the histogram of "x". 
    
    #Multiple data can be provided via "x" as a list of datasets of...
    #...potentially different length ([x0, x1, ...]), or as a 2D ndarray...
    #...in which each column is a dataset. Note that the "ndarray" form is...
    #...transposed relative to the list form.
    
    #The "bins, range, weights, and density" parameters behave as in..
    #..."numpy.histogram"

    #Syntax:
    #Axes.hist(x, bins=None, range=None, density=False, weights=None, cumulative=False, bottom=None, histtype='bar', align='mid', orientation='vertical', rwidth=None, log=False, color=None, label=None, stacked=False, *, data=None, **kwargs)
    
    #Parameters:
        #x: (n,) array or sequence of (n,) arrays.
            #Input values, this takes either a single array or a..
            #...sequence of arrays which are not required to be of the...
            #...same length.
            
        #bins: int or sequence or str, default: rcParams["hist.bins"]..
        #..(default: 10)
            #If bins is an integer, it defines the number of...
            #...equal-width bins in the range.
            #If bins is a sequence, it defines the bin edges,...
            #...including the left edge of the first bin and the right...
            #...edge of the last bin; in this case, bins may be...
            #...unequally spaced. 
            
        #range: tuple or None, default: None
            #The lower and upper range of the bins.   
        
        #density: bool, default: False
            #If True, draw and return a probability density.
            
        #weights: (n,) array-like or None, default: None
            #An array of weights, of the same shape as "x". Each value in...
            #..."x" only contributes its associated weight towards the...
            #...bin count (instead of 1). If density is True, the weights...
            #...are normalized, so that the integral of the density over...
            #...the range remains 1.   
             
        #Returns
            #n: array or list of arrays
                #The values of the histogram bins. See density and weights...
                #...for a description of the possible semantics. 
                #If input "x" is an array, then this is an array of length...
                #..."nbins". 
            #bins: array
                #The edges of the bins. 
            #patches: BarContainer or list of a single Polygon or list of...
            #...such objects   
                #Container of individual artists used to create the...
                #...histogram or list of such containers if there are...
                #...multiple input datasets.

#matplotlib.gridspec.GridSpec
    #Allow us to build a grid layout to place subplots within a "figure".
    #The location of the grid cells is determined in a similar way to..
    #..."Subplot".
    
    #"GridSpec" is a flexible way to layout subplot grids. 
    
    #Syntax:
    #class matplotlib.gridspec.GridSpec(nrows, ncols, figure=None, left=None, bottom=None, right=None, top=None, wspace=None, hspace=None, width_ratios=None, height_ratios=None)
    
    #Parameters:
        #nrows, ncols: int
            #The number of rows and columns of the grid.

#matplotlib.axes.Axes.clear
    #Allow us to clear the "Axes".
   
    #Syntax:
    #Axes.clear()

#In this instance we are going to create a "figure" and inside that "figure"...
#...several "subplots" (to be specific 4 "subplots") as detailed:
    #It is important to know that if we are going to use an several...
    #...subplots we can arrange them in the following patterns:
        #Single Line (i.e. several subplots in the same single row or...
        #...several subplots in the same single column).
        #Array (i.e. several subplots per row and per column).
    #Number of rows/columns of the subplot grid.
        #nrows = 2 
        #ncols = 2
    #ax1 is "Histogram" (made with 10 random samples from the..
    #..."normal distribution")
    #ax2 is "Histogram" (made with 100 random samples from the..
    #..."normal distribution")
    #ax3 is "Histogram" (made with 1000 random samples from the..
    #..."normal distribution")
    #ax4 is "Histogram" (made with 10000 random samples from the..
    #..."normal distribution")
    
    #Create 2x2 grid of axis subplots
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np    
    
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharex=True)
axs = [ax1,ax2,ax3,ax4]

    #Draw n = 10, 100, 1000, and 10000 samples from the "normal...
    #...distribution" and plot corresponding histograms.
    #With the "for loop" we are:
        #Step #1: Moving in a range of the 4 "subplots" created previously.
        #Establishing the sample size.
        #Establishing:
            #Mean = 0
            #Standard Deviation = 1
            #Size: The quantity of samples that we want to output.
                #It is the size or quantity of data (random values) that..
                #...we are going to use to plot our graph.
        #Plot the histograms and put the title of every histogram.
            #Where the input of the histogram x="(n,) array" is x="(sample)"
            #As default we are using 10 bins in each graph; therefore, we..
            #..are going to see.
                #ax1 is "Histogram" (made with 10 random samples...
                #...distributed in a graph of 10 bins)
                #ax1 is "Histogram" (made with 100 random samples...
                #...distributed in a graph of 10 bins)
                #ax1 is "Histogram" (made with 1000 random samples...
                #...distributed in a graph of 10 bins)
                #ax1 is "Histogram" (made with 10000 random samples...
                #...distributed in a graph of 10 bins)   
for n in range(0,len(axs)):
    sample_size = 10**(n+1)
    sample = np.random.normal(loc=0.0, scale=1.0, size=sample_size)
    axs[n].hist(sample)
    axs[n].set_title('n={}'.format(sample_size))
    plt.show()  


#Topic 2.2
#In this instance we apply exactly the same code of the "Topic 2.1" where the...
#...only difference is:
    #We set the number of "bins" set to 100 in every histogram; therefore, we...
    #...are going to see slims "bins" (i.e. "bins" with a very small width or...
    #...in other words we are going to see more "bins" per graph [100]...
    #...considering that default value of bins is [10]; precisely the value..
    #...used to build the histogram of the Topic 1). Moreover, it is...
    #...important to recall that "Width of each bin"is =...
    #...(max value of data – min value of data) / total number of bins).
    
    #As default we are using 10 bins in each graph; therefore, we..
    #..are going to see.
        #ax1 is "Histogram" (made with 10 random samples...
        #...distributed in a graph of 100 bins)
        #ax1 is "Histogram" (made with 100 random samples...
        #...distributed in a graph of 100 bins)
        #ax1 is "Histogram" (made with 1000 random samples...
        #...distributed in a graph of 100 bins)
        #ax1 is "Histogram" (made with 10000 random samples...
        #...distributed in a graph of 100 bins)   
fig, ((ax5, ax6), (ax7, ax8)) = plt.subplots(2, 2, sharex=True)
axs = [ax5,ax6,ax7,ax8]

for n2 in range(0,len(axs)):
    sample_size2 = 10**(n2+1)
    sample2 = np.random.normal(loc=0.0, scale=1.0, size=sample_size2)
    axs[n2].hist(sample2, bins=100)
    axs[n2].set_title('n={}'.format(sample_size2))
    plt.show()  
    
#Topic 2.3
#In this instance graph a scatterplot. Where:
    #"y" values: random values from a Gaussian Distribution with:
        #Mean = 0
        #Standard Deviation = 1
        #Size: 10000
            #It is the size or quantity of data (random values) that..
            #...we are going to use to plot our graph.
    #"x" values: It is the size or quantity of data (random values) that..
    #...we are going to use to plot our graph. Those values (in this case...
    #...10000 values) are random floats in the half-open interval [0.0, 1.0).
plt.figure()
Y = np.random.normal(loc=0.0, scale=1.0, size=10000)
X = np.random.random(size=10000)
plt.scatter(X,Y)
plt.show() 

#Topic 2.4
#In this instance we graph  a "subplot grid" in the same "figure", where...
#...the location of every "subplot" in the grid is established using...
#...the code "gridspec" (i.e. to partition the "figure" into several...
#..."subplot").
    #It is important to remark that we are not doing a graph, just we...
    #...are creating a "subplot grid" in the same "figure".
                         
    #The parameters to build the grid in this case are:
        #number of rows of the grid: 3
        #number of columns of the grid: 3
        #In this case and based in the code of the "range of action" in..
        #...the grid of every "subplot" we have:
            #An "axes" spanning all columns except the column "0" for the...
            #...row "0"--> [0, 1:]
            #An "axes" spanning all rows except the row "0" for the...
            #...column "0"--> [0, 1:]
            #An "axes" spanning all columns except the column "0" for the...
            #...all rows except the row "0" --> [0, 1:]
import matplotlib.gridspec as gridspec

plt.figure()
gspec = gridspec.GridSpec(3, 3)

top_histogram = plt.subplot(gspec[0, 1:])
side_histogram = plt.subplot(gspec[1:, 0])
lower_right = plt.subplot(gspec[1:, 1:])
plt.show() 

#Topic 2.5
#In this instance we are going to plot some graphs inside every component...
#...of the "subplot grid" created in the instance of the "Topic 2.4" (i.e...
#...we are filling the same "figure" created in the instance of the...
#..."Topic 2.4" )
    #We need to be careful to choose the "name of the components" of the grid...
    #...that we want of fill with the subplot. In this case the names are:
        #lower_right (filled with a scatterplot)
        #top_histogram (filled with a histogram)
        #side_histogram (filled with a histogram with "horizontal" orientation).
Y = np.random.normal(loc=0.0, scale=1.0, size=10000)
X = np.random.random(size=10000)
lower_right.scatter(X, Y)
top_histogram.hist(X, bins=100)
s = side_histogram.hist(Y, bins=100, orientation='horizontal')
plt.show() 

#Topic 2.6
#In this instance we are going to "clear" some "Axes" and then plot some...
#...new graphs (several axes) inside every component (subplot) previously..
#...cleared...
#...of the "subplot grid" created in the instance of the "Topic 2.4" (i.e...
#...we are filling the same "figure" created in the instance of the...
#..."Topic 2.4" )
    #We need to be careful to choose the "name of the components" of the grid...
    #...that we want of fill with the subplot. In this case the names are:
        #lower_right (filled with a scatterplot)
        #top_histogram (filled with a histogram)
        #side_histogram (filled with a histogram)
# clear the histograms and plot normed histograms
top_histogram.clear()
top_histogram.hist(X, bins=100, normed=True)
side_histogram.clear()
side_histogram.hist(Y, bins=100, orientation='horizontal', normed=True)
# flip the side histogram's x axis
side_histogram.invert_xaxis()

#8 (rmdlc)
# change axes limits
for ax in [top_histogram, lower_right]:
    ax.set_xlim(0, 1)
for ax in [side_histogram, lower_right]:
    ax.set_ylim(-5, 5)

#Python Class vs Python Module?











































            
            
            
            
            