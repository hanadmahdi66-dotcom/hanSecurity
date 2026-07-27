# 🛡️ Han Security Tool

<div align="center">

```
██╗  ██╗ █████╗ ███╗   ██╗
██║  ██║██╔══██╗████╗  ██║
███████║███████║██╔██╗ ██║
██╔══██║██╔══██║██║╚██╗██║
██║  ██║██║  ██║██║ ╚████║
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝
```

### 🐍 Network Security Monitoring Tool

**A lightweight defensive network analyzer built with Python & Scapy & hanOS Engine**

</div>

---

# 📌 Overview

**Han Security Tool** is a defensive cybersecurity project designed to help
security learners and administrators understand network traffic.

The tool captures and analyzes network packets to provide visibility into:

* 🌐 IP communication
* 🔌 TCP connections
* 📡 DNS queries
* 🖥️ Network devices
* 📊 Traffic behavior

Built for learning, monitoring, and authorized security testing.

---

# ✨ Features

## 🌐 Network Traffic Monitor

Analyze network communication:

```
Source IP  → Destination IP
```

Example:

```
192.168.1.221 → 20.42.65.89
```

---

## 🔍 TCP Analyzer

Monitor TCP connections:

```
Protocol: TCP

52064 → 443
```

Useful for understanding:

* HTTPS connections
* Network sessions
* Port activity

---

## 🌎 DNS Monitor

Track DNS requests:

Example:

```
Device:
192.168.1.221

Domain:
google.com
```

Helps understand:

* Domain activity
* Network behavior
* Security investigation

---

## 🖥️ ARP Monitor

Observe IP-to-MAC relationships:

```
IP Address            MAC Address

192.168.1.1     →     cc:cf:83:b8:94:c0
```

Useful for defensive network visibility.

---

# 🏗️ Architecture

```
                 Network Traffic

                       │

                       ▼

                  hanOS Engine

                       │

                       ▼

              Packet Analyzer


                       |

                       ▼


                       │

          ┌────────────┴────────────┐

          ▼                         ▼

     TCP Monitor              DNS Monitor

          │                         │

          └────────────┬────────────┘

                       ▼

              Security Reports
```

---

# 🛠️ Technologies

| Technology      | Purpose                |
| --------------- | ---------------------- |
| Python          | Core language          |
| Scapy           | Packet analysis        |
| SQLite          | Local storage (future) |
| Linux / Windows | Supported environments |

---

# 📦 Installation

Clone repository:

```bash
git clone https://github.com/hanadmahdi66-dotcom/han-security-tool.git
```

Enter folder:

```bash
cd han-security-tool
```

Install requirements:

```bash
pip install -r requirements.txt
```

Run:

```bash
python main.py
```

---

# 📋 Requirements

```
Python 3.10+
Scapy
Npcap (Windows)
```

Windows users need Npcap installed for packet capture support.

---

# 🖥️ Example Output

```
========================

HAN SECURITY TOOL

========================


SOURCE:
192.168.1.221

DESTINATION:
20.42.65.89

PROTOCOL:
TCP

PORT:
52064 → 443

========================
```

---

# 🔐 Security Purpose

This project is created for:

✅ Defensive security learning
✅ Network monitoring
✅ Cybersecurity education
✅ Authorized testing
✅ Understanding protocols

---

# ⚠️ Legal Disclaimer

This tool must only be used on:

* Networks you own
* Systems you manage
* Environments where you have permission

Unauthorized monitoring, interception, or access to networks is prohibited.

The developer is not responsible for misuse of this software.

---

# 🚀 Roadmap

Future improvements:

* [ ] SQLite logging
* [ ] Security alerts
* [ ] Traffic reports
* [ ] Device discovery
* [ ] Rule-based detection
* [ ] Flask dashboard
* [ ] Export reports

---

# 👨‍💻 Author

**Hanad**

Building defensive security tools with:

🐍 Python
🛡️ Cybersecurity
🌐 Networking
🤖 Technology

---

# ⭐ Support

If this project helps you learn network security,
consider giving it a ⭐ on GitHub.

---

**Stay curious. Stay secure. 🛡️**
