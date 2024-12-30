
`iw dev`


not connected
```sh
glitch@wifi:~$ iw dev
phy#2
        Interface wlan2
                ifindex 5
                wdev 0x200000001
                addr 02:00:00:00:02:00
                type managed
                txpower 20.00 dBm
```

connected to ap
```sh
glitch@wifi:~$ iw dev
phy#2
        Unnamed/non-netdev interface
                wdev 0x200000002
                addr 42:00:00:00:02:00
                type P2P-device
                txpower 20.00 dBm
        Interface wlan2
                ifindex 5
                wdev 0x200000001
                addr 02:00:00:00:02:00
                ssid MalwareM_AP
                type managed
                channel 6 (2437 MHz), width: 20 MHz (no HT), center1: 2437 MHz
                txpower 20.00 dBm
```

### Help

```sh
glitch@wifi:~$ iw --help
Usage:  iw [options] command
Options:
        --debug         enable netlink debugging
        --version       show version (5.16)
Commands:
        dev <devname> ap start 
                <SSID> <control freq> [5|10|20|40|80|80+80|160] [<center1_freq> [<center2_freq>]] <beacon interval in TU> <DTIM period> [hidden-ssid|zeroed-ssid] head <beacon head in hexadecimal> [tail <beacon tail in hexadecimal>] [inactivity-time <inactivity time in seconds>] [key0:abcde d:1:6162636465]


        dev <devname> ap stop 
                Stop AP functionality


        phy <phyname> coalesce enable <config-file>
                Enable coalesce with given configuration.
                The configuration file contains coalesce rules:
                  delay=<delay>
                  condition=<condition>
                  patterns=<[offset1+]<pattern1>,<[offset2+]<pattern2>,...>
                  delay=<delay>
                  condition=<condition>
                  patterns=<[offset1+]<pattern1>,<[offset2+]<pattern2>,...>
                  ...
                delay: maximum coalescing delay in msec.
                condition: 1/0 i.e. 'not match'/'match' the patterns
                patterns: each pattern is given as a bytestring with '-' in
                places where any byte may be present, e.g. 00:11:22:-:44 will
                match 00:11:22:33:44 and 00:11:22:33:ff:44 etc. Offset and
                pattern should be separated by '+', e.g. 18+43:34:00:12 will
                match '43:34:00:12' after 18 bytes of offset in Rx packet.


        phy <phyname> coalesce disable 
                Disable coalesce.

        phy <phyname> coalesce show 
                Show coalesce status.

        dev <devname> disconnect
                Disconnect from the current network.

        dev <devname> connect [-w] <SSID> [<freq in MHz>] [<bssid>] [auth open|shared] [key 0:abcde d:1:6162636465] [mfp:req/opt/no]
                Join the network with the given SSID (and frequency, BSSID).
                With -w, wait for the connect to finish or fail.

        dev <devname> auth <SSID> <bssid> <type:open|shared> <freq in MHz> [key 0:abcde d:1:6162636465]
                Authenticate with the given network.


        dev <devname> cqm rssi <threshold|off> [<hysteresis>]
                Set connection quality monitor RSSI threshold.


        event [-t|-T|-r] [-f]
                Monitor events from the kernel.
                -t - print timestamp
                -T - print absolute, human-readable timestamp
                -r - print relative timestamp
                -f - print full frame for auth/assoc etc.

        dev <devname> ftm get_stats 
                Get FTM responder statistics.


        dev <devname> ftm start_responder [lci=<lci buffer in hex>] [civic=<civic buffer in hex>]
                Start an FTM responder. Needs a running ap interface


        phy <phyname> hwsim getps 


        phy <phyname> hwsim setps <value>


        phy <phyname> hwsim stopqueues 


        phy <phyname> hwsim wakequeues 


        dev <devname> ibss leave
                Leave the current IBSS cell.

        dev <devname> ibss join <SSID> <freq in MHz> [NOHT|HT20|HT40+|HT40-|5MHz|10MHz|80MHz] [fixed-freq] [<fixed bssid>] [beacon-interval <TU>] [basic-rates <rate in Mbps,rate2,...>] [mcast-rate <rate in Mbps>] [key d:0:abcde]
                Join the IBSS cell with the given SSID, if it doesn't exist create
                it on the given frequency. When fixed frequency is requested, don't
                join/create a cell on a different frequency. When a fixed BSSID is
                requested use that BSSID and do not adopt another cell's BSSID even
                if it has higher TSF and the same SSID. If an IBSS is created, create
                it with the specified basic-rates, multicast-rate and beacon-interval.

        phy <phyname> info
                Show capabilities for the specified wireless device.

        list
                List all wireless devices and their capabilities.

        phy
        commands
                list all known commands and their decimal & hex value

        features 


        phy <phyname> interface add <name> type <type> [mesh_id <meshid>] [4addr on|off] [flags <flag>*] [addr <mac-addr>]
                Add a new virtual interface with the given configuration.
                Valid interface types are: managed, ibss, monitor, mesh, wds.

                The flags are only used for monitor interfaces, valid flags are:
                none:     no special flags
                fcsfail:  show frames with FCS errors
                control:  show control frames
                otherbss: show frames from other BSSes
                cook:     use cooked mode
                active:   use active mode (ACK incoming unicast packets)
                mumimo-groupid <GROUP_ID>: use MUMIMO according to a group id
                mumimo-follow-mac <MAC_ADDRESS>: use MUMIMO according to a MAC address

                The mesh_id is used only for mesh mode.

        dev <devname> interface add <name> type <type> [mesh_id <meshid>] [4addr on|off] [flags <flag>*] [addr <mac-addr>]
        dev <devname> del
                Remove this virtual interface

        dev <devname> info
                Show information for this interface.

        dev
                List all network interfaces for wireless hardware.

        dev <devname> switch freq <freq> [NOHT|HT20|HT40+|HT40-|5MHz|10MHz|80MHz] [beacons <count>] [block-tx]
        dev <devname> switch freq <control freq> [5|10|20|40|80|80+80|160] [<center1_freq> [<center2_freq>]] [beacons <count>] [block-tx]
                Switch the operating channel by sending a channel switch announcement (CSA).

        dev <devname> switch channel <channel> [NOHT|HT20|HT40+|HT40-|5MHz|10MHz|80MHz] [beacons <count>] [block-tx]
        help [command]
                Print usage for all or a specific command, e.g.
                "help wowlan" or "help wowlan enable".

        dev <devname> link
                Print information about the current link, if any.

        dev <devname> measurement ftm_request <config-file> [timeout=<seconds>] [randomise[=<addr>/<mask>]]
                Send an FTM request to the targets supplied in the config file.
                Each line in the file represents a target, with the following format:
                <addr> bw=<[20|40|80|80+80|160]> cf=<center_freq> [cf1=<center_freq1>] [cf2=<center_freq2>] [ftms_per_burst=<samples per burst>] [ap-tsf] [asap] [bursts_exp=<num of bursts exponent>] [burst_period=<burst period>] [retries=<num of retries>] [burst_duration=<burst duration>] [preamble=<legacy,ht,vht,dmg>] [lci] [civic] [tb] [non_tb]

        dev <devname> mesh join <mesh ID> [[freq <freq in MHz> <NOHT|HT20|HT40+|HT40-|80MHz>] [basic-rates <rate in Mbps,rate2,...>]], [mcast-rate <rate in Mbps>] [beacon-interval <time in TUs>] [dtim-period <value>] [vendor_sync on|off] [<param>=<value>]*
                Join a mesh with the given mesh ID with frequency, basic-rates,
                mcast-rate and mesh parameters. Basic-rates are applied only if
                frequency is provided.

        dev <devname> mesh leave
                Leave a mesh.

        dev <devname> mesh_param dump 
                List all supported mesh parameters

        dev <devname> mgmt dump frame <type as hex ab> <pattern as hex ab:cd:..> [frame <type> <pattern>]* [count <frames>]
                Register for receiving certain mgmt frames and print them.
                Frames are selected by their type and pattern containing
                the first several bytes of the frame that should match.

                Example: iw dev wlan0 mgmt dump frame 40 00 frame 40 01:02 count 10


        dev <devname> mpath probe <destination MAC address> frame <frame>
                Inject ethernet frame to given peer overriding the next hop
                lookup from mpath table.
                .Example: iw dev wlan0 mpath probe xx:xx:xx:xx:xx:xx frame 01:xx:xx:00


        dev <devname> mpath get <MAC address>
                Get information on mesh path to the given node.

        dev <devname> mpath del <MAC address>
                Remove the mesh path to the given node.

        dev <devname> mpath new <destination MAC address> next_hop <next hop MAC address>
                Create a new mesh path (instead of relying on automatic discovery).

        dev <devname> mpath set <destination MAC address> next_hop <next hop MAC address>
                Set an existing mesh path's next hop.

        dev <devname> mpath dump
                List known mesh paths.

        dev <devname> mpp get <MAC address>
                Get information on mesh proxy path to the given node.

        dev <devname> mpp dump
                List known mesh proxy paths.

        wdev <idx> nan start pref <pref> [bands [2GHz] [5GHz]]


        wdev <idx> nan stop 


        wdev <idx> nan config [pref <pref>] [bands [2GHz] [5GHz]]


        wdev <idx> nan rm_func cookie <cookie>


        wdev <idx> nan add_func type <publish|subscribe|followup> [active] [solicited] [unsolicited] [bcast] [close_range] name <name> [info <info>] [flw_up_id <id> flw_up_req_id <id> flw_up_dest <mac>] [ttl <ttl>] [srf <include|exclude> <bf|list> [bf_idx] [bf_len] <mac1;mac2...>] [rx_filter <str1:str2...>] [tx_filter <str1:str2...>]


        dev <devname> ocb join <freq in MHz> <5MHz|10MHz>
                Join the OCB mode network.

        dev <devname> ocb leave
                Leave the OCB mode network.

        dev <devname> offchannel <freq> <duration>
                Leave operating channel and go to the given channel for a while.

        wdev <idx> p2p start 


        wdev <idx> p2p stop 


        phy <phyname> channels
                Show available channels.

        dev <devname> cac channel <channel> [NOHT|HT20|HT40+|HT40-|5MHz|10MHz|80MHz]
        dev <devname> cac freq <freq> [NOHT|HT20|HT40+|HT40-|5MHz|10MHz|80MHz]
        dev <devname> cac freq <control freq> [5|10|20|40|80|80+80|160] [<center1_freq> [<center2_freq>]]
        dev <devname> cac trigger channel <channel> [NOHT|HT20|HT40+|HT40-|5MHz|10MHz|80MHz]
        dev <devname> cac trigger freq <frequency> [NOHT|HT20|HT40+|HT40-|5MHz|10MHz|80MHz]
        dev <devname> cac trigger freq <frequency> [5|10|20|40|80|80+80|160] [<center1_freq> [<center2_freq>]]
                Start or trigger a channel availability check (CAC) looking to look for
                radars on the given channel.

        reg set <ISO/IEC 3166-1 alpha2>
                Notify the kernel about the current regulatory domain.

        reg get
                Print out the kernel's current regulatory domain information.

        phy <phyname> reg get
                Print out the devices' current regulatory domain information.

        reg reload
                Reload the kernel's regulatory database.

        dev <devname> roc start <freq> <time in ms>


        dev <devname> scan [-u] [freq <freq>*] [duration <dur>] [ies <hex as 00:11:..>] [meshid <meshid>] [lowpri,flush,ap-force,duration-mandatory] [randomise[=<addr>/<mask>]] [ssid <ssid>*|passive]
                Scan on the given frequencies and probe for the given SSIDs
                (or wildcard if not given) unless passive scanning is requested.
                If -u is specified print unknown data in the scan results.
                Specified (vendor) IEs must be well-formed.

        dev <devname> scan dump [-u]
                Dump the current scan results. If -u is specified, print unknown
                data in scan results.

        dev <devname> scan trigger [freq <freq>*] [duration <dur>] [ies <hex as 00:11:..>] [meshid <meshid>] [lowpri,flush,ap-force,duration-mandatory,coloc] [randomise[=<addr>/<mask>]] [ssid <ssid>*|passive]
                Trigger a scan on the given frequencies with probing for the given
                SSIDs (or wildcard if not given) unless passive scanning is requested.
                Duration(in TUs), if specified, will be used to set dwell times.


        dev <devname> scan abort 
                Abort ongoing scan

        dev <devname> scan sched_start [interval <in_msecs> | scan_plans [<interval_secs:iterations>*] <interval_secs>] [delay <in_secs>] [freqs <freq>+] [matches [ssid <ssid>]+]] [active [ssid <ssid>]+|passive] [randomise[=<addr>/<mask>]] [coloc] [flush]
                Start a scheduled scan at the specified interval on the given frequencies
                with probing for the given SSIDs (or wildcard if not given) unless passive
                scanning is requested.  If matches are specified, only matching results
                will be returned.

        dev <devname> scan sched_stop 
                Stop an ongoing scheduled scan.

        dev <devname> get mesh_param [<param>]
                Retrieve mesh parameter (run command without any to see available ones).

        phy <phyname> get txq 
                Get TXQ parameters.

        dev <devname> get power_save 
                Retrieve power save state.

        dev <devname> set bitrates [legacy-<2.4|5> <legacy rate in Mbps>*] [ht-mcs-<2.4|5> <MCS index>*] [vht-mcs-<2.4|5> [he-mcs-<2.4|5|6> <NSS:MCSx,MCSy... | NSS:MCSx-MCSy>*] [sgi-2.4|lgi-2.4] [sgi-5|lgi-5] [he-gi-<2.4|5|6> <0.8|1.6|3.2>] [he-ltf-<2.4|5|6> <1|2|4>]
                Sets up the specified rate masks.
                Not passing any arguments would clear the existing mask (if any).

        dev <devname> set monitor <flag>*
                Set monitor flags. Valid flags are:
                none:     no special flags
                fcsfail:  show frames with FCS errors
                control:  show control frames
                otherbss: show frames from other BSSes
                cook:     use cooked mode
                active:   use active mode (ACK incoming unicast packets)
                mumimo-groupid <GROUP_ID>: use MUMIMO according to a group id
                mumimo-follow-mac <MAC_ADDRESS>: use MUMIMO according to a MAC address

        dev <devname> set meshid <meshid>
        dev <devname> set type <type>
                Set interface type/mode.
                Valid interface types are: managed, ibss, monitor, mesh, wds.

        dev <devname> set 4addr <on|off>
                Set interface 4addr (WDS) mode.

        dev <devname> set noack_map <map>
                Set the NoAck map for the TIDs. (0x0009 = BE, 0x0006 = BK, 0x0030 = VI, 0x00C0 = VO)

        dev <devname> set peer <MAC address>
                Set interface WDS peer.

        dev <devname> set mcast_rate <rate in Mbps>
                Set the multicast bitrate.

        dev <devname> set tidconf [peer <MAC address>] tids <mask> [override] [sretry <num>] [lretry <num>] [ampdu [on|off]] [amsdu [on|off]] [noack [on|off]] [rtscts [on|off]][bitrates <type [auto|fixed|limit]> [legacy-<2.4|5> <legacy rate in Mbps>*] [ht-mcs-<2.4|5> <MCS index>*] [vht-mcs-<2.4|5> <NSS:MCSx,MCSy... | NSS:MCSx-MCSy>*] [sgi-2.4|lgi-2.4] [sgi-5|lgi-5]]
                Setup per-node TID specific configuration for TIDs selected by bitmask.
                If MAC address is not specified, then supplied TID configuration
                applied to all the peers.
                Examples:
                  $ iw dev wlan0 set tidconf tids 0x1 ampdu off
                  $ iw dev wlan0 set tidconf tids 0x5 ampdu off amsdu off rtscts on
                  $ iw dev wlan0 set tidconf tids 0x3 override ampdu on noack on rtscts on
                  $ iw dev wlan0 set tidconf peer xx:xx:xx:xx:xx:xx tids 0x1 ampdu off tids 0x3 amsdu off rtscts on
                  $ iw dev wlan0 set tidconf peer xx:xx:xx:xx:xx:xx tids 0x2 bitrates auto
                  $ iw dev wlan0 set tidconf peer xx:xx:xx:xx:xx:xx tids 0x2 bitrates limit vht-mcs-5 4:9


        dev <devname> set mesh_param <param>=<value> [<param>=<value>]*
                Set mesh parameter (run command without any to see available ones).

        phy <phyname> set name <new name>
                Rename this wireless device.

        phy <phyname> set freq <freq> [NOHT|HT20|HT40+|HT40-|5MHz|10MHz|80MHz|160MHz]
        phy <phyname> set freq <control freq> [5|10|20|40|80|80+80|160] [<center1_freq> [<center2_freq>]]
                Set frequency/channel the hardware is using, including HT
                configuration.

        dev <devname> set freq <freq> [NOHT|HT20|HT40+|HT40-|5MHz|10MHz|80MHz|160MHz]
        dev <devname> set freq <control freq> [5|10|20|40|80|80+80|160] [<center1_freq> [<center2_freq>]]
        phy <phyname> set channel <channel> [NOHT|HT20|HT40+|HT40-|5MHz|10MHz|80MHz|160MHz]
        dev <devname> set channel <channel> [NOHT|HT20|HT40+|HT40-|5MHz|10MHz|80MHz|160MHz]
        phy <phyname> set frag <fragmentation threshold|off>
                Set fragmentation threshold.

        phy <phyname> set rts <rts threshold|off>
                Set rts threshold.

        phy <phyname> set retry [short <limit>] [long <limit>]
                Set retry limit.

        phy <phyname> set netns { <pid> | name <nsname> }
                Put this wireless device into a different network namespace:
                    <pid>    - change network namespace by process id
                    <nsname> - change network namespace by name from /run/netns
                               or by absolute path (man ip-netns)


        phy <phyname> set coverage <coverage class>
                Set coverage class (1 for every 3 usec of air propagation time).
                Valid values: 0 - 255.

        phy <phyname> set distance <auto|distance>
                Enable ACK timeout estimation algorithm (dynack) or set appropriate
                coverage class for given link distance in meters.
                To disable dynack set valid value for coverage class.
                Valid values: 0 - 114750

        phy <phyname> set txpower <auto|fixed|limit> [<tx power in mBm>]
                Specify transmit power level and setting type.

        dev <devname> set txpower <auto|fixed|limit> [<tx power in mBm>]
                Specify transmit power level and setting type.

        phy <phyname> set antenna <bitmap> | all | <tx bitmap> <rx bitmap>
                Set a bitmap of allowed antennas to use for TX and RX.
                The driver may reject antenna configurations it cannot support.

        phy <phyname> set txq limit <packets> | memory_limit <bytes> | quantum <bytes>
                Set TXQ parameters. The limit and memory_limit are global queue limits
                for the whole phy. The quantum is the DRR scheduler quantum setting.
                Valid values: 1 - 2**32

        dev <devname> set power_save <on|off>
                Set power save state to on or off.

        phy <phyname> set sar_specs <sar type> <range index:sar power>*
                Set SAR specs corresponding to SAR capa of wiphy.

        dev <devname> survey dump
                List all gathered channel survey data

        dev <devname> vendor send <oui> <subcmd> <filename|-|hex data>


        dev <devname> vendor recv <oui> <subcmd> <filename|-|hex data>


        dev <devname> vendor recvbin <oui> <subcmd> <filename|-|hex data>


        phy <phyname> wowlan enable [any] [disconnect] [magic-packet] [gtk-rekey-failure] [eap-identity-request] [4way-handshake] [rfkill-release] [net-detect [interval <in_msecs> | scan_plans [<interval_secs:iterations>*] <interval_secs>] [delay <in_secs>] [freqs <freq>+] [matches [ssid <ssid>]+]] [active [ssid <ssid>]+|passive] [randomise[=<addr>/<mask>]] [coloc] [flush]] [tcp <config-file>] [patterns [offset1+]<pattern1> ...]
                Enable WoWLAN with the given triggers.
                Each pattern is given as a bytestring with '-' in places where any byte
                may be present, e.g. 00:11:22:-:44 will match 00:11:22:33:44 and
                00:11:22:33:ff:44 etc.
                Offset and pattern should be separated by '+', e.g. 18+43:34:00:12 will match '43:34:00:12' after 18 bytes of offset in Rx packet.

                The TCP configuration file contains:
                  source=ip[:port]
                  dest=ip:port@mac
                  data=<hex data packet>
                  data.interval=seconds
                  [wake=<hex packet with masked out bytes indicated by '-'>]
                  [data.seq=len,offset[,start]]
                  [data.tok=len,offset,<token stream>]

                Net-detect configuration example:
                 iw phy0 wowlan enable net-detect interval 5000 delay 30 freqs 2412 2422 matches ssid foo ssid bar

        phy <phyname> wowlan disable 
                Disable WoWLAN.

        phy <phyname> wowlan show 
                Show WoWLAN status.

        dev <devname> station get <MAC address>
                Get information for a specific station.

        dev <devname> station del <MAC address> [subtype <subtype>] [reason-code <code>]
                Remove the given station entry (use with caution!)
                Example subtype values: 0xA (disassociation), 0xC (deauthentication)

        dev <devname> station dump [-v]
                List all stations known, e.g. the AP on managed interfaces

        dev <devname> station set <MAC address> txpwr <auto|limit> [<tx power dBm>]
                Set Tx power for this station.

        dev <devname> station set <MAC address> airtime_weight <weight>
                Set airtime weight for this station.

        dev <devname> station set <MAC address> mesh_power_mode <active|light|deep>
                Set link-specific mesh power mode for this station

        dev <devname> station set <MAC address> vlan <ifindex>
                Set an AP VLAN for this station.

        dev <devname> station set <MAC address> plink_action <open|block>
                Set mesh peer link action for this station (peer).


Commands that use the netdev ('dev') can also be given the
'wdev' instead to identify the device.

You can omit the 'phy' or 'dev' if the identification is unique,
e.g. "iw wlan0 info" or "iw phy0 info". (Don't when scripting.)

Do NOT screenscrape this tool, we don't consider its output stable.
```