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

