# Mechanical-Turk

The project involves creating an automated chess system inspired by the legendary "Mechanical Turk". This system allows a human user to play chess against a machine, which not only calculates and executes moves on the board but also interacts emotionally through a robotic face. The objective of the project is to combine advanced computer vision, robotics, and programming techniques to offer a unique and interactive gameplay experience.

## Description

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

*  **LCD Screen**: Displays different facial expressions in response to the state of the game.

*  **Gestures and Expressions**: Programmed gestures and facial expressions to reflect emotions like happiness, surprise, or frustration, depending on the game's progress.

## Install

## Library

* ### Hardware
**Motor paso a paso de 5V :** https://es.aliexpress.com/item/1005006165081645.html?src=google&src=google&albch=shopping&acnt=439-079-4345&slnk=&plac=&mtctp=&albbt=Google_7_shopping&gclsrc=aw.ds&albagn=888888&isSmbAutoCall=false&needSmbHouyi=false&src=google&albch=shopping&acnt=439-079-4345&slnk=&plac=&mtctp=&albbt=Google_7_shopping&gclsrc=aw.ds&albagn=888888&ds_e_adid=&ds_e_matchtype=&ds_e_device=c&ds_e_network=x&ds_e_product_group_id=&ds_e_product_id=es1005006165081645&ds_e_product_merchant_id=109343247&ds_e_product_country=ES&ds_e_product_language=es&ds_e_product_channel=online&ds_e_product_store_id=&ds_url_v=2&albcp=20330803848&albag=&isSmbAutoCall=false&needSmbHouyi=false&gad_source=1&gclid=Cj0KCQjws560BhCuARIsAHMqE0F6jdiGJPwEP1tyPX0AnOv9lnovVhouB58bNKSOfPf0Euqvw0UQUHoaAh7dEALw_wcB&aff_fcid=1dd59fa476e74bb28518f2a71097c23c-1720196255651-05598-UneMJZVf&aff_fsk=UneMJZVf&aff_platform=aaf&sk=UneMJZVf&aff_trace_key=1dd59fa476e74bb28518f2a71097c23c-1720196255651-05598-UneMJZVf&terminal_id=c303013dd33d4a13b816ea2b4fe98f02&afSmartRedirect=n
**ULN2003-Placa de controlador de Motor paso a paso:** https://es.aliexpress.com/item/1005005253187354.html?src=google&src=google&albch=shopping&acnt=439-079-4345&slnk=&plac=&mtctp=&albbt=Google_7_shopping&gclsrc=aw.ds&albagn=888888&isSmbAutoCall=false&needSmbHouyi=false&src=google&albch=shopping&acnt=439-079-4345&slnk=&plac=&mtctp=&albbt=Google_7_shopping&gclsrc=aw.ds&albagn=888888&ds_e_adid=&ds_e_matchtype=&ds_e_device=c&ds_e_network=x&ds_e_product_group_id=&ds_e_product_id=es1005005253187354&ds_e_product_merchant_id=109233205&ds_e_product_country=ES&ds_e_product_language=es&ds_e_product_channel=online&ds_e_product_store_id=&ds_url_v=2&albcp=20330803848&albag=&isSmbAutoCall=false&needSmbHouyi=false&gad_source=1&gclid=Cj0KCQjws560BhCuARIsAHMqE0EkCYMPnQsvTrx-iZY270ItN2ZD4tF2qCkDuRlDzXjfIPUkdrnIQdsaAhmjEALw_wcB&aff_fcid=f124af7403f846278e4792d949f91591-1720196246888-03377-UneMJZVf&aff_fsk=UneMJZVf&aff_platform=aaf&sk=UneMJZVf&aff_trace_key=f124af7403f846278e4792d949f91591-1720196246888-03377-UneMJZVf&terminal_id=c303013dd33d4a13b816ea2b4fe98f02&afSmartRedirect=n
**OcioDual Módulo Relé 5V 10A:** https://www.pccomponentes.com/ociodual-modulo-rele-5v-10a-1-canal-para-raspberry-pi-8051-avr-pic-dsp-logic?campaigntype=eshopping&campaignchannel=shopping&gad_source=1&gclid=Cj0KCQjws560BhCuARIsAHMqE0FDKLX9twEZjFcym31-Wu6wIbpNqpC53AC56IRcgacjXzjZGPnNCu4aAgg7EALw_wcB
**Electroiman 12V:** https://www.transmotec.es/product/em2015-12v/?vat=true&gad_source=1&gclid=Cj0KCQjws560BhCuARIsAHMqE0F_-T0AiABiw6HTlzioaJhOASuCUZf8RiSqUM3F623CIl0FGoPmEw4aAjhuEALw_wcB
**Raspberry Pi 3B:** https://www.amazon.es/Raspberry-Pi-Modelo-Quad-Core-Cortex-A53/dp/B01CD5VC92/ref=asc_df_B01CD5VC92/?tag=googshopes-21&linkCode=df0&hvadid=699858699962&hvpos=&hvnetw=g&hvrand=9935030387353619491&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9198465&hvtargid=pla-344941896120&psc=1&mcid=f31bca0cf4863c51a20eb1713bc04b2f&gad_source=1
**Cámara Raspberry Pi v2:** https://tienda.bricogeek.com/accesorios-raspberry-pi/822-camara-raspberry-pi-v2-8-megapixels.html?gad_source=1&gclid=Cj0KCQjws560BhCuARIsAHMqE0FPMxySeH8Nw4frFMZA8ZZfNim1WFZTpJ7FSy4sNYRpaC1IRxdati0aAuqfEALw_wcB
**Fuente de Alimentación ATX 500W:** https://www.pccomponentes.com/unykach-fuente-de-alimentacion-atx-500w?campaigntype=eshopping&campaignchannel=shopping&gad_source=1&gclid=Cj0KCQjws560BhCuARIsAHMqE0EMWZVXZzKKNMqcAN2GbT8Wlyg1CfwVfRP3YpWx7lcoWziE45mE4qsaAsRXEALw_wcB
**Protoboard de 456 Puntos:** https://www.bt-ingenieros.com/electronica/6752-protoboard-de-456-puntos-con-contactos-de-niquel-plata.html?utm_source=kelkooes&utm_medium=cpc&utm_campaign=kelkooclick&utm_term=Velleman+Protoboard+de+456+Puntos+con+co&from=kelkoo

* ### Schematic

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

* ### (extra)
