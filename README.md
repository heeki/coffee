# Unicorn Coffee
This repository represents a variety of microservice capabilities for running the Unicorn Coffee business.


## APIs
Unicorn Coffee aims to expose business functionality and appropriate data feeds via APIs.

### Core
This section creates a custom domain name in API Gateway for uniform access to all enterprise APIs.


### Customer
This section handles all logic associated with customers.

### Inventory
This section handles all logic associated with inventory management.

### Merchant
This section handles all logic associated with merchants.

### Order
This section handles all logic associated with customer orders.

### Shipping
This section handles all logic associated with shipping of orders or automated coffee restock activities.


## Message Routing
Unicorn Coffee is pursuant of an event-driven architecture where it makes sense. The first two use cases entail:
* Coffee dispensing machines producing IoT messages each time a cup of coffee is consuming
* Coffee dispensing machines producing IoT sensor data with health information of various components within the machines

### EventBridge
This section sets up the core infrastructure for event buses and event rules.


## Workflow Orchestration
Unicorn Coffee aims to reduce code associated with state transitions and aims to push that orchestration logic into AWS Step Functions.

### Consumption
This section focuses on workflows that process coffee consumption events.

### Sensor
This section focuses on workflows that process dispensory sensor data events.
