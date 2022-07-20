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
        - Application-centric netowrk policy for physical, virtua, and cloud infrastructure.
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







































































