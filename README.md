<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f0c29,50:302b63,100:24243e&height=200&section=header&text=Krishna%20Hna&fontSize=60&fontColor=ffffff&fontAlignY=38&desc=Software%20Engineer%20%7C%20Systems%20Builder%20%7C%20AI%2FML%20Researcher&descAlignY=58&descSize=18&animation=fadeIn" width="100%" alt="header"/>

[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&pause=1000&color=7C3AED&center=true&vCenter=true&width=700&lines=Building+systems+that+scale+from+edge+to+cloud;Deep+learning+%7C+IoT+%7C+Full-Stack+%7C+Embedded+C%2B%2B;React+Native+%7C+Next.js+%7C+Python+%7C+TypeScript;Turning+real-world+problems+into+engineered+solutions)](https://git.io/typing-svg)

<p>
  <img src="https://komarev.com/ghpvc/?username=kris07hna&label=Profile+Views&color=7C3AED&style=flat-square" alt="profile views"/>
  <img src="https://img.shields.io/github/followers/kris07hna?label=Followers&style=flat-square&color=7C3AED" alt="followers"/>
  <a href="https://github.com/kris07hna?tab=repositories"><img src="https://img.shields.io/badge/Repositories-View%20All-7C3AED?style=flat-square" alt="repos"/></a>
</p>

</div>

---

## About

I'm a full-stack systems engineer who operates across the entire stack — from C++ firmware on ESP32 microcontrollers to deep learning pipelines in PyTorch, to production-grade React Native and Next.js applications. My work is driven by one consistent principle: **engineer solutions to real problems at the right level of abstraction**.

I don't build demos. I build systems — with documented architecture, modular code, and genuine deployment considerations.

**What I work on:**
- **Edge + Cloud hybrid systems** — real-time IoT pipelines where latency and reliability matter
- **ML / Signal Processing** — deep learning applied to audio enhancement, medical inference, and NLP
- **Cross-platform mobile** — offline-first architectures with cryptographic integrity guarantees
- **Embedded systems** — sensor fusion, hardware-software co-design, firmware in C++

---

## Tech Stack

<div align="center">

**Languages**

![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![C++](https://img.shields.io/badge/C++-00599C?style=for-the-badge&logo=c%2B%2B&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![R](https://img.shields.io/badge/R-276DC3?style=for-the-badge&logo=r&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-4479A1?style=for-the-badge&logo=postgresql&logoColor=white)

**Frameworks & Runtimes**

![React Native](https://img.shields.io/badge/React_Native-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)
![Next.js](https://img.shields.io/badge/Next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white)
![Node.js](https://img.shields.io/badge/Node.js-339933?style=for-the-badge&logo=nodedotjs&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)
![Expo](https://img.shields.io/badge/Expo-000020?style=for-the-badge&logo=expo&logoColor=white)

**Infrastructure & Tooling**

![Supabase](https://img.shields.io/badge/Supabase-3ECF8E?style=for-the-badge&logo=supabase&logoColor=white)
![Firebase](https://img.shields.io/badge/Firebase-FFCA28?style=for-the-badge&logo=firebase&logoColor=black)
![Vercel](https://img.shields.io/badge/Vercel-000000?style=for-the-badge&logo=vercel&logoColor=white)
![WebSocket](https://img.shields.io/badge/WebSocket-010101?style=for-the-badge&logo=socket.io&logoColor=white)
![PlatformIO](https://img.shields.io/badge/PlatformIO-F5822A?style=for-the-badge&logo=platformio&logoColor=white)

**Domains**

![IoT](https://img.shields.io/badge/IoT%20%2F%20Embedded-FF6F00?style=for-the-badge&logo=arduino&logoColor=white)
![Deep Learning](https://img.shields.io/badge/Deep%20Learning-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)
![Signal Processing](https://img.shields.io/badge/Signal%20Processing-4B0082?style=for-the-badge&logoColor=white)
![Blockchain](https://img.shields.io/badge/Web3%20%2F%20Ethereum-3C3C3D?style=for-the-badge&logo=ethereum&logoColor=white)
![Edge Computing](https://img.shields.io/badge/Edge%20Computing-0078D4?style=for-the-badge&logo=microsoftazure&logoColor=white)

</div>

---

## Featured Projects

> Ranked by technical depth, architectural complexity, and real-world impact.

---

### 🥇 1 — VITRide · Campus Edge-Transport System

> *Offline-first campus transit with edge computing, hardware integration, cryptographic ticketing, and crypto payments*

**Stack:** React Native (Expo) · Node.js Edge Server · ESP32 · Supabase · Ethereum Sepolia · WebSocket · mDNS

**Architecture Overview:**
```
Mobile App (React Native)
    |-- mDNS Auto-Discovery --> Edge Server (Node.js on laptop)
    |-- WebSocket (WS:3002) -->     |-- QR Validation (webcam)
    |                               |-- GPS Circle Broadcasting
    |                               `-- mDNS Advertisement
    |
    `-- HTTPS ------------->   Supabase Cloud (profiles, tickets, analytics)
                               ESP32 (GPS module, RGB LEDs, buzzer alerts)
```

**Why it's significant:**
- Implements zero-config networking with mDNS (`_vitride._tcp.local`) — no manual IP configuration required
- SHA-256 cryptographic ticket signatures allow offline validation with tamper-proof 24-hour expiry
- Three-tier proximity alerting (100 m / 50 m / 30 m circles) driven by Haversine distance computation over WebSocket
- MNEE token payment on Sepolia testnet alongside UPI integration — rare combination of Web2 + Web3 payments in a campus app
- Hardware-software co-design: ESP32 firmware synchronizes GPS coordinates to edge server, driving real-time proximity alerts

[![Repo](https://img.shields.io/badge/GitHub-VITRide-7C3AED?style=flat-square&logo=github)](https://github.com/kris07hna/VITRide)

---

### 🥈 2 — DeverbSamsung · Deep Learning Speech Dereverberation

> *State-of-the-art dereverberation system built for the Samsung PRISM competition, targeting PESQ and SDR maximization*

**Stack:** Python · PyTorch · Jupyter · Signal Processing (librosa, scipy) · PESQ / SDR metrics

**Architecture Overview:**
```
Raw Reverberant Audio
    |
    v
STFT Feature Extraction (complex spectrogram)
    |
    v
Deep Neural Network (U-Net / SGMSE-style)
  |-- Skip connections for spectral detail preservation
  |-- Score-based diffusion refinement
  `-- Multi-scale loss (PESQ + SI-SDR + spectral convergence)
    |
    v
Enhanced Waveform --> PESQ / SDR evaluation
```

**Why it's significant:**
- Targets real competition metrics (PESQ >= 3.5, SDR >= 18 dB) rather than toy reconstructions
- Score-based diffusion modeling applied to speech — research-level technique adapted for practical submission
- End-to-end pipeline from raw `.wav` preprocessing to final metric evaluation
- Related work: `sgmse-ultimate` explores SGMSE+ score-based generative speech enhancement

[![Repo](https://img.shields.io/badge/GitHub-DeverbSamsung-7C3AED?style=flat-square&logo=github)](https://github.com/kris07hna/DeverbSamsung)

---

### 🥉 3 — SmartShortCircuit · IoT Electrical Anomaly Detection System

> *Real-time short-circuit and overcurrent detection system bridging ESP32 hardware, INA219 precision sensing, and a Next.js dashboard*

**Stack:** C++ · PlatformIO · INA219 · ESP32 · Next.js · Firebase · WebSocket · Vercel

**Architecture Overview:**
```
INA219 Current/Voltage Sensor
    | I2C (400 kHz)
    v
ESP32 Firmware (C++)
  |-- Threshold anomaly detection (<5 ms response)
  |-- WiFi telemetry to Firebase RTDB
  `-- Hardware relay actuation (load isolation)
    |
    v
Firebase Realtime Database
    |
    v
Next.js Dashboard (Vercel)
  |-- Live current/voltage waveforms
  |-- Anomaly event log
  `-- Alert configuration UI
```

**Why it's significant:**
- Sub-5 ms hardware interrupt response time is the design target for short-circuit isolation — measured on ESP32 at 240 MHz with relay actuation; actual timing varies by hardware revision
- INA219 precision current sensing (0.1 mA resolution) with software-configurable thresholds
- Full stack from C++ firmware to cloud telemetry to web dashboard, all in one coherent system
- PlatformIO build system enables reproducible firmware builds across teams

[![Repo](https://img.shields.io/badge/GitHub-SmartShortCircuit-7C3AED?style=flat-square&logo=github)](https://github.com/kris07hna/SmartShortCircuit)

---

### 4 — PersonaFlux · AI-Powered NPC Dialogue System

> *Stateful, persona-consistent AI NPC engine with long-term memory, emotion modeling, and a real-time game interface*

**Stack:** TypeScript · Next.js · Supabase (pgvector) · LLM APIs · WebSocket · Tailwind CSS

**Architecture Overview:**
```
Game Client (React / Next.js)
    |-- REST / WebSocket --> Persona Engine API
                                |-- Persona State Manager
                                |     |-- Emotion Vector
                                |     |-- Long-term Memory (pgvector)
                                |     `-- Relationship Graph
                                |-- LLM Inference Layer
                                |     |-- System prompt construction
                                |     `-- Context window management
                                `-- Response Evaluator
                                      |-- Consistency checks
                                      `-- Safety filters
```

**Why it's significant:**
- Maintains NPC persona consistency across sessions using vector-indexed long-term memory (pgvector on Supabase)
- Emotion state machine influences dialogue generation — NPCs evolve emotionally based on player interactions
- Designed for game engine integration with documented API contracts
- Separates persona configuration from inference logic, enabling hot-swappable character profiles

[![Repo](https://img.shields.io/badge/GitHub-PersonaFlux--AI--Powered--NPC-7C3AED?style=flat-square&logo=github)](https://github.com/kris07hna/PersonaFlux-AI-Powered-NPC)

---

### 5 — NEXCare · Healthcare Platform

> *Full-stack TypeScript healthcare application with appointment management, patient records, and provider workflows*

**Stack:** TypeScript · React Native / Next.js · Supabase · Node.js

**Why it's significant:**
- Domain: healthcare requires higher data integrity and security standards than general consumer apps
- Multi-role architecture (patient, provider, admin) with row-level security at the database layer
- Demonstrates applied knowledge of privacy-conscious design patterns in a production TypeScript stack

[![Repo](https://img.shields.io/badge/GitHub-NEXCare-7C3AED?style=flat-square&logo=github)](https://github.com/kris07hna/NEXCare)

---

### 6 — DiabeticsAnalyst · Clinical ML Inference Pipeline

> *End-to-end machine learning pipeline for Type 2 diabetes risk stratification with lifestyle factor analysis*

**Stack:** Python · scikit-learn · pandas · Flask · HTML/CSS · Render

**Architecture Overview:**
```
Raw Patient Data (CSV / API input)
    |
    v
Feature Engineering
  |-- Lifestyle normalization (BMI, glucose, insulin)
  |-- Missing value imputation
  `-- Categorical encoding
    |
    v
Ensemble Classifier (Random Forest + Gradient Boosting)
  |-- SHAP explainability layer
  `-- Calibrated probability outputs
    |
    v
Flask REST API --> Web UI (deployed on Render)
```

**Why it's significant:**
- SHAP explainability — model outputs are interpretable, which is a clinical requirement
- Deployed on Render with a clean REST interface, not just a notebook
- Multiple iterations show progressive engineering refinement, not one-shot work

[![Repo](https://img.shields.io/badge/GitHub-DiabeticsAnalyst-7C3AED?style=flat-square&logo=github)](https://github.com/kris07hna/DiabeticsAnalyst)

---

## GitHub Statistics

<div align="center">

<img height="180em" src="https://github-readme-stats.vercel.app/api?username=kris07hna&show_icons=true&theme=tokyonight&include_all_commits=true&count_private=true&hide_border=true&bg_color=0d1117&title_color=7C3AED&icon_color=7C3AED&text_color=c9d1d9"/>
<img height="180em" src="https://github-readme-stats.vercel.app/api/top-langs/?username=kris07hna&layout=compact&theme=tokyonight&hide_border=true&bg_color=0d1117&title_color=7C3AED&text_color=c9d1d9&langs_count=8"/>

</div>

<div align="center">

[![GitHub Streak](https://streak-stats.demolab.com?user=kris07hna&theme=tokyonight&hide_border=true&background=0d1117&stroke=7C3AED&ring=7C3AED&fire=FF6B6B&currStreakLabel=7C3AED)](https://git.io/streak-stats)

</div>

---

## System Design Philosophy

```
Problem Definition
       |
       v
Constraint Analysis           <- latency, bandwidth, fault tolerance, cost
       |
       v
Component Boundary Design     <- separate concerns at the right granularity
       |
       v
Interface Contracts First     <- API contracts / message schemas before implementation
       |
       v
Incremental Delivery          <- working system at each stage, not big-bang releases
       |
       v
Observability Built-in        <- metrics, logs, health endpoints from day one
```

Every system I build follows this process. The VITRide edge server exposes a `/health` endpoint. The SmartShortCircuit firmware emits structured telemetry. The DiabeticsAnalyst API returns calibrated confidence intervals, not raw class labels.

---

## Engineering Standards

**Commit Convention** — [Conventional Commits](https://www.conventionalcommits.org/):
```
feat(auth): add SHA-256 offline ticket validation
fix(gps): correct Haversine calculation for antipodal points
perf(ws): reduce WebSocket heartbeat overhead by 40%
docs(api): document /validate endpoint request schema
chore(deps): upgrade expo-location to 16.5.5
refactor(inference): extract SHAP explainer into separate module
test(ticket): add edge cases for expired token handling
```

**Branch Model:**
```
main        -- production-ready, protected
develop     -- integration branch
feature/*   -- scoped feature work
fix/*       -- targeted bug fixes
release/*   -- release preparation
```

**Code Review Principles:**
- Every PR describes *why*, not just *what*
- Architecture decisions are documented in `ARCHITECTURE.md` or ADR files
- No PR merges with failing CI

---

## What Differentiates This Work

Most student projects are UI-over-database CRUD apps. The systems here address genuine engineering constraints:

| Constraint | How It Is Addressed |
|---|---|
| **No internet on the bus** | Offline-first cryptographic ticket validation (VITRide) |
| **Sub-5 ms fault response (design target)** | Hardware interrupt + relay actuation in C++ firmware (SmartShortCircuit) |
| **Real competition metrics** | PESQ / SDR optimization, not MSE minimization (DeverbSamsung) |
| **NPC memory across sessions** | pgvector long-term memory with persona consistency (PersonaFlux) |
| **Clinical explainability** | SHAP values alongside predictions (DiabeticsAnalyst) |
| **Zero-config networking** | mDNS service discovery — no IP configuration required (VITRide) |

---

## Performance & Optimization Strategy

| Layer | Strategy |
|---|---|
| **Mobile** | Offline-first with local SQLite, sync on reconnect; lazy loading screens; memo/useCallback for expensive renders |
| **Edge Server** | Single-process Node.js with non-blocking I/O; WebSocket multiplexing; in-memory ledger for hot validation paths |
| **Firmware (C++)** | Interrupt-driven I/O on ESP32; DMA for I2C sensor reads; watchdog timer for fault recovery |
| **ML Inference** | Batch prediction with vectorized NumPy ops; ONNX export for production deployment; SHAP pre-computation cached per session |
| **Database** | Row-level security avoids application-layer filtering overhead; pgvector IVFFlat index for NPC memory retrieval |
| **Frontend** | Static generation (Next.js) for dashboard pages; incremental static regeneration for data that changes infrequently |

---

## Deployment Strategy

| Project | Target | Method |
|---|---|---|
| VITRide (mobile) | Android / iOS | Expo EAS Build + OTA updates via Expo Updates |
| VITRide (edge) | On-premise laptop | PM2 process manager + systemd service on Linux |
| SmartShortCircuit | Vercel + Firebase | CI/CD via Vercel Git integration; firmware via PlatformIO OTA |
| PersonaFlux | Vercel | Next.js app deployment with Vercel serverless functions |
| DiabeticsAnalyst | Render | Docker-based Python service with health check endpoint |
| NEXCare | Vercel / Supabase | Supabase hosted backend; Next.js frontend on Vercel |

---

## Currently

- Building: real-time edge + cloud transport infrastructure with hardware-in-the-loop testing
- Exploring: diffusion-based audio enhancement (SGMSE+) and its production deployment constraints
- Reading: *Designing Data-Intensive Applications* — Kleppmann; *The Hardware Hacker* — Huang
- Open to: internships and research collaborations in systems engineering, AI/ML infrastructure, or embedded systems

---

## Connect

<div align="center">

[![GitHub](https://img.shields.io/badge/GitHub-kris07hna-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/kris07hna)

*"The best systems are not those that do the most, but those that fail gracefully and recover predictably."*

</div>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:24243e,50:302b63,100:0f0c29&height=120&section=footer" width="100%" alt="footer"/>

<!-- Topics / Keywords for GitHub discoverability:
react-native expo typescript python cpp iot esp32 edge-computing deep-learning
pytorch signal-processing speech-enhancement dereverberation websocket mdns
supabase firebase full-stack mobile-development embedded-systems machine-learning
ai nlp healthcare blockchain web3 ethereum pgvector nextjs node
-->
