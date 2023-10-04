#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import PoseStamped
from std_msgs.msg import Empty
from actionlib_msgs.msg import GoalID

global poselist
poselist = [[0.0,0.0,0.0],[0.5,0.0,0.0],[1.0, 0.0, 0.0],[1.5, 0.0, 0.0],
                [2.0, 0.0, 0.0],[2.5,0.0,0.0], [3.0,0.0,0.0],[3.5,0.0,0.0] ]
global poseindex
poseindex = 1

import socket


def make_goal_pose(x, y, theta):
    goal_pose = PoseStamped()
    goal_pose.header.frame_id = 'map'  # Assuming the frame ID is "map"
    goal_pose.pose.position.x = x
    goal_pose.pose.position.y = y
    goal_pose.pose.orientation.z = theta
    goal_pose.pose.orientation.w = 1.0
    #print (goal_pose)
    return goal_pose

def control():


    server_ip = "192.168.0.100"
    server_port = 6677

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((server_ip, server_port))
    server.listen(1)

    print("Waiting for a connection...")
    client_socket, client_address = server.accept()
    print("Connected to ",client_address)

    goal_pub    = rospy.Publisher('/move_base_simple/goal', PoseStamped, queue_size = 1)  
    stop_pub    = rospy.Publisher('/move_base/cancel', GoalID, queue_size = 1)  

    rospy.init_node('navigtion_control', anonymous=True)

    global poseindex
    global poselist
    while not rospy.is_shutdown():
        data = client_socket.recv(1024).decode()
        if not data:
            break

        print("Received instruction:", data)
        if data == "forward":
            # Code for moving forward
            poseindex = poseindex + 1
            print("Moving forward...", poseindex)
            if(poseindex >= len(poselist)):
                print("*****WARNing: forward navi out of range" )
                poseindex = len(poselist) -1
            goal_pose= make_goal_pose(poselist[poseindex][0], poselist[poseindex][1], poselist[poseindex][2])
            rospy.loginfo(goal_pose)
            goal_pub.publish(goal_pose)

        elif data == "backward":
            poseindex = poseindex - 1
            # Code for moving backward
            print("Moving backward...",poseindex)
            if(poseindex < 0 ):
                print("*****WARNing: backward navi out of range" )
                poseindex = 0
            goal_pose= make_goal_pose(poselist[poseindex][0], poselist[poseindex][1], poselist[poseindex][2])
            rospy.loginfo(goal_pose)
            goal_pub.publish(goal_pose)

        elif data == "stop":
            # Code for stopping
            print("Canncel the navigation...")
            goal_id = GoalID()
            stop_pub.publish(goal_id)
        
        else:
            print("Invalid Command", data)
             
        
        #goal_pose= make_goal_pose(poselist[poseindex][0], poselist[poseindex][1], poselist[poseindex][2])
        #rospy.loginfo(goal_pose)
        #goal_pub.publish(goal_pose)
        #time.sleep(1)
        #rate.sleep()
        


    client_socket.close()
    server.close()    

 
    
if __name__ == '__main__':
    try:
        control()
    except rospy.ROSInterruptException:
        pass