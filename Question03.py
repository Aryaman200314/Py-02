import boto3
from datetime import datetime, timedelta
def list_all_billings():
    billing_client = boto3.client("ce")
    end_date = datetime.today().strftime('%Y-%m-%d')
    start_date = (datetime.today() - timedelta(days=30)).strftime('%Y-%m-%d')

    response = billing_client.get_cost_and_usage(
    TimePeriod={'Start': start_date, 'End': end_date},
    Granularity='MONTHLY',
    Metrics=['UnblendedCost'],
    GroupBy=[{'Type': 'DIMENSION', 'Key': 'REGION'}]
    )

    billed_regions = [item['Keys'][0] for item in response['ResultsByTime'][0]['Groups']]
    print("Regions where the customer has billed resources:", billed_regions)


list_all_billings()