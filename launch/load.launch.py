from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import Command, FindExecutable, PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare
from launch_ros.parameter_descriptions import ParameterValue

def generate_launch_description():
    # Path to the URDF file
    description_file = PathJoinSubstitution(
        [FindPackageShare("smb_description"), "urdf", "smb.urdf.xacro"]
    )

    # Generate the robot description using xacro
    robot_description = ParameterValue(
        Command([FindExecutable(name="xacro"), " ", description_file]),
        value_type=str
    )

    # Robot State Publisher node
    robot_state_publisher_node = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        name="robot_state_publisher",
        output="screen",
        parameters=[{"robot_description": robot_description}],
    )

    # Define the launch description
    return LaunchDescription([
        robot_state_publisher_node,
    ])