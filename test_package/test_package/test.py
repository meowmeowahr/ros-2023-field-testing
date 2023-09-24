#!/usr/bin/env python

import rclpy
from geometry_msgs.msg import Pose, Point
from gazebo_msgs.msg import ModelState

def set_pose():
    rclpy.init()

    # Create a node
    node = rclpy.create_node('set_ignition_gazebo_pose_node')

    # Create a publisher to publish the desired pose
    pose_publisher = node.create_publisher(ModelState, '/gazebo/set_model_state', 10)

    # Create a ModelState message and fill it with the desired pose information
    model_state_msg = ModelState()
    model_state_msg.model_name = 'cube_0'

    # Ensure that the values are floats
    model_state_msg.pose.position = Point(x=0.0, y=0.0, z=10.0)

    # Publish the desired pose
    pose_publisher.publish(model_state_msg)

    node.get_logger().info('Published pose to set_model_state topic')

    rclpy.spin()

if __name__ == '__main__':
    set_pose()
