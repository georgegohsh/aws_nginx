import requests
import ipaddress


# REST API GET data from URL 
def retrieve():

    url = 'https://fdqn/vend_ip'

    data = {
        "IP" : "",
        "Subnet" : ""
    }

    response = requests.request("GET", url, headers=data)
    return response.json



if __name__ == "__main__":

    # Retrieve data from URL 
     

    #response = retrieve()



    # Sample response (192.168.0.0/16)

    # response = {
    #   "ip_address":"192.168.0.0",
    #    "subnet_size":"/16"
    # }


    # Break down subnets from /16 to /24 
    print(list(ipaddress.ip_network("192.168.0.0/16").subnets(new_prefix=24)))

