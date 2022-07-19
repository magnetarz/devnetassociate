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
       1. built with access to the CLI
       2. built with access to the GUI
       3. Northbound interface for custom tooling
    3. **OpenFlex protocol**: South bound interface for communcation with Nexus Switches.
    4. Key features:
        - Application-centric netowrk policy for physical, virtua, and cloud infrastructure.
        - Data model-based declarative provisioning.
        - designed around open standards and open APIs
        - Cisco ACI fabric inventory and configuration
        - Software image management
        - Fault, event and performance monitoring and management.
        - Integration with third-party management systems such as vmware, Microsoft, and Openstack
        - Cloud APIC appliance for Cisco cloud ACI deployments in public cloud environments. 
    5. Needs 3 controllers in a cluster for High Availability