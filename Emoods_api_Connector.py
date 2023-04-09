from nwsapy import api_connector

#set the request information
api_connector.set_user_agent("EMoods", "lauren.taylor.sheppard@gmail.com")
# Get tonights endtime
endTime = api_connector.get_Tonight(event = 'Tonight_endTime')

df = Tonight_endTime.to_dataframe()

from nwsapy.entrypoint import NWSAPy

nwsapy = api_connector = NWSAPy()