# PowerClient
This is a simple client checking the Live-In Smartgrid API if there is a peak in the power demand

It's using micropython on an ESP8266 to read out the power status
and showing a simple graph of the history of the powertrend.

The calls can easily be changed to instead control different processes
and local GPIO's feel free to invent.

# How to access 

Goto http://my.liv-in.se/join to create your account and get your
token then use curl to test the api out

'curl -i -H "Accept: application/json" -H "Content-Type: text/json" -H
"Authorization: B
'earer DinApiNyckel" -X POST https://my.live-in.se/api/powerstatus

## verbosity

'curl -i -H "Accept: application/json" -H "Content-Type: text/json" -H
'"Authorization: Bearer DinApiNyckel" --data '{"verbose":"1"}' -X POST
'https://my.live-in.se/api/powerstatus

    * 0 simplest level you will only get the output 0 or 1 back

    * 1 standard level

    * 2 more expressive output



## location

'curl -i -H "Accept: application/json" -H "Content-Type: text/json" -H
'"Authorization: Bearer DinApiNyckel" --data '{"location:{"zipcode":"ABC123"}}' -X POST
'https://my.live-in.se/api/powerstatus

    * zipcode

    *  region

    *  grid


