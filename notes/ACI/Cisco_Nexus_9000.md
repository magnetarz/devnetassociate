## A) Nexus 9000 family

1. **Nexus Switches**
   1. Have 2 separate modes of operation.
      1. Standalone (NX-OS) acts like regular layer2/3 switch managed alone.
      2. ACI Mode: Nexus devices become part of the ACI fabric and are managed in a centeralized fashion.
2. **APIC Controller**: The central controller for the ACI Fabric.
   1.  it is the main architectural component of the ACI solution and provides a single point of automation and management of...
       - ACI Fabric
       - Policy Enforcement
       - Health Monitoring
    2. API first architecture 
       1. built with access to the CLI.
       2. built with access to the GUI.
       3. Northbound interface for custom tooling.
    3. **OpenFlex protocol**: South bound interface for communcation with Nexus Switches.
    4. Key features:
        - Application-centric netowrk policy for physical, virtual, and cloud infrastructure.
        - Data model-based declarative provisioning.
        - designed around open standards and open APIs.
        - Cisco ACI fabric inventory and configuration.
        - Software image management.
        - Fault, event and performance monitoring and management.
        - Integration with third-party management systems such as vmware, Microsoft, and Openstack.
        - Cloud APIC appliance for Cisco cloud ACI deployments in public cloud environments. 
    5. Needs 3 controllers in a cluster for High Availability.
   ![ACI Topology](spineleaf.JPG)
3. **Spine-Leaf Architecture** 
   1. **Leaf Switch**: Similar to an access switch connects the spine switches to both physical and virtual endpoint servers.==Leaf switches connect to WAN/Core Routers and APIC controllers.==
   2. **Spine Switch**: Similar to distribution switches.==Spine switches can only connect to leaf switches.==
   3. 40gbps, 100gbps, and 400gbps bandwidth links are available.
   4. ACI Fabric configuration is stored in the APIC using an object-oriented schema.
      1. This configuration represents the logical model of the fabirc.
      2. The APIC compiles the logical model and renders the policies.
      3. The concrete Model runs the rendered policies on the physical infrastructure.
   5. **MIM (Management Information Model)**: Stores the records of the logical and physiacl components of the ACI Fabric.
      1. **MIT(management information tree)**:Hierarchical representation of the MIM.
      2. **MO(Management Objects)**:All components of the ACI fabric can be represented as manged objects.  
      3. Key managed objects ==provided by the system==:
            - **APICs**: Clustered controllers that provide management, application, and policy deployment.
            - **Tenants**: Tenants represent containers for policies that are grouped for a specific acess domain. The following four kinds of tenants are currently supported by the system:
              - User -User tenatns are needed by the fabric andmin to cater to the needs of fabric users.
              - Common - Contains policies and resources that are shared i.e. firewalls, loadbalancers and intrusion dection systems.
              - Infra - Contains management polices for the infrastructure. 
              - Management - Polices and resources for in-bound and out-of-bound configurations.
            - **Access Policies**: Control the operation of leaf switch access ports, which provide fabric connectivity to resources such as virtual machines hypervisors, compute devicces, storage devices etc...
            - **Fabric Policies**: Control the operation of the switch fabric ports. Configurations for time synchronization, routing protocols, and domain name resolution are managed with these policies.
            - **VM domains**: Domain groups of vm controllers. APIC communicates with VM controller to push netowrk configurations all the way to the vm level.
            - **Intergration automation framework**: The Layer 4 to 7 service intergration automation framework enables a system to respond to services coming online or going offline.
            - **AAA Policies**: Access, authentication and accounting polices control user privileges, roles and security domains for the ACI fabric.
