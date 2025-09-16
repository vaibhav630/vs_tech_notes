# JMeter Beginner Tutorial – Part 2: Create First Test Plan

---

### Quick Summary (Steps)

1. Start JMeter
2. Create Test Plan
3. Add Thread Group (users)
4. Add HTTP Request (sampler)
5. Add Listeners
6. Run test
7. View results

---

## 1. Start JMeter

* **Windows**: Run from `bin/jmeter.bat`
* **Mac/Linux**: Run from `bin/jmeter.sh`

JMeter GUI will open with:

* **Left panel** → Test elements (tree view)
* **Right panel** → Configuration for selected element

---

## 2. Create Test Plan

* Rename default **Test Plan** (e.g., `My First Test Plan`).
* Test Plan = container for all test elements.
* **Note:** Elements in **Workbench** are temporary and not saved.

---

## 3. Add Thread Group (Users)

Right-click **Test Plan → Add → Threads (Users) → Thread Group**.

Configure:

* **Number of Threads (users):** number of virtual users
* **Ramp-Up Period (sec):** time to start all users (e.g., 10 users, 20 sec → 1 user every 2 sec)
* **Loop Count:** how many times to repeat (or check *Forever*)

---

## 4. Add Sampler (Request)

Inside Thread Group →
Right-click **Add → Sampler → HTTP Request**.

Example:

* **Name:** My Home Page
* **Server Name or IP:** `example.com` (without `http://`)
* **Path:** `/index.html` or `/`

---

## 5. Add Listeners (View Results)

Right-click **Thread Group → Add → Listener** and select:

* **View Results in Table**
* **View Results Tree**

---

## 6. Run the Test

🔹 Ways to Run Test in JMeter GUI

* From Thread Group (Users)
  Right-click the Thread Group → Start
  This starts execution from that thread group.

* From Menu Bar
  Go to Run → Start in the top menu.

* Using Toolbar Button
  Click the Green Start ▶ button on the toolbar.

* Stop:

  * **Stop** = immediate termination
  * **Shutdown** = graceful stop after current threads finish

---

## 7. Analyze Results

* **Results Tree** → shows response, request, and details
* **Results Table** → shows status, response time, latency, bytes, etc.
* Successful response = **green** (HTTP 200).

---

✅ You’ve created your first JMeter test plan!

---
