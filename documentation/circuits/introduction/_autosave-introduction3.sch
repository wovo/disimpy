EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L disimpy:full_adder U?
U 1 1 5E378500
P 4300 1900
F 0 "U?" H 4550 2200 50  0001 C CNN
F 1 "full_adder" H 4500 1600 50  0001 C CNN
F 2 "" H 4300 1800 50  0001 C CNN
F 3 "" H 4300 1800 50  0001 C CNN
	1    4300 1900
	1    0    0    -1  
$EndComp
$Comp
L disimpy:full_adder U?
U 1 1 5E3796D1
P 5300 2350
F 0 "U?" H 5550 2650 50  0001 C CNN
F 1 "full_adder" H 5500 2050 50  0001 C CNN
F 2 "" H 5300 2250 50  0001 C CNN
F 3 "" H 5300 2250 50  0001 C CNN
	1    5300 2350
	1    0    0    -1  
$EndComp
Text GLabel 2900 1400 0    50   Input ~ 0
carry-in
Text GLabel 2850 2000 0    50   Input ~ 0
port-1
Text GLabel 2850 2650 0    50   Input ~ 0
port-2
$Comp
L disimpy:full_adder U?
U 1 1 5E37C416
P 6300 2800
F 0 "U?" H 6550 3100 50  0001 C CNN
F 1 "full_adder" H 6500 2500 50  0001 C CNN
F 2 "" H 6300 2700 50  0001 C CNN
F 3 "" H 6300 2700 50  0001 C CNN
	1    6300 2800
	1    0    0    -1  
$EndComp
$Comp
L disimpy:full_adder U?
U 1 1 5E37DBBC
P 7550 3750
F 0 "U?" H 7800 4050 50  0001 C CNN
F 1 "full_adder" H 7750 3450 50  0001 C CNN
F 2 "" H 7550 3650 50  0001 C CNN
F 3 "" H 7550 3650 50  0001 C CNN
	1    7550 3750
	1    0    0    -1  
$EndComp
Wire Wire Line
	4800 2100 4800 2250
Wire Wire Line
	5800 2550 5800 2700
Entry Wire Line
	3200 2100 3300 2200
Entry Wire Line
	4450 3000 4550 3100
Wire Wire Line
	4800 2450 3300 2450
Wire Wire Line
	5800 2900 3300 2900
Wire Wire Line
	7050 3650 3300 3650
Entry Wire Line
	3200 2350 3300 2450
Entry Wire Line
	3200 2800 3300 2900
Entry Wire Line
	3200 3550 3300 3650
Wire Bus Line
	2850 2000 3100 2000
Entry Bus Bus
	3100 2000 3200 2100
Wire Bus Line
	2850 2650 3400 2650
Entry Bus Bus
	3400 2650 3500 2750
Wire Wire Line
	3800 1400 3800 1800
Wire Wire Line
	2900 1400 3800 1400
Wire Wire Line
	3800 2000 3350 2000
Wire Bus Line
	3500 1650 3500 4000
Wire Bus Line
	3200 1650 3200 4000
$EndSCHEMATC
