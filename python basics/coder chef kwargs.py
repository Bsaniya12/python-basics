# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 10:53:30 2024

@author: ADMIN
"""

def student_info(**kwargs):              
  for key,value in kwargs.items():
    print(key+":"+value)
student_info(name="saniya",age="19",clg="BITM")