4. **Building Blocks of Cisco ACI Fabric Policies**
   1. **Tenants** are top-level MO's that identify and separate administrative control, application policies and failure domains.
        - **Network objects** provide Layer 2 and 3 connectivity betwwen endpoints and consist of the follwing constructs:
          - **VRF(Virtual routing and forwarding)instances**:Isolated routing tables, defines a Layer 3 address domain. Tenants can have one or multiple VRFs.
          - **Bridge Domains**:Layer 2 forwarding domains defines unique mac address space, flooding domain for broadcast, unkown unicast and multicast frames. ==Each bridge domain can only be associated with one VRF, but a VRF can be associated with multiple bridge domains.==
          - **Subnets**: Layer 3 networks that provide ip address space and gateway services for endpoints to be able to connect to the network. ==Each subnet is associated with one bridge domain.==
            - Public - A subnet can be exported to a routed connection.
            - Private - A subnet is confined within its tenant.
            - Shared - A subnet can be shared and exposed in multiple VRF instances in the same tenant or accross tenants as part of a shared service.
          - **External Networks**
            - Bridged - connect the ACI to legacy layer 2/ spanning tree networks.
            - Routed - Creates layer 3 connection with a network outside the ACI Fabric. 
  ![Tenants](ACI_tenant.jpg)
      - **Policy Objects** are focused on the policies and service the endpoints receive. The tenant policy consists of applicatoin profiles, endpoint groups (EPGs), contracts, and filters.
        - **Application Profile**: defines the policies, services and relationships etween EPGs. A profile can contain one or more EPGs, as many as are required to service the needs of an application.All EPG's in a profile are logically related to providing the capabilities of the application.
        - **Endpoint Group(EPG)**:==The most important object of the policy model.== It is a collection of endpoints that have common policy requirements, such as security, virtual machine mobility, QoS, or Layer 4 to 7 services.
          - IP Address
          - location
          - attributes
          - can be physical or virtual.
          - Can only be related to a single bridge domain.
        - **Contracts**: define the services and policies that get applied to EPGs. Used to control traffic flow between EPGs. EPGs communicate based on contract rules.
          - Specify protocol and ports allowed between EPGs.
          - inter-EPG communication is disabled by default with no contract.
          - Consumer or Provider relationship.
5. **APIC REST API**
    1. accepts XML or JSON
    2. The Generic APIC REST API URI:
            `https://APIC_host:port/api/{mo|class}/{FQDN|classname}/.{xml|json}?[options]`
    3.  Sample request using curl
        ```
       curl -k -X POST
       https://sandboxapicdc.cisco.com/api/aaaLogin/json
       -d '{
        "aaaUser" : {
            "attributes" : {
                "name" : "admin",
                "pwd" : "!v3G@!4@Y"
            }
        }
       }
    Response:
    ```json
    {"totalCount":"1","imdata":[
        {"aaaLogin":
        {"attributes":{"token":"eyJhbGciOiJSUzI1NiIsImtpZCI6Ijc0aTM5MjdtbzN0NTh6cHkxOWRhdmhwYjJvNnYxa
        3I3IiwidHlwIjoiand0In0.eyJyYmFjIjpbeyJkb21haW4iOiJhbGwiLCJyb2xlc1IiOjAsInJvbGVzVyI6MX1dLCJpc3MiOiJBQ
        0kgQVBJQyIsInVzZXJuYW1lIjoiYWRtaW4iLCJ1c2Vy
        aWQiOjE1Mzc0LCJ1c2VyZmxhZ3MiOjAsImlhdCI6MTY1ODM2NTQzOCwiZXhwIjoxNjU4MzY
        MDM4LCJzZXNzaW9uaWQiOiJ1VTd1Tk03Z1QreTFYWWVmTUoyK25RPT0ifQvtFMQgqcDFcqsxihaq-Oh6uQyet9nJt1IoYmHoS1HumdWc1rhrBTACH_
        CFTITAvoif3mtZiH83DV1fxfjg5UDQigD0gJ7IjU_mOD_eaIxEF1q0R54PrZP35WX-h81ILhQIJi5MHwXiveCgn-IJ
        Mti4ucQyxPPyhodX3WM-_Kaiw4q0NQkUUerpwC9nfPtKLT6jjywqFdbOiniQW-14fLu0GOk-z0lHRHyrDgtgzqimXe
        2QXkuq70fojGNp02agBXXIXP1vsjUaiZHLIdJLeD99tiH2OB-w3yx65aqYPVLN15yC85gR7uo1Dv8fcpw8yiriHvTE
        ARFiDnH_yZaOKUcw",
        "siteFingerprint":"74i3927mo3t58zpy19davhpb2o6v1kr7","refreshTimeoutSeconds":"600",
        "maximumLifetimeSeconds":"86400",
        "guiIdleTimeoutSeconds":"1200",
        "restTimeoutSeconds":"90",
        "creationTime":"1658365438",
        "firstLoginTime":"1658365438",
        "userName":"admin",
        "remoteUser":"false",
        "unixUserId":"15374",
        "sessionId":"uU7uNM7gT+y1XYefMJ2+nQ==",
        "lastName":"",
        "firstName":"",
        "changePassword":"no",
        "version":"5.2(1g)",
        "buildTime":"Wed Jul 28 23:09:38 UTC 2021",
        "node":"topology/pod-1/node-1"},
        "children":[{"aaaUserDomain":
        {"attributes":{"name":"all","rolesR":"admin","rolesW":"admin"},
        "children":[{"aaaReadRoles":{"attributes":{}}},
        {"aaaWriteRoles":{"attributes":{},
        "children":[{"role":
        {"attributes":
        {"name":"admin"}}}]}}]}},
        {"DnDomainMapEntry":
        {"attributes":{"dn":"uni/tn-infra",
        "readPrivileges":"admin",
        "writePrivileges":"admin"}}},
        {"DnDomainMapEntry":{"attributes":
        {"dn":"uni/tn-common","readPrivileges":"admin","writePrivileges":"admin"}}},
        {"DnDomainMapEntry":{"attributes":
        {"dn":"uni/tn-mgmt","readPrivileges":"admin","writePrivileges":"admin"}}}]}}]}  
