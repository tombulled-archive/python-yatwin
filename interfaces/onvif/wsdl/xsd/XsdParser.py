"""
Library containing:
    <XsdParser>
"""

class XsdParser(object):
    """
    Class for parsing an <XsdSource> from xml into
    ... a Python dictionary
    """

    def __init__(self, xsd_source):
        """
        Initialises self.

        :param xsd_source - An <xsd.XsdSource> instance to be parsed
        """

        self._init_attrs()

        self.XsdSource = xsd_source

    def __repr__(self):
        """
        Returns a string representation of the object
        ... in the form <class_name(file_name)>
        """

        return f'<{self.__class__.__name__}({self.XsdSource._file_name})>'

    def parse_meta(self):
        """
        Returns the following parsed tags:
            <xs:schema>
            <xs:include>
            <xs:import>
        """

        xs_schema = self.XsdSource.find('xs:schema')
        xs_include = self.XsdSource.find('xs:include')
        xs_imports = self.XsdSource.find_all('xs:import')

        imports = []

        for xs_import in xs_imports:
            import_data = \
            {
                'Namespace': xs_import.get('namespace', None),
                'SchemaLocation': xs_import.get('schemaLocation', None),
            }

            imports.append(import_data)

        schema_data = {}

        if xs_schema is not None:
            schema_data = \
            {
                'XmlnsTt': xs_schema.get('xmlns:tt', None),
                'XmlnsXs': xs_schema.get('xmlns:xs', None),
                'XmlnsXmime': xs_schema.get('xmlns:xmime', None),
                'XmlnsWsnt': xs_schema.get('xmlns:wsnt', None),
                'XmlnsXop': xs_schema.get('xmlns:xop', None),
                'XmlnsSoapenv': xs_schema.get('xmlns:soapenv', None),
                'TargetNamespace': xs_schema.get('targetNamespace', None),
                'ElementFormDefault': xs_schema.get('elementFormDefault', None),
                'Version': xs_schema.get('version', None),
            },

        include_data = {}

        if xs_include is not None: # Only handles one <xs:include> tag, there may be multiple
            include_data = \
            {
                'SchemaLocation': xs_include.get('schemaLocation', None),
            },

        data = \
        {
            'Schema': schema_data,
            'Include': include_data,
            'Imports': imports
        }

        return data

    def parse_complex_types(self):
        """
        Returns parsed <xs:complexType> tags
        """

        xs_complex_types = self.XsdSource.find_all('xs:complexType')

        data = []

        for xs_complex_type in xs_complex_types:
            xs_annotation = xs_complex_type.find('xs:annotation')

            xs_annotation_parent = xs_annotation.find_parent() if xs_annotation is not None else None

            if xs_annotation_parent is None or xs_annotation_parent != xs_complex_type:
                xs_documentation = None
                documentation = None
            else:
                xs_documentation = xs_annotation.find('xs:documentation')
                documentation = xs_documentation.text

            #sequence_any = {}
            sequence_any = None

            xs_sequence = xs_complex_type.find('xs:sequence')

            if xs_sequence is not None:
                xs_any = xs_sequence.find('xs:any')

                if xs_any is not None:
                    sequence_any = \
                    {
                        'Namespace': xs_any.get('namespace', None),
                        'ProcessContents': xs_any.get('processContents', None),
                        'MinOccurs': xs_any.get('minOccurs', None),
                        'MaxOccurs': xs_any.get('maxOccurs', None),
                    }

            attributes = []

            xs_attributes = xs_complex_type.find_all('xs:attribute')

            xs_any_attribute = xs_complex_type.find('xs:anyAttribute')

            #any_attribute = {}
            any_attribute = None

            if xs_any_attribute is not None:
                any_attribute = \
                {
                    'ProcessContents': xs_any_attribute.get('processContents', None),
                }

            for xs_attribute in xs_attributes:
                xs_attribute_documentation = xs_attribute.find('xs:documentation')

                if xs_attribute_documentation is not None:
                    documentation = xs_attribute_documentation.text
                else:
                    documentation = None

                attribute_data = \
                {
                    'Name': xs_attribute.get('name', None),
                    'Type': xs_attribute.get('type', None),
                    'Use': xs_attribute.get('use', None), # Examples: use=literal, use=required
                    'Documentation': documentation,
                }

                attributes.append(attribute_data)

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

            xs_complex_content = xs_complex_type.find('xs:complexContent')

            complex_extension_base = None

            if xs_complex_content is not None:
                xs_extension = xs_complex_content.find('xs:extension')

                if xs_extension is not None:
                    complex_extension_base = xs_extension.get('base', None)

            xs_simple_content = xs_complex_type.find('xs:simpleContent')

            simple_extension_base = None

            if xs_simple_content is not None:
                xs_extension = xs_simple_content.find('xs:extension')

                if xs_extension is not None:
                    simple_extension_base = xs_extension.get('base', None)

                    #xs_simple_attributes = xs_extension.find_all('xs:attribute')

            complex_data = \
            {
                'Name': xs_complex_type.get('name', None),
                'Documentation': documentation,
                'Attributes': attributes,
                'AnyAttribute': any_attribute,
                'SequenceAny': sequence_any,
                'Elements': elements,
                'ComplexContent': \
                {
                    'Extension': \
                    {
                        'Base': complex_extension_base,
                    },
                },
                'SimpleContent': \
                {
                    'Extension': \
                    {
                        'Base': simple_extension_base,
                    },
                },
            }

            data.append(complex_data)

        return data

    def parse_simple_types(self):
        """
        Returns parsed <xs:simpleType> tags
        """

        xs_simple_types = self.XsdSource.find_all('xs:simpleType')

        data = []

        for xs_simple_type in xs_simple_types:
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
                restriction_data = {}

            simple_data = \
            {
                'Name': xs_simple_type.get('name', None),
                'Restriction': restriction_data,
                'Documentation': documentation,
            }

            data.append(simple_data)

        return data

    def parse(self):
        """
        Pulls together all self.parse_***() methods,
        ... returning them in a single dictionary
        """

        meta = self.parse_meta()
        complex_types = self.parse_complex_types()
        simple_types = self.parse_simple_types()

        data = \
        {
            'Meta': meta,
            'ComplexTypes': complex_types,
            'SimpleTypes': simple_types,
        }

        return data

    def _init_attrs(self):
        """
        Initialises the class attributes
        It creates them, then fills them with a default/null value (usually None)
        """

        self.XsdSource = None
