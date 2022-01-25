# pip3 install azure-mgmt-resource #>=18.0.0
# pip3 install azure-identity #>=1.5.0

from azure.mgmt.resource import ResourceManagementClient
from azure.identity import AzureCliCredential
# from msrestazure.azure_active_directory import ServicePrincipalCredentials

credential = AzureCliCredential()
# credentials = ServicePrincipalCredentials(
#     client_id = "7ea7b6ec-36e4-424e-8aea-987eff90060c",
#     secret = "XAB7Q~lGOc1kfyk5DEWqlOY0mbnsvQhzCDJ-P",
#     tenant = "67d8a82a-4833-4b9f-8e67-a7fecfafdd0f"
# )


subscription_id = "3fa72fe6-7b7f-4556-9c96-f0287c8eae1a"

resource_mgmt_client = ResourceManagementClient(credential, subscription_id)
group_list = resource_mgmt_client.resource_groups.list()

# Show the groups in formatted output
column_width = 40

print("Resource Group".ljust(column_width) + "Location")
print("-" * (column_width * 2))

# rg_result = resource_mgmt_client.resource_groups.create_or_update(
#     "PythonAzureExample-rg",
#     {
#         "location": "centralus"
#     }
# )
