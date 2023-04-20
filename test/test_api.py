import json
import pytest
import allure

from core import requestapi
from core.customLogger import Logger
from core.jsonfunctions import json_validation
from core.parameters import parameters

pr = parameters()
js = json_validation()

# Can be replaced by data coming from different source (google sheet, csv, config file, environment, parameters, others)
test_data = [
    (pr.get_baseURI(), "/v1/Categories/6329/Details.json?catalogue=false", "GET", "", 200)
]

test_names = []

# Generate test name that is incremented based on the number of data sets
counter = 0
for data in test_data:
    test_names.append("TestCase_" + str(len(test_data) - counter))
    counter = counter + 1


class Test_api:
    cl = Logger()

    @pytest.mark.parametrize("BASEURI, PATH, METHOD, PAYLOAD, EXPECTED_STATUS", test_data, ids=test_names)
    def test_api(self, BASEURI, PATH, METHOD, PAYLOAD, EXPECTED_STATUS):
        global parseResponse
        headers = ""
        with allure.step("ENDPOINT : " + BASEURI+PATH + " METHOD : " + METHOD):
            api_response = requestapi.run_request(BASEURI, PATH, headers, METHOD, PAYLOAD)

        try:
            parseResponse = json.loads(api_response.text)
            jsonstrResponse = json.dumps(parseResponse, indent=4)
        except json.decoder.JSONDecodeError:
            jsonstrResponse = ""
        except UnboundLocalError:
            jsonstrResponse = ""

        self.cl.testLog().info("RESPONSE BODY IS :")
        self.cl.testLog().info(jsonstrResponse)
        print("RESPONSE BODY IS :")
        print(jsonstrResponse)

        if str(api_response.status_code) == str(EXPECTED_STATUS):
            self.cl.testLog().info("RESPONSE STATUS CODE IS : ")
            self.cl.testLog().info(str(api_response.status_code))
            print("RESPONSE STATUS CODE  IS :")
            print(str(api_response.status_code))
        else:
            pytest.fail("RESPONSE STATUS CODE IS : " + str(api_response.status_code))


        self.cl.testLog().info("Validation of specific fields")
        print("Validation of specific fields")
        if js.validate_jsonobject(parseResponse, "Name", "Home & garden"):
            self.cl.testLog().info("Expected Field name and value exist and correct")
            print("Expected Field name and value exist and correct")
        else:
            print("Response does not contains the specific required fields")
            pytest.fail("Response does not contains the specific required fields")

        if  js.validate_jsonobject(parseResponse, "CanRelist", True):
            self.cl.testLog().info("Expected Field name and value exist and correct")
            print("Expected Field name and value exist and correct")
        else:
            print("Response does not contains the specific required fields")
            pytest.fail("Response does not contains the specific required fields")

        if js.validate_json_field_array_element_if(parseResponse, "Promotions", "Name", "Feature", "Description", "Better position in category"):
            self.cl.testLog().info("Expected Field name and value exist and correct")
            print("Expected Field name and value exist and correct")
        else:
            print("Response does not contains the specific required fields")
            pytest.fail("Response does not contains the specific required fields")



