import requests

def run_request(baseURI, basePATH, header, method, payload):
    """
    Sends an HTTP request to the specified endpoint and returns the response.
    :param baseURI: The base URI of the endpoint.
    :type baseURI: str
    :param basePATH: The path of the endpoint.
    :type basePATH: str
    :param header: The headers to include in the request.
    :type header: dict
    :param method: The HTTP method to use for the request.
    :type method: str
    :param payload: The payload to include in the request.
    :type payload: dict
    :return: The response object.
    :rtype: requests.Response
    """
    response = ''
    if "GET" in method.upper():
         response = requests.get(baseURI + basePATH, headers=header, timeout=60)
    elif "POST" in method.upper():
        response = requests.post(baseURI + basePATH, headers=header, json=payload, timeout=60)
    elif "PUT" in method.upper():
        response = requests.put(baseURI + basePATH, headers=header, json=payload, timeout=60)
    elif "DELETE" in method.upper():
        response = requests.delete(baseURI + basePATH, headers=header, timeout=60)
    return response
