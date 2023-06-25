# File: FITNESS.py 

# imports 
import math
from random import randint
import pandas as pd 

# fitness center class
class FitnessCenter:
  def __init__(self):
    self.programs = [] # list to store program 
    self.trainers = [] # list to store trainers 
    
  # method to add a program
  def add_program(self, program):
    self.programs.append(program)
  
  # method to add a trainer
  def add_trainer(self, trainer):
    self.trainers.append(trainer)
    
  # method to assign a trainer to a program 
  def assign_trainer(self, program, trainer):
    if program in self.programs and trainer in self.trainers:
      program.add_trainer(trainer)
    
  # method to calculate BMI 
  def calculate_bmi(self, height, weight):
    return weight / math.pow(height, 2)

  # method to generate recommended program 
  def generate_program(self, goals):
    program_index = randint(0, len(self.programs) - 1)
    program = self.programs[program_index]
    if goals in program.goals:
      return program
    else:
      return 'No suitable program found.'

  # method to generate recommended trainer 
  def generate_trainer(self, experience):
    trainers = []
    for trainer in self.trainers:
      if trainer.experience == experience:
        trainers.append(trainer)
    # if no trainer is found, return None
    if len(trainers) == 0:
      return None
    #else, randomly select a matching trainer  
    else:
      trainer_index = randint(0, len(trainers) - 1)
      return trainers[trainer_index]

  # method to generate dataframe of trainers 
  def get_trainers_dataframe(self):
    trainers = []
    for trainer in self.trainers:
      trainers.append([trainer.name, trainer.experience, trainer.certificate])
    # create dataframe and return 
    df = pd.DataFrame(trainers, columns=['Name', 'Experience', 'Certificate'])
    return df
  
  
# program class 
class Program:
  def __init__(self, name, goals):
    self.name = name
    self.goals = goals # list of goals 
    self.trainers = [] # list of trainers assigned 
    
  # method to add trainer 
  def add_trainer(self, trainer):
    self.trainers.append(trainer)
  
  
# trainer class 
class Trainer:
  def __init__(self, name, experience, certificate):
    self.name = name
    self.experience = experience 
    self.certificate = certificate