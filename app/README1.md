### תמונה כללית של המערכת



```markdown
# פרויקט Neo4j Exam



```python
# routes

# route A
# /api/phone_tracker
# responsible for receiving data from phone dispatcher


# route B
# /api/all_by_method
# This route is responsible for retrieving the longest path of devices that are connected to each other via Bluetooth


# route C
# /api/all_by_signal
# This route is responsible for finding all the devices that are connected to each other with a signal strength stronger than -60


# route D
# /api/nearest_device_count
# This route is counting how many devices are connected to a specific device based on a provided ID.


# route E
# /api/connected_devices
# This route is responsible for determining whether there is a direct connection between two devices with given devices id's


```

---




## הרצת הפרויקט

1. התקן את כל התלויות:

    ```bash
    pip install -r requirements.txt
    ```

2. הרץ את הקובץ docker-compos
כדי להריץ את neo4j
```bash
docker-compose up
```

3. הרץ את הקובץ `main.py` כדי לבדוק את הדוגמאות:

    ```bash
    python main.py
    ```

---


