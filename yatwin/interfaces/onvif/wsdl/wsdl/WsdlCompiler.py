from .. import assets
from .. import xsd

"""
Library containing:
    <WsdlCompiler>

Imports:
    ..assets
    ..xsd
"""

class WsdlCompiler(object):
    """
    Class allowing a parsed wsdl to be compiled.
    In this case, compilation means combining data from
    ... all available sources to produce a singualar
    ... compiled data-structure.
    """

    def __init__(self, wsdl_parser, xsd_scope=None, _parsed=None):
        """
        Initialises self.

        :param wsdl_parser - A <wsdl.WsdlParser> instance to be compiled.
        :xsd_scope - A list of <xsd.Xsd> instances which are
        ... imported/used by the wsdl
        ... Can leave None for auto-detection
        ... It's recommended to pass an xsd_scope of [onvif_xsd, common_xsd]
        ... This will save a lot of time if multiple wsdls are being compiled
        """

        self._init_attrs()

        self.WsdlParser = wsdl_parser

        self.parsed = self.WsdlParser.parse() if _parsed is None else _parsed

        if xsd_scope is None:
            onvif_xsd = xsd.Xsd(assets.XSD_ONVIF)
            common_xsd = xsd.Xsd(assets.XSD_COMMON)

            self.xsd_scope = [onvif_xsd, common_xsd]
        else:
            self.xsd_scope = xsd_scope

    def __repr__(self):
        """
        Returns a string representation of the object
        ... in the form <class_name(file_name)>
        """

        return f'<{self.__class__.__name__}({self.WsdlParser.WsdlSource._file_name})>'

    def compile(self):
        """
        Compiles a parsed form of self.WsdlParser into a singualar
        ... compiled data-structure.
        This attempts to lose no data and remain as integral as possible.
        """

        wsdl = self.parsed

        data = []

        for operation_index, operation in enumerate(wsdl['PortTypes']['Operations']):
            binding = self._get_binding(wsdl['Bindings'], operation['Name'])
            input_elements = self._get_all_elements(wsdl['Elements'], operation['Name'])
            output_elements = self._get_all_elements(wsdl['Elements'], operation['OutputMessage'].split(':')[-1])

            input_params = []
            output_params = []

            for raw_input_element in input_elements:
                for input_element in raw_input_element['SubElements']:
                    if input_element['SubElementMinOccurs'] == '0':
                        optional = True
                    else:
                        optional = False

                    if input_element['SubElementMaxOccurs'] == 'unbounded':
                        unbounded = True
                    else:
                        unbounded = False

                    input_elements = self._get_element_attributes(input_element['SubElementName'])

                    if input_element['SubElementType'] is not None:
                        input_type = input_element['SubElementType'].split(':')[-1]
                    else:
                        input_type = None

                    input_param = \
                    {
                        'Optional': optional,
                        'Unbounded': unbounded,
                        'Name': input_element['SubElementName'],
                        'Documentation': input_element['SubElementDocumentation'],
                        'Type': input_type,
                        'Attributes': [],
                        'Elements': input_elements,
                    }

                    input_params.append(input_param)

            for raw_output_element in output_elements:
                for output_element in raw_output_element['SubElements']:
                    if output_element['SubElementMinOccurs'] == '0':
                        optional = True
                    else:
                        optional = False

                    if output_element['SubElementMaxOccurs'] == 'unbounded':
                        unbounded = True
                    else:
                        unbounded = False

                    output_elements = self._get_element_attributes(output_element['SubElementName'])

                    output_type = output_element['SubElementType'].split(':')[-1] if output_element['SubElementType'] is not None else None

                    output_param = \
                    {
                        'Optional': optional,
                        'Unbounded': unbounded,
                        'Name': output_element['SubElementName'],
                        'Documentation': output_element['SubElementDocumentation'],
                        'Type': output_type,
                        'Attributes': [],
                        'Elements': output_elements,
                    }

                    output_params.append(output_param)

            if binding is not None:
                soap_action = binding['SoapOperation']['SoapAction']
            else:
                soap_action = None

            operation_data = \
            {
                'Index': operation_index + 1,
                'Name': operation['Name'],
                'Documentation': operation['Documentation'],
                'SOAPAction': soap_action,
                'Input': \
                {
                    'Name': operation['Name'],
                    'Parameters': input_params,
                },
                'Output': \
                {
                    'Name': operation['OutputMessage'].split(':')[-1],
                    'Parameters': output_params,
                },
            }

            data.append(operation_data)

        return data

    @staticmethod
    def _get_binding(bindings, operation_name):
        """
        Get the binding from 'bindings' assosciated with 'operation_name'
        """

        for binding in bindings['Operations']:
            if binding['Name'] == operation_name:
                return binding

    @staticmethod
    def _get_element(elements, operation_name):
        """
        Get the first element from 'elements' assosciated with 'operation_name'

        This may be deprecated soon.
        """

        for element in elements:
            if element['ElementName'] == operation_name:
                return element

    @staticmethod
    def _get_all_elements(elements, operation_name):
        """
        Get all elements from 'elements' assosciated with 'operation_name'
        """

        data = []

        for element in elements:
            if element['ElementName'] == operation_name:
                data.append(element)

        return data

    def _get_element_attributes(self, element_name):
        """
        Create a compiled form of the element assosciated
        ... with 'element_name'
        """

        attribute = None
        max_length = None
        min_length = None
        optional = None
        unbounded = None
        pattern = None
        length = None
        content_type = None
        extension = None

        wsdl = self.parsed

        if attribute is None:
            for ctype in wsdl['ComplexTypes']:
                if ctype['ComplexTypeName'] == element_name:
                    attribute = ctype
                    break

        if attribute is None:
            for ctype in wsdl['SimpleTypes']:
                if ctype['Name'] == element_name:
                    attribute = ctype
                    break

        for xsd in self.xsd_scope:
            parsed_xsd = xsd.compiled

            if attribute is None:
                for ctype in parsed_xsd['ComplexTypes']:
                    if ctype['Name'] == element_name:
                        attribute = ctype
                        break
            else:
                break

        if attribute is None:
            # Failed
            return {}

        attributes = []
        elements = []
        values = []

        if 'Restriction' in attribute: # Attribute is likely a simpleType
            values = []

            for enumeration in attribute['Restriction']['Enumerations']:
                value_data = \
                {
                    'Value': enumeration['Value'],
                    'Documentation': enumeration['Documentation'],
                }

                values.append(value_data)

            attribute_type = attribute['Restriction']['Base']

            max_length = attribute['Restriction']['MaxLength']
            min_length = attribute['Restriction']['MinLength']
            pattern = attribute['Restriction']['Pattern']
            content_type = 'Simple'
            length = attribute['Restriction']['Length']
        else: # Attribute is likely a complexType
            if attribute['ComplexContent']['Extension']['Base'] is not None:
                is_complex = True
                extension = attribute_type = attribute['ComplexContent']['Extension']['Base']
            else:
                is_complex = False

            if attribute['SimpleContent']['Extension']['Base'] is not None:
                is_simple = True
                extension = attribute_type = attribute['SimpleContent']['Extension']['Base']
            else:
                is_simple = False

            if extension is not None:
                extension_element = self._get_element_attributes(extension.split(':')[-1])

                if extension_element:
                    for sub_extension_element in extension_element['Elements']:
                        elements.append(sub_extension_element)

                    for sub_extension_attribute in extension_element['Attributes']:
                        attributes.append(sub_extension_attribute)
                else:
                    pass

            attribute_type = attribute['Name']

            content_type = 'Complex'

            if attribute['SequenceAny'] is not None:
                if attribute['SequenceAny']['MinOccurs'] == '0':
                    optional = True
                if attribute['SequenceAny']['MaxOccurs'] == 'unbounded':
                    unbounded = True

            for complex_attribute in attribute['Elements']:
                # Confusingly, attribute may be a simple complex attribute
                # However, both are treated as a complex attribute
                if complex_attribute['Type'] is not None:
                    if complex_attribute['Type'].split(':')[-1] != element_name:
                        attribute_data = self._get_element_attributes(complex_attribute['Type'].split(':')[-1])#, _parent_name=element_name)
                    else: # Infinite recursion
                        continue

                    if attribute_data:
                        elements.append(attribute_data)

                        continue
                #else: Found None-type
                #else: The type is likely a simpleType, just add itself?

                complex_data = \
                {
                    'Name': complex_attribute['Name'],
                    'Documentation': complex_attribute['Documentation'],
                    'Attributes': [],
                    'Elements': [],
                    'Values': [],
                    'MaxLength': None,
                    'MinLength': None,
                    'Optional': complex_attribute['MinOccurs'] == '0' if complex_attribute['MinOccurs'] is not None else None,
                    'Unbounded': complex_attribute['MaxOccurs'] == 'unbounded' if complex_attribute['MaxOccurs'] is not None else None,
                    'Type': complex_attribute['Type'],
                    'Pattern': None,
                    'Length': None,
                    'ContentType': 'Complex', # Really a ComplexSimple Type
                    'Extension': None,
                }

                elements.append(complex_data)

            for simple_attribute in attribute['Attributes']:
                simple_data = \
                {
                    'Name': simple_attribute['Name'],
                    'Documentation': simple_attribute['Documentation'],
                    'Attributes': [],
                    'Elements': [],
                    'Values': [],
                    'MaxLength': None,
                    'MinLength': None,
                    'Optional': None,
                    'Unbounded': None,
                    'Type': simple_attribute['Type'],
                    'Pattern': None,
                    'Length': None,
                    'ContentType': 'Simple',
                    'Extension': None,
                }

                attributes.append(simple_data)

        data = \
        {
            'Name': attribute['Name'],
            'Documentation': attribute['Documentation'],
            'Attributes': attributes,
            'Elements': elements,
            'Values': values,
            'MaxLength': max_length,
            'MinLength': min_length,
            'Optional': optional,
            'Unbounded': unbounded,
            'Type': attribute_type,
            'Pattern': pattern,
            'Length': length,
            'ContentType': content_type,
            'Extension': extension,
        }

        return data

    def compile_min(self):
        """
        Create a minimal compiled data-structure from self.compile()
        This compilation process will lose data, however maintains
        ... key data.
        """

        compiled = self.compile()

        operations = []

        for operation in compiled:
            index = operation['Index']
            operation_name = operation['Name']
            description = operation['Documentation'].replace('\n        ', ' ').replace('\t\t\t\t', '').strip() if operation['Documentation'] is not None else ''
            soap_action = operation['SOAPAction']
            input_name = operation['Input']['Name']
            output_name = operation['Output']['Name']

            input_elements = []
            output_elements = []

            for input_param in operation['Input']['Parameters']:
                input_attributes = []

                for input_attribute in input_param['Elements'].get('Attributes', ()):
                    input_attribute_name = input_attribute['Name']
                    input_attribute_type = input_attribute['Type'].split(':')[-1]
                    input_attribute_description = input_attribute['Documentation'].strip() if input_attribute['Documentation'] is not None else ''
                    input_attribute_optional = input_attribute['Optional'] is True
                    input_attribute_unbounded = input_attribute['Unbounded'] is True

                    input_attribute_data = \
                    {
                        'Name': input_attribute_name,
                        'Type': input_attribute_type,
                        'Documentation': input_attribute_description,
                        'Optional': input_attribute_optional,
                        'Unbounded': input_attribute_unbounded,
                    }

                    input_attributes.append(input_attribute_data)

                sub_input_elements = []

                for input_element in input_param['Elements'].get('Elements', ()):
                    input_element_name = input_element['Name']
                    input_element_type = input_element['Type'].split(':')[-1]
                    input_element_description = input_element['Documentation'].strip() if input_element['Documentation'] is not None else ''
                    input_element_optional = input_element['Optional'] is True
                    input_element_unbounded = input_element['Unbounded'] is True

                    sub_input_element_attributes = self._compile_min_attributes(input_element['Attributes'])
                    sub_input_element_elements = self._compile_min_elements(input_element['Elements'])

                    sub_input_element_data = \
                    {
                        'Name': input_element_name,
                        'Type': input_element_type,
                        'Documentation': input_element_description,
                        'Optional': input_element_optional,
                        'Unbounded': input_element_unbounded,
                        'Attributes': sub_input_element_attributes,
                        'Elements': sub_input_element_elements,
                    }

                    sub_input_elements.append(sub_input_element_data)

                input_element_data = \
                {
                    'Name': input_param['Name'],
                    'Type': input_param['Type'].split(':')[-1],
                    'Documentation': input_param['Documentation'].strip() if input_param['Documentation'] is not None else '',
                    'Optional': input_param['Optional'] is True,
                    'Unbounded': input_param['Unbounded'] is True,
                    'Elements': sub_input_elements,
                    'Attributes': input_attributes,
                }

                input_elements.append(input_element_data)

            for output_param in operation['Output']['Parameters']:
                param_name = output_param['Name']
                param_type = output_param['Type'].split(':')[-1]
                param_description = output_param['Documentation'].strip() if output_param['Documentation'] is not None else ''
                param_optional = output_param['Optional'] is True
                param_unbounded = output_param['Unbounded'] is True

                output_attributes = []
                sub_output_elements = []

                for output_attribute in output_param['Elements'].get('Attributes', ()):
                    output_attribute_name = output_attribute['Name']
                    output_attribute_type = output_attribute['Type'].split(':')[-1]
                    output_attribute_description = output_attribute['Documentation'].strip() if output_attribute['Documentation'] is not None else ''
                    output_attribute_optional = output_attribute['Optional'] is True
                    output_attribute_unbounded = output_attribute['Unbounded'] is True

                    output_attribute_data = \
                    {
                        'Name': output_attribute_name,
                        'Type': output_attribute_type,
                        'Documentation': output_attribute_description,
                        'Optional': output_attribute_optional,
                        'Unbounded': output_attribute_unbounded,
                    }

                    output_attributes.append(output_attribute_data)

                for output_element in output_param['Elements'].get('Elements', ()):
                    output_element_name = output_element['Name']
                    output_element_type = output_element['Type'].split(':')[-1] if output_element['Type'] is not None else None
                    output_element_description = output_element['Documentation'].strip() if output_element['Documentation'] is not None else ''
                    output_element_optional = output_element['Optional'] is True
                    output_element_unbounded = output_element['Unbounded'] is True

                    sub_output_attributes = self._compile_min_attributes(output_element['Attributes'])
                    sub_output_elements = self._compile_min_elements(output_element['Elements'])

                    output_element_data = \
                    {
                        'Name': output_element_name,
                        'Type': output_element_type,
                        'Documentation': output_element_description,
                        'Optional': output_element_optional,
                        'Unbounded': output_element_unbounded,
                        'Attributes': sub_output_attributes,
                        'Elements': sub_output_elements,
                    }

                    sub_output_elements.append(output_element_data)

                param_data = \
                {
                    'Name': param_name,
                    'Type': param_type,
                    'Documentation': param_description,
                    'Optional': param_optional,
                    'Unbounded': param_unbounded,
                    'Elements': sub_output_elements,
                    'Attributes': output_attributes,
                }

                output_elements.append(param_data)

            operation_data = \
            {
                'Index': index,
                'Name': operation_name,
                'Documentation': description,
                'SOAPAction': soap_action,
                'Input': \
                {
                    'Name': input_name,
                    'Elements': input_elements,
                },
                'Output': \
                {
                    'Name': output_name,
                    'Elements': output_elements,
                }
            }

            operations.append(operation_data)

        return operations

    def _compile_min_attributes(self, attributes):
        """
        Returns a list of minimally compiled attributes
        ... from 'attributes'
        """

        min_attributes = []

        for attribute in attributes:
            attribute_data = self._compile_min_attribute(attribute)

            min_attributes.append(attribute_data)

        return min_attributes

    def _compile_min_elements(self, elements):
        """
        Returns a list of minimally compiled elements
        ... from 'elements'
        """

        min_elements = []

        for element in elements:
            element_data = self._compile_min_element(element)

            min_elements.append(element_data)

        return min_elements

    def _compile_min_attribute(self, attribute):
        """
        Minimally compiles 'attribute'
        """

        attribute_name = attribute['Name']
        attribute_type = attribute['Type'].split(':')[-1]
        attribute_description = attribute['Documentation'].strip() if attribute['Documentation'] is not None else ''
        attribute_optional = attribute['Optional'] is True
        attribute_unbounded = attribute['Unbounded'] is True

        attribute_data = \
        {
            'Name': attribute_name,
            'Type': attribute_type,
            'Documentation': attribute_description,
            'Optional': attribute_optional,
            'Unbounded': attribute_unbounded,
        }

        return attribute_data

    def _compile_min_element(self, element):
        """
        Minimally compiles 'element'
        This is indirectly recursive
        """

        element_name = element['Name']
        element_type = element['Type'].split(':')[-1]
        element_description = element['Documentation'].strip() if element['Documentation'] is not None else ''
        element_optional = element['Optional'] is True
        element_unbounded = element['Unbounded'] is True

        sub_elements = self._compile_min_elements(element['Elements'])
        element_attributes = self._compile_min_attributes(element['Attributes'])

        element_data = \
        {
            'Name': element_name,
            'Type': element_type,
            'Documentation': element_description,
            'Optional': element_optional,
            'Unbounded': element_unbounded,
            'Attributes': element_attributes,
            'Elements': sub_elements,
        }

        return element_data

    def _init_attrs(self):
        """
        Initialises the class attributes
        It creates them, then fills them with a default/null value (usually None)
        """

        self.WsdlParser = None

        self.parsed = None
        self.xsd_scope = None
