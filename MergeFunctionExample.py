import pandas as pd
import csv


android_devices = pd.read_csv(r'C:\\Users\kirby\OneDrive\Documents\android_devices.csv', skiprows=0)
user_device = pd.read_csv(r'C:\\Users\kirby\OneDrive\Documents\user_device.csv', skiprows=0)
user_usage = pd.read_csv(r'C:\\Users\kirby\OneDrive\Documents\user_usage.csv', skiprows=0)
left_merge = pd.merge(user_usage, user_device, on='use_id', how='left')
right_merge = pd.merge(user_usage, user_device, on='use_id', how='right')
inner_merge = pd.merge(user_usage, user_device, on='use_id', how='inner')
outer_merge = pd.merge(user_usage, user_device, on='use_id', how='outer')
left_merge_on = pd.merge(user_device, android_devices,
                         left_on='device', right_on='Model',
                         how='left', indicator=True)
print(left_merge_on)

