#!python

import numpy as np

class time_convert:
    """
    The class is for general time conversion 
    ex: year in decimal to year, month, day,....
    

    1) year2year_mon : 
       input time array need to be representing month as 
           1/24.+1./12.*np.arange(12.)
       below decimal point, and above decimal point representing 
       year. 
       output year, month, string (year-month)

        
    Class's package dependency
    1. numpy


    update history
    7/20/18 - create the class time_convert and year2year_mon

    """
    
    def __init__(self,time_array) :
        """
        Parameters:
            time: numpy array, 
                representing the time series xaxis value     
        Attributes:
            self.origin_fmt: numpy array, 
                numpy array, store the original xaxis value for future reference
        """
        self.origin_fmt=time_array
        return

    def year2year_mon(self):
        """
        Input time array in the class attribute is used 
        The time array need to be in the form of xxxx.ooooooooo  
        where xxxx = year and oooooo= any element in 1/24.+1./12.*np.arange(12.)
       
        Output year, month, string (year-month)      
        The method output variable in the form of dictionary of all three variables

        Returns: a dictionary
            year : numpy array 
                contain the year value for all element in the xaxis array 
            month : numpy array
                contain the month value for all element in the xaxis array 
            string : list of string
                contain the "year-month" string for all element in the xaxis array 

        """
        yeardate=self.origin_fmt
        mon=yeardate-np.floor(yeardate)
        year=yeardate-mon
        mon1year=1/24.+1./12.*np.arange(12.)
        month=[]
        year_month_str=[]
        i=0
        for m in mon:
            mon_ind=np.where(np.abs(mon1year-m)<1E-8)[0]
            month.append(mon_ind+1)
            year_month_str.append("%0.4i-%0.2i"%(year[i],month[i]))
            i+=1

        return {'year':year,'month': month, 'string':year_month_str}