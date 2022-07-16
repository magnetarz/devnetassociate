import meraki

API_KEY = 'ea68a8d9a27556b75066ce71af69eb0bb7c33659'

dashboard = meraki.DashboardAPI(API_KEY)

response = dashboard.organizations.getOrganizations()

print(response)