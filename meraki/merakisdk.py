from meraki_sdk.meraki_sdk_client import MerakiSdkClient

#Cisco DevNet Sandbox Meraki API Key
X_CISCO_MERAKI_API_KEY = 'a66e4a5ab2877931b77e7224244f93ab89f096fb'

#Establish a new client connection to the Meraki REST API
MERAKI = MerakiSdkClient(X_CISCO_MERAKI_API_KEY)

#Get a list of all the organizations for the Cisco DevNet account
ORGS = MERAKI.organizations.getOrganizations()
for ORG in ORGS:
    print("Org ID: {} and Org Name: {}".format(ORG['id'], ORG['name']))

PARAMS = {}
PARAMS["organization_id"] = "549326" # Demo Organization "DevNet Sandbox"


#Get a list of all the networks for the Cisco DevNet organization
NETS = MERAKI.networks.getOrganizationNetworks(PARAMS)
for NET in NETS:
    print('Network ID: {0:20s}, Name: {1:45s}, Tags: {2:<10s}'.format(\
        NET['id'], NET['name'], str(NET['tags'])))


#Get a list of all the devices that are part of the Always On Network
DEVICES = MERAKI.devices.get_network_devices("L_6468294964811005433")
for DEVICE in DEVICES:
    print("Device Model: {0:9s}, Serial: {1:14s}, MAC: {2:17}, Firmware: {3:12s}"\
        .format(DEVICE['model'], DEVICE['serial'], DEVICE['mac'], \
            DEVICE['firmware']))