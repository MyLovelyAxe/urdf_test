import os
from launch import LaunchDescription
from ament_index_python.packages import get_package_share_directory
from launch_ros.actions import Node

def generate_launch_description():

    # ### hard-coded path of urdf file
    # with open('/home/hardli/sereact_interview_coding_challenge/src/moveit_resources/panda_description/urdf/panda.urdf', 'r') as f:
    #     robot_description = f.read()

    ### locate the robot description urdf and mesh sources by package
    urdf_path = os.path.join(
        get_package_share_directory('moveit_resources_panda_description'),
        'urdf',
        'panda.urdf'
    )
    with open(urdf_path, 'r') as infp:
        robot_description = infp.read()

    return LaunchDescription([
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            parameters=[{'robot_description': robot_description}]
        ),
        Node(
            package='joint_state_publisher_gui',  # or 'joint_state_publisher'
            executable='joint_state_publisher_gui', # this launches the gui, if use 'joint_state_publisher', the non-gui, but still able to offer joint values through commands or source code
            parameters=[{'robot_description': robot_description}]
        ),
    ])