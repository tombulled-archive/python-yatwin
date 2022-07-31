# python-yatwin
Python 3 API for Vstarcam and YATWIN IP Cameras (Windows)

<p align="center">
	<img src="https://www.tivaict.com/images/c24s.png" alt="Vstarcam C24H Black 720P WiFi IP Camera" width="500px">
</p>

## Cameras Tested
| Camera                                            | Link                                                                                                  |
| ------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| C24H Black 720P WiFi IP Camera                    | http://www.yatwintech.com/Products-list-detail.html?product_id=56                                     |
| Vstarcam C7824WIP-Plus 720P                       | https://www.vstarcam.com.sg/Smart-IP-Cameras/Indoor/C7824WIP-Plus                                     |
| Vstarcam C24S-Plus FullHD 1080P Wide Angle Camera | https://www.vstarcam.com.sg/Smart-IP-Cameras/Indoor/Vstarcam-C24S-Plus-FullHD-1080P-Wide-Angle-Camera |

## Installation
```sh
Download and install wheel from: https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio (pip install path_to_wheel)

pip install ffmpeg-python
pip install opencv-python
pip install onvif_zeep
pip install comtypes
```

## Getting Started
```python
>>> import yatwin.scripts
>>>
>>> # Scan network and hack any cameras it finds
>>> cams = yatwin.scripts.hack_cameras()
>>> cams
[<BaseHackedYatwin
(
	http:      <Http(admin:888888@192.168.1.223:80)>
	icmp:      <Icmp(192.168.1.223)>
	onvif:     <Onvif(admin:888888@192.168.1.223:10080)>
	telnet:    <Telnet(vstarcam2017:20170912@192.168.1.223:23)>
	ftp:       None
	multicast: <Multicast()>
	imap:      None
	rtsp:      <Rtsp(admin:888888@192.168.1.223:10554)[udp/av1_0]>
)>]
>>>
>>> # Pick the first camera
>>> cam = cams[0]
>>> 
>>> # Access the cameras Telnet interface
>>> cam.telnet
<Telnet(vstarcam2017:20170912@192.168.1.223:23)>
>>> print(cam.telnet.ls())
bin            init           mknod_console  root           tmp
boot           lib            mnt            sbin           usr
dev            linuxrc        nfsroot        share          var
etc            lost+found     opt            sys
home           mkimg.rootfs   proc           system
>>>
>>> from pprint import pprint
>>>
>>> # Get the cameras RTSP parameters using HTTP
>>> pprint(cam.http.get_rtsp())
{<SystemParam(rtspport)>: 10554,
 <SystemParam(rtsppwd)>: '888888',
 <SystemParam(rtspuser)>: 'admin',
 <SystemParam(rtsp_auth_enable)>: 1}
>>> 
```

## Helpful Libraries
| Name                | Link                                                 |
| ------------------- | ---------------------------------------------------- |
| python-onvif-zeep   | https://github.com/FalkTannhaeuser/python-onvif-zeep |
| Requests            | https://github.com/requests/requests                 |
| vlc-python          | https://github.com/geoffsalmon/vlc-python            |
| Beautiful Soup      | https://www.crummy.com/software/BeautifulSoup/       |
| python-ws-discovery | https://github.com/andreikop/python-ws-discovery     |
| pyffmpeg            | https://github.com/mhaller/pyffmpeg                  |
| python-nmap         | https://xael.org/pages/python-nmap-en.html           |
| OpenCV              | https://opencv.org/                                  |

## Helpful Resources
| Name        | Resource                                                                          |
| ----------- | --------------------------------------------------------------------------------- |
| Pierre Kim  | https://pierrekim.github.io/blog/2017-03-08-camera-goahead-0day.html              |
| 4dpa.ru     | https://4pda.ru/forum/lofiversion/index.php?t782299.html                          |
| David Lodge | https://www.pentestpartners.com/security-blog/hacking-the-ip-camera-part-1/       |
| Z           | https://jumpespjump.blogspot.com/2015/09/how-i-hacked-my-ip-camera-and-found.html |