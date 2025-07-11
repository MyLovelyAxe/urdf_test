import os
from launch import LaunchDescription
from ament_index_python.packages import get_package_share_directory
from launch_ros.actions import Node

def generate_launch_description():

    ### rviz node
    rviz_config_file = os.path.join(
        get_package_share_directory("urdf_test"),
        "config",
        "simple_robot_control.rviz",
    )
    rviz_node = Node(
        package="rviz2",
        executable="rviz2",
        name="rviz2",
        output="log",
        arguments=["-d", rviz_config_file],
    )

    ### robot description parameter
    # locate the robot description urdf and mesh sources by package
    urdf_path = os.path.join(
        get_package_share_directory('moveit_resources_panda_description'),
        'urdf',
        'panda.urdf'
    )
    with open(urdf_path, 'r') as infp:
        robot_description = infp.read()

    ### robot_state_publisher
    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        parameters=[{'robot_description': robot_description}]
    )

    ### joint_state_publisher_gui
    joint_state_publisher_gui_node = Node(
        package='joint_state_publisher_gui',  # or 'joint_state_publisher'
        executable='joint_state_publisher_gui', # this launches the gui, if use 'joint_state_publisher', the non-gui, but still able to offer joint values through commands or source code
        parameters=[{'robot_description': robot_description}]
        )


    return LaunchDescription([
        rviz_node,
        robot_state_publisher_node,
        joint_state_publisher_gui_node,
    ])