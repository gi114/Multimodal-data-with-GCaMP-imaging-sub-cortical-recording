import os
import keyring

# get environment variable as token
token = os.environ['MULTIMODAL-DATA-WITH-GCAMP-IMAGING-SUB-CORTICAL-RECORDING_GLOBUS_TOKEN']

# save token as password of the given keyring credentials
keyring.set_password("globus-remote", "auth-tokens", token)
