#!/usr/bin/env python
# coding: utf-8

# BFS->Breadth first search
# DFS->Depth first search

# BREADTH FIRST SEARCH:-

# In[40]:


graph={
    'start':['A','B'],
    'A':['start','E','F'],
    'B':['start','D','C'], 
    'C':['B'],
    'D':['B','Goal'],
    'E':['B','G'],
    'F':['B'],
    'G':['E'],
    'Goal':['E','F']
}


# In[41]:


graph


# QUEUE OPERATIONS:-
# 1.Enqueue
# 2.Dequeue
# 3.size
# 4.Front
# 5.Rear

# ## from collections import deque

# In[32]:


Q=deque(["a","b","c","d","e"])


# In[33]:


Q.appendleft("0")


# In[34]:


Q


# In[35]:


Q.append("f")


# In[36]:


Q


# In[37]:


Q.popleft()


# In[42]:


from collections import deque
def bfs(graph,start,Goal):
    visited=[]
    queue=deque([start])
    while queue:
        node=queue.popleft()
        if node not in visited:
            visited.append(node)
            print("I have visited:",node)
            neighbours=graph[node]
            if node==Goal:
                return("I have reached my goal,this is my traversal")
            for neighbour in neighbours:
                queue.append(neighbour)
                


# In[43]:


bfs(graph,"start","Goal")


# In[ ]:





# In[ ]:




