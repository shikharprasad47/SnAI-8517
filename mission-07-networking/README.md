Concept	|       Explain it in your own words      |    Example

LAN	 | A network covering a small area, such as a home, lab or office.   | 	A home Wi-Fi network or college computer lab connecting local devices.

MAN	 | A network covering a city or large campus area.  |	A university campus network linking multiple buildings or a city-wide broadband network.

WAN	 | A network covering large geographical areas.	 |   The global Internet or a bank's network connecting branches across countries.

DNS	 |  Translates a domain name into an IP address.  | 	Converting any site into its numeric IP address so browser can reach the server.

Router	|   Connects networks and forwards data between them.   |	A home Wi-Fi router forwarding requests from your laptop to your ISP and the Internet.

Protocol    |	A set of rules devices follow to communicate.   |	HTTPS (for secure web browsing)

Packet switching    |	Data is divided into packets that travel across a network.  |	Splitting a webpage or video stream into small data packets that route independently and reassemble at the destination.

Client-server   |   A client requests a service and a server provides it.   |   Your web browser (client) requesting a webpage from GitHub's web server (server).

Task 7.2

We can use,

    ping -c 3 (example.com)
    nslookup (example.com)

Ping sends small ICMP echo packets to a target host and measures whether a reply comes back and how fast (round-trip time in milliseconds), confirming that the system has an active internet connection and can reach the remote server.

"nslookup" shows the DNS resolver used and the public IPv4 and/or IPv6 addresses mapped to the domain name "example.com".

Humans type easy-to-remember domain names like "example.com", while network routers locate servers using numeric IP addresses, DNS acts like the internet's phonebook by looking up and returning the server's IP address before the browser connects.

Task 7.3

User enters a URL: You type a website address (such as [https://example.com](https://example.com)) into your web browser, which acts as the client.

DNS lookup: The browser asks a DNS resolver to translate the human-readable domain name into the web server's numeric IP address.

Routing the connection: Your device sends the request through your local network and router across the internet toward that IP address, establishing a connection using network protocols like TCP/IP.

HTTP/HTTPS request: Following the HTTPS protocol, the client sends a request message asking the server for the webpage's files.

Server processes and responds: The server receives the request, prepares the webpage data (HTML, CSS, JavaScript), splits it into data packets, and sends the response back to your IP address.

Browser renders the page: Your client browser reassembles the incoming packets and renders the visual webpage on your screen.



[This was the mission I learnt alot and had to read things twice or thrice to get it, this was also the mission I took A.I's help. (I'm sorry for that)]


Mission 7 - How computers communicate

1. Task / objective
Explain core computer networking concepts (LAN, MAN, WAN, DNS, router, protocol, packet switching, and client-server), observe safe network connectivity and DNS lookup behavior from Terminal without exposing private IP or Wi-Fi details, and trace what happens step by step when opening a website.

2. Work completed
- Completed Task 7.1 by filling out the eight-row networking concepts table with clear explanations and real-world examples.
- Completed Task 7.2 by running privacy-safe connectivity ("ping") and DNS lookup ("nslookup") checks against "example.com" in Terminal and explaining what each tool reveals.
- Completed Task 7.3 by writing a six-step sequence describing how a client browser, DNS, router, protocols, and web server communicate to load and render a webpage.
- Saved all documentation in "mission-07-networking/README.md" and pushed the commit to GitHub.

3. Commands / tools used
- "ping -c 3 example.com" — Tested network reachability and measured packet round-trip time to a public server.
- "nslookup example.com" — Queried DNS to resolve the human-readable domain name into its public IP address.
- "git add", "git commit", and "git push" — Staged, committed, and published Mission 7 to GitHub.

4. My understanding
Computer networks scale from local home or lab setups (LAN) to campus/city networks (MAN) and global networks like the Internet (WAN). When I enter a URL in a browser (client), DNS translates the domain name into an IP address, routers forward divided data packets across networks following shared protocols like TCP/IP and HTTPS, and the remote server returns the webpage data for my browser to display.

5. Difficulties faced
There were few things that I had forgot about like ping and things

6. How I resolved them
I did asked A.I to help me with that part and asked it to teach me again what it is and how it actually works

7. Evidence / files
- "mission-07-networking/README.md" (containing the Task 7.1 network concepts table, Task 7.2 safe connectivity and DNS lookup notes, and Task 7.3 step-by-step website loading explanation)

8. Commit details
Committed with message "Explain networking concepts and website communication" and pushed to "origin/master" on GitHub.