from . import nmap
from . import ws_discovery
import xml.etree

"""
Library containing <Multicast>

Imports:
    .nmap
    .ws_discovery
    xml.etree
"""

class Multicast(object):
    """
    Class designed for sending *wsdd discover* packets.
    """

    def __init__(self):
        """
        Initialises self
        """

        self._init_attrs()

    def __repr__(self):
        """
        Returns a string representation of the object
        ... in the form <class_name()>
        """

        return f'<{self.__class__.__name__}()>'

    def discover(self, *args, **kwargs):
        """
        Shorthand wrapper for self.ws_discover
        """

        return self.ws_discover(*args, **kwargs)

    def ws_discover(self):
        """
        Broadcasts *wsdd discover* packets using ws_discovery
        
        Returns a list of services
        ... Where each service is a dictionary of values
        """

        wsd = ws_discovery.WSDiscovery()
        wsd.start()

        ttype = ws_discovery.QName("abc", "def")

        ttype1 = ws_discovery.QName("namespace", "myTestService")
        scope1 = ws_discovery.Scope("http://myscope")
        ttype2 = ws_discovery.QName("namespace", "myOtherTestService_type1")
        scope2 = ws_discovery.Scope("http://other_scope")

        xAddrs = ["localhost:8080/abc", '{ip}/device_service']
        wsd.publishService(types=[ttype], scopes=[scope2], xAddrs=xAddrs)

        ret = wsd.searchServices()

        wsd.stop()

        services = []

        for service in ret:
            data = \
            {
                'XAddrs': service.getXAddrs(),
                'EPR': service.getEPR(),
                'InstanceID': service.getInstanceId(),
                'MetadataVersion': service.getMetadataVersion(),
                'Scopes': service.getScopes(),
                'Types': service.getTypes(),
                '_Service': service,
            }

            services.append(data)

        return services

    def broadcast_wsdd_discover_nmap(self, arguments='-Pn'):
        """
        Broadcasts a *wsdd discover* packet, then returns a parsed response.
        This uses nmap (self.PortScanner)

        :param arguments - arguments to be passes to nmap
            Changing these two much can affect the response
        """

        scan = self.PortScanner.scan(hosts='', arguments=arguments + ' --script=broadcast-wsdd-discover')

        script_output = self._get_nmap_broadcast_wsdd_discover_script_output()

        if script_output is None:
            return

        parsed = self._parse_nmap_broadcast_wsdd_discover(script_output)

        return parsed

    def _get_nmap_broadcast_wsdd_discover_script_output(self):
        """
        Finds the <prescript> tag in the nmap xml output
        Then returns what was inside.
        """

        output = self.PortScanner._nmap_last_output

        xml_tree = xml.etree.ElementTree.fromstring(output)

        prescript = xml_tree.find('prescript')

        if prescript is None:
            return

        script = prescript.find('script')
        script_output = script.get('output')

        return script_output

    def _parse_nmap_broadcast_wsdd_discover(self, script_output):
        """
        Parses the <prescript> output from an nmap *wsdd discover* packet
        Returns a dictionary
        """

        script_output = script_output.strip()

        indent_struct = []

        for line in script_output.splitlines():
            spaces = len(line) - len(line.lstrip(' '))
            tabs = spaces // 4

            if not tabs:
                indent_struct.append([line.strip(), []])

                continue

            if tabs == 1:
                indent_struct[-1][1].append([line.strip(), []])
            elif tabs == 2:
                indent_struct[-1][1][-1][1].append([line.strip(), []])

        indent_dict = self._indent_struct_to_dict(indent_struct)

        data = {}

        for device_category_index, device_category_item in enumerate(indent_dict):
            for device_category, device_category_contents in device_category_item.items():
                data[device_category] = []
                for ip_index, ip_item in enumerate(device_category_contents):
                    for ip, ip_contents in ip_item.items():
                        ip_data = {}
                        for detail in ip_contents:
                            detail_dict = self._parse_line(detail)
                            ip_data.update(detail_dict)
                        data[device_category].append({ip: ip_data})

        return data

    def _indent_struct_to_dict(self, indent_struct):
        """
        Returns a parsed dictionary of 'indent_struct'
        ... distinguishing keys from values based on indentation
        This is recursive
        """

        indent_dict_list = []

        for key, sub_indent_struct in indent_struct:
            sub_indent_struct_dict = self._indent_struct_to_dict(sub_indent_struct)

            if sub_indent_struct_dict:
                indent_dict_list.append({key: sub_indent_struct_dict})
            else:
                indent_dict_list.append(key)

        return indent_dict_list

    def _parse_line(self, line):
        """
        Parses a single 'line' into {key: val}
        """

        key, *line_items = line.split(':')
        key = key.strip()
        line = ':'.join(line_items).strip()

        return {key: line}

    def _init_attrs(self):
        """
        Initialises the class attributes
        It creates them, then fills them with a default/null value (usualy None)
        """

        self.PortScanner = nmap.PortScanner()
