
`az ad signed-in-user show`
`az ad user list`
`az ad user list --filter "startsWith('wvusr-', displayName)"`
`az ad group list`

log in as another account:
```shell-session
usr-xxxxxxxx [ ~ ]$ az account clear
usr-xxxxxxxx [ ~ ]$ az login -u EMAIL -p PASSWORD
```

list roles for group
```shell-session
az role assignment list --assignee REPLACE_WITH_GROUP_ID --all
```

list acessible key vaults:
```shell-session
az keyvault list
```

list secrets
```shell-session
az keyvault secret list --vault-name warevillesecrets
```

list secret values
```
az keyvault secret show --vault-name warevillesecrets --name aoc2024
```

### Example output

```sh
usr-12274062 [ ~ ]$ az ad signed-in-user show
{
  "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#users/$entity",
  "businessPhones": [],
  "displayName": "usr-12274062",
  "givenName": null,
  "id": "0b0a65d1-a88e-4dd0-bbd4-5df4f703abc9",
  "jobTitle": null,
  "mail": null,
  "mobilePhone": null,
  "officeLocation": null,
  "preferredLanguage": null,
  "surname": null,
  "userPrincipalName": "usr-12274062@aoc2024.onmicrosoft.com"
}
usr-12274062 [ ~ ]$ az ad user list
[
  {
    "businessPhones": [],
    "displayName": "breakglass",
    "givenName": null,
    "id": "d6c5bb7b-36a2-4706-ad5f-dd5a73e5dfd8",
    "jobTitle": null,
    "mail": null,
    "mobilePhone": null,
    "officeLocation": null,
    "preferredLanguage": null,
    "surname": null,
    "userPrincipalName": "breakglass@aoc2024.onmicrosoft.com"
  },
  {
    "businessPhones": [],
    "displayName": "wiz",
    "givenName": null,
    "id": "b470c1dc-9d37-4ce9-b528-4aeaf819781a",
    "jobTitle": null,
    "mail": null,
    "mobilePhone": null,
    "officeLocation": null,
    "preferredLanguage": null,
    "surname": null,
    "userPrincipalName": "oz_thmtraininglabs.onmicrosoft.com#EXT#@aoc2024.onmicrosoft.com"
  },
  {
    "businessPhones": [],
    "displayName": "usr-12270136",
    "givenName": null,
    "id": "21384598-0e86-40d0-ac12-49d190db8283",
    "jobTitle": null,
    "mail": null,
    "mobilePhone": null,
    "officeLocation": null,
    "preferredLanguage": null,
    "surname": null,
    "userPrincipalName": "usr-12270136@aoc2024.onmicrosoft.com"
  },
  {
    "businessPhones": [],
    "displayName": "usr-12270540",
    "givenName": null,
    "id": "a41d6a5e-675b-4b0c-9001-10042702a93b",
    "jobTitle": null,
    "mail": null,
    "mobilePhone": null,
    "officeLocation": null,
    "preferredLanguage": null,
    "surname": null,
    "userPrincipalName": "usr-12270540@aoc2024.onmicrosoft.com"
  },
  {
    "businessPhones": [],
    "displayName": "usr-12270573",
    "givenName": null,
    "id": "b1960b85-89ce-4bdb-ab60-c9b301f74f9c",
    "jobTitle": null,
    "mail": null,
    "mobilePhone": null,
    "officeLocation": null,
    "preferredLanguage": null,
    "surname": null,
    "userPrincipalName": "usr-12270573@aoc2024.onmicrosoft.com"
  },
  {
    "businessPhones": [],
    "displayName": "usr-12271250",
    "givenName": null,
    "id": "f4d4d2e1-5dec-4714-9ea9-23cbba040507",
    "jobTitle": null,
    "mail": null,
    "mobilePhone": null,
    "officeLocation": null,
    "preferredLanguage": null,
    "surname": null,
    "userPrincipalName": "usr-12271250@aoc2024.onmicrosoft.com"
  },
  {
    "businessPhones": [],
    "displayName": "usr-12271487",
    "givenName": null,
    "id": "a68f6b4e-1af7-4535-93ae-d9b14ed5c736",
    "jobTitle": null,
    "mail": null,
    "mobilePhone": null,
    "officeLocation": null,
    "preferredLanguage": null,
    "surname": null,
    "userPrincipalName": "usr-12271487@aoc2024.onmicrosoft.com"
  },
  {
    "businessPhones": [],
    "displayName": "usr-12272820",
    "givenName": null,
    "id": "4faf055b-c3d3-4c4f-989f-77d17bd05a40",
    "jobTitle": null,
    "mail": null,
    "mobilePhone": null,
    "officeLocation": null,
    "preferredLanguage": null,
    "surname": null,
    "userPrincipalName": "usr-12272820@aoc2024.onmicrosoft.com"
  },
  {
    "businessPhones": [],
    "displayName": "usr-12273720",
    "givenName": null,
    "id": "e5f23436-61a6-4b7e-af96-3983274d49af",
    "jobTitle": null,
    "mail": null,
    "mobilePhone": null,
    "officeLocation": null,
    "preferredLanguage": null,
    "surname": null,
    "userPrincipalName": "usr-12273720@aoc2024.onmicrosoft.com"
  },
  {
    "businessPhones": [],
    "displayName": "usr-12274062",
    "givenName": null,
    "id": "0b0a65d1-a88e-4dd0-bbd4-5df4f703abc9",
    "jobTitle": null,
    "mail": null,
    "mobilePhone": null,
    "officeLocation": null,
    "preferredLanguage": null,
    "surname": null,
    "userPrincipalName": "usr-12274062@aoc2024.onmicrosoft.com"
  },
  {
    "businessPhones": [],
    "displayName": "usr-12274070",
    "givenName": null,
    "id": "e4d18ffe-a482-436d-b3c3-852476f57de8",
    "jobTitle": null,
    "mail": null,
    "mobilePhone": null,
    "officeLocation": null,
    "preferredLanguage": null,
    "surname": null,
    "userPrincipalName": "usr-12274070@aoc2024.onmicrosoft.com"
  },
  {
    "businessPhones": [],
    "displayName": "usr-12274638",
    "givenName": null,
    "id": "1eb0f38b-5809-438b-9564-0c5860839e41",
    "jobTitle": null,
    "mail": null,
    "mobilePhone": null,
    "officeLocation": null,
    "preferredLanguage": null,
    "surname": null,
    "userPrincipalName": "usr-12274638@aoc2024.onmicrosoft.com"
  },
  {
    "businessPhones": [],
    "displayName": "usr-12275242",
    "givenName": null,
    "id": "8fae093d-a6fc-4e39-9372-d73e0be75f37",
    "jobTitle": null,
    "mail": null,
    "mobilePhone": null,
    "officeLocation": null,
    "preferredLanguage": null,
    "surname": null,
    "userPrincipalName": "usr-12275242@aoc2024.onmicrosoft.com"
  },
  {
    "businessPhones": [],
    "displayName": "usr-12275480",
    "givenName": null,
    "id": "a880123a-d81f-48f6-a328-ab14ba967d1a",
    "jobTitle": null,
    "mail": null,
    "mobilePhone": null,
    "officeLocation": null,
    "preferredLanguage": null,
    "surname": null,
    "userPrincipalName": "usr-12275480@aoc2024.onmicrosoft.com"
  },
  {
    "businessPhones": [],
    "displayName": "usr-12276151",
    "givenName": null,
    "id": "65728407-ee5c-40e0-b7d0-c0dd6f697c5a",
    "jobTitle": null,
    "mail": null,
    "mobilePhone": null,
    "officeLocation": null,
    "preferredLanguage": null,
    "surname": null,
    "userPrincipalName": "usr-12276151@aoc2024.onmicrosoft.com"
  },
  {
    "businessPhones": [],
    "displayName": "usr-12276360",
    "givenName": null,
    "id": "d39b7353-bb1f-44af-a826-0c062bab04e6",
    "jobTitle": null,
    "mail": null,
    "mobilePhone": null,
    "officeLocation": null,
    "preferredLanguage": null,
    "surname": null,
    "userPrincipalName": "usr-12276360@aoc2024.onmicrosoft.com"
  },
  {
    "businessPhones": [],
    "displayName": "usr-12276811",
    "givenName": null,
    "id": "c1842ff7-be81-46d4-bb37-96c1583f5355",
    "jobTitle": null,
    "mail": null,
    "mobilePhone": null,
    "officeLocation": null,
    "preferredLanguage": null,
    "surname": null,
    "userPrincipalName": "usr-12276811@aoc2024.onmicrosoft.com"
  },
  {
    "businessPhones": [],
    "displayName": "usr-12277070",
    "givenName": null,
    "id": "63bc289b-5837-472c-bd7d-0361e36cf9dd",
    "jobTitle": null,
    "mail": null,
    "mobilePhone": null,
    "officeLocation": null,
    "preferredLanguage": null,
    "surname": null,
    "userPrincipalName": "usr-12277070@aoc2024.onmicrosoft.com"
  },
  {
    "businessPhones": [],
    "displayName": "usr-12277882",
    "givenName": null,
    "id": "c52ee12f-3569-44b2-b13c-5020d68404ac",
    "jobTitle": null,
    "mail": null,
    "mobilePhone": null,
    "officeLocation": null,
    "preferredLanguage": null,
    "surname": null,
    "userPrincipalName": "usr-12277882@aoc2024.onmicrosoft.com"
  },
  {
    "businessPhones": [],
    "displayName": "usr-12278566",
    "givenName": null,
    "id": "ef6e790e-027e-4218-99df-3f9da0910672",
    "jobTitle": null,
    "mail": null,
    "mobilePhone": null,
    "officeLocation": null,
    "preferredLanguage": null,
    "surname": null,
    "userPrincipalName": "usr-12278566@aoc2024.onmicrosoft.com"
  },
  {
    "businessPhones": [],
    "displayName": "usr-12278902",
    "givenName": null,
    "id": "3d380fe7-120a-47a9-b567-9b237654a7aa",
    "jobTitle": null,
    "mail": null,
    "mobilePhone": null,
    "officeLocation": null,
    "preferredLanguage": null,
    "surname": null,
    "userPrincipalName": "usr-12278902@aoc2024.onmicrosoft.com"
  },
  {
    "businessPhones": [],
    "displayName": "usr-12279132",
    "givenName": null,
    "id": "03af765d-ca8d-47b8-a7c9-f30a1f8f48b4",
    "jobTitle": null,
    "mail": null,
    "mobilePhone": null,
    "officeLocation": null,
    "preferredLanguage": null,
    "surname": null,
    "userPrincipalName": "usr-12279132@aoc2024.onmicrosoft.com"
  },
  {
    "businessPhones": [],
    "displayName": "usr-12279831",
    "givenName": null,
    "id": "0adbea89-1749-44e5-a9cf-f5e979676dbc",
    "jobTitle": null,
    "mail": null,
    "mobilePhone": null,
    "officeLocation": null,
    "preferredLanguage": null,
    "surname": null,
    "userPrincipalName": "usr-12279831@aoc2024.onmicrosoft.com"
  },
  {
    "businessPhones": [],
    "displayName": "weyland",
    "givenName": null,
    "id": "bbbe3752-0ce4-476f-b52f-e2aef17f3183",
    "jobTitle": null,
    "mail": null,
    "mobilePhone": null,
    "officeLocation": null,
    "preferredLanguage": null,
    "surname": null,
    "userPrincipalName": "wayland@aoc2024.onmicrosoft.com"
  },
  {
    "businessPhones": [],
    "displayName": "wvusr-alphaware",
    "givenName": null,
    "id": "d197bfbd-adaf-4e54-9ac1-62b2a9568f91",
    "jobTitle": null,
    "mail": null,
    "mobilePhone": null,
    "officeLocation": null,
    "preferredLanguage": null,
    "surname": null,
    "userPrincipalName": "wvusr-alphaware@aoc2024.onmicrosoft.com"
  },
  {
    "businessPhones": [],
    "displayName": "wvusr-backupware",
    "givenName": null,
    "id": "1db95432-0c46-45b8-b126-b633ae67e06c",
    "jobTitle": null,
    "mail": null,
    "mobilePhone": null,
    "officeLocation": "R3c0v3r_s3cr3ts!",
    "preferredLanguage": null,
    "surname": null,
    "userPrincipalName": "wvusr-backupware@aoc2024.onmicrosoft.com"
  },
  {
    "businessPhones": [],
    "displayName": "wvusr-firmware",
    "givenName": null,
    "id": "1f80a74b-4abc-4f93-b065-965ea5c826c8",
    "jobTitle": null,
    "mail": null,
    "mobilePhone": null,
    "officeLocation": null,
    "preferredLanguage": null,
    "surname": null,
    "userPrincipalName": "wvusr-firmware@aoc2024.onmicrosoft.com"
  },
  {
    "businessPhones": [],
    "displayName": "wvusr-freeware",
    "givenName": null,
    "id": "47f6013e-9533-49f5-a779-615721145e50",
    "jobTitle": null,
    "mail": null,
    "mobilePhone": null,
    "officeLocation": null,
    "preferredLanguage": null,
    "surname": null,
    "userPrincipalName": "wvusr-freeware@aoc2024.onmicrosoft.com"
  },
  {
    "businessPhones": [],
    "displayName": "wvusr-hardware",
    "givenName": null,
    "id": "ac459a56-09cf-440a-be46-2006b36a68e1",
    "jobTitle": null,
    "mail": null,
    "mobilePhone": null,
    "officeLocation": null,
    "preferredLanguage": null,
    "surname": null,
    "userPrincipalName": "wvusr-hardware@aoc2024.onmicrosoft.com"
  },
  {
    "businessPhones": [],
    "displayName": "wvusr-mayor_malware",
    "givenName": null,
    "id": "4d29c472-f2f6-4e18-8a37-dcd2e2040489",
    "jobTitle": null,
    "mail": null,
    "mobilePhone": null,
    "officeLocation": null,
    "preferredLanguage": null,
    "surname": null,
    "userPrincipalName": "wvusr-mayor_malware@aoc2024.onmicrosoft.com"
  },
  {
    "businessPhones": [],
    "displayName": "wvusr-mcskidy",
    "givenName": null,
    "id": "33845c09-f7ad-45eb-ad24-c05cc1e39bda",
    "jobTitle": null,
    "mail": null,
    "mobilePhone": null,
    "officeLocation": null,
    "preferredLanguage": null,
    "surname": null,
    "userPrincipalName": "wvusr-mcskidy@aoc2024.onmicrosoft.com"
  },
  {
    "businessPhones": [],
    "displayName": "yutani",
    "givenName": null,
    "id": "86e14415-abac-486d-b49a-4825bcd3a13e",
    "jobTitle": null,
    "mail": null,
    "mobilePhone": null,
    "officeLocation": null,
    "preferredLanguage": null,
    "surname": null,
    "userPrincipalName": "yutani@aoc2024.onmicrosoft.com"
  }
]
usr-12274062 [ ~ ]$ az ad user list --filter "startsWith('wvusr-', displayName)"
[
  {
    "businessPhones": [],
    "displayName": "wvusr-alphaware",
    "givenName": null,
    "id": "d197bfbd-adaf-4e54-9ac1-62b2a9568f91",
    "jobTitle": null,
    "mail": null,
    "mobilePhone": null,
    "officeLocation": null,
    "preferredLanguage": null,
    "surname": null,
    "userPrincipalName": "wvusr-alphaware@aoc2024.onmicrosoft.com"
  },
  {
    "businessPhones": [],
    "displayName": "wvusr-backupware",
    "givenName": null,
    "id": "1db95432-0c46-45b8-b126-b633ae67e06c",
    "jobTitle": null,
    "mail": null,
    "mobilePhone": null,
    "officeLocation": "R3c0v3r_s3cr3ts!",
    "preferredLanguage": null,
    "surname": null,
    "userPrincipalName": "wvusr-backupware@aoc2024.onmicrosoft.com"
  },
  {
    "businessPhones": [],
    "displayName": "wvusr-firmware",
    "givenName": null,
    "id": "1f80a74b-4abc-4f93-b065-965ea5c826c8",
    "jobTitle": null,
    "mail": null,
    "mobilePhone": null,
    "officeLocation": null,
    "preferredLanguage": null,
    "surname": null,
    "userPrincipalName": "wvusr-firmware@aoc2024.onmicrosoft.com"
  },
  {
    "businessPhones": [],
    "displayName": "wvusr-freeware",
    "givenName": null,
    "id": "47f6013e-9533-49f5-a779-615721145e50",
    "jobTitle": null,
    "mail": null,
    "mobilePhone": null,
    "officeLocation": null,
    "preferredLanguage": null,
    "surname": null,
    "userPrincipalName": "wvusr-freeware@aoc2024.onmicrosoft.com"
  },
  {
    "businessPhones": [],
    "displayName": "wvusr-hardware",
    "givenName": null,
    "id": "ac459a56-09cf-440a-be46-2006b36a68e1",
    "jobTitle": null,
    "mail": null,
    "mobilePhone": null,
    "officeLocation": null,
    "preferredLanguage": null,
    "surname": null,
    "userPrincipalName": "wvusr-hardware@aoc2024.onmicrosoft.com"
  },
  {
    "businessPhones": [],
    "displayName": "wvusr-mayor_malware",
    "givenName": null,
    "id": "4d29c472-f2f6-4e18-8a37-dcd2e2040489",
    "jobTitle": null,
    "mail": null,
    "mobilePhone": null,
    "officeLocation": null,
    "preferredLanguage": null,
    "surname": null,
    "userPrincipalName": "wvusr-mayor_malware@aoc2024.onmicrosoft.com"
  },
  {
    "businessPhones": [],
    "displayName": "wvusr-mcskidy",
    "givenName": null,
    "id": "33845c09-f7ad-45eb-ad24-c05cc1e39bda",
    "jobTitle": null,
    "mail": null,
    "mobilePhone": null,
    "officeLocation": null,
    "preferredLanguage": null,
    "surname": null,
    "userPrincipalName": "wvusr-mcskidy@aoc2024.onmicrosoft.com"
  }
]
usr-12274062 [ ~ ]$ az ad group list
[
  {
    "classification": null,
    "createdDateTime": "2024-10-13T23:10:55Z",
    "creationOptions": [],
    "deletedDateTime": null,
    "description": "Group for recovering Wareville's secrets",
    "displayName": "Secret Recovery Group",
    "expirationDateTime": null,
    "groupTypes": [],
    "id": "7d96660a-02e1-4112-9515-1762d0cb66b7",
    "isAssignableToRole": null,
    "mail": null,
    "mailEnabled": false,
    "mailNickname": "f315e3ef-c",
    "membershipRule": null,
    "membershipRuleProcessingState": null,
    "onPremisesDomainName": null,
    "onPremisesLastSyncDateTime": null,
    "onPremisesNetBiosName": null,
    "onPremisesProvisioningErrors": [],
    "onPremisesSamAccountName": null,
    "onPremisesSecurityIdentifier": null,
    "onPremisesSyncEnabled": null,
    "preferredDataLocation": null,
    "preferredLanguage": null,
    "proxyAddresses": [],
    "renewedDateTime": "2024-10-13T23:10:55Z",
    "resourceBehaviorOptions": [],
    "resourceProvisioningOptions": [],
    "securityEnabled": true,
    "securityIdentifier": "S-1-12-1-2107008522-1091699425-1645680021-3076967376",
    "serviceProvisioningErrors": [],
    "theme": null,
    "uniqueName": null,
    "visibility": "Private"
  }
]
usr-12274062 [ ~ ]$ az account clear
Logout successful. Re-login to your initial Cloud Shell identity with 'az login --identity'. Login with a new identity with 'az login'.
usr-12274062 [ ~ ]$ az login -u wvusr-alphaware@aoc2024.onmicrosoft.com -p R3c0v3r_s3cr3ts!
Authentication with username and password in the command line is strongly discouraged. Use one of the recommended authentication methods based on your requirements. For more details, see https://go.microsoft.com/fwlink/?linkid=2276314
Cloud Shell is automatically authenticated under the initial account signed-in with. Run 'az login' only if you need to use a different account
A Cloud Shell credential problem occurred. When you report the issue with the error below, please mention the hostname 'SandboxHost-638709091829051369'
AADSTS50126: Error validating credentials due to invalid username or password. Trace ID: 245c64d8-b44b-4539-9ae2-68959bddba00 Correlation ID: b5c2e16f-b4d9-4b4e-9104-e28aa1d50337 Timestamp: 2024-12-27 20:28:33Z
Interactive authentication is needed. Please run:
az login
usr-12274062 [ ~ ]$ az login -u wvusr-backupware@aoc2024.onmicrosoft.com -p R3c0v3r_s3cr3ts!
Authentication with username and password in the command line is strongly discouraged. Use one of the recommended authentication methods based on your requirements. For more details, see https://go.microsoft.com/fwlink/?linkid=2276314
Cloud Shell is automatically authenticated under the initial account signed-in with. Run 'az login' only if you need to use a different account
[
  {
    "cloudName": "AzureCloud",
    "homeTenantId": "1ad8a5d3-b45e-489d-9ef3-b5478392aac0",
    "id": "ddd3338d-bc5a-416d-8247-1db1f5b5ff43",
    "isDefault": true,
    "managedByTenants": [],
    "name": "Az-Subs-AoC",
    "state": "Enabled",
    "tenantDefaultDomain": "aoc2024.onmicrosoft.com",
    "tenantDisplayName": "AoC 2024",
    "tenantId": "1ad8a5d3-b45e-489d-9ef3-b5478392aac0",
    "user": {
      "name": "wvusr-backupware@aoc2024.onmicrosoft.com",
      "type": "user"
    }
  }
]
usr-12274062 [ ~ ]$ az role assignment list --assignee 7d96660a-02e1-4112-9515-1762d0cb66b7 --all
[
  {
    "condition": null,
    "conditionVersion": null,
    "createdBy": "b470c1dc-9d37-4ce9-b528-4aeaf819781a",
    "createdOn": "2024-10-14T20:25:32.172518+00:00",
    "delegatedManagedIdentityResourceId": null,
    "description": null,
    "id": "/subscriptions/ddd3338d-bc5a-416d-8247-1db1f5b5ff43/resourceGroups/rg-aoc-akv/providers/Microsoft.KeyVault/vaults/warevillesecrets/providers/Microsoft.Authorization/roleAssignments/3038142a-80c7-4bf1-b7c2-0939b906316d",
    "name": "3038142a-80c7-4bf1-b7c2-0939b906316d",
    "principalId": "7d96660a-02e1-4112-9515-1762d0cb66b7",
    "principalName": "Secret Recovery Group",
    "principalType": "Group",
    "resourceGroup": "rg-aoc-akv",
    "roleDefinitionId": "/subscriptions/ddd3338d-bc5a-416d-8247-1db1f5b5ff43/providers/Microsoft.Authorization/roleDefinitions/21090545-7ca7-4776-b22c-e363652d74d2",
    "roleDefinitionName": "Key Vault Reader",
    "scope": "/subscriptions/ddd3338d-bc5a-416d-8247-1db1f5b5ff43/resourceGroups/rg-aoc-akv/providers/Microsoft.KeyVault/vaults/warevillesecrets",
    "type": "Microsoft.Authorization/roleAssignments",
    "updatedBy": "b470c1dc-9d37-4ce9-b528-4aeaf819781a",
    "updatedOn": "2024-10-14T20:25:32.172518+00:00"
  },
  {
    "condition": null,
    "conditionVersion": null,
    "createdBy": "b470c1dc-9d37-4ce9-b528-4aeaf819781a",
    "createdOn": "2024-10-14T20:26:53.771014+00:00",
    "delegatedManagedIdentityResourceId": null,
    "description": null,
    "id": "/subscriptions/ddd3338d-bc5a-416d-8247-1db1f5b5ff43/resourceGroups/rg-aoc-akv/providers/Microsoft.KeyVault/vaults/warevillesecrets/providers/Microsoft.Authorization/roleAssignments/d2edb9d3-620b-45a0-af60-128b5153a00a",
    "name": "d2edb9d3-620b-45a0-af60-128b5153a00a",
    "principalId": "7d96660a-02e1-4112-9515-1762d0cb66b7",
    "principalName": "Secret Recovery Group",
    "principalType": "Group",
    "resourceGroup": "rg-aoc-akv",
    "roleDefinitionId": "/subscriptions/ddd3338d-bc5a-416d-8247-1db1f5b5ff43/providers/Microsoft.Authorization/roleDefinitions/4633458b-17de-408a-b874-0445c86b69e6",
    "roleDefinitionName": "Key Vault Secrets User",
    "scope": "/subscriptions/ddd3338d-bc5a-416d-8247-1db1f5b5ff43/resourceGroups/rg-aoc-akv/providers/Microsoft.KeyVault/vaults/warevillesecrets",
    "type": "Microsoft.Authorization/roleAssignments",
    "updatedBy": "b470c1dc-9d37-4ce9-b528-4aeaf819781a",
    "updatedOn": "2024-10-14T20:26:53.771014+00:00"
  }
]
usr-12274062 [ ~ ]$ az role assignment list --assignee 7d96660a-02e1-4112-9515-1762d0cb66b7
[]
usr-12274062 [ ~ ]$ az keyvault list
[
  {
    "id": "/subscriptions/ddd3338d-bc5a-416d-8247-1db1f5b5ff43/resourceGroups/rg-aoc-akv/providers/Microsoft.KeyVault/vaults/warevillesecrets",
    "location": "eastus",
    "name": "warevillesecrets",
    "resourceGroup": "rg-aoc-akv",
    "tags": {},
    "type": "Microsoft.KeyVault/vaults"
  }
]
usr-12274062 [ ~ ]$ az keyvault secret list --vault-name warevillesecrets
[
  {
    "attributes": {
      "created": "2024-10-14T20:22:20+00:00",
      "enabled": true,
      "expires": null,
      "notBefore": null,
      "recoverableDays": 90,
      "recoveryLevel": "Recoverable+Purgeable",
      "updated": "2024-10-14T20:22:20+00:00"
    },
    "contentType": null,
    "id": "https://warevillesecrets.vault.azure.net/secrets/aoc2024",
    "managed": null,
    "name": "aoc2024",
    "tags": {}
  }
]
usr-12274062 [ ~ ]$ az keyvault secret show --vault-name warevillesecrets --name REDACTED
(SecretNotFound) A secret with (name/id) REDACTED was not found in this key vault. If you recently deleted this secret you may be able to recover it using the correct recovery command. For help resolving this issue, please see https://go.microsoft.com/fwlink/?linkid=2125182
Code: SecretNotFound
Message: A secret with (name/id) REDACTED was not found in this key vault. If you recently deleted this secret you may be able to recover it using the correct recovery command. For help resolving this issue, please see https://go.microsoft.com/fwlink/?linkid=2125182
usr-12274062 [ ~ ]$ az keyvault secret show --vault-name warevillesecrets --name aoc2024
{
  "attributes": {
    "created": "2024-10-14T20:22:20+00:00",
    "enabled": true,
    "expires": null,
    "notBefore": null,
    "recoverableDays": 90,
    "recoveryLevel": "Recoverable+Purgeable",
    "updated": "2024-10-14T20:22:20+00:00"
  },
  "contentType": null,
  "id": "https://warevillesecrets.vault.azure.net/secrets/aoc2024/7f6bf431a6a94165bbead372bca28ab4",
  "kid": null,
  "managed": null,
  "name": "aoc2024",
  "tags": {},
  "value": "WhereIsMyMind1999"
}
usr-12274062 [ ~ ]$
```
### Help

