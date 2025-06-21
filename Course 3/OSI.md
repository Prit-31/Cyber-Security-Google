# OSI Model vs TCP/IP Model

## OSI Model – 7 Layers

| Layer | Name               | Purpose                                               | Example Protocols / Devices            |
|-------|--------------------|-------------------------------------------------------|----------------------------------------|
| 7     | Application        | End-user access to network applications               | HTTP, FTP, DNS, SMTP                   |
| 6     | Presentation       | Data translation, encryption, compression             | SSL/TLS, JPEG, ASCII, MPEG             |
| 5     | Session            | Manage sessions and control dialogues                 | NetBIOS, RPC, PPTP                     |
| 4     | Transport          | Reliable or best-effort delivery                      | TCP, UDP, SCTP                         |
| 3     | Network            | Routing, logical addressing                           | IP, ICMP, ARP, RIP, OSPF               |
| 2     | Data Link          | MAC addressing, framing, and error detection          | Ethernet, PPP, Switches                |
| 1     | Physical           | Raw bits over cables, connectors, voltages            | Hubs, Cables, NICs, Radio Waves        |

---

## TCP/IP Model – 4 Layers

| Layer | OSI Equivalent                   | Purpose                                | Example Protocols                      |
|-------|----------------------------------|----------------------------------------|----------------------------------------|
| 4     | Application (7–5)                | User interface, encryption, sessions   | HTTP, FTP, DNS, Telnet, SMTP           |
| 3     | Transport (4)                    | Reliable/Unreliable transmission       | TCP, UDP                               |
| 2     | Internet (3)                     | Addressing and routing                 | IP, ICMP, ARP                          |
| 1     | Network Interface (2–1)          | Physical transmission, MAC addressing | Ethernet, Wi-Fi, Token Ring, PPP       |

---

## Mapping OSI ↔ TCP/IP Layers

| OSI Layer         | TCP/IP Layer            |
|-------------------|-------------------------|
| 7 Application      | 4 Application           |
| 6 Presentation     | 4 Application           |
| 5 Session          | 4 Application           |
| 4 Transport        | 3 Transport             |
| 3 Network          | 2 Internet              |
| 2 Data Link        | 1 Network Interface     |
| 1 Physical         | 1 Network Interface     |

---

## Key Differences

| Feature            | OSI Model                 | TCP/IP Model              |
|--------------------|---------------------------|---------------------------|
| Layers             | 7                         | 4                         |
| Design Approach    | Theoretical, generic      | Practical, implementation |
| Protocol Dependency| Protocol-independent      | Based on standard protocols |
| Used In            | Academic, teaching        | Real-world networking     |

