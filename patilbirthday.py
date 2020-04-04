#!/usr/bin/env python
# coding: utf-8

# In[49]:


import os
videolist = os.listdir('Videos')


# In[50]:


videolist = ['intro.mp4','neelamgunmala.mp4','jeetbhaipatel.mp4', 'arun.mp4', 'suvil.mp4', 'ankita.mp4','ramanintro.mp4', 'laddoo.mp4']


# In[51]:


imagelist = [ 'patil.jpg', 'neelam.jpg', 'jeet.jpg', 'baboon.png','baboon.png','ankita.jpg',  'baboon.png','laddoo.jpg']


# In[52]:


from IPython.display import HTML, display
for img, vid in zip(imagelist, videolist):
    display(HTML("""<table><tr><td><img src='Images/{}'  width="400"></td><td><video alt="test"  height="400" controls><source src="Videos/{}" type="video/mp4"></video></td></tr></table>""".format(img, vid)))


# In[ ]:




