# Mission 7 - How computers communicate

## 1. Task / objective
Explain basic network types and concepts, observe a connectivity test and a DNS lookup from the Terminal, and describe step by step what happens when a website opens.

## 2. Work completed
- Completed the network-concepts table with my own explanation and a real example for each (Task 7.1).
- Ran `ping` and `nslookup` / `dig` on the public test domain **example.com** and explained the results (Task 7.2).
- Wrote a 7-step explanation of opening a website (Task 7.3).
- My own IP address, router address and Wi-Fi name are **not** published — they are replaced with `[redacted]`.

### Task 7.1 - Network concepts

| Concept | Explained in my own words | Example |
|---------|---------------------------|---------|
| **LAN** (Local Area Network) | A network covering a small area such as a home, lab or office. Devices are close together and usually connected to one router or switch. | My laptop, phone and smart TV all connected to the Wi-Fi router at home; a college computer lab. |
| **MAN** (Metropolitan Area Network) | A network covering a whole city or a large campus, joining many LANs together. | A university connecting all its buildings across the city; a city-wide cable TV / broadband network. |
| **WAN** (Wide Area Network) | A network covering very large distances — countries or the whole world — usually by joining many smaller networks. | **The Internet** is the biggest WAN; a bank network linking branches across India. |
| **DNS** (Domain Name System) | The "phone book" of the internet. It translates an easy name like `example.com` into the IP address (a number) that computers actually use to find each other. | `nslookup example.com` returned `104.20.23.154`. |
| **Router** | A device that connects different networks and decides the best path to forward each piece of data towards its destination. | My home Wi-Fi router connects my home LAN to my internet provider's network. |
| **Protocol** | An agreed set of rules for how devices format, send and receive data, so different devices can understand each other. | **HTTP/HTTPS** for web pages, **TCP/IP** for delivering data, **DNS** for name lookups, **ICMP** used by `ping`. |
| **Packet switching** | Data is cut into small packets. Each packet travels separately, possibly by different routes, and they are put back together in the right order at the destination. | `ping` sent 4 separate packets of 56 bytes each; a video call is sent as thousands of packets every second. |
| **Client-server** | A client (my device/app) sends a request, and a server (a powerful computer) processes it and sends back a response. | Chrome (client) asks a web server for a page; the GitHub website (server) sends my repository page. |

### Task 7.2 - Observe network information
Full privacy-safe output: [`evidence/mission-07-network-output.txt`](../evidence/mission-07-network-output.txt)

**Connectivity test — `ping -c 4 example.com`**
```
PING example.com (104.20.23.154): 56 data bytes
64 bytes from 104.20.23.154: icmp_seq=0 ttl=59 time=29.504 ms
...
4 packets transmitted, 4 packets received, 0.0% packet loss
round-trip min/avg/max/stddev = 28.201/32.659/43.880/6.495 ms
```
**DNS lookup — `nslookup example.com`**
```
Server:   [redacted - my local router]
Non-authoritative answer:
Name:    example.com   Address: 104.20.23.154
Name:    example.com   Address: 172.66.147.243
```

- **What a connectivity test (`ping`) helps me check:** whether my computer can reach another computer over the network at all, and how fast. It sends small test packets (ICMP "echo requests") and waits for replies. I got **4/4 replies, 0 % packet loss**, with an average **round-trip time of about 33 ms**, so my internet connection was working well. `-c 4` limits it to 4 packets (otherwise it keeps going until Ctrl+C). If ping fails, the problem could be my Wi-Fi, the router, DNS or the remote server.
- **What a DNS lookup displays:** which DNS **server** answered my question (here, my home router — redacted), and the **IP address(es)** linked to the domain name. example.com had **two** IPv4 addresses (`104.20.23.154` and `172.66.147.243`) — big sites use several servers to share load and stay online. "Non-authoritative" means the answer came from a cache, not directly from the domain's own official DNS server. `dig +short example.com` gave the same two addresses.
- **Role of DNS when I type a website name:** computers find each other using IP addresses, but people remember names. When I type `example.com`, the browser first asks DNS "what is the IP address of example.com?". Only after DNS answers can the browser connect to that IP. Without DNS, I would have to type numbers like `104.20.23.154` for every website.

### Task 7.3 - What happens when I open a website?
Example: typing `https://example.com` in Chrome and pressing Enter.

1. **Browser (client) reads the address.** Chrome, acting as the **client**, sees that I want the domain `example.com` using the **HTTPS protocol**. It first checks whether it already remembers the IP address in its cache.
2. **DNS lookup.** If not cached, my computer asks a **DNS** server (through my router) to translate `example.com` into an IP address. DNS replies with `104.20.23.154`.
3. **Data leaves through the router.** My laptop sends the request over Wi-Fi to my home **router**, which forwards it to my internet provider. From there, many routers across the internet (a WAN) pass the data along, hop by hop, towards the destination IP. The data travels as **packets** (packet switching).
4. **Connection is set up.** My computer and the server create a reliable connection using **TCP** (a protocol that makes sure every packet arrives in order) and, because it is HTTPS, they agree on encryption keys (TLS) so nobody in the middle can read the data.
5. **HTTP request is sent.** The browser sends an HTTP request such as `GET /` asking the **server** for the home page.
6. **Server processes and responds.** The web **server** finds the page and sends back an HTTP response with a status code (`200 OK`) and the page's HTML, CSS, images, etc., again split into packets that travel back through the routers to me.
7. **Browser displays the page.** Chrome puts the packets back together, reads the HTML, requests any extra files it needs (images, scripts), and draws the finished page on my screen. All of this usually happens in well under a second.

## 3. Commands / tools used
| Command / tool | Purpose |
|----------------|---------|
| `ping -c 4 example.com` | Test if my computer can reach a public website and measure the round-trip time. |
| `nslookup example.com` | Ask DNS for the IP address of a domain and see which DNS server answered. |
| `dig +short example.com` | Another DNS lookup tool, showing only the IP addresses. |
| Chrome | Opened `example.com` to see the client-server process from the user side. |

`example.com` is a domain reserved for documentation and testing, so it is safe to use for this exercise.

## 4. My understanding
A network is just devices agreeing on rules (protocols) so they can exchange data. Networks come in sizes — LAN at home, MAN across a city, WAN across the world — and the internet is a giant network of networks connected by routers. The most interesting part was seeing DNS work: one `nslookup` showed the name being turned into numbers before any webpage can load. `ping` showed that data really is sent as separate small packets and takes about 30 ms to travel to the server and back. Opening a website is actually a chain of many steps — DNS, routing, TCP/TLS, HTTP request and response — that the browser hides from me.

## 5. Difficulties faced
1. The DNS lookup output showed the address of my own router as the DNS server, which is private network information.
2. I expected one IP address for example.com but got two.

## 6. How I resolved them
1. I replaced the router's address with `[redacted - my local router]` before saving the output, following the privacy rule. I only kept the public IP addresses of example.com, which are not personal.
2. I learned that popular websites are served from several machines (often through a content-delivery network), so DNS can return more than one address. Both addresses point to the same website, and `ping` simply used the first one.

## 7. Evidence / files
- `evidence/mission-07-network-output.txt` — `ping`, `nslookup` and `dig` output with private addresses redacted.

## 8. Commit details
- Commit message: **`Explain networking concepts and website communication`**
- Pushed to GitHub on `main` and verified online.
