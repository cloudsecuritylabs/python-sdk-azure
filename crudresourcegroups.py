# CRUD with PYTHON SDK for Azure
# import libraries
        # pip3 install azure-mgmt-resource
        # pip3 install azure-identity

from azure.identity import AzureCliCredential
from azure.mgmt.resource import ResourceManagementClient

# get credential
credential = AzureCliCredential()

# store subscription
subscription_id = "3fa72fe6-7b7f-4556-9c96-f0287c8eae1a"

# create Resource Manager Client
resource_mgmt_client = ResourceManagementClient(credential, subscription_id)

resource_group_params = { 'location': "eastus"}

rg_name = "rg-eastus"

# CREATE a resource group
resource_mgmt_client.resource_groups.create_or_update(rg_name, resource_group_params)
print("Resorce group is created!")

# READ
list_of_resource_groups = resource_mgmt_client.resource_groups.list()
for rg in list_of_resource_groups:
    if (rg.name == rg_name):
        print("Resource Group found!")


# UPDATE
resource_group_params.update(tags={"cloudsecurity" : "training"})
resource_mgmt_client.resource_groups.update(rg_name, resource_group_params )
print("Update is successful.")

# READ - all items within a resource group
resource_list = resource_mgmt_client.resources.list_by_resource_group(rg_name)
for resource in resource_list:
    print(resource.name + " ," + resource.location)

print("Print list of resources from another resource group")
resource_list = resource_mgmt_client.resources.list_by_resource_group("testweb1233-rg")
for resource in resource_list:
    print(resource.name + " ," + resource.location)

# DELETE the resources  and the resource group.
delete_async_op = resource_mgmt_client.resource_groups.begin_delete(rg_name)
delete_async_op.wait()
print("RG is now deleted!")