Use the token received in the response as a Cookie header to get a list of all ACI Fabrics

```
curl -k -X GET \
https://sandboxapicdc.cisco.com/api/node/class/fabricPod.json \
-H 'Cookie: APIC-Cookie=eyJhbGciOiJSUzI1NiIsImtpZCI6Ijc0aTM5MjdtbzN0NTh6cHkxOWRhdmhwYjJvNnYxa3I3IiwidHlwIjoiand0In0.eyJyYmFjIjpbeyJkb21haW4iOiJhbGwiLCJyb2xlc1IiOjAsInJvbGVzVyI6MX1dLCJpc3MiOiJBQ0kgQVBJQyIsInVzZXJuYW1lIjoiYWRtaW4iLCJ1c2VyaWQiOjE1Mzc0LCJ1c2VyZmxhZ3MiOjAsImlhdCI6MTY1ODM2NTA3MiwiZXhwIjoxNjU4MzY1NjcyLCJzZXNzaW9uaWQiOiJJQjhpQlZFZlJVS29RdEoya3lHSjFnPT0ifQ.JRyr_ej6V2zV-645fa9FxnJlQHMYC8otL2BwoTheATwK-KFvLq0h2NCbS2ft7A6llu4Z2TM_46KvlaWHKCZhsoo2CIch3w8BdXhgBtpTG9cgKPt6LamwnUyvgsejHpXgd1SLyUAKO5-wwTrLURvB699c_p2eSef1IS22LXFHRN-9VSNoU-Nh3s8jShMszQQrOpCz-Ko3Qf2BU16d7nruefjamb0f2JDyybDJv3wnSukGSJRGxua4DDLQbhNavp_HRKUPTLQT6vwczHXPffo16MUPyoFE-37cZJ1Zijc5LcvWzphLatpe9Inuwp66zwz33djwjWP5dqGIXdWYq86RCg'
```
Successful Response:

```json
{"totalCount":"1",
"imdata":
[{"fabricPod":
{"attributes":
{"childAction":"","dn":"topology/pod-1",
"id":"1","lcOwn":"local","modTs":"2022-07-20T02:52:55.999+00:00",
"monPolDn":"uni/fabric/monfab-default",
"podType":"physical","status":""}
}
}]
}
```
        

    
    
   

















