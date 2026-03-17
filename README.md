# Hermes — AI Drone Delivery System

Hermes is an **AI-enhanced autonomous drone delivery system** designed for efficient and safe aerial deliveries in the **Nigerian logistics ecosystem**.

---

## Project Overview

Hermes combines **computer vision**, **autonomous navigation**, and **real-time backend orchestration** to deliver small packages with precision and reliability.

### Core Capabilities

* Autonomous drone navigation and obstacle avoidance (YOLOv8 + LIDAR)
* Secure payload management with OTP/fingerprint authentication
* Real-time telemetry, logging, and fleet monitoring
* NCAA-compliant flight and safety protocols
* Modular microservice architecture (ROS2 + FastAPI)

---

## Project Structure

```
Hermes/
├── src/
│   ├── drone_core/              # Navigation, flight control, path planning
│   ├── ai_vision/              # YOLOv8 vision, obstacle detection, TensorRT
│   ├── delivery_operations/     # Delivery dispatch, payload management
│   ├── safety_monitoring/       # Telemetry, compliance, health checks
│   └── backend_services/        # FastAPI microservices (auth, delivery, fleet)
│
├── simulation/
│   ├── drone_simulation/        # Gazebo simulation launch files
│   │   ├── launch/
│   │   │   └── gazebo_world.launch.py
│   │   ├── urdf/                # Drone model definitions
│   │   └── worlds/              # Gazebo world files
│   ├── drone_models/            # Custom drone models (hexacopter)
│   └── scenarios/               # Simulation test cases
│
├── config/                      # YAML configs (nodes, sensors, topics)
├── launch/                      # System launch configurations
├── tests/                       # Unit and integration tests
├── docs/                        # Documentation and specs
└── README.md
```

---

## Technology Stack

| Layer                  | Technology                            | Purpose                                 |
| ---------------------- | ------------------------------------- | --------------------------------------- |
| **Flight Control**     | PX4 + MAVLink                         | Autopilot firmware and communication    |
| **Robotics Framework** | ROS2 Humble                           | Node orchestration and middleware       |
| **Simulation**         | Gazebo                                | Environment and flight simulation       |
| **AI & Vision**        | YOLOv8 (Ultralytics), OpenCV, PyTorch | Obstacle and object detection           |
| **Backend**            | FastAPI + PostgreSQL + SQLAlchemy     | Mission control, user management, APIs  |
| **Security**           | OAuth 2.0 + JWT + TLS 1.3             | Secure authentication and communication |
| **Compute**            | NVIDIA Jetson Orin Nano               | Edge inference                          |
| **Monitoring**         | Prometheus + Grafana (later)          | System telemetry visualization          |

---

## System Architecture

```
┌─────────────────────────────┐
│       Mobile / Web App      │
│  (User Orders & Tracking)   │
└──────────────┬──────────────┘
               │ REST / WebSocket
┌──────────────┴──────────────┐
│     Backend (FastAPI)       │
│  - Auth Service             │
│  - Delivery Dispatcher      │
│  - Fleet Manager            │
│  - Telemetry API            │
└──────────────┬──────────────┘
               │ ROS2 Topic/Service
┌──────────────┴──────────────┐
│        ROS2 Drone Nodes     │
│  - drone_vision_node        │
│  - path_planner_node        │
│  - telemetry_node           │
│  - controller_node          │
│  - payload_manager_node     │
└──────────────┬──────────────┘
               │ MAVLink
┌──────────────┴──────────────┐
│          PX4 Firmware       │
│   (Flight Control & Safety) │
└─────────────────────────────┘
```

---

## Setup Instructions

### 1. Clone Repository

```bash
git clone https://github.com/your-username/Hermes.git
cd Hermes
```

### 2. Build ROS2 Workspace

```bash
colcon build
source install/setup.bash
```

### 3. Launch Simulation

```bash
ros2 launch drone_simulation gazebo_world.launch.py
```

### 4. Run Core Nodes

```bash
ros2 run drone_core path_planner_node
ros2 run ai_vision drone_vision_node
ros2 run safety_monitoring telemetry_node
```

### 5. Start Backend

```bash
cd src/backend_services
uvicorn main:app --reload --port 8000
```

---

## Core Concepts

| Concept                       | Description                                                |
| ----------------------------- | ---------------------------------------------------------- |
| **ROS2 Nodes**                | Modular components for navigation, vision, and telemetry   |
| **MAVLink**                   | Communication protocol between drone and flight controller |
| **PX4 SITL**                  | Software-in-the-loop testing environment                   |
| **YOLOv8 Integration**        | Real-time object detection for dynamic obstacle avoidance  |
| **FastAPI Backend**           | Manages missions, user auth, and data persistence          |
| **Simulation-first Approach** | Develop all systems virtually before hardware integration  |

---

## Project Development Checklist

### Phase 1 — Environment Setup

* [ ] Install ROS2 Humble & dependencies
* [ ] Setup Gazebo + PX4 SITL simulation
* [x] Create base project structure
* [ ] Verify colcon build and source

### Phase 2 — Core Node Development

* [x] `drone_vision_node` — YOLOv8 + camera streaming
* [x] `telemetry_node` — MAVLink telemetry
* [x] `path_planner_node` — GPS path planning
* [x] `controller_node` — flight command handler

### Phase 3 — AI & Backend Integration

* [ ] Collect Nigerian obstacle dataset
* [ ] Optimize YOLOv8 with TensorRT for Jetson
* [ ] Setup FastAPI backend with OAuth2.0
* [ ] Integrate ROS2 <-> FastAPI via WebSockets

### Phase 4 — Testing & Optimization

* [ ] Full mission simulation (pickup → delivery → return)
* [ ] Emergency RTH testing
* [ ] Network latency < 200ms verification
* [ ] Telemetry logging and analytics

### Phase 5 — Hardware & Compliance

* [ ] Procure components (Pixhawk, Jetson, LIDAR)
* [ ] HITL testing with real sensors
* [ ] NCAA compliance documentation
* [ ] Pilot delivery run

---

## Future Roadmap

| Phase   | Goal                                          |
| ------- | --------------------------------------------- |
| **MVP** | Single-drone simulation and delivery          |
| **V2**  | Hardware prototype + AI optimization          |
| **V3**  | Fleet management and multi-drone coordination |
| **V4**  | Commercial rollout and cloud monitoring       |

---

## License

MIT License © 2025 Hermes Project

