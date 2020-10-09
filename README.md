<h2>Tor-Ip-Changer2 </h2>

<h4>Author : RKT</h4>

### Descripton ###

![tor-network-zdnet-guide-e1506772864127](https://user-images.githubusercontent.com/69615463/95173099-dc46fb80-07d5-11eb-97a0-e802bf754a4b.jpg)

Tor is a anonymity network.This network  also provide us secure connection and secure browsing.we can  browse any website anonymously.Our internet traffic is encryted. Anyone can't monitor our browsing history ,download and protect to tracking.I have create a tor-ip-changer2 script.This is a python program.This program can change our tor idenity/ip.

### What is TOR(The Onion Router) ? ###

Tor is free and open-source software for enabling anonymous communication. The name derived from the acronym for the original software project name "The Onion Router".Tor directs Internet traffic through a free, worldwide, volunteer overlay network consisting of more than seven thousand relays to conceal a user's location and usage from anyone conducting network surveillance or traffic analysis. Using Tor makes it more difficult to trace Internet activity to the user: this includes "visits to Web sites, online posts, instant messages, and other communication forms".Tor's intended use is to protect the personal privacy of its users, as well as their freedom and ability to conduct confidential communication by keeping their Internet activities unmonitored.

Tor does not prevent an online service from determining that it is being accessed through Tor. Tor protects a user's privacy, but does not hide the fact that someone is using Tor. Some websites restrict allowances through Tor. For example, Wikipedia blocks attempts by Tor users to edit articles unless special permission is sought.

Onion routing is implemented by encryption in the application layer of a communication protocol stack, nested like the layers of an onion. Tor encrypts the data, including the next node destination IP address, multiple times and sends it through a virtual circuit comprising successive, random-selection Tor relays. Each relay decrypts a layer of encryption to reveal the next relay in the circuit to pass the remaining encrypted data on to it. The final relay decrypts the innermost layer of encryption and sends the original data to its destination without revealing or knowing the source IP address. Because the routing of the communication was partly concealed at every hop in the Tor circuit, this method eliminates any single point at which the communicating peers can be determined through network surveillance that relies upon knowing its source and destination.An adversary may try to de-anonymize the user by some means. One way this may be achieved is by exploiting vulnerable software on the user's computer.The NSA had a technique that targets a vulnerability – which they codenamed "EgotisticalGiraffe" – in an outdated Firefox browser version at one time bundled with the Tor package and, in general, targets Tor users for close monitoring under its XKeyscore program.Attacks against Tor are an active area of academic research which is welcomed by the Tor Project itself.The bulk of the funding for Tor's development has come from the federal government of the United States,initially through the Office of Naval Research and DARPA. 

The alpha version of Tor, developed by Syverson and computer scientists Roger Dingledine and Nick Mathewson and then called The Onion Routing project, or Tor project, launched on 20 September 2002.The first public release occurred a year later.On 13 August 2004, Syverson, Dingledine, and Mathewson presented "Tor: The Second-Generation Onion Router" at the 13th USENIX Security Symposium.In 2004, the Naval Research Laboratory released the code for Tor under a free license, and the Electronic Frontier Foundation (EFF) began funding Dingledine and Mathewson to continue its development.

In December 2006, Dingledine, Mathewson, and five others founded The Tor Project, a Massachusetts-based 501(c)(3) research-education nonprofit organization responsible for maintaining Tor.The EFF acted as The Tor Project's fiscal sponsor in its early years, and early financial supporters of The Tor Project included the U.S. International Broadcasting Bureau, Internews, Human Rights Watch, the University of Cambridge, Google, and Netherlands-based Stichting NLnet.

Prior to 2014, the majority of funding sources came from the U.S. government.

In November 2014 there was speculation in the aftermath of Operation Onymous that a Tor weakness had been exploited.A BBC News source cited a "technical breakthrough" that allowed the tracking of the physical locations of servers. In November 2015 court documents on the matter,besides generating serious concerns about security research ethics and the right of not being unreasonably searched guaranteed by the US Fourth Amendment,may also link the law enforcement operation with an attack on Tor earlier in the year.

In December 2015, The Tor Project announced that it had hired Shari Steele as its new executive director.Steele had previously led the Electronic Frontier Foundation for 15 years, and in 2004 spearheaded EFF's decision to fund Tor's early development. One of her key stated aims is to make Tor more user-friendly in order to bring wider access to anonymous web browsing.

In July 2016 the complete board of the Tor Project resigned, and announced a new board, made up of Matt Blaze, Cindy Cohn, Gabriella Coleman, Linus Nordberg, Megan Price, and Bruce Schneier. 
 

### First,We need to open the firefox browser and configure SOCKS Proxy in Firefox. ###

![Screenshot at 2020-10-06 08-11-58](https://user-images.githubusercontent.com/69615463/95177022-49a95b00-07db-11eb-9313-4aa585f843ed.png)


### We need to install Tor on our system. Open a terminal and type the following command to install it: ### 

$sudo apt install tor

### Now,we have started tor network.Open a terminal and type the following command : ###

$sudo service tor start
 
### git clone ###

<ul>
<li>git clone https://github.com/r3k4t/tor-ip-changer2.git</li>
<li>cd tor-ip-changer2</li>
<li>sudo python3 tor-ip-changer2.py</li>

![Screenshot at 2020-10-06 15-52-20](https://user-images.githubusercontent.com/69615463/95190504-0eb02300-07ed-11eb-9d17-618966b1e74d.png)


### Old idenity ###

![Screenshot at 2020-10-06 15-50-30](https://user-images.githubusercontent.com/69615463/95190383-db6d9400-07ec-11eb-9699-0087da85223d.png)

### New idenity ###

![Screenshot at 2020-10-06 15-52-38](https://user-images.githubusercontent.com/69615463/95190437-f2ac8180-07ec-11eb-82f3-ed6ff96552c4.png)

