# Mechanical-Turk

## Table of Contents
- [What is it?](#What-is-it?)
- [Requirements](#Requirements)
- [Documentation](#Documentation)
- [Install](#Install)
- [Library](#Library)
  - [Hardware](#Hardware)
     - [Chess](#Chess)
     - [Face](#Face)
  - [Schematic](#Schematic)
  - [Software](#Software)
  - [3D Components](#3D-Components)
     - [Components List](#Components-List)
     - [How to Use the 3D Files](#How-to-Use-the-3D-Files)
     - [Folder Structure](#Folder-Structure)

## What is it?
The project involves creating an automated chess system inspired by the legendary "Mechanical Turk". This system allows a human user to play chess against a machine, which not only calculates and executes moves on the board but also interacts emotionally through a robotic face. The objective of the project is to combine advanced computer vision, robotics, and programming techniques to offer a unique and interactive gameplay experience.

## Requirements

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

## Library

* ### Hardware
- #### Chess
**5V stepper motor :** 
https://goo.su/S9cJCD

**ULN2003-Stepper Motor Driver Board:** 
https://goo.su/S9cJCD

**OcioDual Relay Module 5V 10A:** 
https://goo.su/Mz3IfKR

**Electromagnet 12V:** 
https://goo.su/75PAyq

**Raspberry Pi 3B:** 
https://goo.su/UA1p

**Raspberry Pi Camera v2:** 
https://goo.su/2GHD9UQ

**ATX 500W Power Supply:** 
https://acortar.link/dsBHzn

**456 Point Breadboard:** 
https://acortar.link/TY06Ol

- #### Face  

**Arduino Nano:** https://n9.cl/pvt57b

**Dual Leisure L298N Controller:** https://n9.cl/a0iw4

**4x Micro servo 9G:** https://n9.cl/h44zv

**Arduino Uno:** https://n9.cl/hab0d

**Arduino NaNo:** https://tienda.bricogeek.com/arduino-compatibles/1911-nano-v3-atmega328-compatible-arduino.html?gad_source=1&gclid=Cj0KCQjw-ai0BhDPARIsAB6hmP5ihEMdFwEcptXyFqZtUlX9uEVktSkrFmWxxx4lc-3VZqXkVSCEr5gaAkIQEALw_wcB

**Neopixel Neomatrix 8x32** https://n9.cl/16amx](https://botland.store/segment-displays-matrices/6185-elastic-matrix-8x32-256-rgb-led-rgb-ws2812b-individually-addressed-5904422374952.html

* ### Schematic
- #### Chess
![Chess_sketch](https://github.com/PolLopezPena/MechanicalTurk/assets/101926329/d1a6ae5d-ad86-4b42-886c-01ec72a7d686)
- #### Face
![Cabeza_sketch](https://github.com/PolLopezPena/MechanicalTurk/assets/101926329/ad2e15a4-688d-462c-a651-70540a8c918b)
* ### Software
  

* ### 3D Components

This section lists the 3D components used in the project along with their descriptions, dimensions, and links to the corresponding 3D files.

#### Components List
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

#### How to Use the 3D Files
*  **Download**: Click on the file names above to download the STL files.
*  **Print**: Use a 3D printer to print the components. Ensure that your printer settings match the requirements of each component.

#### Folder Structure
*  **3D Files Folder**: All 3D files are stored in the **`/3D_files`** directory of this repository.
* **`/3D_files`**
    *  **`rail.stl`**
      
    *  **`small_support.stl`**
      
    *  **`wheel_support.stl`**
      
    *  **`motor_support.stl`**
      
    *  **`belt_support.stl`**
      
    *  **`chessboard.stl`**


