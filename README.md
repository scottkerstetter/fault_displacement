# fault_displacement
Calculate net slip of fault given inputs of fault strike, dip, vertical displacement (throw) and transport direction.  

author: S Kerstetter  
created: 2021-12-20  

Calculates displacement for a fault.  
Required data:  
- id
- strike azimuth (degrees)
- dip (degrees)
- vertical displacement (throw, any units)
- transport direction azimuth (degrees)

References:  
http://www.structuralgeology.org/2012/05/how-calculate-apparent-dip-real-dip.html  
https://app.visiblegeology.com/apparentDip.html  
Biholar, A., 2015 (THESIS)  


### Future modules and features  
- blenderMod
- calcStrikeDipFromXYs
- 3D plot feature in matplotlib
- 2D map of rectilinearized faults
