"""
Library containing methods for 'wsdl'

Contains:
    <compiled_operation_sprintfer>
    print_compiled_operation
    sprintf_compiled_operation
    identify_operations
"""

class compiled_operation_sprintfer(object):
    """
    Class for sprintfing a compiled operation
    The operation should have been compiled with
    ... WsdlCompiler.compile (not .compile_min)
    """

    def __call__(self, operation):
        """
        Shorthand for self.print_operation(operation)
        """

        return self.print_operation(operation)

    def print_operation(self, operation):
        """
        Sprintfs the compiler operation into the form
        ... adopted on ONVIF's operation page
        """

        index = operation['Index']
        operation_name = operation['Name']
        description = operation['Documentation'].replace('\n        ', ' ').strip() if operation['Documentation'] is not None else ''
        soap_action = operation['SOAPAction']
        input_name = operation['Input']['Name']
        output_name = operation['Output']['Name']

        data = ''

        str_data = \
        (
            f'{index}. {operation_name}\n'
            'Description:\n'
            f'{description}\n'
            'SOAP action:\n'
            f'{soap_action}\n'
            'Input:\n'
            f'\t[{input_name}]\n'
        )
        data += str_data

        for input_param in operation['Input']['Parameters']:
            attrs = []

            if input_param['Optional']:
                attrs.append('optional')
            if input_param['Unbounded']:
                attrs.append('unbounded')

            if attrs:
                str_attrs = ' - ' + ', '.join(attrs) + ';'
            else:
                str_attrs = ''

            param_name = input_param['Name']
            param_type = input_param['Type'].split(':')[-1] if input_param['Type'] is not None else ''
            param_description = input_param['Documentation'].strip() if input_param['Documentation'] is not None else ''

            str_data = \
            (
                f'\t\t* {param_name}{str_attrs} [{param_type}]\n'
            )
            data += str_data

            if param_description:
                str_data = \
                (
                    f'\t\t\t{param_description}\n'
                )
                data += str_data

            for input_attribute in input_param['Elements'].get('Attributes', ()):
                input_attribute_name = input_attribute['Name']
                input_attribute_type = input_attribute['Type'].split(':')[-1]
                input_attribute_description = input_attribute['Documentation'].strip() if input_attribute['Documentation'] is not None else ''

                input_attribute_attrs = []

                if input_attribute['Optional']:
                    input_attribute_attrs.append('optional')
                if input_attribute['Unbounded']:
                    input_attribute_attrs.append('unbounded')

                if input_attribute_attrs:
                    input_attribute_attrs_str = ' - ' + ', '.join(input_attribute_attrs) + ';'
                else:
                    input_attribute_attrs_str = ''

                str_data = \
                (
                    f'\t\t\to {input_attribute_name}{input_attribute_attrs_str} [{input_attribute_type}]\n'
                )
                data += str_data

                if input_attribute_description:
                    str_data = \
                    (
                        f'\t\t\t  {input_attribute_description}\n'
                    )
                    data += str_data


            for input_element in input_param['Elements'].get('Elements', ()):
                input_element_name = input_element['Name']
                input_element_type = input_element['Type'].split(':')[-1]
                input_element_description = input_element['Documentation'].strip() if input_element['Documentation'] is not None else ''

                input_element_attrs = []

                if input_element['Optional']:
                    input_element_attrs.append('optional')
                if input_element['Unbounded']:
                    input_element_attrs.append('unbounded')

                if input_element_attrs:
                    input_element_attrs_str = ' - ' + ', '.join(input_element_attrs) + ';'
                else:
                    input_element_attrs_str = ''

                str_data = \
                (
                    f'\t\t\t* {input_element_name}{input_element_attrs_str} [{input_element_type}]\n'
                )
                data += str_data

                if input_element_description:
                    str_data = \
                    (
                        f'\t\t\t  {input_element_description}\n'
                    )
                    data += str_data

                for sub_input_attribute in input_element['Attributes']:
                    str_data = self._print_attribute(sub_input_attribute, indent=4)
                    data += str_data

                for sub_input_element in input_element['Elements']:
                    str_data = self._print_element(sub_input_element, indent=4)
                    data += str_data

        str_data = \
        (
            'Output:\n'
            f'\t[{output_name}]\n'
        )
        data += str_data

        for output_param in operation['Output']['Parameters']:
            attrs = []

            if output_param['Optional']:
                attrs.append('optional')
            if output_param['Unbounded']:
                attrs.append('unbounded')

            if attrs:
                str_attrs = ' - ' + ', '.join(attrs) + ';'
            else:
                str_attrs = ''

            param_name = output_param['Name']
            param_type = output_param['Type'].split(':')[-1] if output_param['Type'] is not None else ''
            param_description = output_param['Documentation'].strip() if output_param['Documentation'] is not None else ''

            str_data = \
            (
                f'\t\t* {param_name}{str_attrs} [{param_type}]\n'
            )
            data += str_data

            if param_description:
                str_data = \
                (
                    f'\t\t  {param_description}\n'
                )
                data += str_data

            for output_attribute in output_param['Elements'].get('Attributes', ()):
                output_attribute_name = output_attribute['Name']
                output_attribute_type = output_attribute['Type'].split(':')[-1]
                output_attribute_description = output_attribute['Documentation'].strip() if output_attribute['Documentation'] is not None else ''

                output_attribute_attrs = []

                if output_attribute['Optional']:
                    output_attribute_attrs.append('optional')
                if output_attribute['Unbounded']:
                    output_attribute_attrs.append('unbounded')

                if output_attribute_attrs:
                    output_attribute_attrs_str = ' - ' + ', '.join(output_attribute_attrs) + ';'
                else:
                    output_attribute_attrs_str = ''

                str_data = \
                (
                    f'\t\t\to {output_attribute_name}{output_attribute_attrs_str} [{output_attribute_type}]\n'
                )
                data += str_data

                if output_attribute_description:
                    str_data = \
                    (
                        f'\t\t\t  {output_attribute_description}\n'
                    )
                    data += str_data

            for output_element in output_param['Elements'].get('Elements', ()):
                output_element_name = output_element['Name']
                output_element_type = output_element['Type'].split(':')[-1] if output_element['Type'] is not None else ''
                output_element_description = output_element['Documentation'].strip() if output_element['Documentation'] is not None else ''

                output_element_attrs = []

                if output_element['Optional']:
                    output_element_attrs.append('optional')
                if output_element['Unbounded']:
                    output_element_attrs.append('unbounded')

                if output_element_attrs:
                    output_element_attrs_str = ' - ' + ', '.join(output_element_attrs) + ';'
                else:
                    output_element_attrs_str = ''

                str_data = \
                (
                    f'\t\t\t* {output_element_name}{output_element_attrs_str} [{output_element_type}]\n'
                )
                data += str_data

                if output_element_description:
                    str_data = \
                    (
                        f'\t\t\t  {output_element_description}\n'
                    )
                    data += str_data

                for sub_output_attribute in output_element['Attributes']:
                    str_data = self._print_attribute(sub_output_attribute, indent=4)
                    data += str_data

                for sub_output_element in output_element['Elements']:
                    str_data = self._print_element(sub_output_element, indent=4)
                    data += str_data

        return data

    def _print_attribute(self, attribute, indent=0, ichar='\t'):
        """
        Sprintf's an attribute (usually a simpleType, no sub Elements/Attributes)
        """

        attribute_name = attribute['Name']
        attribute_type = attribute['Type'].split(':')[-1] if attribute['Type'] is not None else ''
        attribute_description = attribute['Documentation'].strip() if attribute['Documentation'] is not None else ''

        attribute_attrs = []

        data = ''

        if attribute['Optional']:
            attribute_attrs.append('optional')
        if attribute['Unbounded']:
            attribute_attrs.append('unbounded')

        if attribute_attrs:
            attribute_attrs_str = ' - ' + ', '.join(attribute_attrs) + ';'
        else:
            attribute_attrs_str = ''

        indent_c = indent * ichar

        str_data = \
        (
            f'{indent_c}o {attribute_name}{attribute_attrs_str} [{attribute_type}]\n'
        )
        data += str_data

        if attribute_description:
            str_data = \
            (
                f'{indent_c}  {attribute_description}\n'
            )
            data = str_data

        return data

    def _print_element(self, element, indent=0, ichar='\t'):
        """
        Sprintf's an element (usually a complexType,
        ... likely to have sub Elements/Attributes)
        This is recursive
        """

        element_name = element['Name']
        element_type = element['Type'].split(':')[-1] if element['Type'] is not None else ''
        element_description = element['Documentation'].strip() if element['Documentation'] is not None else ''

        element_attrs = []

        data = ''

        if element['Optional']:
            element_attrs.append('optional')
        if element['Unbounded']:
            element_attrs.append('unbounded')

        if element_attrs:
            element_attrs_str = ' - ' + ', '.join(element_attrs) + ';'
        else:
            element_attrs_str = ''

        indent_c = indent * ichar

        str_data = \
        (
            f'{indent_c}* {element_name}{element_attrs_str} [{element_type}]\n'
        )
        data += str_data

        if element_description:
            str_data = \
            (
                f'{indent_c}  {element_description}\n'
            )
            data += str_data

        for element_attribute in element['Attributes']:
            str_data = self._print_attribute(element_attribute, indent + 1, ichar)
            data += str_data

        for sub_element in element['Elements']:
            str_data = self._print_element(sub_element, indent + 1, ichar)
            data += str_data

        return data

def print_compiled_operation(operation):
    """
    Wrapper for <compiler_operation_sprintfer>.print_operation(operation)
    Prints what is returned using print()
    """

    printer = compiled_operation_sprintfer()
    data = printer(operation)

    print(data)

def sprintf_compiled_operation(operation):
    """
    Wrapper for <compiler_operation_sprintfer>.print_operation(operation)
    """

    printer = compiled_operation_sprintfer()
    data = printer(operation)

    return data

def identify_operations(onvif_service, wsdl):
    """
    Attempts to identify which operations from 'wsdl'
    ... are adopted by 'onvif_service'
    """

    operations = []

    for operation in wsdl.find_all():
        try:
            request = onvif_service.create_type(operation['Name'])

            operations.append(operation)
        except Exception as error:
            pass
    return operations
