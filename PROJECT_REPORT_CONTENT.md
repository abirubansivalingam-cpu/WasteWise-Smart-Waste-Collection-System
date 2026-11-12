# WASTEWISE – SMART WASTE COLLECTION MANAGEMENT SYSTEM
## MCA Project Report Draft

### Abstract
WasteWise is a web-based waste collection management platform designed to improve the coordination of community waste pickup activities. The system provides a central interface for submitting collection requests, tracking request status, managing collection schedules, maintaining staff and vehicle information, recording complaints and generating operational reports. The application is developed using Python and Django, with HTML, CSS and JavaScript on the frontend. SQLite is provided for simple local setup, while PostgreSQL can be configured for deployment. The system aims to improve visibility, accountability and operational efficiency in local waste collection workflows.

### 1. Introduction
Waste collection operations involve residents, collection teams, vehicles and municipal administrators. Manual processes can make it difficult to track requests, coordinate pickups and monitor service performance. WasteWise digitises these workflows through a role-aware web application.

### 2. Problem Statement
Paper-based or disconnected reporting can result in delayed pickups, duplicate requests, poor visibility of collection progress and limited reporting. A centralised application is needed to record requests and make their status accessible.

### 3. Objectives
- Provide a single platform for waste pickup requests.
- Allow users to monitor request progress.
- Support administrators in managing staff, vehicles and schedules.
- Capture complaints and service feedback.
- Provide summary analytics and CSV reports.
- Offer a responsive and accessible interface.

### 4. Scope
The current implementation covers account registration and authentication, collection request submission, request status tracking, schedule viewing, staff and fleet directories, complaint submission, reports and CSV export. GPS navigation, live sensor integration, automatic route optimisation and third-party notifications are future enhancements.

### 5. Existing System
Traditional workflows may rely on telephone calls, paper registers or separate spreadsheets. These methods can make status updates and consolidated reporting difficult.

### 6. Proposed System
WasteWise stores operational data in a relational database and exposes it through a Django web application. Users submit pickup requests; administrators maintain operational records and update request statuses. Dashboard summaries and reports provide a consolidated view.

### 7. Modules
1. Authentication and user profile
2. Dashboard and analytics
3. Waste collection request management
4. Pickup schedule management
5. Staff management
6. Vehicle and fleet management
7. Complaint management
8. Reports and CSV export
9. Administration

### 8. System Architecture
Browser (HTML/CSS/JavaScript) → Django URL routing and views → Django models/ORM → SQLite or PostgreSQL database. Django authentication protects private views. Chart.js visualises dashboard data.

### 9. Database Design
- User: Django built-in account model.
- WasteRequest: requester, reference, title, category, description, address, area, quantity, preferred date, status, priority, assigned staff and timestamps.
- StaffMember: employee ID, name, phone, role, area and active state.
- Vehicle: registration number, type, capacity, driver, area and availability.
- CollectionSchedule: request, date, time slot, vehicle, notes and completion state.
- Complaint: user, subject, details, area, status and creation time.

### 10. Software and Hardware Requirements
Software: Windows 10/11, Python, Django 5.2, VS Code, web browser and SQLite/PostgreSQL. Hardware: dual-core processor, 4 GB RAM recommended, and sufficient storage for project files.

### 11. Testing
The project includes automated tests for login protection, dashboard access, request creation, user data isolation and CSV export. Manual testing should cover admin workflows, schedule management, complaints, responsive layouts and database configuration.

### 12. Advantages
Centralised request tracking, clearer status visibility, improved administrative coordination, simple reporting, responsive access and extensible architecture.

### 13. Limitations
The initial release does not include live GPS tracking, route optimisation, SMS/email notifications, municipal sensor integration or payment processing. Scheduling records are maintained by administrators through Django admin.

### 14. Future Enhancements
GPS-based vehicle tracking, route optimisation, push notifications, QR-coded collection confirmation, IoT bin fill-level sensors, multilingual support, mobile application and advanced forecasting.

### 15. Conclusion
WasteWise demonstrates how a full-stack web application can organise waste collection workflows. It provides a foundation for request management, administrative coordination and operational reporting, with a modular architecture that can be extended for smart-city use cases.
