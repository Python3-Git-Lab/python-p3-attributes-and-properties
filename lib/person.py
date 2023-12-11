#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self,name, job):
        self.name= name.title()
        self.job= job
    
    #name getter
    def get_name(self):
        return self._name
    
    #job getter
    def get_job(self):
        return self._job
    
    #job setter
    def set_job(self, job):
        if (job in APPROVED_JOBS):
            print(f"The job is: {job}")
            self._job= job
        else:
            print("Job must be in list of approved jobs.")
    
    #name setter
    def set_name(self, name):
        if (isinstance(name, str) and (0 <= len(name)<=25 )):
            print(f"Name is: {name}")
            self._name = name.title()
        else:
            print("Name must be string between 1 and 25 characters.")

    #name property
    name = property(get_name, set_name)

    #job property
    job= property(get_job, set_job)

kelv= Person("david", "Marketing")
            
