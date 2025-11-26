# Sorting Robot with a Twist
## Project Checklist
### Core Tasks
- [x] Create all the necessary classes and methods to create reusable code.
- [x] Create an algorithm to identify and sort objects (e.g., colored cubes) into designated bins based on their color.
- [x] Use the Panda robot manipulator and assume the color of the objects is known.
### For Each Detected Object:
- [x] Compute the picking position (pick) and the placing position (place) based on the object’s color.
- [x] Use inverse kinematics to obtain the robot configurations (q_pick and q_place).

### Control Strategies
- [ ] Implement joint-space trajectory interpolation: move from pick to place positions using interpolated joint trajectories between q_pick and q_place.
- [x] Implement resolved-rate motion control: use Cartesian velocity control to reach pick and place poses smoothly.
### Analysis
- [ ] Plot and compare trajectories for both strategies (joint and Cartesian space).
- [ ] Analyze end-effector path smoothness.
- [ ] Analyze execution time.
- [ ] Analyze sorting accuracy.
### Extra Steps
- [ ] Mock a camera so that the robot has to find the location and color of the spheres based on visual input. (NOT FEASIBLE)
- [ ] Putting cylinders between the berries and the boxes and create vectors of repulsion around these objects, this would make the robot sense the obstacles.
## Aesthetic Modifications
- [ ] Create a matrix of coordinates in the boxes to place the berries in the right position
#### Sensing Approaches
1. [ ] Use OpenCV to process the camera image, using HSV color masking to find the pixel coordinates of each berry. (NOT FEASIBLE)
2. [ ] Use a Convolutional Neural Network (CNN) that takes the raw camera image as direct input and is trained to learn its own policy for “seeing” the berries. (NOT FEASIBLE)