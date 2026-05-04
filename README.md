# 🚗 Kinematic Bicycle Model Simulation

## 📌 Overview
This project implements a **kinematic bicycle model** to simulate and analyze vehicle motion under different steering and velocity inputs.

The objective is to understand how control inputs influence trajectory generation through a series of experiments, including circular motion, square paths, and figure-eight trajectories.

---

## 🎯 Objectives
- Model vehicle motion using a simplified kinematic approach  
- Explore the effect of steering and velocity on trajectories  
- Simulate different control strategies  
- Visualize motion in 2D space  

---

## ⚙️ Model Description
The kinematic bicycle model approximates a vehicle using a single front and rear wheel.

### State Variables
- `xc, yc` → vehicle position  
- `theta` → heading angle  
- `delta` → steering angle  
- `beta` → slip angle  

### Parameters
- `L` → wheelbase  
- `lr` → rear axle distance  
- `w_max` → maximum steering rate  
- `sample_time` → simulation step  

---

## 🔄 Simulation Logic
At each time step:
1. Update steering angle using angular velocity (`w`)
2. Compute slip angle (`beta`)
3. Update position and orientation using kinematic equations  

This iterative process generates the vehicle trajectory over time.

---

## 🧪 Experiments

### 1. Circular Motion
- Constant steering angle  
- Produces a circular trajectory  

### 2. Steering to Target Angle
- Steering increases until a desired value  
- Demonstrates controlled turning  

### 3. Square Path
- Steering applied at specific intervals  
- Produces sharp turns and straight segments  

### 4. Figure-Eight Trajectory
- Alternating steering direction  
- Generates a continuous figure-eight path  

---

## 📊 Visualization
Trajectories are plotted using `matplotlib` with equal axis scaling to preserve geometry.

---

## 🛠️ Technologies
- Python  
- NumPy  
- Matplotlib  

---

## ▶️ How to Run
```bash
pip install numpy matplotlib
python main.py
