# Fast-CSV-Search
## (Really FAST) FastAPI service to query a CSV file* 
##### * - (any CSV that has the column names defined as first line)



-----


#### Size of example database (CSV file) is 830KB, ~18K lines:

```
$ (Fast-CSV-Search) ➜  compatlist_search-fastapi wc -l file.csv 
   17949 file.csv
```

#### Runtime, note the query serving time:

```
$ (Fast-CSV-Search) ➜ uvicorn app:app --reload

INFO:     Started server process [60041]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
PERF:	  Query served in 0.011279 seconds
INFO:     127.0.0.1:49992 - "GET /search/?query=111 HTTP/1.1" 200 OK
PERF:	  Query served in 0.008723 seconds
INFO:     127.0.0.1:49992 - "GET /search/?query=115 HTTP/1.1" 200 OK
PERF:	  Query served in 0.007777 seconds
INFO:     127.0.0.1:49994 - "GET /search/?query=111 HTTP/1.1" 200 OK
PERF:	  Query served in 0.059983 seconds
INFO:     127.0.0.1:49994 - "GET /search/?query= HTTP/1.1" 200 OK
PERF:	  Query served in 0.026290 seconds
INFO:     127.0.0.1:49997 - "GET /search/?query=adapter HTTP/1.1" 200 OK
```

#### Example HTTP reply:

```wrap
{"results":[{"vendor_n_device_id":"1013:1112","device_name":"PD 6834 PCMCIA/CardBus Ctrlr","driver":" ✅"},{"vendor_n_device_id":"1095:3112","device_name":"SiI 3112 [SATALink/SATARaid] Serial ATA Controller","driver":" ✅"},{"vendor_n_device_id":"10b5:8112","device_name":"PEX8112 x1 Lane PCI Express-to-PCI Bridge","driver":" ✅"},{"vendor_n_device_id":"10de:0112","device_name":"NV11M [GeForce2 Go]","driver":" ✅"},{"vendor_n_device_id":"10df:f112","device_name":"Saturn-X LightPulse Fibre Channel Host Adapter","driver":" ✅"},{"vendor_n_device_id":"1106:1122","device_name":"VX800/VX820 Chrome 9 HC3 Integrated Graphics","driver":" ✅"},{"vendor_n_device_id":"1106:3112","device_name":"VT8361 [KLE133] Host Bridge","driver":" ✅"},{"vendor_n_device_id":"1106:b112","device_name":"VT8361 [KLE133] AGP Bridge","driver":" ✅"},{"vendor_n_device_id":"1112:2200","device_name":"FDDI Adapter","driver":" ✅"},{"vendor_n_device_id":"1112:2300","device_name":"Fast Ethernet Adapter","driver":" ✅"},{"vendor_n_device_id":"1112:2340","device_name":"4 Port Fast Ethernet Adapter","driver":" ✅"},{"vendor_n_device_id":"1112:2400","device_name":"ATM Adapter","driver":" ✅"},{"vendor_n_device_id":"1119:0112","device_name":"GDT 6537RD","driver":" ✅"},{"vendor_n_device_id":"1120:2306","device_name":"Unity Fibre Channel Controller","driver":" ✅"},{"vendor_n_device_id":"1120:2501","device_name":"Unity Ethernet Controller","driver":" ✅"},{"vendor_n_device_id":"1120:2505","device_name":"Unity Fibre Channel Controller","driver":" ✅"},{"vendor_n_device_id":"1124:2581","device_name":"Picport Monochrome","driver":" ✅"},{"vendor_n_device_id":"1127:0200","device_name":"ForeRunner PCA-200 ATM","driver":" ✅"},{"vendor_n_device_id":"1127:0210","device_name":"PCA-200PC","driver":" ✅"},{"vendor_n_device_id":"1127:0250","device_name":"ATM","driver":" ✅"},{"vendor_n_device_id":"1127:0300","device_name":"ForeRunner PCA-200EPC ATM","driver":" ✅"},{"vendor_n_device_id":"1127:0310","device_name":"ATM","driver":" ✅"},{"vendor_n_device_id":"1127:0400","device_name":"ForeRunnerHE ATM Adapter","driver":" ✅"},{"vendor_n_device_id":"112b:0001","device_name":"SCU5","driver":" ✅"},{"vendor_n_device_id":"112f:0000","device_name":"MVC IC-PCI","driver":" ✅"},{"vendor_n_device_id":"112f:0001","device_name":"MVC IM-PCI Video frame grabber/processor","driver":" ✅"},{"vendor_n_device_id":"112f:0004","device_name":"PCDig Digital Image Capture","driver":" ✅"},{"vendor_n_device_id":"112f:0008","device_name":"PC-CamLink PCI framegrabber","driver":" ✅"},{"vendor_n_device_id":"118d:0112","device_name":"Model 12 Road Runner Frame Grabber","driver":" ✅"},{"vendor_n_device_id":"119f:1121","device_name":"BXI Host Channel Adapter v1.3","driver":" ✅"},{"vendor_n_device_id":"11f6:0112","device_name":"ENet100VG4","driver":" ✅"},{"vendor_n_device_id":"1217:7112","device_name":"OZ711EC1/M1 SmartCardBus/MemoryCardBus Controller","driver":" ✅"},{"vendor_n_device_id":"1556:1112","device_name":"QuickPCIe","driver":" ✅"},{"vendor_n_device_id":"16e2:1120","device_name":"GX1120 Arbitrary Waveform and Function Generator PXI Board","driver":" ✅"},{"vendor_n_device_id":"179c:5112","device_name":"DP-cPCI-5112 [MM-Carrier]","driver":" ✅"},{"vendor_n_device_id":"17d3:1120","device_name":"ARC-1120 8-Port PCI-X to SATA RAID Controller","driver":" ✅"},{"vendor_n_device_id":"194a:1112","device_name":"FireSpy450b","driver":" ✅"},{"vendor_n_device_id":"1a3b:1112","device_name":"AR9285 Wireless Network Adapter (PCI-Express)","driver":" ✅"},{"vendor_n_device_id":"1def:e112","device_name":"Altra PCI Express Root Port b1","driver":" ✅"},{"vendor_n_device_id":"1fde:1125","device_name":"OpenEdge 1125P","driver":" ✅"},{"vendor_n_device_id":"8086:0112","device_name":"2nd Generation Core Processor Family Integrated Graphics Controller","driver":" ✅"},{"vendor_n_device_id":"8086:7112","device_name":"82371AB/EB/MB PIIX4 USB","driver":" ✅"},{"vendor_n_device_id":"8086:8112","device_name":"US15W/US15X/US15L/UL11L SCH [Poulsbo] PCI Express Port 2","driver":" ✅"},{"vendor_n_device_id":"8086:a112","device_name":"100 Series/C230 Series Chipset Family PCI Express Root Port #3","driver":" ✅"}]}
```

#### Sponsored by:
This was created for AlmaLinux as _Simple FastAPI service for Driver Compatibility Table (List) Searching_.
