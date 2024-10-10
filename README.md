# PetWellTech 

PetWellTech develops hardware and software for monitoring pet health and associated activities.

The goal of the pilot project is to investigate possibilities of monitoring VOCs in dog breath with hardware available on the market and build a prototype solution 
that can detect for example acetone in dog breath. 

# Sensors investigated 
| <img src="https://github.com/iot-lnu/iotlab-pilotcase-jemac/raw/main/images/image-4.png" width="145" height="100"> | "Electronic nose", Bosch BME688 sensor | A [development kit](https://www.sparkfun.com/products/19630) consisting of 8 individual BME688 sensors was used to collect data along with a [Thing Plus - ESP32 WROOM (Micro-B)](https://www.sparkfun.com/products/15663) |
| --------------------------------------------------------------- | -------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

Documentation for the BME688 sensor can be found [here](https://www.bosch-sensortec.com/software/bme/docs/overview/getting-started.html).

## Collecting data from the BME688 sensor 

### Test 1 
Controlled environment in a plastic box. 
Volume of the box is 0,013 cubic meters. The amount of acetone injected was 0.01 ml 

- **Density of acetone**: 0.791 g/ml.
- **Molecular weight of acetone**: 58.08 g/mol.
- **Temperature**: 35°C (converted to Kelvin: 308.15 K).
- **Gas constant**: 8.3145 J/(mol⋅K).

### Steps:

1. **Convert Liquid Volume to Mass**:
   - Mass of acetone = 0.01 ml x 0.791 g/ml = 0.00791 g

2. **Convert Mass to Moles**:
   - Moles of acetone = mass / molecular weight = 0.00791 g / 58.08 g/mol ≈ 0.000136 mol

3. **Use Ideal Gas Law to Find Volume of Gas at 35°C**:
   - Calculate volume using V = nRT / p, assuming standard pressure (101325 Pa). For example using [this calculator for ideal gas law](https://www.omnicalculator.com/physics/ideal-gas-law?calculatorResult=H4sIAAAAAAAAA71X2W7cNhT9FUNP48BVRFHUYqABWqcFjCLJg9u8BIZBj2hZDbWAy6BGMP%2BeS2qjPPIsbhC9jLjcc%2B5%2BNd88VhdlzW4UVcy7%2FOatKV9rDov8MxUlvedMfqQVk97lF69qYOVdmF8q7ioqpXd74a0faV0sXd80XFfMXmnqvFRlU0tDUdatVrMXC%2BwH5nVDuQZFuq2zd2cB8OVMsbWr0aTM7dZVx0fPIPr9AzijMQDWCialFswPXahh9%2Bzdry8jDZc6pYw6eKbOIUUGFTq%2F%2BZEr3O3tpR%2FcDQiKVS0TVBk7iAvjHBisX8IE%2B4i8hOjcBljAbbTajdi%2B6FwMzEpoBnqJsiiYKOtiuGySZTTPWwjmwZgdS1FQeQd5KBWtlbcT6AMBfS3JlAV7Qn66k9wM2ZsLr9V7J4EO58frqExW6dJtBm6a2WO4vGFCQvf4sxEV9CbbRKzrTL8aT6%2BHcyBZrdBbFNjn%2FM1KsAcmWL1mn42G5%2BeeC%2FpJq0mul3mz2pWZ5eYe5o74fAniRdoVsqRLnGMO7mEMEA7JKWZaJY3Qoprz%2BO9z8gmMizR9mv7UMAItA5mrPXOuV6sr327eLcw99p8S9D1V1Gav%2FC3fUODJvcsHyiVUQCk%2FNPclZ%2BOGlkx0tupaiaerJjf1cPOHsUMLo%2BWTXf%2FlbNw8VfcNh%2B2vAnY5TFpNC9aLstqzqNcmWCXl%2F9Slkj2dsfOhc4jZfs9aVucG8QNtuyrjzfrrkvWzAr01Tqg15demPG3ez85hbcrXS32MoigOY5QigsMosMGpQMaAdwWrHv8FAO%2F3svioq3tmDBrm0nNxG6bO7dZhE1CtOe9ahreYqEdTYuL1vad%2FfV7dRyOR1A%2FSEWxczSv3aDQ0IqFhgpyIkPjZBNIttkMYD4R77lDHhotnRXE7dOlPNX9yh8IwB35yqvResgSBb6s%2FAcNPQnbktv8nHwCHpCjCQRQnCY5CjBBJUIhxlKIsIjEiGU7iGKMkDOMsIQgnJIarBCEMIlEaT%2BH7QViLpXSMOxCOgwgnaQjcGUmyNAaf45iQFEcJkEchCrIsRkma4RA0gidLcBKQIAhxlmauIT8GzS2rrkzsJDst1L3MdreDDA3hJDjcQU3jzM1DHEWvykMjt7VfQIKtm5KPf9GoVo2kG9ZV27rhnLaS5dd5X3%2BPjLd%2Fw3Ry2%2FxSY5eM2286OzZuuC5shrj%2BbUVZUWGmkhHKqcjvqKoa2T7CUJ0P8OlqxRca83R85XY1R6rY7cHTaQEH1hnfAUxqtSawDgAA). 
   - Volume ≈ 3.44 ml  

4. **Convert to ppm**:
   - Concentration (ppm) = (Volume of gas / Volume of box) x 1,000,000
   - Concentration ≈ (3.44 ml / 13000 ml) x 1,000,000 ≈ 265 ppm

The acetone was added to the enclosed box using a small syringe at the beginning of the test. There was no more acetone added during the test.

### The plastic test box
<img src="images/box.JPG" width="75%">

### Syringe & chemically clean acetone source

<img src="images/syringe.JPG" width="25%" > <img src="images/aceton.JPG" width="25%">


The table below shows the data collected for the different acetone concentrations and for clean air, as well as the duration of the data collection.

|               | \*Temperature (°C) | \*Humidity (%) | \*Pressure (hPa) | \*Gas Resistance (Ω) | Duration (mins) |
| ------------- | ------------------ | -------------- | ---------------- | --------------------- | ---------------- |
| Air training  |     3.501277e+01   | 1.925969e+01   | 1.020081e+03     | 3.489649e+07          | 45      |
|  Air test     |     3.459404e+01   | 1.943559e+01   | 1.018670e+03     | 3.361244e+07          | 45      |
|Acetone training| 3.635105e+01       | 2.050594e+01   | 1.021596e+03     | 1.580791e+07          | 15       |
| Acetone test  | 3.543839e+01       | 1.962744e+01   |  1.018924e+03    | 1.418220e+07          | 15 |

#### Formatted data (observe gas resistance in Mega ohms) 

|                 | Temperature (°C) | Humidity (%) | Pressure (hPa) | Gas Resistance (MΩ) | Duration (mins) |
| --------------- | ---------------- | ------------ | -------------- | ------------------- | ---------------- |
| Air training    |        35.01     |      19.26   |     1020.08    |         34.90       |       45        |
| Air test        |        34.59     |      19.44   |     1018.67    |         33.61       |       45        |
| Acetone training|        36.35     |      20.51   |     1021.60    |         15.81       |       15        |
| Acetone test    |        35.44     |      19.63   |     1018.92    |         14.18       |       15        |

The image below shows the resistance change over time when the sensor was exposed to acetone and air. The highlighted area shows the resistance change when the sensor was exposed to acetone for the first cycle. WWhen the sensor was exposed to air the resistance decreased notably. The average resistance here was X
![alt text](images/graf_test1-10_2_hour.png)

Compared to the reference air, the resistance change for acetone was significant. This is a good indication that the sensor can be trained to detect it at least at relatively high concentration.

#### AI training

Using the BME studio software an algorithm was trained to detect acetone. The training data set was used to train the data with a 70/30 split. 
The image below shows the confusion matrix for the training data set.
![confusion matrix](images/test2_10_training.png)

The table below shows the accuracy of the training data set.

| Accuracy | F1 score | False positive |
| -------- | -------- | -------------- |
| 96.01%   | 96.11%   | 4.01%          |

#### AI testing
USing the BME studio software the trained algorithm was tested with the test data set. The image below shows the confusion matrix for the test data set.
![confusion matrix](images/test_2_10_test.png)
This show that the algorithm was able to detect acetone with a high accuracy.

| Accuracy | F1 score | False positive |
| -------- | -------- | -------------- |
| 91.54%   | 91.53%   | 8.55%          |

## Test 2


# Relevant publications 

1. Z. Wang, C. Wang and P. Lathan, Breath Acetone Analysis of Diabetic Dogs Using a Cavity Ringdown Breath Analyzer, in IEEE Sensors Journal, [doi: 10.1109/JSEN.2013.2293705](https://ieeexplore.ieee.org/document/6678180).
2. Saasa V, Malwela T, Beukes M, Mokgotho M, Liu CP, Mwakikunga B. Sensing Technologies for Detection of Acetone in Human Breath for Diabetes Diagnosis and Monitoring. Diagnostics (Basel). 2018 Jan 31;8(1):12. [doi: 10.3390/diagnostics8010012](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5871995/).  
 
