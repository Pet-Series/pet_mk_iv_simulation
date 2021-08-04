# README: /pet_mk_iv_simulation/ #

ROS repository in the https://github.com/Pet-Series Git-Organizations.</br>
Containing a ROS-package.

## **What is this folder for?** ##
ROS package neccesary to be able to run robot simulation of Pet-Mk.IV, using Gazebo.</br>

<table>
    <tr>
        <td>
            <img src="doc/pet_mk.iv_simulation.png" width="300px">
        </td>
        <td width="250px">
            This package is only necessary if you are going to launch your robot into a simulated world.</br>
            </br>
            If you only will run the physical robot - Then you do not need this package.
        </td>
    </tr>
</table>


* Robot descriptions as .urdf/.xacro files.
* World descriptions as .world filess.
* Robot launch files as .launch</br>
  - Load simulation world</br>
  - Spawn/insert/launch robot into the simulated world.</br>
  - Launch simulations nodes/scripts.
* Simulation nodes/scripts as .py files.</br>
  - Interface between the simulation enviroment and the common robot softaware.
* Simulation 3D-models

### **How do I get set up?** ###

Set up for simuation in Gazebo
* PC with Ubuntu 20.04
* ROS(1) melodic</br>
  /TODO: Upgrade to ROS(1) Noetic.

### **Who do I talk to?** ###

* Repo owner: "Kullken" <karl.viktor.kull@gmail.com>
* Folder contributor: "SeniorKullken" <stefan.kull@gmail.com>
