from . import errors

"""
Contains:
    <WsdlParser>

Imports:
    .errors
"""

class WsdlParser(object):
    """
    Class for parsing a <WsdlSource> from xml into
    ... a Python dictionary
    """

    def __init__(self, wsdl_source):
        """
        Initialises self.

        :param wsdl_source - A <WsdlSource> instance to be parsed
        """

        self._init_attrs()

        self.WsdlSource = wsdl_source

    def __repr__(self):
        """
        Returns a string representation of the object
        ... in the form <class_name(file_name)>
        """

        return f'<{self.__class__.__name__}({self.WsdlSource._file_name})>'

    def parse_elements(self):
        """
        Returns parsed <xs:element> tags from inside
        ... of <xs:schema>
        """

        xs_schema = self.WsdlSource.find('xs:schema')

        if xs_schema is not None:
            xs_elements = xs_schema.find_all('xs:element')
        else:
            raise errors.ParseError('No schema tag found when parsing wsdl elements')

        data = []

        for xs_element in xs_elements:
            sub_elements = []

            xs_element_parent = xs_element.find_parent()

            if xs_element_parent != xs_schema:
                continue

            xs_sub_elements = xs_element.find_all('xs:element')

            for xs_sub_element in xs_sub_elements:
                sub_documentation = xs_sub_element.find('xs:documentation')
                if sub_documentation is not None:
                    sub_documentation = sub_documentation.text


                sub_min_occurs = xs_sub_element.get('minOccurs', None)
                sub_max_occurs = xs_sub_element.get('maxOccurs', None)

                sub_element_data = \
                {
                    'SubElementName': xs_sub_element.get('name', None),
                    'SubElementType': xs_sub_element.get('type', None),
                    'SubElementDocumentation': sub_documentation,
                    'SubElementMinOccurs': sub_min_occurs,
                    'SubElementMaxOccurs': sub_max_occurs,
                }

                sub_elements.append(sub_element_data)

            element_data = \
            {
                'ElementName': xs_element['name'],
                'SubElements': sub_elements,
            }

            data.append(element_data)

        return data

    def parse_messages(self):
        """
        Returns parsed <wsdl:message> tags
        """

        wsdl_messages = self.WsdlSource.find_all('wsdl:message')

        data = []

        for wsdl_message in wsdl_messages:
            wsdl_part = wsdl_message.find('wsdl:part')

            if wsdl_part is not None:
                part_name = wsdl_part.get('name', None)
                part_element = wsdl_part.get('element', None)
            else:
                part_name = None
                part_element = None

            message_data = \
            {
                'MessageName': wsdl_message.get('name', None),
                'PartName': part_name,
                'PartElement': part_element,
            }

            data.append(message_data)

        return data

    def parse_complex_types(self):
        """
        Returns parsed <xs:complexType> tags from
        ... within <xs:schema>
        """

        xs_schema = self.WsdlSource.find('xs:schema')

        if xs_schema is None:
            raise errors.ParseError('No schema found when parsing complex types')

        xs_complex_types = xs_schema.find_all('xs:complexType')

        data = []

        for xs_complex_type in xs_complex_types:
            attributes = []

            xs_complex_type_parent = xs_complex_type.find_parent()

            if xs_complex_type_parent != xs_schema:
                continue

            xs_elements = xs_complex_type.find_all('xs:element')

            elements = []

            for xs_element in xs_elements:
                #xs_element_annotation = xs_element.find('xs:annotation')
                xs_element_documentation = xs_element.find('xs:documentation')

                if xs_element_documentation is not None:
                    documentation = xs_element_documentation.text
                else:
                    documentation = None

                element_data = \
                {
                    'Name': xs_element.get('name', None),
                    'Type': xs_element.get('type', None),
                    'MinOccurs': xs_element.get('minOccurs', None),
                    'MaxOccurs': xs_element.get('maxOccurs', None),
                    'Documentation': documentation,
                }

                elements.append(element_data)

            sequence_any_data = {}

            xs_sequence = xs_complex_type.find('xs:sequence')

            if xs_sequence is not None:
                xs_sequence_any = xs_sequence.find('xs:any')

                if xs_sequence_any is not None:
                    sequence_any_data = \
                    {
                        'NameSpace': xs_sequence_any.get('namespace', None),
                        'ProcessContents': xs_sequence_any.get('processContents', None),
                        'MinOccurs': xs_sequence_any.get('minOccurs', None),
                        'MaxOccurs': xs_sequence_any.get('maxOccurs', None),
                    }

            xs_any_attribute = xs_complex_type.find('xs:anyAttribute')

            if xs_any_attribute is not None:
                any_attribute_data = \
                {
                    'ProcessContents': xs_any_attribute.get('processContents'),
                },
            else:
                any_attribute_data = {}

            xs_attributes = xs_complex_type.find_all('xs:attribute')

            for xs_attribute in xs_attributes:
                xs_documentation = xs_attribute.find('xs:documentation')

                if xs_documentation is not None:
                    attribute_description = xs_documentation.text
                else:
                    attribute_description = None

                attribute_data = \
                {
                    'Name': xs_attribute.get('name', None),
                    'Type': xs_attribute.get('type', None),
                    'Documentation': attribute_description,
                }

                attributes.append(attribute_data)

            type_data = \
            {
                'ComplexTypeName': xs_complex_type.get('name', None),
                'Sequence': sequence_any_data,
                'Attributes': attributes,
                'AnyAttribute': any_attribute_data,

                # The following are added for compatability
                # ... with Xsd.parse_complex_types
                'Name': xs_complex_type.get('name', None),
                'Documentation': None,
                'Elements': elements,
                'AnyAttribute': None,
                'SequenceAny': None,
                'ComplexContent': \
                {
                    'Extension': \
                    {
                        'Base': None,
                    },
                },
                'SimpleContent': \
                {
                    'Extension': \
                    {
                        'Base': None,
                    },
                },
            }

            data.append(type_data)

        return data

    def parse_port_types(self):
        """
        Returns parsed <wsdl:operation> tags from
        ... within <wsdl:portType>
        """

        wsdl_port_type = self.WsdlSource.find('wsdl:portType')

        if wsdl_port_type is None:
            raise errors.ParseError('No port type found when parsing operations')

        wsdl_operations = wsdl_port_type.find_all('wsdl:operation')

        operations = []

        for wsdl_operation in wsdl_operations:
            wsdl_documentation = wsdl_operation.find('wsdl:documentation')
            wsdl_input = wsdl_operation.find('wsdl:input')
            wsdl_output = wsdl_operation.find('wsdl:output')

            if wsdl_input is not None:
                input_message = wsdl_input.get('message', None)
            else:
                input_message = None

            if wsdl_output is not None:
                output_message = wsdl_output.get('message', None)
            else:
                output_message = None

            if wsdl_documentation is not None:
                operation_description = wsdl_documentation.text
            else:
                operation_description = None

            operation_data = \
            {
                'Name': wsdl_operation.get('name', None),
                'InputMessage': input_message,
                'OutputMessage': output_message,
                'Documentation': operation_description,
            }

            operations.append(operation_data)

        data = \
        {
            'Name': wsdl_port_type.get('name', None),
            'Operations': operations,
        }

        return data

    def parse_bindings(self):
        """
        Returns parsed <soap:binding> tags from
        ... within <wsdl:binding>
        """

        wsdl_binding = self.WsdlSource.find('wsdl:binding')

        if wsdl_binding is None:
            raise errors.ParseError('No binding found when parsing operations')

        soap_binding = wsdl_binding.find('soap:binding')

        if soap_binding is not None:
            soap_binding_data = \
            {
                'Style': soap_binding.get('style', None),
                'Transport': soap_binding.get('transport', None),
            },
        else:
            soap_binding_data = {}

        operations = []

        wsdl_operations = wsdl_binding.find_all('wsdl:operation')

        for wsdl_operation in wsdl_operations:
            soap_operation = wsdl_operation.find('soap:operation')

            if soap_operation is not None:
                soap_operation_data = \
                {
                    'SoapAction': soap_operation.get('soapAction', None),
                }
            else:
                soap_operation_data = {}

            input_data = {}
            output_data = {}

            wsdl_input = wsdl_operation.find('wsdl:input')

            if wsdl_input is not None:
                wsdl_input_soap_body = wsdl_input.find('soap:body')

                if wsdl_input_soap_body is not None:
                    input_data = \
                    {
                        'SoapBody': \
                        {
                            'Use': wsdl_input_soap_body.get('use', None),
                        },
                    }

            wsdl_output = wsdl_operation.find('wsdl:output')

            if wsdl_output is not None:
                wsdl_output_soap_body = wsdl_output.find('soap:body')

                if wsdl_output_soap_body is not None:
                    output_data = \
                    {
                        'SoapBody': \
                        {
                            'Use': wsdl_output_soap_body.get('use', None),
                        },
                    }

            operation_data = \
            {
                'Name': wsdl_operation.get('name', None),
                'SoapOperation': soap_operation_data,
                'Input': input_data,
                'Output': output_data,
            }

            operations.append(operation_data)

        data = \
        {
            'Name': wsdl_binding.get('name', None),
            'Type': wsdl_binding.get('type', None),
            'SoapBinding': soap_binding_data,
            'Operations': operations,
        }

        return data

    def parse_meta(self):
        """
        Returns the following parsed tags:
            <wsdl:definitions>
            <xs:schema>
            <xs:import>
        """

        wsdl_definitions = self.WsdlSource.find('wsdl:definitions')
        xs_schema = self.WsdlSource.find('xs:schema')
        xs_import = self.WsdlSource.find('xs:import')

        if wsdl_definitions is not None:
            definitions_data = \
            {
                'XmlnsWsdl': wsdl_definitions.get('xmlns:wsdl', None),
                'XmlnsTptz': wsdl_definitions.get('xmlns:tptz', None),
                'XmlnsXs': wsdl_definitions.get('xmlns:xs', None),
                'XmlnsSoap': wsdl_definitions.get('xmlns:soap', None),
                'Name': wsdl_definitions.get('name', None),
                'TargetNamespace': wsdl_definitions.get('targetNamespace', None),
            }
        else:
            definitions_data = {}

        if xs_schema is not None:
            schema_data = \
            {
                'TargetNamespace': xs_schema.get('targetNamespace', None),
                #'XmlnsTt': xs_schema.get('xmlns:tt', None),
                #'XmlnsTptz': xs_schema.get('xmlns:tptz', None),
                #'XmlnsXs': xs_schema.get('xmlns:xs', None),
                'ElementFormDefault': xs_schema.get('elementFormDefault', None),
                'Version': xs_schema.get('version', None),
            }
        else:
            schema_data = {}

        if xs_import is not None:
            import_data = \
            {
                'NameSpace': xs_import.get('namespace', None),
                'SchemaLocation': xs_import.get('schemaLocation', None),
            },
        else:
            import_data = {}

        data = \
        {
            'Definitions': definitions_data,
            'Schema': schema_data,
            'Import': import_data,
        }

        return data

    def parse_simple_types(self):
        """
        Returns parsed <xs:simpleType> tags from
        ... within <xs:shema>
        """

        xs_schema = self.WsdlSource.find('xs:schema')

        if xs_schema is None:
            raise errors.ParseError('No schema found when parsing simple types')

        xs_simple_types = xs_schema.find_all('xs:simpleType')

        data = []

        for xs_simple_type in xs_simple_types:
            xs_simple_type_parent = xs_simple_type.find_parent()

            if xs_simple_type_parent != xs_schema:
                continue

            xs_annotation = xs_simple_type.find('xs:annotation')

            documentation = None

            if xs_annotation is not None:
                xs_annotation_parent = xs_annotation.find_parent()

                if xs_annotation_parent == xs_simple_type:
                    xs_documentation = xs_annotation.find('xs:documentation')

                    if xs_documentation is not None:
                        documentation = xs_documentation.text

            xs_restriction = xs_simple_type.find('xs:restriction')

            if xs_restriction is not None:
                xs_enumerations = xs_restriction.find_all('xs:enumeration')

                enumerations = []

                for xs_enumeration in xs_enumerations:
                    xs_enumeration_annotation = xs_enumeration.find('xs:annotation')

                    enumeration_documentation = None

                    if xs_enumeration_annotation is not None:
                        xs_enumeration_annotation_parent = xs_enumeration_annotation.find_parent()

                        if xs_enumeration_annotation_parent == xs_enumeration:
                            xs_enumeration_documentation = xs_enumeration_annotation.find('xs:documentation')

                            if xs_enumeration_documentation is not None:
                                enumeration_documentation = xs_enumeration_documentation.text

                    enumeration_data = \
                    {
                        'Value': xs_enumeration.get('value', None),
                        'Documentation': enumeration_documentation,
                    }

                    enumerations.append(enumeration_data)

                xs_max_length = xs_restriction.find('xs:maxLength')

                if xs_max_length is not None:
                    max_length = xs_max_length.get('value')
                else:
                    max_length = None

                xs_min_length = xs_restriction.find('xs:minLength')

                if xs_min_length is not None:
                    min_length = xs_min_length.get('value')
                else:
                    min_length = None

                xs_length = xs_restriction.find('xs:length')

                length = None if xs_length is None else xs_length.get('value')

                xs_pattern = xs_restriction.find('xs:pattern')

                pattern = None if xs_pattern is None else xs_pattern.get('value')

                xs_list = xs_simple_type.find('xs:list')

                if xs_list is not None:
                    item_type = xs_list.get('itemType', None)

                    list_data = \
                    {
                        'ItemType': item_type,
                    }
                else:
                    list_data = \
                    {
                        'ItemType': None,
                    }

                restriction_data = \
                {
                    'Base': xs_restriction.get('base', None),
                    'Enumerations': enumerations,
                    'MaxLength': max_length,
                    'MinLength': min_length,
                    'Length': length,
                    'Pattern': pattern,
                    'List': list_data,
                }
            else:
                restriction_data = \
                {
                    'Base': None,
                    'Enumerations': [],
                    'MaxLength': None,
                    'MinLength': None,
                    'Length': None,
                    'Pattern': None,
                }

            type_data = \
            {
                'Name': xs_simple_type.get('name', None),
                'Restriction': restriction_data,
                'Documentation': documentation,
            }

            data.append(type_data)

        return data

    def parse(self):
        """
        Pulls together all self.parse_***() methods,
        ... returning them in a single dictionary
        """

        messages = self.parse_messages()
        elements = self.parse_elements()
        complex_types = self.parse_complex_types()
        port_types = self.parse_port_types()
        bindings = self.parse_bindings()
        meta = self.parse_meta()
        simple_types = self.parse_simple_types()

        data = \
        {
            'Messages': messages,
            'Elements': elements,
            'ComplexTypes': complex_types,
            'PortTypes': port_types,
            'Bindings': bindings,
            'Meta': meta,
            'SimpleTypes': simple_types,
        }

        return data

    def _init_attrs(self):
        """
        Initialises the class attributes
        It creates them, then fills them with a default/null value (usually None)
        """

        self.WsdlSource = None
