from google.cloud import monitoring

client = monitoring.Client()

resource = client.resource(
    type_='gce_instance',
    labels={
        'instance_id': '2097361145662751147',
        'zone': 'us-west1-a',
    }
)

metric = client.metric(
    type_='custom.googleapis.com/my_metric',
    labels={}
)

# Default arguments use endtime datetime.utcnow()
client.write_point(metric, resource, 3.14)
print('Successfully wrote time series.')