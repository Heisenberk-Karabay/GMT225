import math
import numpy as np

#this function converts degrees to radians 
def degree_to_Rad(degree_angle):
    radian_angle = (degree_angle*math.pi)/180

    return round(radian_angle,2)

#this two functions returns the sine and cosine value by using the degree_to_Rad function
def cos(Angle):
    return round(math.cos(degree_to_Rad(Angle)),4)
def sin(Angle):
    return round(math.sin(degree_to_Rad(Angle)),4)

#with that function we determine the rotation matrix by looking up to its axis and angle and we retrun that matrix
def determine_rotation_matrices(angle , axis):
  # this means we are working with the x axis
  if axis == 1:
    rotation_matrices = np.array([[1 , 0 , 0], [0 , cos(angle) ,sin(angle)],[0 , -sin(angle),cos(angle)]])

    return rotation_matrices

  # this means we are working with the y axis
  elif axis == 2:
    rotation_matrices = np.array([[cos(angle),0,-sin(angle)], [0,1,0], [sin(angle),0, cos(angle)]])

    return rotation_matrices

  # this means we are working with the z axis
  elif axis == 3:
    rotation_matrices = np.array([[cos(angle),sin(angle),0], [-sin(angle),cos(angle),0], [0,0,1]])

    return rotation_matrices

# this is the main function we are using np.dot to do the matrix multipication 
def rotation(vector,angle,axis):
  if vector.shape == (3,) :
    vector = np.transpose(vector)
    rotation_matrix = determine_rotation_matrices(angle,axis)
    print(np.dot(vector,rotation_matrix))
    return (np.dot(vector,rotation_matrix))

  else:
     rotation_matrix = determine_rotation_matrices(angle,axis)
     print(np.dot(vector,rotation_matrix))
     return (np.dot(vector,rotation_matrix))

#this is the inital position vector from the assingment paper
vector = np.array([100 , 120 , 200])

#this is the position vector after rotation around x axis
aft_x_rot = rotation(vector,-20,1)

#this is the position vector after rotation around y axis
aft_y_rot = rotation(aft_x_rot,25,2)

#this is the position vector after rotation around z axis
aft_z_rot = rotation(aft_y_rot,7,3)

