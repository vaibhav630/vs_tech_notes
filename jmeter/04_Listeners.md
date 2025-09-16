# JMeter Beginner Tutorial – Listeners

---

Listeners in JMeter are elements that **collect and display test execution results**.
They help analyze performance metrics, validate responses, and export results.

---

## 1. What Are Listeners?

* Capture **test execution data**.
* Display results in various formats: tables, trees, graphs, reports.
* Can log results to external files (CSV/XML).
* ⚠️ Some listeners (View Results Tree, Graph Results) are **memory heavy** → avoid in large load tests.

---

## 2. Commonly Used Listeners

### 📊 View Results in Table

* Displays data in a tabular format.
* Columns:

  * **Sample #** – request number.
  * **Thread/User info** – e.g., `User 1-1` = User 1, Iteration 1.
  * **Label** – sampler/request name.
  * **Sample Time (ms)** – response time.
  * **Status** – green if success (`200`), red if fail.
  * **Bytes** – response size.
  * **Latency** – time to first byte.
  * **Connect Time** – time to establish server connection.

---

### 🌳 View Results Tree

* Shows **detailed request and response**.
* Tabs:

  * **Sampler Result** – response code, message, headers.
  * **Request** – exact request sent.
  * **Response Data** – response body (HTML/XML/JSON).
* ⚠️ High memory usage.
* Use only for debugging, not for heavy load tests.

---

### 📈 Aggregate Report

* Provides a **summary line** with averages.
* Metrics:

  * **Samples** – total requests.
  * **Average** – mean response time.
  * **Median** – 50% requests faster, 50% slower.
  * **90%/95%/99% Line** – percentile timings.
  * **Min/Max** – fastest/slowest responses.
  * **Throughput** – requests/sec.
  * **KB/sec** – data received per second.
* Useful for consolidated performance stats.

---

### 📉 Graph Results

* Plots metrics as colored dots on a graph:

  * Green → Throughput
  * Blue → Average
  * Black → Median
  * Red → Deviation
* Can toggle metrics on/off.
* ⚠️ Memory intensive → avoid for large-scale runs.

---

### 📑 Summary Report

* Similar to Aggregate Report but simpler.
* Metrics: Samples, Average, Min, Max, Std. Dev, Error %, Throughput, KB/sec.
* Missing percentiles (90/95/99).
* Lightweight and commonly used.

---

### 📂 Simple Data Writer

* Writes results **directly to a file (CSV/XML)**.
* Lightweight, ideal for heavy load tests.
* Configurable fields to log.
* Lets you run tests via **command line (non-GUI)** and still capture results.

---

## 3. Best Practices

* Use **View Results Tree/Table** only during **test design & debugging**.
* For **load tests**, prefer:

  * **Summary Report**
  * **Aggregate Report**
  * **Simple Data Writer** (logs for later analysis).
* Always log results to files for post-run analysis.

---