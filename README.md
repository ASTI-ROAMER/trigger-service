# Trigger Service


A simple ROS Noetic package that allows triggering actions using the keyboard. Pressing **`r`** publishes a message to a topic that other nodes can listen to, enabling keyboard-based control of ROS features.

## Features

- Publishes a `std_msgs/Bool` message on `/trigger_topic` when `r` is pressed.
- Listens for the topic and performs an action (e.g., print "Hello Carlo", take snapshots of leaves, etc.).
- Includes a service (`trigger_service`) that also triggers the same topic.

## Files Included 

- trigger_service.py - ROS service server node using std_srvs/Trigger
- keyboard_trigger_client.py - Keyboard client node that calls the service on key press uses pynput
- listener_node.py - listens to the ros service. You can edit this.
- launch file

## Requirements

ROS Noetic installed on Ubuntu 20.04 with Python 3.

## Setup
1. **Place Files in Your ROS Package**

   ```bash
   cd ~/catkin_ws/src/your_package_name/scripts
   # Copy the files here
   ```

2. **Make Scripts Executable**

   ```bash
   chmod +x trigger_service.py keyboard_trigger_client.py
   ```

3. **Build the Workspace**

   ```bash
   cd ~/catkin_ws
   catkin_make
   source devel/setup.bash
   ```

4. **Run the Nodes/Launch File**

## Notes

- You can modify the service callback to **publish to a topic** or trigger other actions.
- Uses raw terminal input, so **run it in a terminal, not in IDEs** like VSCode or PyCharm terminal.## Usage

- Press **`r`** to call the service
- Press **`q`** to exit the client


