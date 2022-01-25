# pip3 install azure-mgmt-resource
# pip3 install azure-identity
from azure.identity import AzureCliCredential
from azure.mgmt.resource import ResourceManagementClient

# Get creadentials from the CLI.
# only use for development.
credential = AzureCliCredential()

# subscripton
subscription_id = "3fa72fe6-7b7f-4556-9c96-f0287c8eae1a"

# a resouce management client is needed to work with resource group and resources in Azure
resouce_mgmt_client = ResourceManagementClient(credential, subscription_id)

# print the list of all resource group names with their locations
resouce_group_list = resouce_mgmt_client.resource_groups.list()
for count, item in enumerate(resouce_group_list):
    print(str(count+1) + ", " + item.name + ", " + item.location)

# print all resources in a subscription with their name and location
resource_list = resouce_mgmt_client.resources.list()
for count, resource in enumerate(resource_list):
    print(str(count+1) + ", " + resource.name + ", " + resource.location + ", " + resource.type)