```sh
Requesting a Cloud Shell.Succeeded. 
Connecting terminal...

Welcome to Azure Cloud Shell

Type "az" to use Azure CLI
Type "help" to learn about Cloud Shell

Your Cloud Shell session will be ephemeral so no files or system changes will persist beyond your current session.
usr-12274062 [ ~ ]$ help

Welcome to Azure Cloud Shell, a browser-based shell experience to manage Azure resources.
Cloud Shell is installed with the Azure CLI in addition to common developer tools and language support.

Cloud Shell requires an attached Azure file share in order to persist file changes in your $HOME directory across sessions.
Run "clouddrive -h" to learn how to update your Azure file share.

For more info, visit https://aka.ms/cloudshell
Enter "az help" to learn about the Azure CLI.
Enter "builtin help" to see Bash help.
Enter "builtin help <bash-command>" to see help for a Bash command.

usr-12274062 [ ~ ]$ az help

Group
    az

Subgroups:
    account               : Manage Azure subscription information.
    acr                   : Manage private registries with Azure Container Registries.
    ad                    : Manage Microsoft Entra ID (formerly known as Azure Active Directory,
                            Azure AD, AAD) entities needed for Azure role-based access control
                            (Azure RBAC) through Microsoft Graph API.
    advisor               : Manage Azure Advisor.
    afd                   : Manage Azure Front Door Standard/Premium.
    ai-examples [Preview] : Add AI powered examples to help content.
    aks                   : Manage Azure Kubernetes Services.
    ams                   : Manage Azure Media Services resources.
    apim                  : Manage Azure API Management services.
    appconfig             : Manage App Configurations.
    appservice            : Manage App Service plans.
    aro                   : Manage Azure Red Hat OpenShift clusters.
    backup                : Manage Azure Backups.
    batch                 : Manage Azure Batch.
    bicep                 : Bicep CLI command group.
    billing               : Manage Azure Billing.
    bot                   : Manage Microsoft Azure Bot Service.
    cache                 : Commands to manage CLI objects cached using the `--defer` argument.
    capacity              : Manage capacity.
    cdn                   : Manage Azure Content Delivery Networks (CDNs).
    cloud                 : Manage registered Azure clouds.
    cognitiveservices     : Manage Azure Cognitive Services accounts.
    compute-recommender   : Manage sku/zone/region recommender info for compute resources.
    config [Experimental] : Manage Azure CLI configuration.
    connection            : Commands to manage Service Connector local connections which allow local
                            environment to connect Azure Resource. If you want to manage connection
                            for compute service, please run 'az webapp/containerapp/spring
                            connection'.
    consumption [Preview] : Manage consumption of Azure resources.
    container             : Manage Azure Container Instances.
    containerapp          : Manage Azure Container Apps.
    cosmosdb              : Manage Azure Cosmos DB database accounts.
    databoxedge [Preview] : Manage device with databoxedge.
    deployment            : Manage Azure Resource Manager template deployment at subscription scope.
    deployment-scripts    : Manage deployment scripts at subscription or resource group scope.
    disk                  : Manage Azure Managed Disks.
    disk-access           : Manage disk access resources.
    disk-encryption-set   : Disk Encryption Set resource.
    dla      [Deprecated] : Manage Data Lake Analytics accounts, jobs, and catalogs.
    dls         [Preview] : Manage Data Lake Store accounts and filesystems.
    dms                   : Manage Azure Data Migration Service (classic) instances.
    eventgrid             : Manage Azure Event Grid topics, domains, domain topics, system topics
                            partner topics, event subscriptions, system topic event subscriptions
                            and partner topic event subscriptions.
    eventhubs             : Eventhubs.
    extension             : Manage and update CLI extensions.
    feature               : Manage resource provider features.
    functionapp           : Manage function apps. To install the Azure Functions Core tools see
                            https://github.com/Azure/azure-functions-core-tools.
    group                 : Manage resource groups and template deployments.
    hdinsight             : Manage HDInsight resources.
    identity              : Managed Identities.
    image                 : Manage custom virtual machine images.
    iot                   : Manage Internet of Things (IoT) assets.
    keyvault              : Manage KeyVault keys, secrets, and certificates.
    kusto                 : Manage Azure Kusto resources.
    lab         [Preview] : Manage azure devtest labs.
    lock                  : Manage Azure locks.
    logicapp              : Manage logic apps.
    managed-cassandra     : Azure Managed Cassandra.
    managedapp            : Manage template solutions provided and maintained by Independent
                            Software Vendors (ISVs).
    managedservices       : Manage the registration assignments and definitions in Azure.
    maps                  : Manage Azure Maps.
    mariadb               : Manage Azure Database for MariaDB servers.
    ml                    : Manage Azure Machine Learning resources with the Azure CLI ML extension
                            v2.
    monitor               : Manage the Azure Monitor Service.
    mysql                 : Manage Azure Database for MySQL servers.
    netappfiles           : Manage Azure NetApp Files (ANF) Resources.
    network               : Manage Azure Network resources.
    policy                : Manage resource policies.
    postgres              : Manage Azure Database for PostgreSQL servers.
    ppg                   : Manage Proximity Placement Groups.
    private-link          : Private-link association CLI command group.
    provider              : Manage resource providers.
    redis                 : Manage dedicated Redis caches for your Azure applications.
    relay                 : Manage Azure Relay Service namespaces, WCF relays, hybrid connections,
                            and rules.
    resource              : Manage Azure resources.
    resourcemanagement    : Resourcemanagement CLI command group.
    restore-point         : Manage restore point with res.
    role                  : Manage Azure role-based access control (Azure RBAC).
    search                : Manage Azure Search services, admin keys and query keys.
    security              : Manage your security posture with Microsoft Defender for Cloud.
    servicebus            : Servicebus.
    sf                    : Manage and administer Azure Service Fabric clusters.
    sig                   : Manage shared image gallery.
    signalr               : Manage Azure SignalR Service.
    snapshot              : Manage point-in-time copies of managed disks, native blobs, or other
                            snapshots.
    sql                   : Manage Azure SQL Databases and Data Warehouses.
    ssh                   : SSH into resources (Azure VMs, Arc servers, etc) using AAD issued
                            openssh certificates.
    sshkey                : Manage ssh public key with vm.
    stack                 : A deployment stack is a native Azure resource type that enables you to
                            perform operations on a resource collection as an atomic unit.
    staticwebapp          : Manage static apps.
    storage               : Manage Azure Cloud Storage resources.
    synapse               : Manage and operate Synapse Workspace, Spark Pool, SQL Pool.
    tag                   : Tag Management on a resource.
    term   [Experimental] : Manage marketplace agreement with marketplaceordering.
    ts                    : Manage template specs at subscription or resource group scope.
    vm                    : Manage Linux or Windows virtual machines.
    vmss                  : Manage groupings of virtual machines in an Azure Virtual Machine Scale
                            Set (VMSS).
    webapp                : Manage web apps.

Commands:
    configure             : Manage Azure CLI configuration. This command is interactive.
    feedback              : Send feedback to the Azure CLI Team.
    find                  : I'm an AI robot, my advice is based on our Azure documentation as well
                            as the usage patterns of Azure CLI and Azure ARM users. Using me
                            improves Azure products and documentation.
    interactive [Preview] : Start interactive mode. Installs the Interactive extension if
                            not installed already.
    login                 : Log in to Azure.
    logout                : Log out to remove access to Azure subscriptions.
    rest                  : Invoke a custom request.
    survey                : Take Azure CLI survey.
    upgrade     [Preview] : Upgrade Azure CLI and extensions.
    version               : Show the versions of Azure CLI modules and extensions in JSON format by
                            default or format configured by --output.

To search AI knowledge base for examples, use: az find "az "

You have 2 update(s) available. They will be updated with the next build of Cloud Shell.

usr-12274062 [ ~ ]$ 
```