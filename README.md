# Differential_Drive (Phase 3c)

## Step 1

### Run Code
Open the file "a_star_differential_drive.py" from 'code' directory in an IDE (Spyder, VS Code etc) of your choice. Enter valid input such that point does not lie in obstacle space or outside of workspace. Also enter a valid angle for the starting vector. For invalid inputs it exits with invalid input prompt. The video visualization can be found in 'Differential Drive Visualization (A-star).mp4'.

### Description
This code aims at implementing A* algorithm for a differential drive (using non-holomonic constraints). The robot here under consideration is a turtlebot3 of 'Waffle' type. All the nodes corresponding with different points (x,y) on the map are explored until a goal is found.

### Dependencies
a) python -version 3

b) numpy

c) sys

d) matplotlib

e) time

f) math

### Parameters
a) r_wheel = 0.038 (radius of wheels in m)

b) L_wheel = 0.354 (distance between two wheels in m)

c) dt = 0.1 (differential time needed for integration in s)

d) time = 1 (total time for each action in s)

d) threshold_distance = 0.1 (threshold distance between each node in m)

e) goal_threshold_radius = 0.2 (threshold radius for goal node in m)

f) clearance = 0.25 (effective clearance i.e., radius of robot & obstacle clearance)

Note: RPM's of left and right wheel are defined in the code and not obtained from the user. Six different actions are considered and these are (5, 5), (10, 10), (5, 0), (0, 5), (5, 10), and (10, 5).

### Function Descriptions
#### 1) workspace_check
In this functiom the given value is checked to see if it lies in the workspace.

#### 2) obstacle_space
In this function the given value is checked against obstacles and true is returned if it lies outside obstacle space and also takes into consideration the clearance needed for the mobile robot. Obstacles which are given are two circles, 1 square, and two rectangles.

#### 3) find_index
For a given (x, y) node_state, it finds its corresponding node index. 

#### 4) a_star
In this function the initial input values (x, y, theta) are taken and action sets based on RPM's of left and right wheels are performed to generate next set of moves. These moves are implemented with non-holomonic constraints for a differential drive. Only valid actions are stored in an 'unvisited_nodes_index' list. Finally, the node_flag is updated to one for the parent_index (see code). 

#### 5) traj
In this function, backtracking is done from goal node to start node to obtain optimal path.

##### NOTE :
Using Matplotlib, animation is generated. Firstly, animation for node exploration is generated and followed by optimal path trajectory's animation. 150 frames for node exploration and 50 frames for solution trajectory are used as default values for the animation. The resulting animation is also stored in 'Differential Drive Visualization (A-star).mp4' file.

If you get error while trying to save the animation in .mp4 file format, installation of FFMPEG may be required. [https://ffmpeg.org/download.html]
