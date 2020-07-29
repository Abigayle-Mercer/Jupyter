Chapter 4: Discussion and Conclusions
======================================  
  
1.) What is the true number of infections in the U.S.?  

I have learned two main ways to estimate the true number of infections. One uses the reported death count and estimated death rate, and the other applies an estimate for the detection rate to the number of confirmed cases. In my own opinion, reported deaths appear to be a more accurate statistic than confirmed cases to derive an infection estimate from. With limited testing kits and such a large percentage of asymptomatic cases, the number of confirmed cases is inherently an inaccurate statistic. Especially in counties with low levels of resources, wide spread COVID 19 testing is diffcult and thus varies greatly from county to county.   
On the other hand, the greatest source of uncertainty in the death-count / death-rate method is the wide percentage range within the estimated death rate of COVID 19. While 0.1% - 1% may sound like a inconsequential difference, these values vary by a factor of 10, which results in vastly different predictions. At this point, with the available knowledge, determining which end of the death rate spectrum is more accurate is a near impossible task. The best range I can provide, as of July, is a true infection count that could fall anywhere between 10 million and 100 million infections nationwide.   
  
2.) What are the number of infections over days for    
       a. LA     
       b. Cook    
       c. NYC    
       d. Maricopa      
       e. Miami-Dade    
       f. My home county (Lane County)   
       
I calculated an estimate for the numbner of infections in each county using both methods of calculation (death rate and detection rate applied to death count and confirmed cases).
  
3.) Are we flattening the curve?    

To determine if the U.S. is 'flattening the curve', one must first define what exactly that means. Prior to this internship, I, like many other uninformed citizens, thought a flattened curve was a graph who's trajectory turned over, like the logarithmic function in chapter 3.6. Imagine, however, that the point at which a viral infection graph turned over, was when it reached the total population count. By my old definition of flattening the curve, this plot would be flattened just as hoped. Unfortunately, in the case of this hypothetical virus, it would be too late to save anyone who is susceptible. Clearly, this is not the flattening of the curve you hear about on your local news source.  

Flattening the curve actually has to do with the number I calculated using the curvefit models back in chapter 3.5: the maximum potential number of infections. For example, if a county initiates lock down protocol, and their maximum possible number of infections decreases from 300,000 to 250,000 because of this, they would have flattened the curve. The maximum potential number of infections is the value on the x axis where a function completely turns over. Or in a standard logistic function, such as f(x) = *L*/(1+Ae^bx), the maximum potential number of infections is *L*. 

Using curvefit, I had a crude estimate for where the total possible number of infections may reach for a given county. The only way to determine if that county has flattened the curve, however, is if the original potential number of infections is a known quantity. In epidemiology, it's understood that most virus's don't infect the entire population, due to herd immunity. Exactly how many, or what *ratio* of the population will be infected, is extremely difficult to predict, especially in situation where very little is known about the virus. Without the original potential number of infections for comparison, it is impossible me to determine if we are 'flattening the curve' with the tools and information available to me. 