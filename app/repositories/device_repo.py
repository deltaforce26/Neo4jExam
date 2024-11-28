class DeviceRepository:
    def __init__(self, driver):
        self.driver = driver


    def insert_devices(self, device):
        with self.driver.session() as session:
            query = """
            MERGE (d:Device {id: $id, name: $name, brand: $brand, model: $model, os: $os})
            RETURN d.id as device_id
            """
            # TODO: add the number of times the relation had happened in a field
            result = session.run(query, {'id': device['id'], 'name': device['name'],
                                         'brand': device['brand'], 'model': device['model'],
                                         'os': device['os']})
            return result.single()['device_id']


    def connect_devices(self, data, d1_id, d2_id):
        with self.driver.session() as session:
            query = """
            MATCH (d1:Device {id: $d1_id}), (d2:Device {id: $d2_id}) 
            CREATE (d1)-[c:CONNECTED{id: randomUuid(), from_device: $from_device, to_device: $to_device,
                        method: $method, bluetooth_version: $bluetooth_version,
                        signal_strength_dbm: $signal_strength_dbm, distance_meters: $distance_meters,
                        duration_seconds: $duration_seconds, timestamp: datetime($timestamp)}]->(d2)
            RETURN c.id as connection_id
            """
            result = session.run(query, {'d1_id': d1_id, 'd2_id': d2_id, 'from_device': data['from_device'],
                                         'to_device': data['to_device'], 'method': data['method'],
                                         'bluetooth_version': data['bluetooth_version'],
                                         'signal_strength_dbm': data['signal_strength_dbm'],
                                         'distance_meters': data['distance_meters'],
                                         'duration_seconds': data['duration_seconds'],
                                         'timestamp': data['timestamp']})
            return result.single()['connection_id']



    def find_by_method(self, method):
        with self.driver.session() as session:
            query = """
            MATCH (start:Device)
            MATCH (end:Device)
            WHERE start <> end
            MATCH path = shortestPath((start)-[:INTERACTED_WITH*]->(end))
            WHERE ALL(r IN relationships(path) WHERE r.method = $method)
            WITH path, length(path) as pathLength
            ORDER BY pathLength DESC
            LIMIT 1
            RETURN length(path)
            """
            result = session.run(query, {'method': method})
            return result.single()['length']