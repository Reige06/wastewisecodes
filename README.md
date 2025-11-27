# **WasteWise – Smart Garbage Bin (IoT Device)**

## **Description**

The WasteWise IoT device is a smart automatic waste-sorting garbage bin designed to make waste management more efficient. The ESP32-CAM identifies the type of garbage using FOMO Edge 
Impulse machine learning model. The ESP32 Main receives information from the ESP32-CAM, decides how the servo motor should move, and sends the bin status (Not Full/Full) to the WasteWise mobile app every 3 seconds. The ESP32 Main connects to Wi-Fi to communicate with the backend, and the system runs on rechargable batteries. The system uses IR proximity sensors to detect if the bin is Not Full or full and a servo motor to sort waste.

## **Features**

Automatic Waste Sorting: One servo motor sorts waste based on type detected by the ESP32-CAM.

Garbage Type Identification: ESP32-CAM uses FOMO Model to classify trash.

Battery-Powered: Fully portable, rechargable and independent from mains electricity.

Periodic Updates: Bin status updates every 3 seconds to the mobile app.

Bin Level Monitoring: IR sensors detect whether the bin is Not Full or full, updating the mobile app.

## **Hardware Components**

ESP32-CAM module (identifies garbage type using FOMO Model)

ESP32 Main module (controls servo, sends status to app)

One SG92R servo for sorting mechanism

IR proximity sensors (detect bin fullness)

Rechargable batteries for power supply

## **System Operation**

ESP32-CAM identifies the type of garbage using ML.

ESP32 Main receives the garbage type information and decides the servo motor movement.

IR sensors detect trash presence and determine if the bin is Not Full or full.

ESP32 Main sends bin status (Not Full/Full) to the backend server every 3 seconds.

WasteWise app displays bin status for maintenance staff.

If the bin is full, it prevents further trash from being added until emptied.

## **Setup Instructions**

### **Assemble Hardware**

Connect the ESP32-CAM to the ESP32 Main.

Attach the servo motor to the ESP32 Main.

Connect IR sensors to ESP32 Main to detect bin fullness.

Power the system using batteries.

### **Flash Firmware**

Use Arduino IDE to upload code to both ESP32-CAM and ESP32 Main.

ESP32-CAM: Runs FOMO Edge Impulse ML model to identify garbage type.

ESP32 Main: Receives data from the camera, controls the servo motor, and sends bin status to the app.

### **Connect ESP32 Main to Wi-Fi**

Only the ESP32 Main connects to Wi-Fi to communicate with the backend.

Enter Wi-Fi credentials in the ESP32 Main code.

### **Test Sensors and Servo Motor**

Confirm that the servo motor moves according to garbage type.

Place trash in the bin and verify that the IR sensors detect it after 5 seconds.

Ensure the mobile app updates bin status (Not Full/Full).

### **Deploy Bin**

Place WasteWise in cafeteria.

**The system will automatically:**

Identify garbage type

Sort waste via servo motor

Detect trash presence (full/Not Full)

Update the app every 3 seconds

When full, the bin prevents additional trash from being added.


## **Integration with App**

Communicates with WasteWise mobile app via the backend server(Render).

Bin status updates every 3 seconds for monitoring by maintenance staff.

## **Contributors**

Junefree Yamson – Mobile App Developer

Reige Bongo – Backend Developer

Rex Belli Isidore B. Lumantao – IoT Hardware Developer
