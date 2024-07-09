# Mechanical-Turk

## Table of Contents
- [What is it?](#What-is-it?)
- [Requirements](#Requirements)
- [Documentation](#Documentation)
- [Install](#Install)
- [Hardware](#Hardware)
  - [Chess](#Chess)
  - [Face](#Face)
- [Schematic](#Schematic)
- [Software](#Software)
- [3D Components](#3D-Components)
  - [Components List](#Components-List)
  - [How to Use the 3D Files](#How-to-Use-the-3D-Files)
  - [Folder Structure](#Folder-Structure)
- [Authors](#Authors)


## What is it?
The project involves creating an automated chess system inspired by the legendary "Mechanical Turk". This system allows a human user to play chess against a machine, which not only calculates and executes moves on the board but also interacts emotionally through a robotic face. The objective of the project is to combine advanced computer vision, robotics, and programming techniques to offer a unique and interactive gameplay experience.


## Requirements
 **pip install chess**
 **pip install stockfish**
 **pip install time**
 **pip install RPi.GPIO**

## Documentation

**Project Components**

The project consists of several key components that work together to create a cohesive and smooth experience:

**1. Interactive Chessboard**

*  **Board**: A standard chessboard with magnetic pieces.

*  **Camera**: A camera mounted above the board or into the robotic face to capture images and detect piece movements.

**2. Computer Vision System** 

*  **Piece Detection**: Uses computer vision techniques to recognize and track the pieces on the board.

*  **Movement Recognition**: Detects and records the user's moves by comparing the current state of the board with a reference image.

**3. Piece Movement Mechanism**

*  **Axis System**: X-Y axes equipped with stepper motors that control an electromagnet to move the pieces on the board.

*  **Electromagnet**: Placed under the board, this device lifts and moves the pieces to the desired position.

**4. Chess Control Software**

*  **Chess Engine**: Uses Stockfish, one of the most advanced chess engines, to calculate the machine's moves.

*  **Control Interface**: A Python program that coordinates communication between the chess engine, the vision system, and the motor controller.

**5. Interactive Robotic Face**

*  **Eyes, Brows and Mouth**: Displays different facial expressions in response to the state of the game.

*  **Gestures and Expressions**: Programmed gestures and facial expressions to reflect emotions like happiness, surprise, or frustration, depending on the game's progress.


## Install
To set up Mechanical Turk, follow these steps:

1. Clone the repository to your local machine. $git clone https://github.com/PolLopezPena/MechanicalTurk.git
2. Install the required libraries (check requirements).
3. Execute main Python script.


## Hardware
- ### Chess
| Component | Image | Link |
|----------------------|-----|-----------------------|
|**5V stepper motor :**| ![motor-28byj-48-paso-a-paso-de-5v](https://github.com/PolLopezPena/MechanicalTurk/assets/75804697/0fd51982-075c-423f-9ab6-4d9dc1fa928c) | https://goo.su/S9cJCD |
|**ULN2003-Stepper Motor Driver Board:**| ![1631-00](https://github.com/PolLopezPena/MechanicalTurk/assets/75804697/5af206d2-333f-41d8-aa23-8f11db6fdf94) | https://goo.su/S9cJCD |
|**OcioDual Relay Module 5V 10A:**|![51sQx-WGVOL](https://github.com/PolLopezPena/MechanicalTurk/assets/75804697/9f88efdf-bd56-44a2-b1e7-76e7df18c7ac) | https://goo.su/Mz3IfKR |
|**Electromagnet 12V:**|![s-l1600](https://github.com/PolLopezPena/MechanicalTurk/assets/75804697/14a2cb08-ef98-481e-b826-76ce928c1337) | https://goo.su/75PAyq |
|**Raspberry Pi 3B:**|![91zSu44+34L _AC_UF894,1000_QL80_](https://github.com/PolLopezPena/MechanicalTurk/assets/75804697/4a6e4b41-1469-4c85-be64-189009533e3b) | https://goo.su/UA1p |
|**Raspberry Pi Camera v2:**|![6169R+wUp8L](https://github.com/PolLopezPena/MechanicalTurk/assets/75804697/6943c9f3-2bc2-4c3a-ab7f-99478f34a816) | https://goo.su/2GHD9UQ |
|**ATX 500W Power Supply:**|![s-l600](https://github.com/PolLopezPena/MechanicalTurk/assets/75804697/95704f58-51b6-4dd2-b28f-7ca0d144d7e3) | https://acortar.link/dsBHzn |
|**456 Point Breadboard:**|![Breadboard_456P_Vellemans_1-600x600](https://github.com/PolLopezPena/MechanicalTurk/assets/75804697/22165cd8-e895-4ac8-a4de-a5170c47d1df) |https://acortar.link/TY06Ol |


- ### Face
| Component | Image | Link |
|----------------------|-----|-----------------------|
|**Arduino Nano:**| ![73b102980_arduino-nano-r3_x](https://github.com/PolLopezPena/MechanicalTurk/assets/75804697/8be2982c-821a-40b3-a744-c2c4fc985f39) | https://n9.cl/pvt57b|
|**PCA9685 Controller:**| ![51kshHMO+YL _AC_](https://github.com/PolLopezPena/MechanicalTurk/assets/75804697/38aa901e-25dd-435f-a7bc-e467941461d6) | https://acortar.link/6Guztp
|**4x Micro servo 9G:**| ![61uoCSp26qL](https://github.com/PolLopezPena/MechanicalTurk/assets/75804697/00a61852-7760-4cb2-a128-7cf9032155a0) | https://n9.cl/h44zv|
|**Arduino Uno:**| ![2356913-40](https://github.com/PolLopezPena/MechanicalTurk/assets/75804697/6c051796-b6c7-48cd-93c8-46779110314d) | https://n9.cl/hab0d|
|**Neopixel Neomatrix 8x32** | ![PPADA2294_Neopixel_RGB_LED_MATRIX_FLEXIBLE_main3__44844](https://github.com/PolLopezPena/MechanicalTurk/assets/75804697/ea0c40aa-b552-4ab1-bb5c-e5fbd8d19743) |https://acortar.link/TBNjKt|


## Schematic
- ### Chess
![Chess_sketch](https://github.com/PolLopezPena/MechanicalTurk/assets/101926329/d1a6ae5d-ad86-4b42-886c-01ec72a7d686)
- ### Face
![Cabeza_sketch](https://github.com/PolLopezPena/MechanicalTurk/assets/101926329/ad2e15a4-688d-462c-a651-70540a8c918b)


## Software

## 3D Components
This section lists the 3D components used in the project along with their descriptions, dimensions, and links to the corresponding 3D files.


### Components List
**1. Rail (2 pieces)**

*  **Description**: Rails for moving the X-Y axes.
*  **Dimensions**:
     * Length: 39.5 cm
       
     * Width: 4 cm
       
     * Height: 3 cm
       
*  **File**: rail.stl

**2. Small Support (2 pieces)**

*  **Description**: First support for mounting one rail on top of another; second support for mounting the electromagnet on the upper rail.
*  **Dimensions**:
     *  Length: 6 cm

     *  Width: 5 cm

     *  Height: 3.65 cm
       
*  **File**: small_support.stl

**3. Wheel Support (2 pieces)**

*  **Description**: Provides stability to the upper rail to prevent oscillation during movement.
*  **Dimensions**:
     *  Length: 1.4 cm
       
     *  Width: 4.2 cm
       
     *  Height: 3.5 cm
       
*  **File**: wheel_support.stl

**4. Motor Support (2 pieces)**

*  **Description**: Holds the motor that drives the belt.
*  **Dimensions**:
     *  Length: 6.5 cm
       
     *  Width: 5 cm
       
     *  Height: 2 cm
       
*  **File**: motor_support.stl

**5. Belt Support (2 pieces)**

*  **Description**: Provides extra support for the belt at the end of the rail.
*  **Dimensions**:
     *  Length: 4 cm
       
     *  Width: 5 cm
       
     *  Height: 2 cm
       
*  **File**: belt_support.stl

**6. Chessboard**

*  **Description**: The chessboard where the game is played.
*  **Dimensions**:
     *  Length: 47.5 cm
       
     *  Width: 47.5 cm
       
     *  Height: 10 cm
       
*  **File**: chessboard.stl


### How to Use the 3D Files
*  **Download**: Click on the file names above to download the STL files.
*  **Print**: Use a 3D printer to print the components. Ensure that your printer settings match the requirements of each component.


### Folder Structure
*  **3D Files Folder**: All 3D files are stored in the **`/3D_files`** directory of this repository.
* **`/3D_files`**
    *  **`rail.stl`**
      
    *  **`small_support.stl`**
      
    *  **`wheel_support.stl`**
      
    *  **`motor_support.stl`**
      
    *  **`belt_support.stl`**
      
    *  **`chessboard.stl`**


## Authors
* Pol López Peña
* Jhonatan Alejandro Quisbert Tarqui
* Pol González Casals

