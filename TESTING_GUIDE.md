# WasteWise Testing Guide

## 1. Installation verification
Run `python manage.py check`. Expected: `System check identified no issues`.

## 2. Authentication
- Open `/accounts/register/` and create a new account.
- Sign out and sign back in.
- Confirm dashboard redirects to login for anonymous visitors.

## 3. Collection requests
- Submit a request with title, category, address, area, quantity and future preferred date.
- Confirm a unique WW reference is created.
- Open the request detail page.
- Confirm a normal user sees only their own requests.

## 4. Admin workflow
- Sign in with a superuser at `/admin/`.
- Add StaffMember and Vehicle records.
- Add CollectionSchedule linked to a WasteRequest.
- Update request status in the admin panel.
- Confirm status badges update on the user-facing detail page.

## 5. Complaints and reports
- Submit a complaint at `/complaints/`.
- Confirm the complaint appears in the list.
- Open `/reports/` and export CSV.
- Verify the CSV columns and data.

## 6. Responsive UI
Test dashboard, tables and forms at desktop width and mobile width (375px).
