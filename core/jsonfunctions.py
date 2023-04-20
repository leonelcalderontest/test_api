import os


class json_validation:

    def __init__(self):
        print("Able to call JSON Validation")

    def validate_jsonobject(self, jsonobject, fieldname, fieldvalue):
        """
        Validate the value or values of a field in a JSON object.
        :param jsonobject: The JSON object to validate.
        :type jsonobject: dict
        :param fieldname: The name of the field to validate.
        :type fieldname: str
        :param fieldvalue: The expected value or values of the field to validate.
        :type fieldvalue: any
        :return: True if the validation passed, False otherwise.
        :rtype: bool
        """
        isPassed = True
        print("FIELD NAME TO CHECK IS : " + str(fieldname))
        print("EXPECTED VALUE IS : " + str(fieldvalue))
        print("ACTUAL VALUE IS : " + str(jsonobject[fieldname]))
        if jsonobject[fieldname] != fieldvalue:
            isPassed = False
            print(f"Validation failed for {fieldname}")
        return isPassed

    def validate_json_field_array_element_if(self, jsonobject, field, arrayfieldname_check, arrayfieldvalue_check,
                                             arrayfieldname_val, arrayfieldvalue_val):
        """
        Validates a JSON object based on the value of a field, and then validates another field based on its name and value.
        :param jsonobject: The JSON object to validate.
        :type jsonobject: dict
        :param field: The name of the field that contains the array to check.
        :type field: str
        :param arrayfieldname_check: The name of the field to check if included in validation.
        :type arrayfieldname_check: str
        :param arrayfieldvalue_check: The value of the field to check if included in validation.
        :type arrayfieldvalue_check: any
        :param arrayfieldname_val: The name of the field to validate.
        :type arrayfieldname_val: str
        :param arrayfieldvalue_val: The value to validate the field against.
        :type arrayfieldvalue_val: any
        :return: True if the validation passed, False otherwise.
        :rtype: bool
        """
        isPassed = True
        print("FIELD NAME CONTAINING ARRAY VALUES IS : " + str(field))
        print("CHECK IF ARRAY FIELD NAME IS : " + str(arrayfieldname_check) + " AND ITS VALUE IS : " + str(arrayfieldvalue_check))
        print("ARRAY FIELD NAME TO VALIDATE : " + str(arrayfieldname_val))
        print("ARRAY FIELD VALUE TO VALIDATE : " + str(arrayfieldvalue_val))
        if field in jsonobject:
            if isinstance(jsonobject[field], list):
                for element in jsonobject[field]:
                    if arrayfieldname_check in element and element[arrayfieldname_check] == arrayfieldvalue_check:
                        if arrayfieldname_val in element and element[arrayfieldname_val] != arrayfieldvalue_val:
                            isPassed = False
                            print(f"Validation failed for {arrayfieldname_val}")
                            break
            else:
                isPassed = False
                print(f"{field} field in JSON object is not a list")
        else:
            isPassed = False
            print(f"{field} field not found in JSON object")

        return isPassed