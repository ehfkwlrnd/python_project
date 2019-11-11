from dynamics365webAPI import D365
crmOrg = 'https://iui79.crm5.dynamics.com'
clientId = '7f50b6d6-8bd8-496b-91b3-a867d28cd3c5'
tenantId = '04a21131-941d-42f6-a817-bf2c5bf69be0'
userName = 'ehfkwlrnd@iui79.onmicrosoft.com'

##crmOrg = 'https://iui.crm5.dynamics.com'
##clientId = 'b3f04e82-3f62-4b8b-b3f8-a98e1a8ff900'
##tenantId = '5a10b9d1-bae4-4270-8007-59299bafbcc5'
##userName = 'ehfkwlrnd@iui.email'

password = 'gkdlf1320**'
user1 = D365(crmOrg, clientId, tenantId, userName, password)
##d = user1.updateRecord("/new_beverages(845911d9-ffb4-e911-a9c5-000d3aa371be)", {'new_price' : 2500})
d = user1.deleteRecord("/new_beverages(845911d9-ffb4-e911-a9c5-000d3aa371be)")
print(d)
