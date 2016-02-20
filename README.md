# Gatttool-Scripts

Example gatttool command line sequence for LightBlue Heart profile




sudo gatttool -i hci0 -b 43:BC:E6:DA:76:48 -t random -I

[ ][43:BC:E6:DA:76:48][LE]>

[ ][43:BC:E6:DA:76:48][LE]> connect

[CON][43:BC:E6:DA:76:48][LE]> primary

[CON][43:BC:E6:DA:76:48][LE]>

attr handle: 0x0001, end grp handle: 0x0005 uuid: 00001800-0000-1000-8000-00805f9b34fb

attr handle: 0x0006, end grp handle: 0x0009 uuid: 00001801-0000-1000-8000-00805f9b34fb

attr handle: 0x000a, end grp handle: 0x000e uuid: d0611e78-bbb4-4591-a5f8-487910ae4366

attr handle: 0x002b, end grp handle: 0x002e uuid: 0000180f-0000-1000-8000-00805f9b34fb

attr handle: 0x002f, end grp handle: 0x0034 uuid: 00001805-0000-1000-8000-00805f9b34fb

attr handle: 0x0035, end grp handle: 0x003e uuid: 7905f431-b5ce-4e99-a40f-4b1e122d00d0

attr handle: 0x003f, end grp handle: 0x004a uuid: 89d3502b-0f36-433a-8ef4-c502ad55f8dc

attr handle: 0x004b, end grp handle: 0x005d uuid: 0000180a-0000-1000-8000-00805f9b34fb

attr handle: 0x005e, end grp handle: 0x0066 uuid: 0000180d-0000-1000-8000-00805f9b34fb

// Heart Rate 0000180d-0000-1000-8000-00805f9b34fb

// https://developer.bluetooth.org/gatt/services/Pages/ServicesHome.aspx

// handle: 0x005e, end grp handle: 0x0066

[CON][43:BC:E6:DA:76:48][LE]> characteristics 0x005e 0x0066

[CON][43:BC:E6:DA:76:48][LE]>

handle: 0x005f, char properties: 0x88, char value handle: 0x0060, uuid: 00002a39-0000-1000-8000-00805f9b34fb

handle: 0x0062, char properties: 0x02, char value handle: 0x0063, uuid: 00002a38-0000-1000-8000-00805f9b34fb

handle: 0x0064, char properties: 0x10, char value handle: 0x0065, uuid: 00002a37-0000-1000-8000-00805f9b34fb

// char properties: 0x10 Notification

[CON][43:BC:E6:DA:76:48][LE]> char-desc 0x0064

[CON][43:BC:E6:DA:76:48][LE]>

handle: 0x0064, uuid: 2803

handle: 0x0065, uuid: 2a37

handle: 0x0066, uuid: 2902

[CON][58:48:82:AC:A5:84][LE]> char-write-req 0x0066 0100

[CON][58:48:82:AC:A5:84][LE]> Characteristic value was written successfully

Notification handle = 0x0065 value: 00 50

[CON][58:48:82:AC:A5:84][LE]>

[CON][58:48:82:AC:A5:84][LE]>

Notification handle = 0x0065 value: 00 3c

[CON][58:48:82:AC:A5:84][LE]>

Notification handle = 0x0065 value: 00 3c

[CON][58:48:82:AC:A5:84][LE]>

Notification handle = 0x0065 value: 00 3c

[CON][58:48:82:AC:A5:84][LE]>

Notification handle = 0x0065 value: 00 3c

[CON][58:48:82:AC:A5:84][LE]>

Notification handle = 0x0065 value: 00 3c

// Notification stop

[CON][58:48:82:AC:A5:84][LE]> char-write-req 0x0066 0000

[CON][58:48:82:AC:A5:84][LE]> disconnect
